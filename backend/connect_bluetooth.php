<?php
header('Content-Type: application/json');

// Path to Python script
$pythonPath = "C:\\Users\\natra\\Anaconda3\\python.exe";  // Ensure this is correct
$pythonScript = escapeshellarg("C:\\xampp\\htdocs\\robotics\\python_scripts\\server_bluetooth.py");

// Execute the Python script
$output = shell_exec("$pythonPath $pythonScript 2>&1");

// Check if Bluetooth is connected
if (strpos($output, "Connected to COM") !== false) {
    echo json_encode(["status" => "success", "message" => "✅ Bluetooth Connected"]);
} else {
    echo json_encode(["status" => "error", "message" => "❌ Connection Failed: " . nl2br(htmlspecialchars($output))]);
}
?>
