#university system display information
class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        self.lecturers = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def display_info(self):
        print(f"\n University: {self.name}")
        print("\n Courses Offered:")
        for course in self.courses:
            print(f" - {course}")
        
        print("\n Students:")
        for student in self.students:
            print(f" - {student}")
        
        print("\n Lecturers:")
        for lecturer in self.lecturers:
            print(f" - {lecturer}")


# Sample data
uni = University("Makerere University")

uni.add_course("Software Engineering")
uni.add_course("Data Science")
uni.add_course("Information Systems")

uni.add_student("Sebabe Abdu")
uni.add_student("Haalima Namuli")

uni.add_lecturer("Dr. Muwanguzi")
uni.add_lecturer("Prof. Nabirye")

# Display all information
uni.display_info()
