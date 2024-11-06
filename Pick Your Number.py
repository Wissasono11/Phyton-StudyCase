import random

def main() -> None:
    while True:
        number: int = random.randint(1, 10)
        guess: int = 0

        print("Welcome to my game!")
        print("Silly game! Guess number between 1 and 10")
        
        while guess != number:
            try:
                guess: int = int(input("Guess the number: "))
            except ValueError:
                print("Input the valid number, fool!")
                continue 

            if guess < number:
                print("Too small like your D!")
            elif guess > number:
                print("Too big you asshole!")
            else:
                print(f"Congratulations! This thumbs for you brother 👍, the number is {number} ")
        
        opsi: str = str(input("Try again? (yes/no): ")).lower

        if opsi != "yes":
            print("Thank you for playing with me, goodbye.")
        break

if __name__ == "__ main__":
    main()