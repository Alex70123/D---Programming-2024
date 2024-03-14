while True:
        response = input("Helooo, welcomeeee to McDO, Would you like ENORMOUSLY SIZED fries with your meal?: ").strip().lower()
        if response == 'yes':
            print("Great choice! Adding ENORMOUSLY SIZED fries to your meal.")
            break
        elif response == 'no':
            print("No problem! Enjoy your meal without ENORMOUSLY SIZED fries.")
            break
        else:
            print(f"Sorry, I didn't understand'{response}'.would you like ENORMOUSLY SIZED fries? Please try again.")