# 매직 메소드 기초

# 기초형
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

n = 100

# n은 int 클래스의 인스턴스인가?
print('EX1-1 - ', n + 200)
print('EX1-2 - ', n.__add__(200))
print('EX1-3 - ', n.__doc__)
print('EX1-4 - ', n.__bool__())
print('EX1-5 - ', n.__mul__(100))

print()
print()


# 클래스 예제1

class Student:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self.name, self.height)

    def __ge__(self, other):
        print('Called >> __ge__ Method.')
        if self.height >= other.height:
            return True
        else:
            return False

    def __le__(self, other):
        print('Called >> __le__ Method.')
        if self.height <= other.height:
            return True
        else:
            return False

    def __sub__(self, other):
        print('Called >> __sub__ Method.')
        return self.height - other.height


# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# 매직 메소드 출력
print('EX2-1 - ', s1 >= s2)
print('EX2-2 - ', s1 <= s2)
print('EX2-3 - ', s1 - s2)
print('EX2-4 - ', s2 - s1)
print('EX2-5 - ', s1)
print('EX2-6 - ', s2)

print()
print()
