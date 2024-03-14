# Create a function called translate
# Accepts a string
# Replace all 100 with 💯
# Replace all noodles with  🍜
# Return the result
# Author: Alex
# 37 Feburary 2024

def translate(input_str):

    # Replace '100' with :100:
    translated_str = input_str.replace('100', ':💯:')
    
    # Replace 'noodles' with :ramen:
    translated_str = translated_str.replace('noodles', ':🍜:')
    return translated_str
