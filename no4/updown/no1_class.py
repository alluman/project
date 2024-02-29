import random

class updown:
    def __init__(self, min_range, max_range):
        self.best_i = None
        self.min_range = min_range
        self.max_range = max_range

    def p_input(self):
        while True:             # 입력을 판단하고 넣어주는 부분
                pstring= input(f'정수를 입력해주세요({self.min_range}~{self.max_range}), 게임 중단은 p를 입력하세요. ')
                if pstring == 'p':
                    print('플레이해주셔서 감사합니다. 게임을 종료합니다.')
                    return
                elif pstring.isdigit() and self.min_range<=int(pstring)<=self.max_range:
                    pnumber = int(pstring)
                    break
                elif pstring.isdigit():
                    print('입력한 숫자가 범위에 맞지 않습니다.')
                else:
                    print('숫자(정수)를 입력하셔야 합니다.') 
    def result(self):
        if self.pnumber > self.answer:    # 기존 숫자와 비교해서 정답을 확인하는 부분
                max_range = self.pnumber - 1
                print('정답보다 큽니다.')
        elif self.pnumber < self.answer: 
            min_range = self.pnumber + 1
            print('정답보다 작습니다.')
        elif self.best_i == None or self.best_i > self.i:
            self.best_i = self.i
            print(f'정답입니다. 시도횟수: {self.i}, 최고횟수: {self.best_i}')
            return 
    
    def updown_continue(self):
        while True:     #다시 시작할지 물어보는 부분
            self.pchoice = input('게임을 다시 하시겠습니까? (y/n)')
            if self.pchoice.lower() == 'y':
                print('게임을 다시 시작합니다.')
                updown(1,100)
                break
            elif self.pchoice.lower() == 'n':
                print('플레이해주셔서 감사합니다. 게임을 종료합니다.')
                return
            else:
                print('다시 입력해주세요')

    def updown_play(self):
        self.i = 0
        self.answer = random.randint(self.min_range,self.max_range)
        while True:
            self.i += 1
            self.p_input()
            self.result()          


game = updown()
game.updown_play()
