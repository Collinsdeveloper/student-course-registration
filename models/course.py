class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = capacity

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "trainer_name": self.trainer_name,
            "capacity": self.capacity
        }

    def display(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Trainer: {self.trainer_name}")
        print(f"Capacity: {self.capacity}")
        print("-" * 30)