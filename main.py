from collage import entry_classes
from collage.Course import Course
from collage import enter_classes
while(1==1):
    print("1.enter classes")
    print("2.view classes")
    print("3.exit")
    x = input("select a number from the menu: ")
    if x == str(1) :
        print("Enter classes")
        course = enter_classes.print_enter_class_menu()
    elif x == str(2):
        print("View classes")
    elif x == str(3):
        print("goodbye")
        break


