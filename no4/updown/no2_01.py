import random

def main():
    win_count = lose_count = draw_count = 0
    def rps_game():
        nonlocal win_count, lose_count, draw_count
        rps = random.choice(['가위', '바위', '보'])
        
        print('가위바위보 게임을 시작합니다.')
        while True:
            user_rps = input("가위(s), 바위(r), 보(p) 중 하나를 입력하세요 : ")
            if user_rps in ['가위', '바위', '보', 's', 'r', 'p']:
                break
            else:
                print('잘못된 입력입니다')
        if user_rps == '가위' or user_rps == 's':
            user_rps = '가위'
            if rps == '가위':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 무승부입니다.')
                draw_count += 1
            elif rps == '바위':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 패배입니다.')
                lose_count += 1
            elif rps == '보':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 승리입니다.')
                win_count += 1
        elif user_rps == '바위' or user_rps == 'r':
            user_rps = '바위'
            if rps == '가위':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 승리입니다.')
                win_count += 1
            elif rps == '바위':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 무승부입니다.')
                draw_count += 1
            elif rps == '보':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 패배입니다.')
                lose_count += 1
        elif user_rps == '보' or user_rps == 'p':
            user_rps = '보'
            if rps == '가위':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 패배입니다.')
                lose_count += 1
            elif rps == '바위':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 승리입니다.')
                win_count += 1
            elif rps == '보':
                print(f'사용자:{user_rps}, 컴퓨터: {rps} 무승부입니다.')
                draw_count += 1
        while True:     #다시 시작할지 물어보는 부분
            pchoice = input('게임을 다시 하시겠습니까? (y/n)')
            if pchoice.lower() == 'y':
                print('게임을 다시 시작합니다.')
                rps_game()
                break
            elif pchoice.lower() == 'n':
                print(f'승: {win_count} 무: {draw_count} 패: {lose_count}')
                print('플레이해주셔서 감사합니다. 게임을 종료합니다.')
                return
            else:
                print('다시 입력해주세요')
    rps_game()    #실행

main()
