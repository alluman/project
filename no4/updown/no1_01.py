import random

def main():
    best_i = None # 변수선언

    def updown(min_range, max_range): 
        nonlocal best_i # 변수선언
        i = 0
        answer = random.randint(min_range,max_range)
        print('UPDOWN 게임을 시작합니다.')    
        while True:
            i += 1
            while True: # 입력을 판단하고 넣어주는 부분
                pstring= input(f'정수를 입력해주세요({min_range}~{max_range}), 게임 중단은 p를 입력하세요. ')
                if pstring == 'p':
                    print('플레이해주셔서 감사합니다. 게임을 종료합니다.')
                    return
                elif pstring.isdigit() and min_range<=int(pstring)<=max_range:
                    pnumber = int(pstring)
                    break
                elif pstring.isdigit():
                    print('입력한 숫자가 범위에 맞지 않습니다.')
                else:
                    print('숫자(정수)를 입력하셔야 합니다.') 
                    
            if pnumber > answer:    # 기존 숫자와 비교해서 정답을 확인하는 부분
                max_range = pnumber - 1
                print('정답보다 큽니다.')
            elif pnumber < answer: 
                min_range = pnumber + 1
                print('정답보다 작습니다.')
            elif best_i == None or best_i > i:
                best_i = i
                print(f'정답입니다. 시도횟수: {i}, 최고횟수: {best_i}')
                break
            
        while True: #다시 시작할지 물어보는 부분
            pchoice = input('게임을 다시 하시겠습니까? (y/n)')
            if pchoice.lower() == 'y':
                print('게임을 다시 시작합니다.')
                updown(1,100)
                break
            elif pchoice.lower() == 'n':
                print('플레이해주셔서 감사합니다. 게임을 종료합니다.')
                return
            else:
                print('다시 입력해주세요')
    updown(1,100)    #실행

main()



# 1. 플레이어와 컴퓨터가 참여하는 업다운 게임을 만드세요.
# 2. 프로그램은 다음과 같은 기능을 포함해야 합니다.
#     - 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성합니다.
#     - 플레이어는 숫자를 입력하고, 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다.
#     - 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다.
#     - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.

# **추가 도전 과제:**

# 1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요.
# 2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
# 3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.


# **평가**

#  input을 이용해서 사용자의 입력을 받을 수 있는가?
#  input으로 받은 값을 string에서 int로 바꿀 수 있는가?
#  while문을 사용하고 특정조건에서 break를 걸어서 멈출 수 있는가?
#  if문을 이용해서 조건에 따른 코드 실행을 바꿀 수 있는가?























