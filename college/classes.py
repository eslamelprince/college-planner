class classes:
    semester = "spring-2021"
    class_num = "MATH-101"
    credit_hours = 1
    grade = "A"

    def __init__(self, semester):
        self.semester = semester
        self.class_num = ""
        self.credit_hours = 0
        self.grade = "" 

    def __str__(self):
        return   self.class_num + ", " + self.semester + ", " + self.credit_hours + ", " + self.grade 

    def __repr__(self):
       return str(self)