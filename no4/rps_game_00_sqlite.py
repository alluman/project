from flask import Flask, render_template, request, g
import sqlite3
import random
import os

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), 'rps_data.db')
conn = sqlite3.connect('rps_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS game (
            id INTEGER PRIMARY KEY,
            user_rps TEXT,
            computer_rps TEXT,
            result TEXT
            )''')
conn.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

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

@app.route('/play', methods=['POST'])
def play():
    result = rps_play()
    conn = sqlite3.connect('rps_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO game (user_rps, computer_rps, result) VALUES (?, ?, ?)", (request.form['choice'], random.choice(['가위', '바위', '보']), result))
    conn.commit()
    c.execute("SELECT COUNT(*) FROM game WHERE result = '승리'")    
    win_game_row = c.fetchone()
    win_game = win_game_row[0] if win_game_row else 0   
    c.execute("SELECT COUNT(*) FROM game WHERE result = '무승부'")
    draw_game_row = c.fetchone()
    draw_game = draw_game_row[0] if draw_game_row else 0
    c.execute("SELECT COUNT(*) FROM game WHERE result = '패배'")    
    lose_game_row = c.fetchone()
    lose_game = lose_game_row[0] if lose_game_row else 0   
    win_rate = (win_game / (win_game+draw_game+lose_game)) * 100
    return render_template('rps_game.html', result=result, win=win_game, draw=draw_game, lose=lose_game, win_rate=win_rate)
    
@app.route('/result', methods = ['POST'])
def result():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM game")
    all_results = cursor.fetchall()
    cursor.close()  
    return render_template('rps_game_result.html', all_results=all_results)

if __name__ == "__main__":
    app.run(debug=True)

    