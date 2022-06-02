from random import randint

money = 100

class Card:


while True:
    betting = input(f'얼마를 거실건지 입력하세요(현재 돈: {money})>>')

    try:
        betting = int(betting)

        money -= betting

        nums = []

        for i in range(5):
            num = input(f'1~10사이에 숫자가 나옵니다. 원하는 숫자를 입력하세요({i}번째 숫자 입력중)>>')
            try:
                nums.append(int(num))
            except ValueError:
                print('알맞은 값을 입력하세요')
                i-=1
                continue

        specialNum = input('스페셜 넘버를 입력하세요>>')

        lotto = []

        for i in range(5):
            lotto.append(randint(1, 10))

    except ValueError:
        print('알맞은 값을 입력하세요')