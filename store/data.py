def insert_course(course):
    y = { course.course_number : course}
    x = open("data.dat", "a")
    x.write( str(y) + "\n")
    x.close()

def retrieve_course():
    f = open("data.dat", "r")
    print(f.read())
    f.close()

def delete_courese(course):
    f = open("data.dat", "r")
    search_course(course)
    lines = f.readlines()
    x = 0
    y = 0
    for i in lines:
        y += 1
        if course in i:
            x += 1
            break
        else:
            course == None
    if x == 1:
        del lines[y - 1]
        new_lines = open("data.dat", "w+")
        for line in lines:
            new_lines.write(line)
        new_lines.close()
        print("course deleted")
    f.close

def count_courses():
    f = open("data.dat", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
    f.close()
    return count

def search_course(course):
    f = open("data.dat", "r")
    lines = f.readlines()
    x = 0
    for i in lines:
        if course in i:
            print(i)
            x += 1
            break
        elif course == "x":
            x +=1
        else:
            course == None
    if x == 0:
        print("given class not found")
    f.close()

