from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random

app = Flask(__name__)
conn = sqlite3.connect('rps_data.db') #db연결
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS game (
            id INTEGER PRIMARY KEY,
            user_rps TEXT,
            computer_rps TEXT,
            result TEXT
            )''')  #테이블
conn.commit() #저장

def rps_play():
    user_rps = request.form['choice']
    computer_rps = random.choice(['가위', '바위', '보'])
    if user_rps == computer_rps:
        return '무승부'
    elif (user_rps == '가위' and computer_rps == '보') or (user_rps == '바위' and computer_rps == '가위') or (user_rps == '보' and computer_rps == '바위'):
        return '승리'
    else:
        return '패배'
    
@app.route("/")
def start():
    return render_template('rps_game.html')

@app.route('/play', methods = ['POST'])
def play():
    result = rps_play()
    conn = sqlite3.connect('rps_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO game (user_rps, computer_rps, result) VALUES (?, ?, ?)", (request.form['choice'], random.choice(['가위', '바위', '보']), result))
    conn.commit()
    c.execute("SELECT * FROM game")
    all_results = c.fetchall()
    win = 0
    draw = 0
    lose = 0
    for i in all_results:
        if i[3] == '승리':
            win += 1
        elif i[3] == '무승부':
            draw += 1
        else:
            lose += 1
    if len(all_results) > 0:
        win_rate = (win/len(all_results))*100
    else:
        win_rate = 0
    return render_template('rps_game.html', result = result, win = win, draw = draw, lose = lose, all_results = all_results, win_rate = win_rate)
   
if __name__ == "__main__":
    app.run(debug=True)

