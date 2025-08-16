import os

import random

class Student:
    educational_platform = "udemy"
    
    def __init__(self, name, age = 34):
        self.name = name
        self.age = age

    def greet(self):
        greetings = ["Hi, I'm ", "Hey there, my name is ", "Hi. Oh, my name is "]

        return random.choice(greetings) + self.name


names = ["Alice", "Lebron", "Dawit", "Carson", "Justin", "Lucky"]

for student in names:
  student = Student(student)
  print(student.greet())