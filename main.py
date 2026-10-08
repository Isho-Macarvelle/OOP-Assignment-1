#Creating a class for Course 
class Course:
    def __init__(self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title
    def display_course(self):
        print("Course Code:", self.course_code)
        print("Course Title:", self.course_title)

#Creating a class for Student
class Student:
    student_count = 0
    def __init__(self, student_ID, student_name, student_age, student_course):
        self.student_ID = student_ID
        self.student_name = student_name
        self.student_age = student_age
        self.student_course = student_course
        Student.student_count += 1

#Defining a method to display student information
    def display_student(self):
        print("Student ID: ", self.student_ID)
        print("Student Name: ", self.student_name)
        print("Student Age(yrs): ", self.student_age)
        print("Course Code: ", self.student_course.course_code)
        print("Course Title: ", self.student_course.course_title)
        print("-----------------------------")

    @classmethod
    def total_registered_students(cls):
        return cls.student_count

course1 = Course("BICT101", "Bsc. in Information and Communication Technology")
course2 = Course("BSEM101", "Bsc. in Software Engineering and Management")
course3 = Course("BBIT101", "Bsc. in Business Information Technology")

#Creating Student Objects and adding them to a list
students = []

student1 = Student(905004568, "Barba M Dumbuya", 20, course1)
student2 = Student(905006090, "Alusine Kamara", 25, course2)
student3 = Student(905007623, "Mohamed LA Kamara", 22, course3)
student4 = Student(905005667, "Abu Kamara", 25, course1)
student5 = Student(905004523, "Alpha Seasay", 24, course3)

students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)

#Display Student Information
for student in students:
    student.display_student()

#Display Total Registered Students
print("Total Registered Students: ", Student.total_registered_students())