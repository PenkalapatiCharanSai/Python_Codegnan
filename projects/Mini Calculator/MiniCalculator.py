# importing required modules
# syntax: import filename

# importing function from another module
# syntax: from filename import function
import addition
import subtraction
import multiplication
import division
# giving alias for module
# ex: import multiplication as Mul

# Main
if __name__ == "__main__":
    print("Welcome to the Calculator")  
    print("Select your operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5.Exit")     
    while True:
        choice = int(input("Enter your choice(1-5) "))
        #print("Select your operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5.Exit")
        if choice == 1:
            x, y = map(int,input("Enter two numbers seperated by space:").split())
            res = addition.addition(a = x, b = y)
            print(res)
        elif choice == 2:
            x, y = map(int,input("Enter two numbers seperated by space:").split())
            res = subtraction.subtraction(a = x, b = y)
            print(res)
        elif choice == 3:
            x, y = map(int,input("Enter two numbers seperated by space:").split())
            res = multiplication.multiplication(a = x, b = y)
            print(res)
        elif choice == 4:
            x, y = map(int,input("Enter two numbers seperated by space:").split())
            res = division.division(a = x, b = y)
            print(res)
        elif choice == 5:
            print("Bye Bye Charan....")
            exit()
        else:
            print("Invalid operation selection")





