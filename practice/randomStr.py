name = ['프디', '바쭈', '파파', '연두', '박성준']
attribute = ['병신임', '천재임', '허준원 성노예임', '일단 사람은 아님', '여자임', '거의 신에 근접함']

dst = attribute.copy()

from random import randint
for i in name:
    attr = attribute.pop(randint(0, len(attribute)-1))

    print(f'{i}은 {attr}')