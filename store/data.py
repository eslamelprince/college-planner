def insert_course(course):
    x = open("data.dat", "a")
    x.write(str(course) + "\n")
    x.close()

def retrieve_course():
    f = open("data.dat", "r")
    print(f.read())
def delete_courese():
    print("delete_courese")