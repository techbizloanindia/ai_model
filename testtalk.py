import speech_recognition as sr
from deep_translator import GoogleTranslator
import time
import os

def listen_and_translate():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Create or open a notepad file
    file_path = "voice_translation.txt"
    
    # Create header in file if it doesn't exist
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Hindi (Original) | English (Translation)\n")
            file.write("-" * 60 + "\n")
    
    print("Hindi Voice-to-Text and Translation Program Started")
    print("Speak in Hindi (or say 'बंद करो' to stop the program)...")
    
    try:
        while True:
            # Listen to microphone
            with sr.Microphone() as source:
                print("\nListening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                
            try:
                # Convert speech to text (specify Hindi language)
                hindi_text = recognizer.recognize_google(audio, language="hi-IN")
                print(f"Recognized Hindi: {hindi_text}")
                
                # Check if user wants to exit
                if "बंद करो" in hindi_text.lower():
                    print("Exiting program...")
                    break
                
                # Translate text to English
                translator = GoogleTranslator(source='hi', target='en')
                english_text = translator.translate(hindi_text)
                print(f"English Translation: {english_text}")
                
                # Write both to notepad file
                with open(file_path, "a", encoding="utf-8") as file:
                    file.write(f"{hindi_text} | {english_text}\n")
                    print(f"Text written to {file_path}")
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"Error in translation: {e}")
                
    except KeyboardInterrupt:
        print("\nProgram stopped by user")

if __name__ == "__main__":
    listen_and_translate()
