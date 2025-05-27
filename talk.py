import speech_recognition as sr
import time
import os

def listen_and_write():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Create or open a notepad file
    file_path = "voice_notes.txt"
    
    print("Voice-to-Text Program Started")
    print("Speak now (or say 'exit' to stop the program)...")
    
    try:
        while True:
            # Listen to microphone
            with sr.Microphone() as source:
                print("\nListening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                
            try:
                # Convert speech to text
                text = recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                
                # Check if user wants to exit
                if text.lower() == "exit":
                    print("Exiting program...")
                    break
                
                # Write to notepad file
                with open(file_path, "a") as file:
                    file.write(text + "\n")
                    print(f"Text written to {file_path}")
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                
    except KeyboardInterrupt:
        print("\nProgram stopped by user")

if __name__ == "__main__":
    listen_and_write()
