import cgi
import random
import math

# フォームデータを取得
form = cgi.FieldStorage()
user_number = int(form.getvalue("user_number"))
user_text = form.getvalue("user_text")

# 数字の処理
if user_number % 2 == 0:
    number_result = f"The number {user_number} is even. Its square root is {math.sqrt(user_number):.2f}."
else:
    number_result = f"The number {user_number} is odd. Its cube is {user_number ** 3}."

# テキストの処理
binary_text = ' '.join(format(ord(char), '08b') for char in user_text)
vowel_count = sum(1 for char in user_text.lower() if char in "aeiou")

text_result = f"Binary: {binary_text}<br>Vowel Count: {vowel_count}"

# トレジャーハント
secret_number = random.randint(1, 100)
attempts = []
for i in range(5):
    guess = random.randint(1, 100)  # シミュレーションのためランダム
    if guess == secret_number:
        attempts.append(f"Attempt {i+1}: {guess} (Correct!)")
        break
    elif guess > secret_number:
        attempts.append(f"Attempt {i+1}: {guess} (Too high!)")
    else:
        attempts.append(f"Attempt {i+1}: {guess} (Too low!)")

treasure_result = "<br>".join(attempts)
if secret_number in [int(a.split()[1]) for a in attempts]:
    treasure_result += "<br>You found the treasure!"
else:
    treasure_result += "<br>You did not find the treasure."

# 結果を出力（PHPへ返す）
print("Content-type: text/html\n")
print(f"""
<html>
<head><title>Results</title></head>
<body>
<h2>Results</h2>
<p>{number_result}</p>
<p>{text_result}</p>
<p>{treasure_result}</p>
</body>
</html>
""")
