import random

print("🎯 NUMBER GUESSING GAME 🎯")
print("Maine 1 se 100 ke beech ek number socha hai")
print("Dekh tujhse kitni try mein guess hota hai\n")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Apna guess daal: "))
        attempts += 1
        
        if guess < secret_number:
            print("Chhota hai bhai! Upar soch ⬆️\n")
        elif guess > secret_number:
            print("Bada hai bhai! Neeche soch ⬇️\n")
        else:
            print(f"🏆 JEET GAYA BHAI! Number tha {secret_number}")
            print(f"Total tries: {attempts}")
            if attempts <= 5:
                print("Rank: LEGEND 😎")
            elif attempts <= 10:
                print("Rank: PRO 🔥")
            else:
                print("Rank: Practice karega toh better hoga 💪")
            break
            
    except ValueError:
        print("Bhai number daal, text nahi! 😅\n")

play_again = input("\nPhir khelega? y/n: ")
if play_again.lower() == 'y':
    print("Game restart kar file ko dobara run kar bhai 🚀")
else:
    print("Bye! Accha khela 🔥")
