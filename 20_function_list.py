# 1.반환타입: O매개변수:O 인형뽑기,커피그라인더
# 2.반환타입: O매개변수:X번호표기기
# 3.반환타입: X매개변수:O오락실게임
# 4.반환타입: X매개변수:X호출벨

def hole(dull):
    print (f'{dull}을 뽑았습니다.')
    return f'인형이 나왔습니다.'

co=hole('토끼인형')
print(co)

def 번호표기계():
    return "번호표"
print(번호표기계())

def 저금통(coin):# 저금통에는 return 이 없는데
    #저금통 실행후 나온값을 출력하려고 하니
    # None 이 출력 되는 것
    print(f'{coin}원 저축')
저금통(500)


def bell():
    print('호출!!!')
bell()







