import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import random
import time
import os

def hindi_chatbot():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Define responses
    english_responses = [
        "Hello! How can I help you today?",
        "That's interesting. Tell me more.",
        "I understand. What else would you like to talk about?",
        "Nice to chat with you!",
        "I'm here to assist you. What's on your mind?",
        "That's a good point. How are you feeling today?",
        "I see. Would you like to know more about something?",
        "I appreciate our conversation. What else would you like to discuss?"
    ]
    
    hindi_responses = [
        "नमस्ते! मैं आपकी कैसे मदद कर सकती हूँ?",
        "यह दिलचस्प है। मुझे और बताएं।",
        "मैं समझती हूँ। आप और किस बारे में बात करना चाहेंगे?",
        "आपसे बात करके अच्छा लगा!",
        "मैं आपकी सहायता के लिए यहां हूं। आप क्या सोच रहे हैं?",
        "यह एक अच्छी बात है। आज आप कैसा महसूस कर रहे हैं?",
        "मैं समझती हूं। क्या आप किसी चीज के बारे में अधिक जानना चाहेंगे?",
        "मैं हमारी बातचीत की सराहना करती हूं। आप और किस बारे में बात करना चाहेंगे?"
    ]
    
    # Function to speak text with female voice
    def speak_text(text, language='en'):
        # Create temporary file for audio
        temp_file = "temp_audio.mp3"
        # Generate speech with Google TTS (female voice)
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(temp_file)
        # Play the audio
        playsound(temp_file)
        # Clean up by removing the temporary file
        try:
            os.remove(temp_file)
        except:
            pass
    
    # Greeting
    print("Hindi-English Chatbot Started with Female Voice")
    print("Speak in Hindi or English. Say 'goodbye' or 'अलविदा' to exit.")
    greeting = "Hello! I'm your bilingual assistant with a female voice. How can I help you today?"
    print(f"Chatbot: {greeting}")
    speak_text(greeting)
    
    chatting = True
    
    while chatting:
        try:
            # Listen to microphone
            with sr.Microphone() as source:
                print("\nListening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                
            try:
                # Try to recognize as English first
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"You said (English): {text}")
                
                # Check if it's a goodbye
                if "goodbye" in text.lower() or "bye" in text.lower():
                    response = "Goodbye! Have a nice day!"
                    print(f"Chatbot: {response}")
                    speak_text(response)
                    chatting = False
                    continue
                
                # Give an English response
                response = random.choice(english_responses)
                print(f"Chatbot: {response}")
                speak_text(response, 'en')
                
            except:
                # If English recognition fails, try Hindi
                try:
                    text = recognizer.recognize_google(audio, language="hi-IN")
                    print(f"आपने कहा (हिंदी): {text}")
                    
                    # Check if it's a goodbye in Hindi
                    if "अलविदा" in text.lower():
                        response = "अलविदा! अच्छा दिन हो!"
                        print(f"चैटबॉट: {response}")
                        speak_text(response, 'hi')
                        chatting = False
                        continue
                    
                    # Respond in Hindi
                    response = random.choice(hindi_responses)
                    print(f"चैटबॉट: {response}")
                    speak_text(response, 'hi')
                    
                except sr.UnknownValueError:
                    response = "Sorry, I couldn't understand that."
                    print(response)
                    speak_text(response)
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

                    
                
        except KeyboardInterrupt:
            print("\nChatbot terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    hindi_chatbot()