# IMPORTATION OF NECESSARY LIBRARIES

import I2C_LCD_driver_library # imports the I2C LCD Driver to interact and control I2C LCD module
from time import * # imports all methods fromt "time" library
import sounddevice as sd # imports sounddevice library for handling audio input/output
from scipy.io.wavfile import write, read # imports write and read functions from scipy to save and read audio data respectively
from gpiozero import Button # imports button class from GPIO library for handling GPIO pins connected to buttons
import numpy as np # imports numpy library for handling the audio data as arrays
from datetime import datetime # imports the datetime module to generate timestamps for file names
import spitch_translator_api_integration as sp # imports custom "spitch_translator" library for speech-to-text-to-speech conversion

mylcd = I2C_LCD_driver_library.lcd() # initializes an object "mylcd" for interacting with the LCD

# LCD INITIAL DISPLAY

mylcd.lcd_display_string("Welcome!", 1) # displays "Welcome" on first row of the 16 x 2 LCD

mylcd.lcd_display_string("Press to Record", 2) # displays "Press to Record" on the second row of the 16 x 2 LCD

# PIN CONFIGURATION

BUTTON_PIN = 25  # assigns GPIO pin 25 to the button

# AUDIO SETTINGS

SAMPLE_RATE = 44100  # sets the sampling rate of the audio record to 44.1 kHz (CD-Quality Audio)
CHANNELS = 1  # sets audio recording to mono recording (single channel)
AUDIO_DATA = []  # initializes an empty list to store recorded audio chunks

# Function for Generating Filenames
def generate_filename(base_name = "hausa_audio"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # captures the current date and time in year-month-day_hour-minute-second format
    return f"{base_name}_{timestamp}.wav" # returns a filename that combines the base name and timestamp

OUTPUT_FILE = generate_filename() # variable for generated filenames

# Function to Start Recording
def record_audio_start():
    """Start recording audio."""
    global AUDIO_DATA # declares "AUDIO_DATA" as a global variable to access it inside the function
    print("Recording started. Speak into the microphone...")
        
    # STARTS RECORDING CONTINUOUSLY IN CHUNKS

    AUDIO_DATA = []  # clears previous data
    stream.start() # starts the audio input stream to capture audio

# Function to stop recording
def record_audio_stop():
    """Stop recording audio and save to a file."""
    global AUDIO_DATA # declares "AUDIO_DATA" as a global variable to access it inside the function
    print("Recording stopped.")
        
    stream.stop() # stops the audio input stream
    
    final_audio = np.concatenate(AUDIO_DATA, axis=0) # combines all audio chunks into a single numpy array
    
    write(OUTPUT_FILE, SAMPLE_RATE, final_audio) # saves the audio data to a .wav file
    print(f"Recording saved to '{OUTPUT_FILE}'.")
    
    
    return OUTPUT_FILE # returns the path to the saved audio file

def playback_audio(file_path):
    """Play a .WAV file."""
   
    rate, data = read(file_path) # reads the .wav file into "rate" and "data" varibales (i.e for sample rate and audio data)
    
    sd.play(data, samplerate=rate) # plays the audio using sounddevice library
    sd.wait()  # waits until the audio playback finishes
    
    
# Functionn for Button Press
def button_pressed():
    """Callback function when button is pressed."""
    mylcd.lcd_clear() # clears the LCD screen
    mylcd.lcd_display_string("Recording...", 1) # displays "Recording" on first row of the 16 x 2 LCD        
    record_audio_start() # calls function to begin recording
        
# Function for Button Release
def button_released():
    """Callback function when button is released."""
    mylcd.lcd_clear() # clears the LCD screen
    mylcd.lcd_display_string("Record Stop...", 1) # displays "Record Stop" on first row of the 16 x 2 LCD        
    audio_record = record_audio_stop() # calls "record_audio_stop" function to stop recording and stores the audio file path
    mylcd.lcd_clear() # clears the LCD screen
    mylcd.lcd_display_string("Transcribing...", 1) # displays "Transcribing" on first row of the 16 x 2 LCD
    final_speech = sp.speech_to_text(audio_record, "ha", "en" ) # transcribes the recorded audio from Hausa - ha to English -en 
    aud_path = generate_filename("English_audio") # generates a filename for the synthesized audio 
    final_audio = sp.text_to_speech(final_speech, 'en', 'lucy', aud_path) # converts the transcribed text into English audio
    print("Second Stage Done")
    playback_audio(aud_path)  # plays the synthesized audio
    
    
    mylcd.lcd_clear() # clears the LCD screen
    text_pad = "" * 16 # creates a string of 16 empty spaces
    text = final_speech # stores the transcribed speech in the "text" variable
    text = text_pad + text
    
    for i in range (0, len(text)):
        lcd_text = text[i:(i+16)] # extracts slice of text starting at the current index "i" and ending at "i + 16"
        mylcd.lcd_display_string(lcd_text, 1) # displays the extracted text on the first row of the LCD
        sleep(0.35) # pauses the program for 0. 35 seconds before updating the LCD screen
        mylcd.lcd_display_string(text_pad, 1) # clears the current row by displaying the empty "text_pad" string
    
    mylcd.lcd_clear() # clears the LCD screen
    mylcd.lcd_display_string("Thank You!", 1) # displays "Thank You!" on first row of the 16 x 2 LCD
    mylcd.lcd_clear() # clears the LCD screen

# INITIALIZE THE GPIO BUTTON

button = Button(BUTTON_PIN) # creates a button object connected to the specific GPIO pin

button.when_pressed = button_pressed # links the "button_pressed" callback to the button press event
button.when_released = button_released # links the "button_released" callback to the button release event

# CREATE A SOUNDDEVICE STREAM

stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype='int16',
    callback=lambda indata, frames, time, status: AUDIO_DATA.append(indata.copy())
) # configures an audio input stream with a sample rate, mono channel, and a callback to save audio data


try:
    print("Program ready. Press and hold the button to record audio.")
    
    while True:
        # Keep the script running and waiting for button press events
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    # Stop the stream and cleanup
    if stream.active:
        stream.stop()
    print("Program terminated.")
    
