class Course:
    name = "Introduction to Computer Science"
    credit_hours = 3
    prerequests = []
    location = "online"

    def __init__(self, name):
        self.name = name
        self.prerequests = []
        self.credit_hours = 0 
        self.location = ""

    def __str__(self):
        return "[" + self.name + ", " + self.credit_hours + ", " + str(self.prerequests) + ", " + self.location + "]"

    def __repr__(self):
       return str(self)