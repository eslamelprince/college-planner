from collage.Course import Course
from collage import enter_classes
from collage import view_classes
course_list = []
while(1==1):
    print("1.enter classes")
    print("2.view classes")
    print("3.exit")
    x = input("select a number from the menu: ")
    if x == str(1) :
        print("Enter classes")
        course = enter_classes.print_enter_class_menu()
        course_list.append(course)
        print(course)
    elif x == str(2):
        print("View classes")
        view_classes.view_class(course_list)
    elif x == str(3):
        print("goodbye")
        break


