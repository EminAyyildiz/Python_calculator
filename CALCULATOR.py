
print("Written by EMİN AYYILDIZ")
while True:
    operation = str(input("Enter the symbol you want to perform : (+,-,*,/,**, !)   :"))
    if operation=='0' :
        break

    first_number = int(input("Please enter a number         :"))
    second_number = int(input("Please enter another number   :"))

    if operation=='+': #The calculations to be taken if the selection is '+'.

        print('The result of the addition operation      :'  ,first_number +second_number)
    elif operation=='-':#The calculations to be taken if the selection is '-'.

        print("Your subtraction result                   :" ,(first_number)-(second_number))
    elif operation == '*':#The calculations to be taken if the selection is '*'.
        print("Your multiplication result                :", first_number * second_number)
    elif operation == '/': #The calculations to be taken if the selection is '/'.
        print("Your division result                      : ", first_number/second_number)
    elif operation == '**':#The calculations to be taken if the selection is '**'.
        print("Your exponential expression result        : ", first_number**second_number,)
    elif operation == '!': #The calculations to be taken if the selection is '!'.
        sayi = 1
        sayi2 =1
        for i in range(first_number):
            sayi = sayi * (i + 1)
        print("First number factorial value   : ", sayi)
        for a in range(second_number):
            sayi2 = sayi2 * (a + 1)
        print("Second number factorial value : ", sayi2)

    else:# Warning message that the user will encounter in any wrong entry
        print("ERROR PLEASE PAY ATTENTION")

##The message that the user will see when he/she wants to exit the system
print("BYE BYE")