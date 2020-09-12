# How to Run : python3 main.py
import os
import sys
from src.board import Board
from src.post import Post


class FreeBoard(Board):
    post_data = [
        Post("자유제목1", "자유내용1", "자유1").set(),
        Post("자유제목2", "자유내용2", "자유2").set(),
        Post("자유제목3", "자유내용3", "자유3").set(),
        Post("자유제목4", "자유내용4", "자유4").set(),
        Post("자유제목5", "자유내용5", "자유5").set(),
        Post("자유제목6", "자유내용6", "자유6").set(),
    ]

    def __init__(self):
        super().__init__()

    def show_post(self):
        super().show_post(self.post_data)

    def create_post(self):
        super().create_post(self.post_data)

    def delete_post(self):
        super().delete_post(self.post_data)


class AnonymousBoard(Board):
    post_data = [
        Post("익명제목1", "익명내용1", "익명1", "11").set(),
        Post("익명제목2", "익명내용2", "익명2", "22").set(),
        Post("익명제목3", "익명내용3", "익명3", "33").set(),
        Post("익명제목4", "익명내용4", "익명4", "44").set(),
        Post("익명제목5", "익명내용5", "익명5", "55").set(),
        Post("익명제목6", "익명내용6", "익명6", "66").set(),
    ]

    def __init__(self):
        super().__init__()

    def show_post(self):
        print("{0} {1:20} \n".format("제목", "작성일"))
        for post in self.post_data:
            print(
                "#{0}\t {1:20} {2:20} {3}".format(
                    self.post_data.index(post) + 1,
                    post["title"],
                    post["created_at"],
                    post["password"],
                )
            )

        post_number = int(input("내용을 보고 싶다면 번호를 고르세요 (취소 : 0)\n\n # : "))

        if post_number > len(self.post_data):
            print("글 리스트 내의 번호를 입력해주세요.\n\n")

        else:
            post = self.post_data[post_number - 1]
            os.system("clear")
            print(f'내용 : {post["content"]}\n')

        from main import Main

        Main()

    def create_post(self):
        while True:
            try:
                title = input("글 제목을 입력해주세요. \n 제목 : ")
                content = input("글 내용을 입력해주세요. \n 내용 : ")

                if title == "" or content == "":
                    print("입력란에 공백은 허용되지 않습니다.\n")

                else:
                    while True:
                        check = input(
                            f"\n\n\t제목 : {title}\n\t내용 : {content}\n 저장하시겠습니까? (Y / N)\t"
                        )
                        if check == "Y" or check == "y":  # 유저가 y를 누를 시 리스트에 저장한다.

                            password = input("비밀번호를 입력해주세요. \n 비밀번호 : (공백 허용)\t")

                            self.post_data.append(
                                Post(title, content, "관리자", password).set(),
                            )
                            print("\n성공적으로 저장되었습니다.\n\n\n")
                            from main import Main

                            Main()

                        elif check == "N" or check == "n":
                            print("\n저장되지 않았습니다.\n\n\n")
                            from main import Main

                            Main()

                        else:
                            print("\n유효하지 않은 입력입니다.\n\n\n")

            except Exception:
                print(Exception)

    def delete_post(self):
        while True:
            try:
                for post in self.post_data:
                    print(
                        "#{0}\t {1:20} {2:20}".format(
                            self.post_data.index(post) + 1,
                            post["title"],
                            post["created_at"],
                        )
                    )

                post_number = int(input("삭제할 글을 고르세요\n\n # : "))

                if post_number > len(self.post_data):
                    print("글 리스트 내의 번호를 입력해주세요.\n\n")

                else:
                    password = int(input("비밀번호를 입력해주세요 : "))
                    if int(self.post_data[post_number - 1]["password"]) == password:
                        self.post_data.pop(post_number - 1)
                        print("글이 정상적으로 삭제 되었습니다.\n\n")
                        Main()
                    else:
                        print("비밀번호가 다릅니다. 강제 종료합니다.\n")
                        sys.exit(0)

            except Exception:
                print(Exception)
                print("숫자를 입력해 주세요.\n\n")


class JobBoard(Board):
    post_data = [
        Post("취업제목1", "취업내용1", "취업1").set(),
        Post("취업제목2", "취업내용2", "취업2").set(),
        Post("취업제목3", "취업내용3", "취업3").set(),
        Post("취업제목4", "취업내용4", "취업4").set(),
        Post("취업제목5", "취업내용5", "취업5").set(),
        Post("취업제목6", "취업내용6", "취업6").set(),
    ]

    def __init__(self):
        super().__init__()

    def show_post(self):
        super().show_post(self.post_data)

    def create_post(self):
        super().create_post(self.post_data)

    def delete_post(self):
        super().delete_post(self.post_data)


class Main:
    """ Main Class """

    def __init__(self):
        self.greeting_first_time()

    def greeting_first_time(self):
        print("[코인 - 한기대 커뮤니티] 입니다!\n\n 3가지 게시판 중 하나를 선택해주세요. (1, 2, 3)\n")
        print("종료를 원하시면 4를 입력해주세요.\n")
        print("[1] 자유 게시판 \n")
        print("[2] 익명 게시판 \n")
        print("[3] 취업 게시판 \n")
        board_code = self.handle_board_input()
        if board_code == 1:
            FreeBoard()
        elif board_code == 2:
            AnonymousBoard()
        elif board_code == 3:
            JobBoard()
        else:
            print("Bye Bye 이용해주셔서 감사합니다!!")
            sys.exit(0)

    def handle_board_input(self):
        while True:
            try:
                number = int(input("# : "))
                if number in range(1, 5):
                    return number
                else:
                    print("1~4 사이의 숫자를 입력해주세요.\n")
            except Exception:
                print("숫자를 입력해주세요. \n")


Main()
