from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rps_data_01.db')
db = SQLAlchemy(app)

class rps_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(20), nullable=False)
    user_rps = db.Column(db.String(20), nullable=False)  
    computer_rps = db.Column(db.String(20), nullable=False)

class rps_game:
    def rps_play(self):
        rps = random.choice(['가위', '바위', '보'])
        user_rps = request.form['choice'] 
        if user_rps == rps:
            result = '무승부'
        elif (user_rps == '가위' and rps == '보') or (user_rps == '바위' and rps == '가위') or (user_rps == '보' and rps == '바위'):
            result = '승리'
        else:
            result = '패배'
        
        record = rps_data(result=result, user_rps=user_rps, computer_rps=rps)
        db.session.add(record)
        db.session.commit()
        return result
    
@app.route("/")
def start():
    return render_template('rps_game_01.html')

@app.route('/play', methods=['POST'])
def play():    
    game = rps_game()
    result = game.rps_play()
    all_results = rps_data.query.all()  
    win = draw = lose = 0
    win = len([1 for i in all_results if i.result == '승리'])
    draw = len([1 for i in all_results if i.result == '무승부'])
    lose = len([1 for i in all_results if i.result == '패배'])
       
    total_games = len(all_results)
    win_rate = (win / total_games) * 100 if total_games > 0 else 0
    
    return render_template('rps_game_01.html', result=result, win=win, draw=draw, lose=lose, all_results=all_results, win_rate=win_rate)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
