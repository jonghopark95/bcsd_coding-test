# How to Run : python3 main.py
import os
import sys
from datetime import datetime


class Post:
    """ Post Class """

    def __init__(self, title, content, writer):
        self.title = title
        self.content = content
        self.writer = writer
        self.created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def set(self):
        return {
            "title": self.title,
            "content": self.content,
            "writer": self.writer,
            "created_at": self.created_at,
        }


class Board:
    """ Board Class """

    def __init__(self):
        os.system("clear")
        self.guide_board()
        guide_code = self.handle_guide_board_input()

        if guide_code == 1:
            self.show_post()
        elif guide_code == 2:
            self.create_post()
        elif guide_code == 3:
            self.delete_post()
        elif guide_code == 4:
            os.system("clear")
            Main()
        else:
            print("이용해주셔서 감사합니다!!\n\nBye Bye")
            sys.exit(0)

    def guide_board(self):
        print(
            "메뉴를 선택해 주세요.\n\n 1 : 조회\t 2 : 작성\t 3 : 삭제\t 4 : 뒤로 이동\t 5 : 종료\t (1, 2, 3, 4)\n"
        )

    def handle_guide_board_input(self):
        while True:
            try:
                number = int(input("# : "))
                if number in range(1, 6):
                    return number
                else:
                    print("1 ~ 5 사이의 숫자를 입력해주세요.\n")
            except Exception:
                print("숫자를 입력해주세요. \n")

    def show_post(self, post_list):
        print(" {0:20} {1:20} {2:20}\n".format("제목", "작성자", "작성일"))
        for post in post_list:
            print(
                "#{0}\t {1:20} {2:20} {3:20}".format(
                    post_list.index(post) + 1,
                    post["title"],
                    post["writer"],
                    post["created_at"],
                )
            )

        Main()

    def create_post(self, post_list):
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
                            post_list.append(
                                Post(title, content, "관리자").set(),
                            )
                            print("\n성공적으로 저장되었습니다.\n\n\n")
                            Main()

                        elif check == "N" or check == "n":
                            print("\n저장되지 않았습니다.\n\n\n")
                            Main()

                        else:
                            print("\n유효하지 않은 입력입니다.\n\n\n")

            except Exception:
                print(Exception)

    def delete_post(self, post_list):
        for post in post_list:
            print(
                "#{0}\t {1:20} {2:20} {3:20}".format(
                    post_list.index(post) + 1,
                    post["title"],
                    post["writer"],
                    post["created_at"],
                )
            )

        post_number = input(print("삭제할 글을 고르세요\n\n # : "))
        print(post_number)


class FreeBoard(Board):
    post_data = [
        Post("으으으으으", "술", "박종호").set(),
        Post("으으으으", "마", "박종호").set(),
        Post("으으으", "시", "박종호").set(),
        Post("으으", "고", "박종호").set(),
        Post("으", "싶", "박종호").set(),
        Post("으으", "다", "박종호").set(),
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
    post_data = []

    def __init__(self):
        super().__init__()


class JobBoard(Board):
    post_data = []

    def __init__(self):
        super().__init__()


class Main:
    """ Main Class """

    def __init__(self):
        self.greeting_first_time()

    def greeting_first_time(self):
        print("[코인 - 한기대 커뮤니티] 입니다!\n\n 3가지 게시판 중 하나를 선택해주세요. (1, 2, 3)\n")
        print("종료를 원하시면 4를 입력해주세요.\n")
        print("[1] 자유 게시판 \n")
        print("[2] 익명 게시판 \n")
        print("[3] 자유 게시판 \n")
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
