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

class rps_game:
    def __init__(self):
        self.win_count = 0
        self.draw_count = 0
        self.lose_count = 0
    
    def rps_play(self):#게잉을 시작하는건 html에서, 받아오는건 input이랑 html에서
        rps = random.choice(['가위', '바위', '보'])
        user_rps = self.user_input()   
        if user_rps == rps:
            result = print(f'사용자:{user_rps}, 컴퓨터: {rps} 무승부입니다.')
            self.draw_count += 1
        elif (user_rps == '가위' and rps == '보') or (user_rps == '바위' and rps == '가위') or (user_rps == '보' and rps == '바위'):
            result = print(f'사용자:{user_rps}, 컴퓨터: {rps} 승리입니다.')
            self.win_count += 1
        else:
            result = print(f'사용자:{user_rps}, 컴퓨터: {rps} 패배입니다.')
            self.lose_count += 1
        return result, self.win_count, self.draw_count, self.lose_count

@app.route("/", methods = ['post'])
def play_game():
    game = rps_game()
    result, win_count, draw_count, lose_count = game.rps_play()
    return render_template('rps_game.html', result = result, win_count = win_count, draw_count = draw_count, lose_count = lose_count)
    
if __name__ == "__main__":
    app.run(debug=True)
    


# 입력 - 가위/바위/보
# 계산 - 랜덤생성(가위바위보) / 승무패
# 출력 - 승/무/패
# 저장하는것 - 입력과 승무패
# 요청시 출력 - 최근 20경기 입력과 승무패
# db에 저장을 어떻게 할 것인가?