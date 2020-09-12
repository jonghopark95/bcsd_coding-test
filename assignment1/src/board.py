import os
import sys
from .post import Post


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
            from main import Main

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

        post_number = int(input("내용을 보고 싶다면 번호를 고르세요 (취소 : 0)\n\n # : "))

        if post_number > len(post_list):
            print("글 리스트 내의 번호를 입력해주세요.\n\n")

        else:
            post = post_list[post_number - 1]
            print(f'작성자 : {post["writer"]}\n 내용 : {post["content"]}\n')

        from main import Main

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

    def delete_post(self, post_list):

        while True:
            try:
                for post in post_list:
                    print(
                        "#{0}\t {1:20} {2:20} {3:20}".format(
                            post_list.index(post) + 1,
                            post["title"],
                            post["writer"],
                            post["created_at"],
                        )
                    )

                post_number = int(input("삭제할 글을 고르세요\n\n # : "))

                if post_number > len(post_list):
                    print("글 리스트 내의 번호를 입력해주세요.\n\n")

                else:
                    post_list.pop(post_number - 1)
                    print("글이 정상적으로 삭제 되었습니다.\n\n")
                    from main import Main

                    Main()

            except Exception:
                print("숫자를 입력해 주세요.\n\n")
