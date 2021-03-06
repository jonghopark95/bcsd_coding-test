import os
import sys
from .post import Post

# Board Class는 많은 역할을 담당하고 있다.
# guide_board : 메뉴를 선택하기 위한 출력문을 생성한다.
# handle_guide_board_input : 1 ~ 5 사이의 숫자를 사용자에게 요청한다.
# show_post : 조회 기능을 사용할 때 실행하는 메소드이다.
# create_post : 작성 기능을 사용할 때 실행하는 메소드이다.
# delete_post : 삭제 기능을 사용할 때 실행하는 메소드이다.
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
        # 기능적으로는 단지 가지고 있는 post_list를 순회하며 값을 뿌려주는 것 뿐이다.
        # formatting을 위해 코드가 길어졌다.
        print("{0:<20} {1:<20} {2:<20} {3:<20}\n".format("글 번호", "제목", "작성자", "작성일"))
        for post in post_list:
            print(
                "{0:<20} {1:<20} {2:<20} {3:<20}".format(
                    f"#{post_list.index(post) + 1}",
                    post["title"],
                    post["writer"],
                    post["created_at"],
                )
            )

        post_number = int(input("내용을 보고 싶다면 번호를 고르세요 (뒤로 가기 : 0)\n\n # : "))

        # 사용자가 글 리스트 내의 번호를 입력하지 않을 경우, 재요청한다.
        if post_number > len(post_list):
            os.system("clear")
            print("글 리스트 내의 번호를 입력해주세요.\n\n")
            self.show_post()

        # 취소를 선택하였을 시 메인으로 다시 돌아간다.
        elif post_number == 0:
            os.system("clear")
            from main import Main

            Main()

        # 사용자가 유효한 값을 입력했을 경우 해당 값에 맞는 데이터를 보여준다.
        else:
            post = self.post_data[post_number - 1]
            os.system("clear")
            print(f'내용 : {post["content"]}\n')

            self.show_post()

    def create_post(self, post_list):
        while True:
            try:
                title = input("글 제목을 입력해주세요. \n 제목 : ")
                content = input("글 내용을 입력해주세요. \n 내용 : ")

                # 사용자가 입력란에 공백을 입력할 경우 입력 재요청을 한다.
                if title == "" or content == "":
                    print("입력란에 공백은 허용되지 않습니다.\n")

                # 사용자에게 저장할 것인지 요청한다.
                else:
                    while True:
                        check = input(
                            f"\n\n\t제목 : {title}\n\t내용 : {content}\n 저장하시겠습니까? (Y / N)\t"
                        )

                        # 사용자가 저장을 원할 시 해당 데이터를 추가해주고 초기화면으로 보내준다.
                        if check == "Y" or check == "y":
                            post_list.append(
                                Post(title, content, "관리자").set(),
                            )
                            print("\n성공적으로 저장되었습니다.\n\n\n")
                            from main import Main

                            Main()

                        # 사용자가 저장을 원하지 않을 시 초기화면으로 보내준다.
                        elif check == "N" or check == "n":
                            print("\n저장되지 않았습니다.\n\n\n")
                            from main import Main

                            Main()

                        # 유효하지 않은 값을 입력할 시 재요청한다.
                        else:
                            print("\n유효하지 않은 입력입니다.\n\n\n")

            except Exception:
                print(Exception)

    def delete_post(self, post_list):

        while True:
            try:
                # 삭제에 앞서 현재 리스트를 보여준다.
                for post in post_list:
                    print(
                        "#{0}\t {1:<20} {2:<20} {3:<20}".format(
                            post_list.index(post) + 1,
                            post["title"],
                            post["writer"],
                            post["created_at"],
                        )
                    )

                post_number = int(input("삭제할 글을 고르세요\n\n # : "))

                # 사용자에게 삭제를 원하는 글 id를 요청한다.
                if post_number > len(post_list):
                    print("글 리스트 내의 번호를 입력해주세요.\n\n")

                # 유효한 값일 시 해당 글을 삭제한다.
                else:
                    post_list.pop(post_number - 1)
                    print("글이 정상적으로 삭제 되었습니다.\n\n")
                    from main import Main

                    Main()

            except Exception:
                print("숫자를 입력해 주세요.\n\n")
