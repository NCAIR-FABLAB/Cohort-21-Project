# IMPORTATION OF NECESSARY LIBRARIES

import os # imports operating system module to interact with the file system and peform OS-level operations
import json # imports the JSON module to work with JSON data
from spitch import Spitch # imports the "Spitch" class from the "spitch" library for the speech-to-text-to-speech functionality

# LOAD API KEY

with open("config.json", "r") as file: # opens the "config.json" file in read mode
    config = json.load(file) # parses the JSON content of the file into a Python dictionary
    api_key = config["API_KEY"] # retrieves the value of "API_KEY" from the dictionary

os.environ["SPITCH_API_KEY"] = api_key # sets the API key as an environment variable named "SPITCH_API_KEY"
client = Spitch() # creates an instance of the "Spitch" class

# N.B: file should be a .wav or .mp3
# Valid Language Codes: 'ha', 'en','yo'

def speech_to_text(file, src, target):
    print("Transcribing...") # message indicating transcription process has started

    with open(file, 'rb') as f: # opens the audio file in binary read mode

        # calls the transcribe method of the "speech" object from the "client" to transcribe the audio content
        response = client.speech.transcribe(
            language=src, # specifies the source language for transcription
            content=f.read(), # reads the binary content of the audio file
        )
    
    print(f'Read Succesfully: {response.text}') # prints the transcribed text

    # calls the translate method of the "text" object from the "client" to translate the transcribed text
    translation = client.text.translate(
        text=response.text, # passes the transcribed text as the text to be translated
        source=src, # specifies the source language of the text
        target=target # specifies the target language for translation
    )

    print(f'Translation Done: {translation.text}') # prints the translated text
    
    return translation.text # returns the translated text as the output of the function
    
# N.B: English voices: 'john', 'lucy', 'lina', 'jude'

def text_to_speech(text, language, voice, output_file):
    
    with open(output_file, 'wb') as f: # opens the specifed output file in binary write mode to save the generated  audio

        # calls the "generate" method of the "speech" object from the "client" to synthesize speech from text
        response = client.speech.generate(
            text=text, # specifies the input text to convert to speech
            language=language, # specifies the language of the generated speech 
            voice=voice, # specifies the desired voice for the speech synthesis
        )

        f.write(response.read()) # writes the generated audio content to the output file in binary format.

# text_to_speech("How many eggs can you get by tonight?", 'en', 'lucy', 'new_audio.wav')