# import random module

import random

# Definr lists of subjects, actions and places for the headlines. They should be in the indian version

indian_subjects = ["Shahrukh khan", "Virat kohli", "Niramala sitaraman", "Allu arjun", "Vamshi"]
indian_actions = ["launches", "kills", "eats", "says", "buys"]
indian_places = ["in hyderabad", "metro station", "idli", "assi ghat"]

#Create a loop to generate random headlines.

while True:
    subject = random.choice(indian_subjects)
    action = random.choice(indian_actions)
    place = random.choice(indian_places)
    # Print the generated fake headline
    headline = f"BREAKING NEWS:{subject} {action} {place}"
    print("\n" + headline)
    # Ask the user if they want to generate another headline
    user_input = input("\nDo you want another headline?(yes/no):").strip().lower()
    
    if user_input == "no":
        print("Thank you for using fake news headlines generator. Have a funny day!")