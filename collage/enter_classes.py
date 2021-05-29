from collage.Course import Course

def print_enter_class_menu():
    semester = input("semester :")
    course = Course(semester)
    course.subject = input("subject :")
    course.credit_hours = input("credit hours :")
    course.prerequisists = input("prerequisits :")
    course.location = input("location :")
    return course
