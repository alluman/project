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
            while True: # 입력을 넣어주는 부분
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
                    
            if pnumber > answer:    # 기존 숫자와 비교하는 부분
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




















