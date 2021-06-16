from college.Course import Course
from store import data
from store import clazz
from college import enter_classes
from college import view_classes
from college import current_classes
course_list = []
while(1==1):
    print("1.enter classes")
    print("2.view classes")
    print("3.enter classes taken")
    print("4.view classes taken")
    print("5.find class")
    print("6.delete class")
    print("7.delete taken class")
    print("8.exit")
    x = input("select a number from the menu: ")
    if x == str(1) :
        print("Enter classes")
        course = enter_classes.print_enter_class_menu()
        course_list.append(course)
        data.insert_course(course)
        print(course)
    elif x == str(2):
        print("View classes")
        data.retrieve_course()
    elif x == str(3):
        print("enter classes taken")
        classes = current_classes.print_current_class_menu()
        clazz.insert_course(classes)
        print(classes)
    elif x == str(4):
        print("view classes taken")
        clazz.retrieve_course()
    elif x == str(5):
        print("find class")
        Class = data.search_course(input("type course number: "))
    elif x == str(6):
        print("delete class")
        data.delete_courese(input("type course number: "))
    elif x == str(7):
        print("delete taken class")
        clazz.delete_courese(input("type course number: "))
    elif x == str(8):
        print("goodbye")
        break


