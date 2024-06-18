from Person import Person


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name : {self._name} - YoB : {self._yob} - Specialist : {self._specialist}")


if __name__ == "__main__":
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1 . describe()
