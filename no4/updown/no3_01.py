import hashlib

class Member:
    members = []
    def __init__(self, name, username, password): # 멤버 설정
        self.name = name
        self.username = username
        self.hash_pw = self.password_hashing(password)
        Member.members.append(self)

    def password_hashing(self, password): # 비밀번호 해싱
        password_hash = hashlib.sha256()
        password_hash.update(password.encode())
        return password_hash.hexdigest() # 해싱은 추가공부가 필요함
        
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

    while True:
        user_choice = input('용건을 입력해주세요.(member, post, search (종료시 end) : ')
        if user_choice == 'member':
            while True:
                choice_member = input('member를 선택하셨습니다. 생성, 변경, 삭제 중 원하시는 항목을 입력하세요: ')
                if choice_member == '생성':
                    print('생성을 선택하셨습니다. ')
                    while True:                        
                        new_name = input('이름을 입력하세요. back 입력시 처음으로 돌아갑니다. ')
                        for i in Member.members:
                            if new_name == i.name:
                                print('이미 존재하는 이름입니다.')
                                continue
                            elif new_name == 'back':
                                print('처음으로 돌아갑니다. ')
                                break
                            while True:
                                new_username = input('아이디를 입력하세요: ') 
                                for j in Member.members:
                                    if new_username == j.username:
                                        print('이미 존재하는 아이디입니다.')
                                        continue                                    
                                    else:
                                        new_password = input('패스워드를 입력하세요: ')
                                        new_member = Member(new_name, new_username, new_password)
                                        print('추가되었습니다. 현재 모든 member: ')
                                        for i in Member.members:
                                            print(i.name)                            
                                        break

                elif choice_member == '변경':
                    while True:
                        choice_username = input('변경하실 아이디를 입력하세요. back 입력시 처음으로 이동합니다.: ')
                        for i in Member.members:
                            if choice_username == i.username:
                                choice_user_password = input('비밀번호를 입력하세요: ')
                                hash_input_password = hashlib.sha256(choice_user_password.encode()).hexdigest()
                                if hash_input_password == i.hash_pw:
                                    while True:
                                        request_change = input('id/pw중 변경할 부분을 입력해주세요. back 입력시 처음으로 이동합니다.: ')
                                        if request_change == 'id':
                                            request_id = input('무엇으로 바꾸시겠습니까?: ')
                                            for j in Member.members:
                                                if request_id == j.username:
                                                    print('이미 존재하는 아이디입니다. 다시 입력해주세요')
                                                    continue
                                                else:
                                                    i.username = request_id
                                                    print('아이디가 변경되었습니다.')
                                                    break
                                        elif request_change == 'pw':
                                            request_pw = input('무엇으로 바꾸시겠습니까?: ')
                                            i.hash.pw = i.password_hashing(request_pw)
                                            print('변경되었습니다.')
                                            break
                                        elif request_change == 'back':
                                            print('처음으로 이동합니다.')
                                            break
                                    break
                                elif choice_user_password == 'back':
                                    print('처음으로 이동합니다.')
                                    break                                    
                                else:
                                    print('잘못된 비밀번호입니다.')
                                    break
                            elif choice_username == 'back':
                                print('처음으로 이동합니다.')
                                break
                            else:
                                print('아이디가 존재하지 않습니다.')
                                break

                elif choice_member == '삭제':
                    choice_username = input('삭제하실 아이디를 입력하세요.(back 입력시 처음으로 이동합니다.) :')
                    for i in Member.members:
                        if choice_username == i.username:
                            choice_user_password = input('비밀번호를 입력하세요: ')
                            if choice_user_password == i.hash_pw:
                                del Member.members[i]
                                print('멤버가 삭제되었습니다.')
                            else:
                                print('잘못된 비밀번호입니다.')
                                print('처음으로 이동합니다.')
                                break
                        elif choice_username == 'back':
                            print('처음으로 이동합니다.')
                            break
                        else:
                            print('아이디가 존재하지 않습니다.')
                            print('처음으로 이동합니다.')
                            break
                elif choice_member == '뒤로':
                    break
                else:
                    print('잘못된 입력입니다.')
            
        elif user_choice == 'post':
            choice_post = input('post를 선택하셨습니다. 생성, 변경, 삭제 중 원하시는 항목을 입력하세요: ')
            if choice_post == '생성':
                new_title = input('제목을 입력하세요: ')
                new_content = input('내용을 입력하세요: ')
                while True:
                    new_username = input('작성자를 입력하세요: ')
                    for i in Member.members:
                        if new_username == i.username:
                            new_post = Post(new_title, new_content, i)
                            print('입력을 완료하였습니다. 처음으로 돌아갑니다.')
                            break
                    else:
                        print('입력이 잘못되었습니다.')
            elif choice_post == '변경':
                changepost_username = input("글의 작성자를 입력해주세요.")
                if changepost_username in Member.members:
                    for i in Post.posts:
                        if i.author == changepost_username:
                            print(i.title)    
                            changepost_title = input("변경하고자 하는 글의 제목을 입력해주세요: ")
                            for j in Post.posts:
                                if changepost_title == j.title:
                                    print(f'{changepost_title} 글을 선택하셨습니다.')
                                    changepost_choice = input('글의 무엇을 변경하시겠습니까?(제목/내용): ')
                                    if changepost_choice == '제목':
                                        changetitle = input('제목을 선택하셨습니다. 무엇으로 바꾸시겠습니까? ')
                                        j.title = changetitle
                                        print('제목이 변경되었습니다.')
                                    elif changepost_choice == '내용':
                                        changecontent = input('내용을 선택하셨습니다. 무엇으로 바꾸시겠습니까? ')
                                        j.content = changecontent
                                        print('제목이 변경되었습니다.')
                                    else:
                                        print('잘못된 입력입니다.')
                                else:
                                    print('해당하는 글이 없습니다.')
                    else:
                        print('잘못된 입력입니다.')


            elif choice_post == '삭제':
                changepost_username = input("글의 작성자를 입력해주세요.")
                for i in Post.posts:
                    if changepost_username == i.author:
                        print(i.title)
                        print(i.content)
                        print(i.author)
                        changepost_title = input("삭제하고자 하는 글의 제목을 입력해주세요: ")
                        for j in Post.posts:
                            if changepost_title == j.title:
                                del Post.posts[i]
                                print('삭제가 완료되었습니다.')
                            else:
                                print('해당하는 글이 없습니다.')

                    else:
                        print('잘못된 입력입니다.')
            
            
        elif user_choice == 'search':
            choice_search = input('검색 종류를 선택해주세요(제목, 내용, 제목+내용, 작성자): ')
            if choice_search == '제목':
                search_title = input('제목을 선택하셨습니다. 검색어를 입력해주세요: ')
                for i in Post.posts:
                    if search_title in i.title:
                        print(i.title)
                        print(i.content)
                        print(i.author)

            elif choice_search == '내용':
                search_content = input('내용을 입력하셨습니다. 검색어를 입력해주세요: ')
                for i in Post.posts:
                    if search_content in i.content:
                        print(i.title)
                        print(i.content)
                        print(i.author)
                
            elif choice_search == '제목+내용':
                search_titlecontent = input('제목+내용을 선택하셨습니다. 검색어를 입력해주세요: ')
                for i in Post.posts:
                    if search_titlecontent in i.title or search_titlecontent in i.content:
                        print(i.title)
                        print(i.content)
                        print(i.author)

            elif choice_search == '작성자':
                search_username = input('작성자를 입력해주세요: ')
                for i in Post.posts:
                    if search_username == i.author:
                        print(i.title)
                        print(i.content)
                        print(i.author)
        elif user_choice == 'end':
            print('실행을 종료합니다.')
            break

main()

# 이거 공유도 힘들거같고 그냥 클래스로 묶어보는 시도를
#