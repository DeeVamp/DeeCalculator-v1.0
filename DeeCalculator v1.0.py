# Import external libraries to use their functions

import math


# This is a switch for program , True is On , False is Off

active = True

# create a while loop so that our program will keep running everything inside as long as its Active(True)

while active == True :

    # get numbers from user

    print('***  Welcome to DeeCalculator v1.0  ***')

    print ('''
            Select An Operation from the List below : 
            1 - Add
            2 - Substract
            3 - Multiply
            4 - Divide
            5 - Square
            6 - Square Root
            
            0 - To Exit The Program !''')

    print("")


    # make a simple UI for the user to select which operation to use

    # using a try/except method to handle errors
    # because anything except integers , like special characters and letters will cause an error
    
    while True :
        try :
            Selected_Operation = int(input("Selected Operation : "))
            break
        except ValueError :
            print ("ValueError : Please Use Numbers Only !")


    print # a simple print for neatness !

    

    # using if/else statements for simplicity
 
    while Selected_Operation == 1 :
        try :
            First_Number = int(input("Enter Your First Number : "))
            Second_Number = int(input("Enter Your Second Number : "))
            Result = First_Number + Second_Number
            print ('Add {} to {}'.format(First_Number , Second_Number))
            print ('Result : {} + {} = {}'.format(First_Number , Second_Number , Result))
        except NameError :
            print ("NameError : Please Use Numbers Only !")

        except SyntaxError :
            print ("SyntaxError : Please Use Numbers Only !")

        except TypeError :
            print ("TypeError : Please Use Numbers Only !")

        except AttributeError :
            print ("AttributeError : Please Use Numbers Only !")

        except ValueError :
            print ("ValueError : Please Use Numbers Only !")
 

    while Selected_Operation == 2 :
        try :
            First_Number = int(input("Enter Your First Number : "))
            Second_Number = int(input("Enter Your Second Number : "))
            Result = First_Number - Second_Number
            print('Substract {} from {}'.format(First_Number , Second_Number))
            print ('Result : {} - {} = {}'.format(First_Number , Second_Number , Result))
        except NameError :
            print ("NameError : Please Use Numbers Only !")

        except SyntaxError :
            print ("SyntaxError : Please Use Numbers Only !")

        except TypeError :
            print ("TypeError : Please Use Numbers Only !")

        except AttributeError :
            print ("AttributeError : Please Use Numbers Only !")

        except ValueError :
            print ("ValueError : Please Use Numbers Only !")


    while Selected_Operation == 3 :
        try :
            First_Number = int(input("Enter Your First Number : "))
            Second_Number = int(input("Enter Your Second Number : "))
            Result = First_Number * Second_Number
            print('Multiply {} by {}'.format(First_Number , Second_Number))
            print ('Result : {} * {} = {}'.format(First_Number , Second_Number , Result))

        except NameError :
            print ("NameError : Please Use Numbers Only !")

        except SyntaxError :
            print ("SyntaxError : Please Use Numbers Only !")

        except TypeError :
            print ("TypeError : Please Use Numbers Only !")

        except AttributeError :
            print ("AttributeError : Please Use Numbers Only !")

        except ValueError :
            print ("ValueError : Please Use Numbers Only !")

    while Selected_Operation == 4 :
        try :
            First_Number = int(input("Enter Your First Number : "))
            Second_Number = int(input("Enter Your Second Number : "))
            Result = First_Number // Second_Number
            print('Divide {} to {}'.format(First_Number , Second_Number))
            print ('Result : {} / {} = {}'.format(First_Number , Second_Number , Result))
        except NameError :
            print ("NameError : Please Use Numbers Only !")

        except SyntaxError :
            print ("SyntaxError : Please Use Numbers Only !")

        except TypeError :
            print ("TypeError : Please Use Numbers Only !")

        except AttributeError :
            print ("AttributeError : Please Use Numbers Only !")

        except ValueError :
            print ("ValueError : Please Use Numbers Only !")

    while Selected_Operation == 5 :
        try :
            square_num = int(input("The Number You want to Calculate its Square : "))
            Result = square_num * square_num
            print ("Square of {} is : '{}'".format(square_num , Result))
        except NameError :
            print ("NameError : Please Use Numbers Only !")

        except SyntaxError :
            print ("SyntaxError : Please Use Numbers Only !")

        except TypeError :
            print ("TypeError : Please Use Numbers Only !")

        except AttributeError :
            print ("AttributeError : Please Use Numbers Only !")

        except ValueError :
            print ("ValueError : Please Use Numbers Only !")

    while Selected_Operation == 6 :
        try :  
            squareroot_num = int(input("Enter the number you want to Calculate its Square Root : "))
            Result = math.sqrt(squareroot_num)
            print ("Square Root of {} is : '{}'".format(squareroot_num , Result))

        except NameError :
            print ("NameError : Please Use Numbers Only !")

        except SyntaxError :
            print ("SyntaxError : Please Use Numbers Only !")

        except TypeError :
            print ("TypeError : Please Use Numbers Only !")

        except AttributeError :
            print ("AttributeError : Please Use Numbers Only !")

        except ValueError :
            print ("ValueError : Please Use Numbers Only !")

    while Selected_Operation == 0 :
        active = False
        print ("***  Thank You for Using DeeCalculator v1.0  ***")
        break
        
