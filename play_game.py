import TravelerDilemma as td

if __name__ =="__main__":
    print("[게임설명]\n"
          "항공사는 두 명의 다른 여행자의 여행가방을 잃어버렸습니다.\n"
          "항공사는 여행가방당 최대 $100까지 보상해주겠다고 합니다\n"
          "단 두 사람이\n"
          "1.   모두 같은 금액을 적어내면 그 금액으로 보상하고\n"
          "2.   서로 다른 금액을 적어내면 둘 중 작은 금액으로 보상하고\n"
          "2-1. 작은금액을 적너낸 사람에게는 정직함의 대가로 $2를 높은금액의 사람에게서 공제하여 지급한다\n\n"
          "*두 명의 player는 5회차까지 금액을 제시하며, 회차가 끝날 때마다 제시한 금액을 공개합니다.*\n")

    print("player1 정보를 입력하세요.")
    player1 = td.player(input("이름:"),input("나이:"),input("성별:"),input("학교:"))
    #player1 = td.player('choi', 26, 'F', 'hanyang')
    print("player2 정보를 입력하세요.")
    player2 = td.player(input("이름:"),input("나이:"),input("성별:"),input("학교:"))
    #player2 = td.player('bae', 27, 'M', 'hanyang')

    print("금액을 제시하세요.")
    # 5회차까지 게임 실행
    for round in range(5):
        player1.setNum(input)
        player2.setNum(input)

        # 두 사람이 서로 같은 금액을 제시하면 무승부 처리
        if player1.getNum() == player2.getNum():
            player1.getMoney(player1.getNum())
            player2.getMoney(player2.getNum())
            print("\n'무승부'\n게임이 종료되었습니다.")
            print(round+1,"회차\n player1:", player1.getNum(), "player2:", player2.getNum())
            break

        # Nash 평형 도달(서로 받을 돈이 없어짐), $2를 입력하면 무승부 처리
        elif player1.getNum() == 2 or player2.getNum() == 2:
            print("\n상대방이 $2를 제시하여 게임이 종료되었습니다.\n")
            print(round+1,"회차\n player1:", player1.getNum(), "player2:", player2.getNum())
            player1.getMoney(2)
            player2.getMoney(2)
            break

        # 5회차 실행 후 마지막 결과 값으로 승부 판단
        elif round == 4 and player1.getNum() > player2.getNum():
            print("\n'player2 승리'\n게임이 종료되었습니다.")
            player1.getMoney(int(player2.getNum()) - 2)
            player2.getMoney(int(player2.getNum()) + 2)
        elif round == 4 and player1.getNum() < player2.getNum():
            print("\n'player1 승리'\n게임이 종료되었습니다.")
            player1.getMoney(int(player1.getNum()) + 2)
            player2.getMoney(int(player1.getNum()) - 2)

        # 매 회차 실행 후 결과 값 출력
        else:
            print(round + 1, "회차\n player1:", player1.getNum(), "player2:", player2.getNum())