class human:
    nationality = "Viet Nam"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        print(f"{self.name} is now studying python")
    def playgame(self):
        print(f"{self.name} was busted because of playing game in training class")
    def sing(self):
        print("sing random")
    def __str__(self):
        return f"{self.name} {self.age}"

student = human("Vinh", "18")
print(f"my student's name is {student.name}")
print(f"my student's age is {student.age}")
print(student.sing())