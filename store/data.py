def insert_course(course):
    y = {count_courses() + 1 : course}
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
    if (int(course)) > len(lines):
        course == None
    else:
        del lines[int(course)-1]
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
    if (course == "x"):
        course == None
    elif (int(course)) > len(lines):
        print("given class not found")
        course == None
    else:
        print(lines[int(course) - 1])
    f.close()

