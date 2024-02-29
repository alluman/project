import hashlib

class Member:
    members = []
    def __init__(self, name, username, password): # 멤버 설정
        self.name = name
        self.username = username
        self.hash_pw = self.password_hashing(password)
        Member.members.append(self) # Member 인스턴스를 자동으로 members 리스트에 추가

    def password_hashing(self, password):
        password_hash = hashlib.sha256()
        password_hash.update(password.encode())
        return password_hash.hexdigest() 
        
    def display(self):
        print(f'이름: {self.name}')
        print(f'아이디: {self.username}')

class Post:
    posts = []
    def __init__(self, title, content, author): # post 설정
        self.title = title
        self.content = content
        self.author = author.username
        Post.posts.append(self)

def main():
    member1 = Member('name1', 'username1', 'password1')
    member2 = Member('name2', 'username2', 'password2')
    member3 = Member('name3', 'username3', 'password3')


    print('생성이 완료되었습니다.')

    post1 = Post('post1','post2',member3)
    print(post1.author)

    member1.display()
    for i in Member.members:
        print(i.name)
            
    post1_1 = Post('title1_1', 'content1_1', member1)
    post1_2 = Post('title1_2', 'content1_2', member1)
    post1_3 = Post('title1_3', 'content1_3', member1)
    post2_1 = Post('title2_1', 'content2_1', member2)
    post2_2 = Post('title2_2', 'content2_2', member2)
    post2_3 = Post('title2_3', 'content2_3', member2)
    post3_1 = Post('title3_1', 'content3_1', member3)
    post3_2 = Post('title3_2', 'content3_2', member3)
    post3_3 = Post('title3_3', 'content3_3', member3)

    for i in Post.posts:
        if i.author == 'username2':
            print(i.title)
    for i in Post.posts:
        if '_2' in i.content:
            print(i.title)

    user_choice = input('추가하실 항목을 정해주세요(member, post): ') # 추가
    if user_choice == 'member':
        print('member를 입력하셨습니다.')
        new_name = input('이름을 입력하세요: ')
        new_username = input('아이디를 입력하세요: ')
        new_password = input('패스워드를 입력하세요: ')
        new_member = Member(new_name, new_username, new_password)
        print('추가되었습니다. 현재 모든 member: ')
        for i in Member.members:
            print(i.username)

    elif user_choice == 'post':
        print('post를 입력하셨습니다.')
        new_title = input('제목을 입력하세요: ')
        new_content = input('내용을 입력하세요: ')
        while True:
            new_username = input('작성자를 입력하세요: ')
            for i in Member.members:
                if new_username == i.username:
                    new_post = Post(new_title, new_content, i)
                    print('입력을 완료하였습니다.')
                    break
            else:
                print('입력이 잘못되었습니다.')
main()

