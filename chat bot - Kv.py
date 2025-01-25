import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import random
import pyttsx3
import speech_recognition as sr
from googletrans import Translator

# Initializing the chatbot's name and its state (sentiment)
chatbot = "KV"
sentiment = ""

# Setting up the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Take microphone input from the user and return it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language=',en-IN')
            return query
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Can you please speak again?")
            return "None"
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Can you repeat?")
            return "None"
        except sr.RequestError:
            speak("There seems to be an issue with the recognition service. Try again later.")
            return "None"

def get_chatbot_response(message):
    from googletrans import Translator
    translator = Translator()

    # Detect language
    detected_lang = translator.detect(message).lang

    # Translate to English if in Hindi
    if detected_lang == 'hi':
        message = translator.translate(message, src='hi', dest='en').text
    """Generate the chatbot's response based on sentiment analysis of the user's message."""
    global sentiment

    # Preprocessing the user's message
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('vader_lexicon', quiet=True)
    nltk.download('stopwords', quiet=True)
    stop_words = stopwords.words('english')
    message = " ".join([word for word in message.split() if word.lower() not in stop_words])

    # Initializing the sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Analyzing the sentiment of the user's message
    sentiment_scores = sia.polarity_scores(message)

    # Classifying the sentiment
    if sentiment_scores['compound'] > 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Generating the chatbot's response based on the user's sentiment
    if sentiment == "Positive":
        chatbot_response = random.choice([
            "That's great to hear!",
            "I'm glad you're feeling that way.",
            "Wow, I'm happy to know you're doing well."
        ])
    elif sentiment == "Negative":
        chatbot_response = random.choice([
            "I'm sorry to hear that.",
            "I understand. It happens.",
            "Don't worry, we'll figure it out."
        ])
    else:
        chatbot_response = random.choice([
            "That's interesting.",
            "I see. Can you tell me more about it?",
            "Alright, how can I help?"
        ])

    # Speak the response
    speak(chatbot_response)
    return chatbot_response

def chatbot_main():
    """Run the chatbot interaction loop."""
    speak(random.choice(["Hi", "Hello", "Hey"]))
    speak("I'm KV ")
    user_message=takeCommand()
    if user_message=="hi" or "hello" or "hey":
     speak("how's your day ?")

    while True:
        user_message = takeCommand()

        if user_message == "None":
            continue

        print(f"You: {user_message}")

        if user_message.lower() in ["bye", "exit", "quit", "goodbye","see you later", "see you soon"]:
            speak("Bye! Have a great day!")
            print(f"{chatbot}: Bye! Have a great day!")
            break

        bot_response = get_chatbot_response(user_message)
        print(f"{chatbot}: {bot_response}")

# Run the chatbot
chatbot_main()
