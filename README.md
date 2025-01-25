# voice-chat-bot

This is a voice-based chatbot that uses speech recognition to interact with users and performs sentiment analysis on their input to generate responses. It is powered by various Python libraries including pyttsx3 for text-to-speech functionality, speech_recognition for voice input, and nltk for sentiment analysis.

Features:
Voice Interaction: The chatbot listens to user input and responds via speech.
Sentiment Analysis: The chatbot analyzes the sentiment of the user's message and responds accordingly.
Multi-Language Support: It can detect the language of the input and translate it to English if needed using Google Translate.
Various Responses: The chatbot can respond based on the sentiment of the input message (Positive, Negative, or Neutral).
Exit Option: The chatbot can exit gracefully when the user says goodbye or quit.
Requirements:
Python 3.x
nltk library for sentiment analysis
pyttsx3 for text-to-speech
speech_recognition for recognizing voice commands
googletrans for language translation
Installation:
Clone the repository:

bash
Copy
Edit
git clone <repository_url>
Install the required libraries:

bash
Copy
Edit
pip install nltk pyttsx3 speechrecognition googletrans==4.0.0-rc1
Download the necessary NLTK datasets:

python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('stopwords')
How to Run:
Once everything is set up, simply run the script:
bash
Copy
Edit
python voice_assistant_chatbot.py
The assistant will start by greeting you and asking how your day is going. After that, you can chat with the assistant, and it will respond based on your inputs.
Example Interaction:
vbnet
Copy
Edit
You: Hi
Assistant: Hello! How's your day?
You: It's going great!
Assistant: That's great to hear!
You: Bye
Assistant: Bye! Have a great day!
Notes:
Ensure that your microphone is working properly for the voice recognition to function.
If you encounter issues with the speech_recognition library, check your microphone settings or the library's documentation for troubleshooting.
You can modify or extend the chatbot's responses and functionality to suit your requirements.
License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments:
nltk library for sentiment analysis and text processing.
pyttsx3 for text-to-speech conversion.
speech_recognition for voice input functionality.
googletrans for language translation.
