import random

number = random.randint(1, 31) # 1~31 까지의 숫자를 랜덤하게 뽑아서 number에 대입
print(f' 내 마음속 숫자:{number}')
running = True

# while 은 오른쪽에 있는 조건 결과가 True 일 경우 반복되는 구문
#running 이 초기에 ture 이므로 무조건 실행되는 구조
while running :
    guess = int(input('1~31 중 내가 생각한 숫자는?'))# 입력받은 값을 정수(int)로 변환하여 guess에 대입
    print(f'입력받은 숫자 :{guess}')# 입력받은 숫자는  guess이다 라고 출력한다
    if guess < number:# 또 다른 만약 입력받은 값이 내 마음속 숫자보다 작다면
        print(f'{guess}가 더 작습니다.')# 입력받은 값이 더 작습니다 라고 출력한다
    elif guess > number:# 또 다른 만약 입력받은 값이 내 마음속 숫자보다 크다면
        print(f'{guess}가 더 큽니다.')# 입력받은 값이 더 큽니다 라고 출력한다
    else:
        running = False# running = True 반복문에서 running = False로 바껴서 반복문은 멈춘다
