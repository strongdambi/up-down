import random

while True:
    random_number = random.randint(1, 100)
    count = 0
    while True:
        count += 1
        try:
            print("UP&DOWN! 1~100까지 숫자를 입력하세요!")
            number = int(input("숫자 입력: "))
            if not 1 <= number <= 100:
                print("유효한 범위 내 숫자를 넣어주세요\n")
                continue
            elif number < random_number:
                print("\nUP\n")
                continue
            elif number > random_number:
                print("\nDOWN\n")
                continue
            else:
                print(f"\n딩동댕! 정답은 {random_number}입니다!")
                print(f"시도한 횟수: {count}\n")
                break
        except ValueError:
            print()
            print("다시 플레이 하시겠습니까?")
            print("y 또는 n을 입력하세요 (대소문자)")
            print("(유효한 입력이 아닐시 게임을 종료합니다)")
    while True:
        re_game = input("다시 하시겠습니까? (y/n): ")
        if re_game == "y":
            print(f"이전 게임 플레이어 최고 시도 횟수: {count}\n")
            print("<새로운 게임>")
            break
        elif re_game == "n":
            print("게임을 종료합니다")
            break
        else:
            print("\ny 또는 n을 입력하세요\n")
            continue
    if re_game == "n":
        break
