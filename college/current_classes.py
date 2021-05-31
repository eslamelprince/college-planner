from college.classes import classes

def print_current_class_menu():
    semester = input("semester: ")
    classes1 = classes(semester)
    classes1.course_num = input("course number: ")
    classes1.grade = input("grade: ")
    return classes1