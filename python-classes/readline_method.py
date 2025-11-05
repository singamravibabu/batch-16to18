with open("courses.txt", "r") as file:
    c1 = file.readline()
    c2 = file.readline()
    c3 = file.readline()
    print(c1,c2,c3, sep="", end="")