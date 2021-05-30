class Course:
    semester = "spring 2021"
    subject = "Introduction to Computer Science"
    credit_hours = 3
    prerequests = "Math 113"
    location = "online"

    def __init__(self, semester):
        self.semester = semester
    def __str__(self):
        return "[" + self.semester + ", " + self.subject + ", " + self.credit_hours + ", " + self.prerequests + ", " + self.location + "]"
    def __repr__(self):
       return str(self)