class Runner:
    def run(self):
        pass
        print(f'달린다.')

    def sprint(self):
        pass
        print(f'전력질주를 한다.')

class Jumper:
    def jump(self):
        pass
        print(f'점프를 한다.')

    def high_jump(self):
        pass
        print(f'높이 점프를 한다.')

class Person(Jumper, Runner):
    pass
class Person(Jumper, Runner): # Jumper 와 Runner 를 상속 받았다.
    def walk(self):
        print(f'걷는다.')
