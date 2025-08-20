import speech_recognition as sr
import serial

bluetooth_port = "COM12"  # Ensure this is correct
baud_rate = 9600

def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")  # For debugging
        return command
    except sr.UnknownValueError:
        print("Speech not understood.")
        return None
    except sr.RequestError:
        print("Speech recognition service error.")
        return None

try:
    # Use the existing Bluetooth connection
    ser = serial.Serial(bluetooth_port, baud_rate, timeout=1)

    command = record_voice()
    
    if command:
        ser.write((command + "#").encode())  # Append '#' to mark end
        print(f"Sent: {command}")  # Output for PHP extraction
    else:
        print("No command recognized.")

    ser.close()
except serial.SerialException as e:
    print(f"Error: {e}")
