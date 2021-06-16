class classes:
    semester = "spring 2021"
    course_num = "MATH-101"
    credit_hours = 1
    grade = "A"

    def __init__(self, semester):
        self.semester = semester
        self.course_num = ""
        self.credit_hours = 0
        self.grade = "" 

    def __str__(self):
        return   self.course_num + ", " + self.semester + ", " + self.credit_hours + ", " + self.grade 

    def __repr__(self):
       return str(self)