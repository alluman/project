from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rps_data_02.db')
db = SQLAlchemy(app)

class rps_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(20), nullable=False)
    user_rps = db.Column(db.String(20), nullable=False)  
    computer_rps = db.Column(db.String(20), nullable=False)

class rps_game:
    def __init__(self):
        if 'win_count' not in session:
            session['win_count'] = 0
        if 'draw_count' not in session:
            session['draw_count'] = 0
        if 'lose_count' not in session:
            session['lose_count'] = 0
   
    def rps_play(self):
        win_count = session['win_count']
        draw_count = session['draw_count']
        lose_count = session['lose_count']

        rps = random.choice(['가위', '바위', '보'])
        user_rps = request.form['choice']
        if user_rps == rps:
            result = f'사용자:{user_rps}, 컴퓨터: {rps} 무승부입니다.'
            draw_count += 1
        elif (user_rps == '가위' and rps == '보') or (user_rps == '바위' and rps == '가위') or (user_rps == '보' and rps == '바위'):
            result = f'사용자:{user_rps}, 컴퓨터: {rps} 승리입니다.'
            win_count += 1
        else:
            result = f'사용자:{user_rps}, 컴퓨터: {rps} 패배입니다.'
            lose_count += 1

        session['win_count'] = win_count
        session['draw_count'] = draw_count
        session['lose_count'] = lose_count

        record = rps_data(result=result, user_rps = user_rps, computer_rps = rps)
        db.session.add(record)
        db.session.commit()
        return result, win_count, draw_count, lose_count

@app.route("/")
def start():
    return render_template('rps_game_02.html')
    
@app.route("/play", methods = ['POST'])
def play_game():
    game = rps_game()
    result, win_count, draw_count, lose_count = game.rps_play()
    all_results = rps_data.query.all()
    win_rate = (win_count/(win_count+draw_count+lose_count))*100
    return render_template('rps_game_02.html', result = result, win = win_count, draw = draw_count, lose = lose_count, all_results = all_results, win_rate = win_rate)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


#세션이라서 브라우저에 영향을 받음
#브라우저를 껐다 켜야 갱신이 되는 시스템인데 db랑 따로임