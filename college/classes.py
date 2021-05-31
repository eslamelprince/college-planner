class classes:
    semester = "spring 2021"
    course_num = 1
    grade = "A"

    def __init__(self, semester):
        self.semester = semester
        self.course_num = 0
        self.grade = "" 

    def __str__(self):
        return  "[ " + self.semester + ", " + self.course_num + ", " + self.grade + " ]"

    def __repr__(self):
       return str(self)