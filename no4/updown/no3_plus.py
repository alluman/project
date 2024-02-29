from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = "1122334455"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'no3_plus.db')
db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    hash_pw = db.Column(db.String(64), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)



@app.route('/')
def index():
    return render_template('no3_plus.html')

@app.route('/회원가입', methods=['POST'])








# 회원가입 / 로그인 두고
# 회원가입 클릭하면 이름 닉네임 대조하고 비밀번호 받고 db에 넣고
# 로그인 클릭하면 닉네임 비밀번호 받고 db랑 대조하고 로그인 on부여(session)하고

# 로그인 상태엔 로그아웃/회원탈퇴로 두고
# 로그아웃 클릭하면 yes?물어보고 yes 클릭하면 로그인 off 부여하고
# 회원탈퇴 클릭하면 yes? 물어보고 yes 클릭하면 db에서 삭제

# 글 목록을 항상 테이블로 띄워주고
# 글 목록 아래에 검색기능(제목, 내용, 작성자)
# 아래 오른쪽에 글생성기능
# 로그인 상태에서 클릭하면 new_post.html에서 title, content 입력받아서
# Post에 title = title, content = content, author = 로그인된 아이디 로 저장
# 글 삭제시 로그인된 아이디가 author인지 확인하고 맞으면 삭제