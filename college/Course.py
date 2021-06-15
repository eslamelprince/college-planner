class Course:
    name = "Introduction to Computer Science"
    course_number = "CS-112"
    credit_hours = 3
    prerequests = []
    location = "online"

    def __init__(self, course_number):
        self.name = ""
        self.course_number = course_number
        self.prerequests = []
        self.credit_hours = 0 
        self.location = ""

    def __str__(self):
        return  self.name + ", " + self.course_number + ", " + self.credit_hours + ", " + str(self.prerequests) + ", " + self.location

    def __repr__(self):
       return str(self)