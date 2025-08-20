<?php
header('Content-Type: application/json');

$command = 'C:\\Users\\natra\\Anaconda3\\python.exe C:\\xampp\\htdocs\\robotics\\python_scripts\\client_bluetooth.py';
$output = shell_exec($command . ' 2>&1');  // Capture full output from Python script

// Check if the expected "Sent to Bluetooth:" message is present
if (preg_match('/Sent to Bluetooth:\s*(.*)/', $output, $matches)) {
    $commandSent = trim($matches[1]); 
    echo json_encode(["status" => "success", "message" => "✅ Sent: " . $commandSent]);
} else {
    echo json_encode(["status" => "error", "message" => "❌ Command Not Recognized. Full Output: " . $output]);
}
?>
