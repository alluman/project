from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'rps_data.db')
db = SQLAlchemy(app)

class rps_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(20), nullable=False)
    user_choice = db.Column(db.String(20), nullable=False)  
    computer_choice = db.Column(db.String(20), nullable=False)

class rps_game: # 변수 초기화가 계속 돌아감 (수정해야함)
    def __init__(self):
        self.win_count = 0
        self.draw_count = 0
        self.lose_count = 0

    def user_input(self):
        while True:
            user_rps = request.form['choice']
            if user_rps in ['가위', '바위', '보']:
                return user_rps
            else:
                return "잘못된 입력입니다"
    
    def rps_play(self):#게잉을 시작하는건 html에서, 받아오는것도 html에서
        rps = random.choice(['가위', '바위', '보'])
        user_rps = self.user_input()   
        if user_rps == rps:
            result = f'사용자:{user_rps}, 컴퓨터: {rps} 무승부입니다.'
            self.draw_count += 1
        elif (user_rps == '가위' and rps == '보') or (user_rps == '바위' and rps == '가위') or (user_rps == '보' and rps == '바위'):
            result = f'사용자:{user_rps}, 컴퓨터: {rps} 승리입니다.'
            self.win_count += 1
        else:
            result = f'사용자:{user_rps}, 컴퓨터: {rps} 패배입니다.'
            self.lose_count += 1
        record = rps_data(result=result, user_choice = user_rps, computer_choice = rps)
        db.session.add(record)
        db.session.commit()
        return result, self.win_count, self.draw_count, self.lose_count

@app.route("/", methods = ['GET', 'POST'])
def play_game():
    if request.method == 'GET':
        return render_template('rps_game.html')
    elif request.method == 'POST':
        game = rps_game()
        result, win_count, draw_count, lose_count = game.rps_play()
        return render_template('rps_game.html', result = result, win_count = win_count, draw_count = draw_count, lose_count = lose_count, image_path = "image/")
    
@app.route("/records")
def records():
    records = rps_data.query.all()
    return render_template('rps_game.html', records=records)

if __name__ == "__main__":
    app.run(debug=True)



    # 이미지 위치찾고 연결할것
    # DB 도대체 어떻게?

    #따로 변수를 만들어서 누적하는 방법으로 돌릴까
    #rps_game을 쪼개는게 더 좋지 않을까