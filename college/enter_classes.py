from college.Course import Course

def print_enter_class_menu():
    name = input("name :")
    course = Course(name)
    course.credit_hours = input("credit hours :")
    while (1==1):
        prepeq = input("prerequests :")
        if (prepeq == "x"):
            prepeq = ""
            break
        else:
            course.prerequests.append(prepeq)
    course.location = input("location :")
    return course
