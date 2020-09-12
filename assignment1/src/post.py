from datetime import datetime

# Post Class는 글 제목, 내용, 작성자, 비밀번호를 받는다.
# 비밀번호는 익명 게시판을 위해 필요한 변수로, 나머지 게시판은 요구하지 않으므로 디폴트로 공백을 넣어준다.
# 생성일을 표시하기 위해 datetime 모듈을 사용하였다.
class Post:
    """ Post Class """

    def __init__(self, title, content, writer, password=""):
        self.title = title
        self.content = content
        self.writer = writer
        self.password = password
        self.created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def set(self):
        return {
            "title": self.title,
            "content": self.content,
            "writer": self.writer,
            "password": self.password,
            "created_at": self.created_at,
        }
