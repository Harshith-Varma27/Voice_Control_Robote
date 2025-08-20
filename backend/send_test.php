<?php
header('Content-Type: application/json');

$command = 'C:\\Users\\natra\\Anaconda3\\python.exe C:\\xampp\\htdocs\\robotics\\python_scripts\\client_bluetooth.py';
$output = shell_exec($command . ' 2>&1');

echo json_encode([
    "status" => "debug",
    "full_output" => $output  // Show Python script output
]);
?>
