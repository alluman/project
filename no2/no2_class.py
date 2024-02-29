import random

class rps_game:
    def __init__(self): # 변수선언
        self.win_count = 0
        self.draw_count = 0
        self.lose_count = 0
    
    def user_input(self):
        while True: # 입력받는 부분
            user_rps = input("가위(s), 바위(r), 보(p) 중 하나를 입력하세요 : ")
            if user_rps in ['가위', '바위', '보', 's', 'r', 'p']:
                if user_rps == 's':
                    self.user_rps = '가위'
                elif user_rps == 'r':
                    self.user_rps = '바위'
                elif user_rps == 'p':
                    self.user_rps = '보'                
                return self.user_rps
            else:
                print('잘못된 입력입니다')
    
    def rps_result(self): #컴퓨터와 비교하는 부분
        rps = random.choice(['가위', '바위', '보'])
        if self.user_rps == rps:
            print(f'사용자:{self.user_rps}, 컴퓨터: {rps} 무승부입니다.')
            self.draw_count += 1
        elif (self.user_rps == '가위' and rps == '보') or (self.user_rps == '바위' and rps == '가위') or (self.user_rps == '보' and rps == '바위'):
            print(f'사용자:{self.user_rps}, 컴퓨터: {rps} 승리입니다.')
            self.win_count += 1
        else:
            print(f'사용자:{self.user_rps}, 컴퓨터: {rps} 패배입니다.')
            self.lose_count += 1
           
    def rps_continue(self):
        while True:     #다시 시작할지 물어보는 부분
            pchoice = input('게임을 다시 하시겠습니까? (y/n)')
            if pchoice.lower() == 'y':
                print('게임을 다시 시작합니다.')
                self.rps_play()
                break
            elif pchoice.lower() == 'n':
                print(f'승: {self.win_count} 무: {self.draw_count} 패: {self.lose_count}')
                print('플레이해주셔서 감사합니다. 게임을 종료합니다.')
                return
            else:
                print('다시 입력해주세요')

    def rps_play(self): #실행하는 부분
        print('가위바위보 게임을 시작합니다.')
        self.user_input()
        self.rps_result()
        self.rps_continue()

game = rps_game()
game.rps_play()
