import sys
import math
import random


def trasurenumber_puzzle(number):
    
    if number % 2 == 0:
        
        return ['even',f"sqrt is {math.sqrt(number)}"]
    else:
        
        return ['odd',f"cube is {number ** 3}"]

def text_puzzle(text):
    
    binary_list = []
    for char in text:
        ascii_code = ord(char)
        binary = format(ascii_code, '08b')
        binary_list.append(binary)
    binary_text = ' '.join(binary_list)

    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1

    return [binary_text, vowel_count]

def treasurehunter_hunt():
    attempts = 5
    attempt_count = 0
    
    target = random.randint(1, 100)
    html_output = f"<p>- The secret number is {target}.</p>"
    

    while attempt_count < attempts:
        guess = random.randint(1, 100)
        attempt_count += 1
        if guess == target:
            html_output += f"""
            <p>-Attempt {attempt_count}: {guess} (Correct!)</p>
            <p>You found the treasure in {attempt_count} attempts!</p>"""
            return html_output
        else:
            if guess > target:
                html_output += f"<p>-Attempt {attempt_count}: {guess} (Too high!)</p>"
            else:
                html_output += f"<p>-Attempt {attempt_count}: {guess} (Too low!)</p>"
    return html_output

if __name__ == "__main__":
    number = int(sys.argv[1])
    text = sys.argv[2]
    
    oddOrEven,number_result = trasurenumber_puzzle(number)
    binary,vowel = text_puzzle(text)
    treasure_result = treasurehunter_hunt()

    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Calculation Results</title>
    </head>
    <body>
    <h2>Number Puzzle:</h2>
    <p>- The number {number} is {oddOrEven}. Its {number_result}.</p>
    <h2>Text Puzzle:</h2>
    <p>- Binary: {binary}</p>
    <p>- Vowel Count: {vowel}</p>
    <h2>Treasure Hunt:</h2>
    {treasure_result}
    </body>
    </html>
    """
    print(f"{html_output}")