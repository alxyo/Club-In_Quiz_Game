print("Welcome this is a quiz game called <<CLUB-IN>>\n")
name = input("What is your name?: ")
age=int(input("How old are you?: "))

if age < 18:
    print("Better go home!!!")
    exit()

print(f"\nWelcome {name}, find 10 items in a row to enter the club!!!\n")

while True:
    user_input = input("Are you ready? (Type yes or no): ")

    if user_input.lower() == "yes":        
        print("\nWhat item do you hold when you enter a club?\n")
        break
    elif user_input.lower() == "no":        
        print("\nBye Bye\n")
        exit()
    else:
        print("\nType yes or no") 

enter_tries = 1

while True:
    user_item = input("I hold: ")

    if user_item.upper() == name.upper():
        print("That is your name fool!\n")
        continue
    elif user_item.upper()[0] == name.upper()[0]:
        print("That's a right item ",enter_tries,"/10\n")
        enter_tries+=1
        if enter_tries == 11:
            print("Welcome to the club!\n")
            exit()
    else:
        print("Security Check\n")
        enter_tries=1
        continue