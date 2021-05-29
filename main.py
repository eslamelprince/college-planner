from collage import entry_classes

print("1.enter classes")
print("2.view classes")
x = input("select a number from the menu: ")
if x == str(1) :
    print("Enter classes")
    entry_classes.print_entry_class_menu()


elif x == str(2):
    print("View classes")
