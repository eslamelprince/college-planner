from store import data
from store import clazz
from college.classes import classes
import re

def insert_class(clazz):
    y = {clazz.semester : clazz}
    x = open("clazz.dat", "a")
    x.write( str(y) + "\n")
    x.close()

def count_classes():
    f = open("clazz.dat", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
    f.close()
    return count

def retrieve_class():
    f = open("clazz.dat", "r")
    print(f.read())
    f.close()

def search_classes(clazz):
    f = open("clazz.dat", "r")
    lines = f.readlines()
    x = 0
    class_found = ""
    for i in lines:
        if clazz in i or clazz in i.lower():
            print(i)
            class_found = i
            x += 1
            break
        elif clazz == "x":
            x +=1
        else:
            clazz == None
    if x == 0:
        print("given class not found")
    f.close()
    return class_found

def delete_classes(clazz):
    f = open("clazz.dat", "r")
    search_classes(clazz)
    lines = f.readlines()
    x = 0
    y = 0
    for i in lines:
        y += 1
        if clazz in i or clazz in i.lower():
            x += 1
            break
        else:
            clazz == None
    if x == 1:
        del lines[y - 1]
        new_lines = open("clazz.dat", "w+")
        for line in lines:
            new_lines.write(line)
        new_lines.close()
        print("class deleted")
    f.close

def semester_search(clazz):
    f = open("clazz.dat", "r")
    lines = f.readlines()
    x = 0
    if clazz == "all":
        retrieve_class()
    else:
        for i in lines:
            if clazz in i or clazz in i.lower():
                print(i)
                x += 1
            elif clazz == "x":
                x +=1
            else:
                clazz == None
        if x == 0:
            print("given class not found")
    f.close()

def build_semester(course_number):
    classes.class_num = course_number
    f = open("clazz.dat", "r")
    lines = f.readlines()
    
    s = data.search_course(course_number)
    start = s.find("[") + 1 
    end = s.find("]", start)
    prereq = s[start:end]
    prereq_list = list(prereq.split(","))

    credit_hour_list = list(s.split(","))
    credit_hours = credit_hour_list[2]

    print(prereq_list)

    x = 0
    for a in prereq_list:
        for i in lines:
            if a in i:
                x += 1

    if prereq_list == ['']:
        x = 1
    if x == (len(prereq_list)):
        print("1.yes")
        print("2.no")
        add_class = input("would you like to add this class: ")
        if add_class == "1": 
            semester = input("semester: ")
            classes1 = classes(semester)
            classes1.class_num = "'" + course_number + "'"
            classes1.credit_hours = credit_hours
            classes1.grade = "N/A"
            insert_class(classes1)
            print("class added")
            
        if add_class == "2":
            print("class not added")
    if x != (len(prereq_list)):
        print("prerequisite not met")

def gpa():
    f = open("clazz.dat", "r")
    lines = f.readlines()
    total = []
    credit_hour_subtotal = []
    for i in lines:
        x = list(i.split(","))
        y = x[3]
        start = y.find(" ") + 1 
        end = y.find("}", start)
        grade = y[start:end]
        z = x[2]
        grade_point = 0

        if z == "  1":
            credit_hour = 1
        elif z == "  2":
            credit_hour = 2
        elif z == "  3":
            credit_hour = 3
        elif z == "  4":
            credit_hour = 4

        credit_hour_total = 0
        total_point = 0

        if grade == "A+":
            grade_point = grade_point + 4.0
        elif grade == "A":
            grade_point = grade_point + 4.0
        elif grade == "A-":
            grade_point = grade_point + 3.7
        elif grade == "B+":
            grade_point = grade_point + 3.3
        elif grade == "B":
            grade_point = grade_point + 3.0
        elif grade == "B-":
            grade_point = grade_point + 2.7
        elif grade == "C+":
            grade_point = grade_point + 2.3
        elif grade == "C":
            grade_point = grade_point + 2.0
        elif grade == "C-":
            grade_point = grade_point + 1.7
        elif grade == "D":
            grade_point = grade_point + 1.0
        elif grade == "F":
            grade_point = grade_point + 0.0
        subtotal = credit_hour * int(grade_point)

        if grade == "N/A":
            subtotal = None
        else:
            total.append(subtotal)
            credit_hour_subtotal.append(credit_hour)
    
    for i in total:
        total_point += i
    for b in credit_hour_subtotal:
        credit_hour_total += b
    total_gpa = total_point / credit_hour_total
    print("total GPA: ")
    print(total_gpa)
    f.close