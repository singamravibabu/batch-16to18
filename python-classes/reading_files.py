# f_obj = open("sample.txt", "r")
# open
contents = open("courses.txt", "r")

# reading
text = contents.read()
print(text)

# closing
contents.close()