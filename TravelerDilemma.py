"""
여행자의 딜레마 게임을 플레이할 player 클래스 정의
이름, 나이, 성별, 학교 정보수집
"""

class player:
    # player의 기초 정보 변수
    name =""
    old = ""
    gender = ""
    school = ""
    num = ""
    money = ""

    # player의 기초 정보 초기화
    def __init__(self, name, old, gender, school):
        self.name = name
        self.old = old
        self.gender = gender
        self.school = school
        self.money = 0
        self.num = 0

    # player의 이름 반환
    def getName(self):
        return self.getname()

    # player의 나이 반환
    def getOld(self):
        return  self.getold()

    # player의 성별 반환
    def getGender(self):
        return self.getGender()

    # player의 학교 반환
    def getSchool(self):
        return self.getSchool()

    # 플레이어가 제시할 금액을 입력받음, 1~100 사이의 금액, 초과하면 에러메세지 띄움
    def setNum(self, num):
       self.num = int(input("제시금액:"))
       if self.num not in range(1-101):
           print("제시금액의 범위를 초과하였습니다.\n 다시 입력하세요.")
           self.num = int(input("제시금액:"))

    # player의 제시금액 반환
    def getNum(self):
        return self.num

    # player가 획득한 금액
    def getMoney(self,money):
        self.money = money
        print(self.name,"이 $", self.money,"획득하였습니다.")




