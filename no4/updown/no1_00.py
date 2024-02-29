import random

best_attempt = None

def updown():
    global best_attempt
    print('게임을 시작합니다.')
    
    answer = random.randint(1,100)
    i = 0
    while True:
        n = int(input('숫자를 입력해주세요.'))
        
        if n in range(1,101):
            i += 1
            if n > answer:
                print('down')
            elif n < answer:
                print('up')
            elif n == answer:
                if best_attempt == None or best_attempt > i:
                    best_attempt = i       
                print(f'정답입니다. 기록 : {i}, 최고기록 :{best_attempt}')
                break
        else: 
            print("다시")
    s = input('계속? y')
    if s == 'y':
        updown()
    else:
        print('ㅂㅂ')
updown()


# 1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요.
# 2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
# 3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.
# 최고 횟수를 기록 / 다음게임 표시....를 어떻게 하지

        