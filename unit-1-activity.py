# Function to check if a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "an even number"
    else:
        return "an odd number"

# Main program
def main():

    # Greet the user
    print("Hello! How are you?")
    response = input()

    # Get user's age
    age = int(input("What's your age?"))

    # Ask another question
    print("What's your favorite color?")
    favorite_color = input()

    # Display user's information
    print(f"WOW! you're {age} years old! and your favorite color, is {favorite_color}?, mine as well!")
    
    # Check if the age is even or odd
    age_type = check_even_odd(age)
    print(f"Your age is {age_type}.")

    # Convert age to months
    age_in_months = age * 12
    print(f"Your age in months is {age_in_months}!")
if __name__ == "__main__":
    main()