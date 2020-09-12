from datetime import datetime


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
