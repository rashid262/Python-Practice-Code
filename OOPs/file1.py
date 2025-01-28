class School:
    # Class variable
    school_name = "Global High School"

    def __init__(self, student_name, grade):
        # Instance variables
        self.student_name = student_name
        self.grade = grade

    def display_info(self):
        # Accessing instance and class variables
        print(f"Student Name: {self.student_name}, Grade: {self.grade}, School: {School.school_name}")

# Creating objects (instances)
student1 = School("Alice", "5th")
student2 = School("Bob", "6th")

# Accessing instance variables
student1.display_info()
student2.display_info()

# Modifying the class variable
School.school_name = "National High School"

# Accessing after modifying the class variable
student1.display_info()
student2.display_info()
