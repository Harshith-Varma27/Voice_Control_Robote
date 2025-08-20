<?php
// Run Python script to release only the process using COM12
$output = shell_exec("C:\\Users\\natra\\Anaconda3\\python.exe backend/release_com.py 2>&1");

if (strpos($output, "released") !== false) {
    echo json_encode(["status" => "success", "message" => "🔴 Bluetooth Disconnected (COM12 Released)"]);
} else {
    echo json_encode(["status" => "error", "message" => "❌ Failed to release COM12."]);
}
?>
