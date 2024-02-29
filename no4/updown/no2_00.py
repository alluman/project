import random

win_count = 0
lose_count = 0
draw_count = 0 # 승무패 저장할 변수

def rpsgame():
    global win_count, lose_count, draw_count
    #함수에서 횟수 변경해야하니 글로벌넣고 횟수기록 가져올것
    print('가위바위보 게임을 시작합니다.')

    user_rps = input('가위, 바위, 보 중 하나를 입력하세요 :')
    rps = random.choice(['가위', '바위', '보'])

    if user_rps == '가위':
        if rps == '가위':
            print('무승부')
            draw_count += 1
        elif rps == '바위':
            print('패배')
            lose_count += 1
        elif rps == '보':
            print('승리')
            win_count += 1
    elif user_rps == '바위':
        if rps == '가위':
            print('승리')
            win_count += 1
        elif rps == '바위':
            print('무승부')
            draw_count += 1
        elif rps == '보':
            print('패배')
            lose_count += 1
    elif user_rps == '보':
        if rps == '가위':
            print('패배')
            lose_count += 1
        elif rps == '바위':
            print('승리')
            win_count += 1
        elif rps == '보':
            print('무승부')
            draw_count += 1
    s = input('계속? y')
    if s == 'y':
        rpsgame()
    else:
        print(f'승: {win_count} 무: {draw_count} 패: {lose_count} ㅂㅂ')
rpsgame()

 
# **추가 도전 과제:**

# 1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요.
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요.
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.

# **평가**

# - 사용자의 입력값을 ‘가위 바위 보’로 제한할 수 있는가
# - 컴퓨터가 랜덤으로 ‘가위 바위 보’를 선택하게 할 수 있는가
# - 다중 if 문으로 승패를 비교할 수 있는가
# - while문을 이용해서 경기롤 반복시키고 통계를 만들 수 있는가 