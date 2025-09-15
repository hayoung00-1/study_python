import oper

#dir() 내장함수를 사용하면 모듈에 정의되어있눈 변수, 함수목록을 볼수있다.
print(dir(oper))

# 모듈의 이름확인
print(oper.__name__) # 특정 모듈이 이름을 확인
print(__name__) # 현재 나의 이름-> 현재 실행되는 함수