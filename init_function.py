class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
      
    def show(self):
        print("My Name is",self.name,"\n","My RollNo is",self.rollno)
obj=student("Jatin",29)
obj.show()


