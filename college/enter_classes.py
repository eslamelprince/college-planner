from college.Course import Course
from store import data

def print_enter_class_menu():
    course_num = input("course number :")
    course = Course(course_num)
    course.name = input("name :")
    course.credit_hours = input("credit hours :")
    while (1==1):
        prepeq = input("prerequests :")
        data.search_course(prepeq)
        if (prepeq == "x"):
            prepeq = ""
            break
        else:
            course.prerequests.append(prepeq)
    course.location = input("location :")
    return course
