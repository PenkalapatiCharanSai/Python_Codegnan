import csv

#? read content from csv file
# with open(file = "users.csv", mode = "r") as file:
#     reader_obj = csv.reader(file)
#     print(reader_obj)
#     for row in reader_obj:
#         print(row)


#? add one or more new rows into csv file
# with open(file = "users.csv", mode = "a",newline="") as file:
#     writer_obj = csv.writer(file)
#     user_data = [4,'charan',12]
#     writer_obj.writerow(user_data)
#     users_data =[[5,'sai',13], [6,'kumar',14]]
#     writer_obj.writerows(users_data)
#     print("content added")

#? Update id - 5 class as 10
with open("users.csv","r+",newline="") as file:
    reader_obj = csv.reader(file)
    
    # finding id 5
    users = list(reader_obj)
    for rowno in range(len(users)):
        if users[rowno][0] == str(5):
            users[rowno][2] = 10
            break
    file.seek(0)
    print(users)
    writer_obj = csv.writer(file)
    writer_obj.writerows(users)
    print("Content Updated")