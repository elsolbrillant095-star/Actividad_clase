

print("Hey! Jarvis here! I have some things we can do together. But first, what is your name?")
name = input("Name: ")
print(f"Nice to meet you, {name}! Now let's get started. Do you want to know about a new fact, play a game or do you want to hear a joke?")
answer = input("Type 'fact', 'game', or 'joke': ").lower()

if answer == "fact": 
    print("Did you know that honey never spoils? You could theoretically eat 3,000-year-old Egyptian mummy honey and it would be perfectly fine!")


elif answer == "game": 
    tries = 4
    for i in range(1,4,1):
        tries -= 1
        
        print(f"Great! Let's play a quick game of rock, paper, scissors. You have {tries} rounds to play with me!")
        user_choice = input("Your choice (rock/paper/scissors): ").lower()
        import random
        
        choices = ["rock", "paper", "scissors"]
        jarvis_choice = random.choice(choices)
        print(f"Jarvis chose: {jarvis_choice}")
        
        if user_choice == jarvis_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and jarvis_choice == "scissors") or (user_choice == "paper" and jarvis_choice == "rock") or (user_choice == "scissors" and jarvis_choice == "paper"):
            print("You win!")
        else: 
            print("Good try! Jarvis wins")
            
elif answer == "joke": 
    print("How do you call a fake noodle?")
    input()
    print("An impasta!") 
    
else: 
    print("Sorry, I didn't understand that. Please retry and type 'fact', 'game', or 'joke'.") 
    
