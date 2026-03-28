import getpass as gp
secret_num = int(gp.getpass("Enter a secret number: "))
count = 1
while True:
    guess = int(input("Enter your guess: "))
    if count >= 5:
        print("Game Over!!")
        break
    
    else:
        if guess == secret_num:
            print("Congratulations!!")
            print(f"Congratulations!! Your Lives: {5-count}")
            break
        else:
            print(f"Try again... Your Lives Remaining: {5-count}")
    count += 1