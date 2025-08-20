import socket
import serial
import time

# Bluetooth Serial Configuration
BLUETOOTH_PORT = "COM11"  # Ensure this is correct
BAUD_RATE = 9600

# Server Configuration
SERVER_IP = "127.0.0.1"  # Localhost
SERVER_PORT = 12345

# Initialize Bluetooth connection
try:
    ser = serial.Serial(BLUETOOTH_PORT, BAUD_RATE, timeout=1)
    print(f" Connected to Bluetooth Module on {BLUETOOTH_PORT}")
except serial.SerialException as e:
    print(f" Bluetooth Connection Failed: {e}")
    exit(1)

# Initialize Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(1)
print(f" Server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    conn, addr = server.accept()
    print(f" Connection from {addr}")

    while True:
        try:
            # Receive command from client
            command = conn.recv(1024).decode().strip()
            if not command:
                break  # No command received, break loop

            print(f" Received Command: {command}")

            # Ensure Bluetooth connection is open
            if ser.is_open:
                time.sleep(0.5)  # Small delay for stability
                formatted_command = command.lower() + "#"  # Add '#' delimiter

                ser.write(formatted_command.encode())  # Send command
                print(f" Sent to Bluetooth: {formatted_command}")

                conn.sendall(" Command sent to Bluetooth".encode())  # Confirm to client
            else:
                print("⚠ Bluetooth serial port is closed!")
                conn.sendall("⚠ Bluetooth serial port is closed!".encode())

        except Exception as e:
            print(f" Error: {e}")
            conn.sendall(f" Error: {e}".encode())
            break

    conn.close()
    print(" Client disconnected.")

ser.close()
