def insert_course(course):
    y = {count_courses() + 1 : course}
    x = open("data.dat", "a")
    x.write( str(y) + "\n")
    x.close()

def retrieve_course():
    f = open("data.dat", "r")
    print(f.read())
    f.close()

def delete_courese():
    print("delete_courese")

def count_courses():
    f = open("data.dat", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
    f.close()
    return count

