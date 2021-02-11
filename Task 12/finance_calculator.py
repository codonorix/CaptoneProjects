import math

#**************************************# Task 12 #**************************************#
#the lines below just print information
print("Chose either \'investment\' or \'bond\' from the menu below to proceed:")

print("investment   - to calculate the amount of interest you\'ll earn on interest.")
print("bond         - to calculate the amount you'll have to pay on a home load.")
print("")

user_input = str(input())       #This gets the users input for the options
user_input = user_input.lower() #This changes the users input to lowercase so that the input is not case sensitive

#**************************************# Investment Option #**************************************#

if user_input == 'investment':                                                                               #This checks if the users input was ivestment and the requests the users information
    deposite = float(input("Please enter the amount you'd like you deposite: "))
    interest_rate = int(input("Please enter the interest rate (Please note you do NOT need to add a %, just a numer): "))
    investment_period = int(input("Please enter the number of years you'll be investing for: "))
    
    interest = str(input("Please selecte the interest type you\'d like to use \'simple\' or \'compound\': ")) #We then ask them what interest they'll be using
    interest = interest.lower()                                                                               #Then we change it to lower case so that it's not case sensitive
    
    interest_rate_calc = interest_rate / 100                                       #We divide it by 100 to calculate the interest
    
    if interest == 'simple':                                                       #Checks if the user typed "simple"
        total_on_invest = deposite*(1 + interest_rate_calc * investment_period)    #Calculates the deposite plust simple interest
        total_on_invest = round(total_on_invest, 2)                                #This rounds it down to 2 decimal places
        
        print(f"Your total outcome will be: {total_on_invest}")
        
    elif interest == 'compound':                                                   #Checks if the user typed compound
        total_on_invest = deposite * math.pow((1 + interest_rate_calc), investment_period) #calculates the deposite with coundpoubnd interest
        total_on_invest = round(total_on_invest, 2)                                #Rounds the answer down to 2 decimal places
        
        print(f"Your total outcome will be: R{total_on_invest}")
    
    else:
        print("You entered an incorrect value, please try again.")                #Stay safe value, so that the user sees the error
        
#**************************************# Bond Calculation #**************************************#

elif user_input == 'bond': #The below all requests the users info
    house_value = float(input("Please enter the value of the house: "))
    interest_rate = float(input("Please enter your interest rate (Please note you must NOT add a % just the number): "))
    months_payback = float(input("How many months would you like to pay off the house?"))
     
    interest_rate = interest_rate / 100
    interest_rate = interest_rate / 12
    
    pay_per_month = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months_payback)) #This is the monthly paypack formula, we divide by 12 to get the monthly value
    pay_per_month = round(pay_per_month, 2) #Rounds the answer to 2 decimal places
    
    print(f"Your monthly payback on your loan will be: R{pay_per_month}")
    
#**************************************# incorrect string #**************************************#

else:
    print("You entered an incorrect value. Please try again.") #Stay safe code incase they don't enter bond or investment