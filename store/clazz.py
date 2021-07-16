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
    if x == (len(prereq_list)):
        print("1.yes")
        print("2.no")
        add_class = input("would you like to add this class: ")
        if add_class == "1": 
            semester = input("semester: ")
            classes1 = classes(semester)
            classes1.class_num = course_number
            classes1.credit_hours = credit_hours
            classes1.grade = "N/A"
            insert_class(classes1)
            print("class added")
            
        if add_class == "2":
            print("class not added")
    if x != (len(prereq_list)):
        print("prerequisite not met")
