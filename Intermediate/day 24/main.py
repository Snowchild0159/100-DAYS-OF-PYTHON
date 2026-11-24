# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


#if you don't want to forget to close your files:

# with  open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# #this will replace the text on your file:
# with  open("my_file.txt", mode="w") as file:
#     file.write("snow")


# #append text to your file:
# with  open("my_file.txt", mode="a") as file:
#     file.write("\n new text.")


# #creating new file also!
# with  open("new_file.txt", mode="w") as file:
#     file.write("bomboclat wallahi.")


#open file whn its on another place by its absoloute path: 
# with open("/home/snow/my_file.txt") as file: 
#     content = file.read()
#     print(content)

#open file using releative path:
with open("../../../../../my_file.txt") as file: 
    content = file.read()
    print(content)
