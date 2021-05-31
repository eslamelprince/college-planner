def insert_course(course):
    y = {count_courses() + 1 : course}
    x = open("class.dat", "a")
    x.write( str(y) + "\n")
    x.close()

def count_courses():
    f = open("class.dat", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
    f.close()
    return count