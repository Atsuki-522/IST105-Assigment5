<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input Form</title>
</head>
<body>
    <h2>Welcome to the Interactive Treasure Hunt</h2>
    <h2>Enter your details to solve the puzzle and find the treasures</h2>
    <form action="process.php" method="POST">
        <div>
            <label for="number">Enter a Number(e.g., birth year):</label>
            <input type="number" id="number" name="number" required/>
        </div>
        <div>
            <label for="text">Enter a Text(e.g., name or secret word):</label>
            <input type="text" id="text" name="text" required/>
        </div>
        <button type="submit">Solve the Puzzle!</button>
    </form>
</body>
</html>
