import json
import os

from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = {}

    # -------------------------
    # Student Methods
    # -------------------------

    def add_student(self):
        student_id = input("Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        if self.find_student(student_id):
            print("Student ID already exists.")
            return

        name = input("Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        email = input("Email: ").strip()

        if "@" not in email:
            print("Invalid email.")
            return

        phone = input("Phone Number: ").strip()

        if not phone:
            print("Phone number cannot be empty.")
            return

        student = Student(
            student_id,
            name,
            email,
            phone
        )

        self.students.append(student)

        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        keyword = input(
            "Enter Student ID or Name: "
        ).lower()

        found = False

        for student in self.students:
            if (
                keyword == student.student_id.lower()
                or keyword in student.name.lower()
            ):
                student.display()
                found = True

        if not found:
            print("Student not found.")

    # -------------------------
    # Course Methods
    # -------------------------

    def add_course(self):
        course_id = input("Course ID: ").strip()

        if not course_id:
            print("Course ID cannot be empty.")
            return

        if self.find_course(course_id):
            print("Course ID already exists.")
            return

        course_name = input(
            "Course Name: "
        ).strip()

        if not course_name:
            print("Course name cannot be empty.")
            return

        trainer_name = input(
            "Trainer Name: "
        ).strip()

        try:
            capacity = int(
                input("Capacity: ")
            )

            if capacity <= 0:
                print(
                    "Capacity must be greater than zero."
                )
                return

        except ValueError:
            print("Capacity must be a number.")
            return

        course = Course(
            course_id,
            course_name,
            trainer_name,
            capacity
        )

        self.courses.append(course)

        print("Course added successfully.")

    def view_courses(self):
        if not self.courses:
            print("No courses available.")
            return

        for course in self.courses:
            course.display()

    # -------------------------
    # Registration Methods
    # -------------------------

    def register_student(self):
        student_id = input(
            "Student ID: "
        ).strip()

        course_id = input(
            "Course ID: "
        ).strip()

        student = self.find_student(student_id)
        course = self.find_course(course_id)

        if not student:
            print("Student not found.")
            return

        if not course:
            print("Course not found.")
            return

        if course_id not in self.registrations:
            self.registrations[course_id] = []

        if student_id in self.registrations[course_id]:
            print(
                f"{student.name} is already registered "
                "for this course."
            )
            return

        if (
            len(self.registrations[course_id])
            >= course.capacity
        ):
            print(
                "Registration failed. "
                "This course is already full."
            )
            return

        self.registrations[course_id].append(
            student_id
        )

        print(
            f"{student.name} successfully "
            f"registered for "
            f"{course.course_name}."
        )

    def view_students_in_course(self):
        course_id = input(
            "Course ID: "
        ).strip()

        if course_id not in self.registrations:
            print(
                "No students registered."
            )
            return

        print("\nRegistered Students")

        for student_id in self.registrations[course_id]:
            student = self.find_student(student_id)

            if student:
                print(
                    f"{student.student_id} - "
                    f"{student.name}"
                )

    def view_courses_for_student(self):
        student_id = input(
            "Student ID: "
        ).strip()

        student = self.find_student(student_id)

        if not student:
            print("Student not found.")
            return

        found = False

        print(
            f"\nCourses for {student.name}"
        )

        for course_id, students in (
            self.registrations.items()
        ):
            if student_id in students:
                course = self.find_course(
                    course_id
                )

                if course:
                    print(
                        f"{course.course_id} - "
                        f"{course.course_name}"
                    )
                    found = True

        if not found:
            print(
                "No courses registered."
            )

    # -------------------------
    # Helper Methods
    # -------------------------

    def find_student(self, student_id):
        for student in self.students:
            if (
                student.student_id
                == student_id
            ):
                return student
        return None

    def find_course(self, course_id):
        for course in self.courses:
            if (
                course.course_id
                == course_id
            ):
                return course
        return None

    # -------------------------
    # Save Data
    # -------------------------

    def save_data(self):
        with open(
            "data/students.json",
            "w"
        ) as file:
            json.dump(
                [s.to_dict()
                 for s in self.students],
                file,
                indent=4
            )

        with open(
            "data/courses.json",
            "w"
        ) as file:
            json.dump(
                [c.to_dict()
                 for c in self.courses],
                file,
                indent=4
            )

        with open(
            "data/registrations.json",
            "w"
        ) as file:
            json.dump(
                self.registrations,
                file,
                indent=4
            )

        print("Data saved successfully.")

    # -------------------------
    # Load Data
    # -------------------------

    def load_data(self):

        if os.path.exists(
            "data/students.json"
        ):
            with open(
                "data/students.json",
                "r"
            ) as file:

                data = json.load(file)

                self.students = [
                    Student(
                        item["student_id"],
                        item["name"],
                        item["email"],
                        item["phone_number"]
                    )
                    for item in data
                ]

        if os.path.exists(
            "data/courses.json"
        ):
            with open(
                "data/courses.json",
                "r"
            ) as file:

                data = json.load(file)

                self.courses = [
                    Course(
                        item["course_id"],
                        item["course_name"],
                        item["trainer_name"],
                        item["capacity"]
                    )
                    for item in data
                ]

        if os.path.exists(
            "data/registrations.json"
        ):
            with open(
                "data/registrations.json",
                "r"
            ) as file:

                self.registrations = (
                    json.load(file)
                )