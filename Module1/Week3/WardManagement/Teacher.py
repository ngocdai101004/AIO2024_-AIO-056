from Person import Person


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name : {self._name} - YoB : {self._yob} - Subject : {self._subject}")


if __name__ == "__main__":
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1 . describe()
