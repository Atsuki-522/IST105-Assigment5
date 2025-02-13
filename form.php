<!DOCTYPE html>
<html>
<head>
    <title>Interactive Treasure Hunt</title>
</head>
<body>
    <h2>Welcome to the Interactive Treasure Hunt!</h2>
    <form action="process.php" method="POST">
        <label>Enter a Number (e.g., birth year):</label>
        <input type="number" name="user_number" required><br><br>
        
        <label>Enter a Text Message (e.g., name or secret word):</label>
        <input type="text" name="user_text" required><br><br>
        
        <input type="submit" value="Solve the Puzzle">
    </form>
</body>
</html>
