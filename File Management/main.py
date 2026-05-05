# with open(file = "sample.txt", mode = "w") as file:
#     string = """Hi, Hello
#     I am from Python Full Stack - 051 Student. """ 
#     file.write(string)
#     print("file created and contents also added")



## opening an existing file in write mode
# with open(file = "sample.txt", mode = "w") as file:
#     string = """Hi, Hello
#     Myself Charan Sai. """ 
#     file.write(string)
#     print("content added")


## Reading content from a file
# with open(file = "sample.txt", mode = "r") as file:
#     file_data = file.read() # read() return entire file content a single string 
#     print("File Content is:",file_data)


## Append Mode
with open(file = "sample.txt", mode = "a") as file:
    string = """Hi, Hello 
 I am from Python Full Stack - 051 Student. """ 
    file.write(string)
    print("content added")
