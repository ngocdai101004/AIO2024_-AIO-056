from Person import Person
from Teacher import Teacher
from Doctor import Doctor
from Student import Student


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        doctor_count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                doctor_count += 1
        return doctor_count

    def sort_age(self):
        self.people.sort(key=lambda person: person._yob)

    def compute_average(self):
        total_age = 0
        num_teachers = 0
        for person in self.people:
            if isinstance(person, Teacher):
                total_age += person._yob
                num_teachers += 1
        average_age = total_age / num_teachers
        return average_age


if __name__ == "__main__":
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    student1 = Student(name="studentA", yob=2010, grade="7")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name=" Ward1 ")
    ward1 . add_person(student1)
    ward1 . add_person(teacher1)
    ward1 . add_person(teacher2)
    ward1 . add_person(doctor1)
    ward1 . add_person(doctor2)
    ward1 . describe()

    print(f"\nNumber of doctors : {ward1.count_doctor()}")

    print("\nAfter sorting Age of Ward1 people ")
    ward1 . sort_age()
    ward1 . describe()

    print(f"\nAverage year of birth ( teachers ): {ward1 . compute_average()}")
