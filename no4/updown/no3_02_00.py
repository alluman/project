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

    def add_member(self, member):
        self.members.append(member)

    def check_password(self, username, password):
        for member in self.members:
            if member.username == username and member.hash_pw == self.hashing_password(password):
                return True
        return False

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def add_post(self, post): #로그인 상태 확인
        self.posts.append(post)
        print('글이 작성되었습니다.')

    def remove_post(self, post): 
        self.posts.remove(post)
        print('글이 삭제되었습니다.')



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

    def user_login(self):
        if self.check_login:
            print("이미 로그인 중입니다.")
            return
        username = input('아이디를 입력하세요: ')
        for member in Member.members:
            if member.username == username:
                password = input('비밀번호를 입력하세요: ')
                if self.check_password(username, password):
                    self.check_login = username
                    print(f'{username} 로그인 되었습니다.')
                    return
                else:
                    print('비밀번호가 맞지 않습니다.')
                return
        print('아이디를 찾을 수 없습니다.')

    def logout(self):
        if not self.check_login:
            print("로그인 상태가 아닙니다.")
            return
        self.check_login = None
        print('로그아웃 되었습니다.')

    def manage_members():
        while True:
            choice_member = input('member를 선택하셨습니다. 생성, 탈퇴, 뒤로 중 선택하세요: ')
            if choice_member == '생성':
                create_member()
            elif choice_member == '탈퇴':
                remove_member()
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
        new_member.add_member(new_member)
        print('멤버가 추가되었습니다.')

    def remove_member(self, username):
        if Member.check_login_member:
            check_user_out = input('정말로 탈퇴하시겠습니까? (y/n): ')
        if check_user_out.lower() == 'y':
            current_password = input('비밀번호를 입력하세요: ')
            if Member.check_password(Member.logged_in_member.username, current_password):
                Member.remove_member(Member.logged_in_member)
                Member.log_out()
                print('회원 탈퇴가 완료되었습니다.')
            else:
                print('비밀번호가 일치하지 않습니다.')
        else:
            print('현재 로그인 되어있지 않습니다..')
    
    def manage_posts():
        while True:
            choice_post = input('post를 선택하셨습니다. 생성, 삭제, 뒤로 중 선택하세요: ')
            if choice_post == '생성':
                create_post()
            elif choice_post == '삭제':
                delete_post()
            elif choice_post == '뒤로':
                break
            else:
                print('잘못된 입력입니다.')

    def create_post():
        if Member.check_login_member:
            new_title = input('제목을 입력하세요: ')
            new_content = input('내용을 입력하세요: ')
            new_post = Post(new_title, new_content, Member.check_login_member)
            Post.add_post(new_post)
        else:
            print('로그인이 필요합니다.')

    def delete_post():
        if Member.check_login_member:
            user_posts = [post.title for post in Post.posts if post.author == Member.check_login_member]
            if not user_posts:
                print('작성한 글이 없습니다.')
                return                
            for i in user_posts:
                print(i)
            remove_title = input('삭제할 글의 제목을 입력하세요: ')
            for post in Post.posts:
                if remove_title == post.title and post.author == Member.check_login_member:
                    Post.remove_post(post)
                    print('글이 삭제되었습니다.')
        else:
            print('로그인이 필요합니다.')

    def search_posts():
        while True:
            search_posts = input('search를 선택하셨습니다. 제목, 내용, 작성자, 뒤로중 선택하세요: ')
            if search_posts == '제목':
                search_title()
            elif search_posts == '내용':
                search_content()
            elif search_posts == '작성자':
                search_author()
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
            if search_author == Post.author:
                print(post.title)

    if __name__ == "__main__":
        main()

