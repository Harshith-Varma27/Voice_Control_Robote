import serial

bluetooth_port = "COM12"  # Ensure this is correct
baud_rate = 9600

try:
    ser = serial.Serial(bluetooth_port, baud_rate, timeout=1)
    print(f"Connected to {bluetooth_port}")
    
    # Keep the connection open
    while True:
        pass  # Keeps the script running in the background

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Bluetooth connection closed.")
