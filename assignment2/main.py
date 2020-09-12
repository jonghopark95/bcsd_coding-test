# How to Run : python3 main.py

# Person 클래스는 이름, 찍기 패턴을 인스턴스 변수로 가진다.
class Person:
    """ Normal Person Class """

    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern


class Main:
    """ Main Class """

    answer_list = "12543341243245321345"

    def __init__(self):
        self.a = Person("A", "1524")
        self.b = Person("B", "134")
        self.c = Person("C", "123454321")

        print(f"문제의 답은 {self.answer_list} 입니다.")
        self.show_result(self.a, self.check_num_corrects(self.a))
        self.show_result(self.b, self.check_num_corrects(self.b))
        self.show_result(self.c, self.check_num_corrects(self.c))

    # show_result는 수험자가 몇개를 찍어서 맞췄는지 보여주는 메소드이다.
    def show_result(self, person, num_corrects):
        print(f"{person.name}가 맞춘 것은 총 {num_corrects}개이다.")

    # check_num_corrects는 answer_list와 찍기 패턴을 비교한다.
    # 찍기 패턴을 순차적으로 비교하며 문항 수가 패턴의 길이보다 길어지면 다시 처음부터 찍기 패턴을 비교한다.
    # 정답을 맞출 경우 몇 개를 맞췄는지 체크하다 모든 비교가 끝나면 이를 반환한다.
    def check_num_corrects(self, person):
        num_corrects = 0
        index_pattern = 0

        for answer in self.answer_list:
            if answer == person.pattern[index_pattern]:
                num_corrects += 1

            index_pattern += 1

            if index_pattern == len(person.pattern):
                index_pattern = 0

        return num_corrects


Main()
