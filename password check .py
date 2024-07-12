#to check if the password is of min 8 characters contains 1 number, 1 letter, 1 special character

#first take the input

print("Enter your password")


#this will convert the input in string and store in password
#we are finding the length by len and storing it in lengthofpassword

password = str(input())
lengthofpasword = len(password)

print("Your password has", lengthofpasword, "characters")

#here we are first checking if the input received has more than 8 characters

if lengthofpasword < 8:
    print("the password should be of min 8 characters")

else:
    print("Checking the password")

#checking if the the password contains letters, number, special character
# .isaplha() is to check if string contain character A-Z, a-z

firstcharacter = password[0:1]
print(firstcharacter)

firstcharacteraplha = firstcharacter.isalpha()
firstcharactercheck = firstcharacter.isnumeric()
firstcharacterspecial = firstcharacter.isascii()

if (firstcharacteraplha == True):
    print("the string is a alphabet")
elif (firstcharacteraplha == False):
        if (firstcharactercheck == True):
             print("the string is a number")
        elif (firstcharacterspecial == True):
             print("the string is special character")

secondcharacter = password[1:2]
print(secondcharacter)

secondcharacteraplha = secondcharacter.isalpha()
secondcharactercheck = secondcharacter.isnumeric()
secondcharacterspecial = secondcharacter.isascii()

if (secondcharacteraplha == True):
    print("the string is a alphabet")
elif (secondcharacteraplha == False):
        if (secondcharactercheck == True):
             print("the string is a number")
        elif (secondcharacterspecial == True):
             print("the string is special character")

thirdcharacter = password[2:3]
print(thirdcharacter)

thirdcharacteraplha = thirdcharacter.isalpha()
thirdcharactercheck = thirdcharacter.isnumeric()
thirdcharacterspecial = thirdcharacter.isascii()

if (thirdcharacteraplha == True):
    print("the string is a alphabet")
elif (thirdcharacteraplha == False):
        if (thirdcharactercheck == True):
             print("the string is a number")
        elif (thirdcharacterspecial == True):
             print("the string is special character")

fourtcharacter = password[3:4]
print(fourtcharacter)

fourtcharacteraplha = fourtcharacter.isalpha()
fourtcharactercheck = fourtcharacter.isnumeric()
fourtcharacterspecial = fourtcharacter.isascii()

if (fourtcharacteraplha == True):
    print("the string is a alphabet")
elif (fourtcharacteraplha == False):
        if (fourtcharactercheck == True):
             print("the string is a number")
        elif (fourtcharacterspecial == True):
             print("the string is special character")

fifthcharacter = password[4:5]
print(fifthcharacter)

fifthcharacteraplha = fifthcharacter.isalpha()
fifthcharactercheck = fifthcharacter.isnumeric()
fifthcharacterspecial = fifthcharacter.isascii()

if (fifthcharacteraplha == True):
    print("the string is a alphabet")
elif (fifthcharacteraplha == False):
        if (fifthcharactercheck == True):
             print("the string is a number")
        elif (fifthcharacterspecial == True):
             print("the string is special character")


sixthcharacter = password[5:6]
print(sixthcharacter)

sixthcharacteraplha = sixthcharacter.isalpha()
sixthcharactercheck = sixthcharacter.isnumeric()
sixthcharacterspecial = sixthcharacter.isascii()

if (sixthcharacteraplha == True):
    print("the string is a alphabet")
elif (sixthcharacteraplha == False):
        if (sixthcharactercheck == True):
             print("the string is a number")
        elif (sixthcharacterspecial == True):
             print("the string is special character")



seventhcharacter = password[6:7]
print(seventhcharacter)

seventhcharacteraplha = seventhcharacter.isalpha()
seventhcharactercheck = seventhcharacter.isnumeric()
seventhcharacterspecial = seventhcharacter.isascii()

if (seventhcharacteraplha == True):
    print("the string is a alphabet")
elif (seventhcharacteraplha == False):
        if (seventhcharactercheck == True):
             print("the string is a number")
        elif (seventhcharacterspecial == True):
             print("the string is special character")



eigthcharacter = password[7:8]
print(eigthcharacter)

eigthcharacteraplha = eigthcharacter.isalpha()
eigthcharactercheck = eigthcharacter.isnumeric()
eigthcharacterspecial = eigthcharacter.isascii()

if (eigthcharacteraplha == True):
    print("the string is a alphabet")
elif (eigthcharacteraplha == False):
        if (eigthcharactercheck == True):
             print("the string is a number")
        elif (eigthcharacterspecial == True):
             print("the string is special character")

print("Your password is a mix of numbers,letters and special characters. GOOD JOB!")









