import hashlib

class Member:
    members = []
    check_login = None

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.hash_pw = self.hashing_password(password)

    def hashing_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def add_member(cls, member):
        cls.members.append(member)

    @classmethod #이름중복확인
    def check_name(cls, name):
        for member in cls.members:
            if member.name == name:
                return True
        return False

    @classmethod #아이디중복확인
    def check_username(cls, username):
        for i in cls.members:
            if i.username == username:
                return True
        return False
    
    @classmethod #비밀번호 일치 확인
    def check_password(cls, username, password):
        for i in cls.members:
            if i.username == username and i.hash_pw == i.hashing_password(password):
                return True
        return False

class Post:
    posts = []

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    @classmethod
    def add_post(cls, post):
        Post.posts.append(post)
        print('글이 작성되었습니다.')

    @classmethod  #글 삭제
    def remove_post(cls, title):
        for post in cls.posts:
            if post.title == title:
                cls.posts.remove(post)
                print('글이 삭제되었습니다.')
                return
        print('해당하는 글이 없습니다.')

def main():
    while True:
        user_choice = input('용건을 입력해주세요. (login, member, post, search / 종료: end): ')
        if user_choice == 'login':
            user_login()
        elif user_choice == 'member':
            manage_members()
        elif user_choice == 'post':
            manage_posts()
        elif user_choice == 'search':
            search_posts()
        elif user_choice == 'end':
            print('프로그램을 종료합니다.')
            break
        else:
            print('잘못된 입력입니다.')

def user_login():
    if Member.check_login:
        log_check = input("이미 로그인 중입니다. 로그아웃 하시겠습니까? (y/n)")
        if log_check.lower() == 'y':
            print(f'{Member.check_login} 님, 로그아웃 되었습니다.')
            Member.check_login = None
            return
        else:
            print('처음으로 돌아갑니다.')
            return
    username = input('아이디를 입력하세요: ')
    for member in Member.members:
        if member.username == username:
            password = input('비밀번호를 입력하세요: ')
            if Member.check_password(username, password):
                Member.check_login = username
                print(f'{username} 로그인 되었습니다.')
                return
            else:
                print('비밀번호가 맞지 않습니다. 처음으로 돌아갑니다.')
            return
    print('아이디를 찾을 수 없습니다. 처음으로 돌아갑니다.')

def manage_members():
    while True: # return으로 변경해서 모양을 만들수는 없을까
        choice_member = input('member를 선택하셨습니다. 생성, 탈퇴, 뒤로 중 선택하세요: ') 
        if choice_member == '생성':
            create_member()
            break
        elif choice_member == '탈퇴':
            remove_member()
            break
        elif choice_member == '뒤로':
            break
        else:
            print('잘못된 입력입니다.')

def create_member():
    while True:
        input_name = input('이름을 입력하세요: ')
        if Member.check_name(input_name):
            print('중복된 이름입니다.')
            continue
        else:
            new_name = input_name
            break
    while True:
        input_username = input('아이디를 입력하세요: ')    
        if Member.check_username(input_username):
            print('중복된 아이디입니다.')
            continue
        else:
            new_username = input_username
            break    
    new_password = input('패스워드를 입력하세요: ')
    new_member = Member(new_name, new_username, new_password)
    Member.add_member(new_member)
    print('멤버가 추가되었습니다.')

def remove_member():
    if Member.check_login:
        check_user_out = input('정말로 탈퇴하시겠습니까? (y/n): ')
        if check_user_out.lower() == 'y':
            current_password = input('비밀번호를 입력하세요: ')
            if Member.check_password(Member.check_login, current_password):
                Member.members.remove(Member.check_login)
                Member.check_login = None
                print('회원 탈퇴가 완료되었습니다.')
            else:
                print('비밀번호가 일치하지 않습니다.')
        else:
            print('취소되었습니다.')
    else:
        print('로그인이 필요합니다.')

def manage_posts():
    while True:
        choice_post = input('post를 선택하셨습니다. 생성, 삭제, 뒤로 중 선택하세요: ')
        if choice_post == '생성':
            create_post()
            break
        elif choice_post == '삭제':
            delete_post()
            break
        elif choice_post == '뒤로':
            break
        else:
            print('잘못된 입력입니다.')

def create_post(): #이거 입력하다가 도중에 종료하는 느낌을 만들고 싶은데 명령어로 하자니 해당 내용으로 글이나 내용작성이 안된다..
    if Member.check_login:
        new_title = input('제목을 입력하세요: ')
        new_content = input('내용을 입력하세요: ')
        new_post = Post(new_title, new_content, Member.check_login)
        Post.add_post(new_post)
    else:
        print('로그인이 필요합니다.')

def delete_post():
    if Member.check_login:
        user_posts = [post.title for post in Post.posts if post.author == Member.check_login]
        if not user_posts:
            print('작성한 글이 없습니다.')
            return                
        for i in user_posts:
            print(i)
        remove_title = input('삭제할 글의 제목을 입력하세요: ')
        Post.remove_post(remove_title)
    else:
        print('로그인이 필요합니다.')

def search_posts():
    while True:
        search_posts = input('search를 선택하셨습니다. 제목, 내용, 작성자, 뒤로중 선택하세요: ')
        if search_posts == '제목':
            search_title()
            break
        elif search_posts == '내용':
            search_content()
            break
        elif search_posts == '작성자':
            search_author()
            break
        elif search_posts == '뒤로':
            break            
        else:
            print('잘못된 입력입니다.')

def search_title():
    search_title = input('검색할 제목을 입력해주세요: ')
    for post in Post.posts:
        if search_title in post.title:
            print(post.title)

def search_content():
    search_content = input('검색할 내용을 입력해주세요: ')
    for post in Post.posts:
        if search_content in post.content:
            print(post.title)

def search_author():
    search_author = input('검색할 작성자를 입력해주세요: ')
    for post in Post.posts:
        if search_author == post.author:
            print(post.title)

if __name__ == "__main__":
    main()
    