import random

def generate_lotto_numbers():
    lotto_numbers = set()

    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 45))

    return sorted(lotto_numbers)

if __name__ == "__main__":
    numbers = generate_lotto_numbers()
    print("로또 번호:", numbers)


    


import random

def generate_lotto_numbers():
    lotto_numbers = set()

    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 45))

    return sorted(lotto_numbers)

if __name__ == "__main__":
    numbers = generate_lotto_numbers()
    print("로또 번호:", numbers)


from collections import Counter

def count_common_elements(list1, list2):
    # Counter 객체 생성
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # 두 Counter 객체의 교집합 구하기
    intersection = counter1 & counter2

    # 교집합의 요소 개수 합산
    common_count = sum(intersection.values())

    return common_count

# 예시 리스트
list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 3, 3, 5]

# 두 리스트에서 같은 요소의 개수 확인
result = count_common_elements(list1, list2)
print("두 리스트에서 같은 요소의 개수:", result)