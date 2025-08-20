import socket
import speech_recognition as sr

# Server Configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

def send_command(command):
    """Sends the voice command to the server after formatting it."""
    try:
        formatted_command = command.strip().lower() + "#"  # Convert to lowercase and add "#"

        # Connect to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, SERVER_PORT))

        print(f" Sending: {formatted_command}")

        # Send command
        client.sendall(formatted_command.encode())

        # Receive response
        response = client.recv(1024).decode()
        print(f" Server Response: {response}")

        # Close connection
        client.close()

    except Exception as e:
        print(f" Client Error: {e}")

def recognize_voice():
    """Captures voice input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak a command...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source)  # Listen to user
            command = recognizer.recognize_google(audio)  # Convert speech to text
            print(f" Recognized: {command}")
            return command
        except sr.UnknownValueError:
            print(" Could not understand the audio. Try again.")
            return None
        except sr.RequestError:
            print(" Could not request results. Check your internet connection.")
            return None

# 🏁 Run only once when executed
command = recognize_voice()
if command:
    send_command(command)
