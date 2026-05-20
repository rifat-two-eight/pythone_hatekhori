class Teacher():
    
    college_name = "sherpur govt college"


    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome teacher",self.name)

    def get_marks(self):
        return self.marks

t1= Teacher("kashem",55)

print(t1.name)
print(t1.marks)
print(t1.college_name)
print(t1.get_marks())
