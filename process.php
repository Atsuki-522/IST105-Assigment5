<?php
    $number = escapeShellarg($_POST["number"]);
    $text = escapeShellarg($_POST["text"]);
    
    $command = escapeshellcmd("python3 process.py $number $text");
    $output = shell_exec($command);
    
    echo $output;
?>