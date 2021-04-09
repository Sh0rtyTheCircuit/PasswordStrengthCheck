#judging the strength of passwords based on length and most common passwords

#Top 10 passwords list + noteworthy passwords
top_passwords = ("password", "123456", "nothing", "secret", "admin", "iloveyou")

def PasswordCheck():
    password = input("Your password: ")

    if (len(password) >= 13):
        #if the user input contains any words from the top 10 passwords
        if any(password.find(s) >=0 for s in top_passwords):
            print ("Medium-well")
        else:
        #user input is greater than 13 characters and has no words from the top 10 passwords
            print ("Hard-Core Warrior!")
    else:
        print ("Easy-Peasy")

def main():
    print ("How strong is your password? Enter it below")
    while True:
        #Loops main
        PasswordCheck()
main()