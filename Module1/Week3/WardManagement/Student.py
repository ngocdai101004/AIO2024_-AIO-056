from Person import Person


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name : {self._name} - YoB : {self._yob} - Grade : {self._grade}")


if __name__ == "__main__":
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1 . describe()
