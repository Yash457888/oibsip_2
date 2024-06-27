                                             # Project-2 [ BMI( BODY MASS INDEX CALCULATOR)] , Level-1


Height = float(input("Enter your Height in Centemeters: "))
Weight = float(input("Enter your Weight in Kg's: "))

Height = Height/100
BMI = Weight/(Height*Height)

print("Your Body Mass Index is :", BMI)

if(BMI>0):
    if(BMI<16):
        print("You are severely Underweight")
    elif(BMI >= 18.5 and BMI <= 18.5):
        print("You are Underweight")
    elif(BMI >= 18.5 and BMI < 25):
        print("You are Healthy")
    elif(BMI >= 25 and BMI < 30):
        print("You are Overweight")
    elif(BMI >= 30):
        print("You are Obese")
else:
    print("Please enter valid details.....")


# Steps to execution of code :
# (1) First, Enter your Height in Centemeters , for example 156
# (2) Secondly, Enter your Weight in Kg's , for example 62
# (3)  Now , Finally you will get the Status of your BMI( Body Mass Index ).
         
                                                                 
                                                                  # THANK YOU