print("Welcome this is a quiz game called <<How do you enter a club?!>>\n")
name = input("What is your name?: ")

print(f"\nWelcome {name}, lets find out how you enter a club!!!\n")

user_input=""

while True:
    user_input = input("Are you ready? (Type yes or no): ")

    if user_input.lower() == "yes":        
        print("What item do you hold when you enter a club?")
        break
    elif user_input.lower() == "no":        
        print("Better go home")
        exit()
    else:
        print("Type yes or no") 

while True:
    user_item = input("I hold: ")

    if user_item.upper() == name.upper():
        print("That is your name fool!\n")
        continue
    elif user_item.upper()[0] == name.upper()[0]:
        print(">>>YOU ENTER!<<<\n")
        #playing = False
        continue
    else:
        print("--You don't enter!--\n")
        continue