# Student Learning Portal

## 1. Project Overview

The Student Learning Portal is a Python-based educational application developed using Object-Oriented Programming (OOP) concepts.

The system demonstrates how classes, objects, methods, and Python data structures can be used to manage student and course information.

The project was developed for the OOP1 assignment under the Education domain.

## 2. Problem Statement

Educational institutions need simple ways to organize student and course information.

This project provides a simple Python-based solution that allows student objects to be created, associated with course objects, stored in a list, and displayed using a loop.

## 3. Objectives

The main objectives of the project are:

- To demonstrate Object-Oriented Programming concepts.
- To create and use classes and objects.
- To demonstrate interaction between Student and Course objects.
- To use a Python list to store multiple student objects.
- To demonstrate instance and class methods.
- To apply Digital Public Goods (DPG) principles.

## 4. OOP Concepts Used

### Course Class

The Course class stores course information such as:

- Course code
- Course title

### Student Class

The Student class stores:

- Student ID
- Student name
- Student course

The Student object is associated with a Course object.

## 5. Python Data Structure

The project uses a Python list:

students = []

The list stores multiple Student objects.

The append() method is used to add student objects to the list.

A for loop is then used to display the students.

## 6. Methods

### Instance Methods

The project uses instance methods such as:

- display_course()
- display_student()

These methods work with individual objects.

### Class Method

The project uses:

@classmethod
def total_students(cls):

This method returns the total number of Student objects created.

## 7. Sample Output

Student ID:  905004568
Student Name:  Barba M Dumbuya
Student Age(yrs):  20
Course Code:  BICT101
Course Title:  Bsc. in Information and Communication Technology
-----------------------------
Student ID:  905006090
Student Name:  Alusine Kamara
Student Age(yrs):  25
Course Code:  BSEM101
Course Title:  Bsc. in Software Engineering and Management
-----------------------------
Student ID:  905007623
Student Name:  Mohamed LA Kamara
Student Age(yrs):  22
Course Code:  BBIT101
Course Title:  Bsc. in Business Information Technology
-----------------------------
Student ID:  905005667
Student Name:  Abu Kamara
Student Age(yrs):  25
Course Code:  BICT101
Course Title:  Bsc. in Information and Communication Technology
-----------------------------
Student ID:  905004523
Student Name:  Alpha Seasay
Student Age(yrs):  24
Course Code:  BBIT101
Course Title:  Bsc. in Business Information Technology
-----------------------------
Total Registered Students:  5

## 8. Digital Public Goods (DPG) Alignment

### Open-source

The project source code and documentation have been uploaded to GitHub so that the solution can be viewed, studied, and reused.

### Inclusive and Accessible Design

The program uses clear labels, descriptive names, and simple output to make the information easy to understand.

### Privacy-respecting

The program uses fictional student information for demonstration purposes and does not store sensitive personal data.

### Modular and Reusable

The program separates Student and Course responsibilities into different classes. Methods are used to organize functionality, making the code easier to maintain and reuse.

## 9. How to Run the Program

1. Install Python.
2. Download or clone the project from GitHub.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run:

python main.py

## 10. Future Improvements

Future versions could include:

- Searching for students.
- Updating student information.
- Removing student records.
- Adding more courses.
- Adding a simple user interface.