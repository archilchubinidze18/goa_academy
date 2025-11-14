# Simple text adventure game in Python

def intro():
    print("🌲 Welcome to the Forest Adventure! 🌲")
    print("You wake up in a mysterious forest. You see two paths ahead.")
    print("1. Take the left path")
    print("2. Take the right path")
    choice = input("Choose (1 or 2): ")
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("You stand still until night falls... Game over.")
        
def left_path():
    print("\nYou take the left path and find a small cottage.")
    print("Do you want to enter?")
    print("1. Yes")
    print("2. No")
    choice = input("Choose (1 or 2): ")
    if choice == "1":
        print("\nInside, you find treasure! 💰 You win!")
    else:
        print("\nYou walk away... and get lost. 😵 Game over.")

def right_path():
    print("\nYou take the right path and meet a hungry wolf 🐺!")
    print("Do you want to fight or run?")
    print("1. Fight")
    print("2. Run")
    choice = input("Choose (1 or 2): ")
    if choice == "1":
        print("\nYou bravely fight but the wolf is too strong... 🩸 Game over.")
    else:
        print("\nYou run fast and escape to safety! 🏃 You win!")

intro()
