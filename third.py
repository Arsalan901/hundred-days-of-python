def main ():
    print("Well come to Mini Calculator")
    
    print("Enter 1 for Addition \n Enter 2 for subtraction \n Enter 3 for Multiplication \n Enter 4 fo Division ")

while True: 

        choice = input("Enter your choice 1/2/3/4: ")


        if choice in  ('1','2','3','4'):
              num1 = float(input("Enter Your First Number: "))
              num2 =float(input("Enter Your second Number: "))
              if choice == '1':
                    print("Result: " , (num1+num2))

              elif choice == '2':
                    print("Result: " , (num1-num2))

              elif choice == '3':
                    print("Result: " (num1*num2))

              elif choice =='4':
                    if num2 == 0:
                          print("Error! Divsion with zero ")
                    else:
                          print("Result: ", (num1/num2))
        else :
           print ("Invalid Input!")
        again = input("Do You want to perform another calculation (yes/No): ")
        if again.lower() != 'yes':
              break
