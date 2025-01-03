# Speech-to-Speech 🗣️ Language Translator Using Raspberry Pi

---

## 🚀 Overview

The **Speech-to-Speech Language Translator** is a portable device designed to make communication across languages seamless. It captures voice input through a microphone,  translates it using the machine learning model [Spitch](https://spi-tch.com/), and plays the translated speech through a speaker. To promote user interaction, the text is displayed on an I2C LCD screen, providing a clear visual representation.

Built on a Raspberry Pi and housed in a 3D-printed casing, the device combines functionality with portability. This project bridges the fields of machine learning and embedded systems, offering a seamless solution for real-time language translation. Whether you're traveling, participating in international meetings, or simply engaging in conversations across languages, the translator provides an intuitive and effective way to communicate.

---

## 📑 Table of Contents

1. [🌟 Features](#-features)
2. [🛠️ How to Run](#️-how-to-run)
    - [🖥️ Hardware Requirements](#️-hardware-requirements)
    - [💾 Software Requirements](#-software-requirements)
    - [▶️ Running the Program](#️-running-the-program)
3. [🔌 Circuit Diagram](#-circuit-diagram)
4. [🖨️ 3D Printing](#️-3d-printing)
    - [🖼️ 3D Models](#️-3d-models)
    - [📸 Printing Process](#-printing-process)
5. [How It Works](#how-it-works)
    - [🔗API Integration](#-api-integration)
    - [Supported Languages](#supported-languages)
    - [Workflow](#workflow)
6. [🏁 Conclusion](#-conclusion)
7. [👥 Contributors](#-contributors)

---

## 🌟 Features

- **⚡ Real-Time Language Translation**: Instant speech-to-speech translation for seamless communication.
- **📝 Text Display**: Displays the translated text on a screen, providing both auditory and visual feedback.
- **🌍 Multilingual Support**: Currently supports only translation from Hausa to English. But can easily be extended to Yoruba and Igbo with minimal modifications to the code.
- **📦 Portable Design**: Compact and lightweight with a 3D-printed enclosure.
- **👆 User-Friendly Interface**: Simple operation with a button to start the translation process, designed for easy interaction.

---

## 🛠️ How to Run

To run the **Speech-to-Speech Language Translator**, both hardware and software components are needed. This section outlines the necessary hardware setup and the software libraries that need to be installed to get the system up and running. Follow the steps below to ensure everything is properly configured before running the program.

### 🖥️ Hardware Requirements

- **🎛️ Raspberry Pi 4B**: The central processing unit that runs the translation software and controls the hardware peripherals.
<p align="center">
    <img src="NCAIR Speech-to-Speech Image Collection/raspberry_pi.png" alt="Raspberry Pi 4b Pictorial Representation" width="1500"/>
    <br>
    <em>The Raspberry Pi 4b</em>
</p>

- **📺 LCD Screen**: Displays the translated text for visual feedback.
<p align="center">
    <img src="NCAIR Speech-to-Speech Image Collection/16 x 2 LCD.jpg" alt="Displays the translated text for visual feedback" width="1500"/>
    <br>
    <em>The 16 X 2 I2C LCD</em>
</p>

- **🎤 USB Mini Microphone**: Captures the voice input for translation.
<p align="center">
    <img src="NCAIR Speech-to-Speech Image Collection/usb_microphone.png" alt="Captures the voice input for translation" width="1500"/>
    <br>
    <em>USB Mini Microphone</em>
</p>

- **🖲️ Push Button**: Initiates the translation process when pressed.
<p align="center">
    <img src="NCAIR Speech-to-Speech Image Collection/push_button.png" alt="Initiates the translation process when pressed" width="1500"/>
    <br>
    <em>Push Button</em>
</p>

- **🔌 Connecting Wires**: Used to connect various components, including the microphone, speaker, and LCD.
<p align="center">
    <img src="NCAIR Speech-to-Speech Image Collection/connecting_wires.jpg" alt="Used to connect various components, including the microphone, speaker, and LCD" width="1500"/>
    <br>
    <em>Connecting Wires</em>
</p>

- **🔊 Speaker**: Outputs the translated speech after processing.

- **🏗️ 3D-Printer**: Prints the final casing that houses all components securely using a portable and compact design.
<p align="center">
    <img src="NCAIR Speech-to-Speech Image Collection/prusa_i3_mk_3D_printer.jpg" alt="Prints the final casing that houses all components securely using a portable and compact design" width="1500"/>
    <br>
    <em>3D Printer</em>
</p>

### 💾 Software Requirements

To run the **Speech-to-Speech Language Translator** system, the following libraries are required:

- **I2C_LCD_driver_library:**  
  Used to interact with the I2C LCD module. To install, clone the repository:  
  ```bash
  git clone https://github.com/NCAIR-FABLAB/Cohort-21-Project/blob/main/I2C_LCD_driver_library.py
  ```
- **sounddevice:**  
  Handles audio input/output for the system. To install, use:
  ```bash
  pip install sounddevice
  ```
- **scipy:**  
  Provides functions to read and write audio data. To install, use:
  ```bash
    pip install scipy
  ```
- **gpiozero:**  
  Used for handling GPIO pins connected to the button. To install, use apt-get (for Raspberry Pi):
  ```bash
    sudo apt-get install python3-gpiozero
  ```
- **numpy:**  
  Required for handling binary audio data as arrays. To install, use:
  ```bash
    pip install numpy
  ```
- **datetime (pre-installed):**  
Used for generating timestamps for creating distinct file names. To use:
```bash
from datetime import datetime
```
- **time (pre-installed):**  
Used for pausing program execution during runtime. To use:
```bash
from time import *
```
- **spitch_translator_api_integration:**  
Used for the for speech-to-text-to-speech conversion. To install, clone the repository 
```bash
git clone https://github.com/NCAIR-FABLAB/Cohort-21-Project/blob/main/spitch_translator_api_integration.py
```
For More Information on the Libraries and the Versions Used, Check the Complete [requirements.txt file](https://github.com/NCAIR-FABLAB/Cohort-21-Project/blob/main/requirements.txt)

### ▶️ Running the Program

After installing the required software libraries, follow these steps to run the **Speech-to-Speech Language Translator** system:

#### 1. Ensure All Components Are Connected:
To connect the components, check the [🔌 Circuit Diagram](#-circuit-diagram) section. Make sure that the Raspberry Pi is properly connected to the microphone, speaker, push button, and I2C LCD screen using the provided connecting wires.

#### 2. Install Required Libraries:
If you haven’t already installed the necessary libraries, do so using the commands listed in the [💾 Software Requirements](#-software-requirements) section.

#### 3. Clone the Project:
Clone the **Speech-to-Speech Language Translator** repository to your Raspberry Pi:

```bash
git clone https://github.com/NCAIR-FABLAB/Cohort-21-Project
```
#### 4. Run the Program:
To start the program, execute the Python script on command line:

```bash
python3 speech_to_speech_translator_language.py
```
#### 5. Using the System:
Press and hold the button to begin recording your speech. After releasing the button, the system will process the translation and output the result through both the speaker and the LCD screen.

#### 6. End the Session:
Once you’re finished, press Ctrl+C to stop the program or unplug the Raspberry Pi.

---

## 🔌 Circuit Diagram

<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/circuit_diagram.png" alt="Speech-to-Speech Translator Circuit Diagram" width="1500"/>
  <br>
  <em>Device Circuit Diagram</em>
</p>

---

## 🖨️ 3D Printing

### 🎨 Designing the 3D Casing
To design the enclosure, Fusion 360 was used for 3D modeling. The design was printed using the Prusa i3 Mk 3 3D printer, and additional structural parts were cut using the Epilog laser cutter.

The final device case dimensions are 87.5 mm in height, 140 mm in length, and 100 mm in width. The compact size of the case allows for an easy-to-use interface while housing all components securely, making it portable and user-friendly for everyday use.

### 🖼️ 3D Models
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/device_top_view_.jpg" alt="A Clear Image Showing the Top Part of the Device" width="600"/>
  <br>
  <em>Device Top View</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/stand_for_internal_components.jpg" alt="An Image Revealing The Internal Stand of the Device Before Assembly" width="600"/>
  <br>
  <em>Stand for Internal Components</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/hollow_compartment_layout.jpg" alt="A View of the Hollow Compartment Designed To House the Components" width="600"/>
  <br>
  <em>Hollow Compartment Designed to House the Components</em>
</p>

<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/component_encapsulation.png" alt="Pictorial View of How The Various Components are Arranged Within The Hollow Compartment" width="600"/>
  <br>
  <em>Pictorial View of How The Various Components are Arranged Within The Hollow Compartment</em>
</p>

<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/final_assembled_device_design.png" alt="An Image of The Full Assembled Device Highlighting its Final Structure and Design" width="600"/>
  <br>
  <em>An Image of The Full Assembled Device Highlighting its Final Structure and Design</em>
</p>

### 📸 Printing Process
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/Initial Stage of Top View 3D Printing with Prusa i3 mK 3.jpg" alt="Initial Stage of Top View 3D Printing with Prusa i3 mK 3" width="600"/>
  <br>
  <em>Top View 3D Printing (Initial Stage)</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/Latter Stage of Top View 3D Printing with Prusa i3 mK 3.jpg" alt="Latter Stage of Top View 3D Printing with Prusa i3 mK 3" width="600"/>
  <br>
  <em>Top View 3D Printing (Latter Stage)</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/Inner Compartment Stand.jpg" alt="Printed Inner Compartment" width="600"/>
  <br>
  <em>Inner Compartment Stand</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/final device.jpg" alt="The Speech-to-Speech Translator Device" width="600"/>
  <br>
  <em>The Speech-to-Speech Language Translator</em>
</p>
<video width="600" controls>
  <source src="NCAIR Speech-to-Speech Image Collection/bottom_part2.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## How It Works

### 🔗 API Integration

The Speech-to-Speech Language Translator device uses [Spitch](https://spi-tch.com/), a natural language processing model hosted on a backend server. The translation process works by first transcribing the speech to text, then translating it to the target language, and finally converting the translated text back into speech in the target language. The API allows seamless interaction with the model while performing these steps to translate the spoken language.

### Supported Languages
The API supports transcription and translation for the following languages:
- Hausa
- Yoruba
- Igbo
- English
  
**Note:** In this application, the project focused on Translation of Hausa to English

### Workflow
- **Speech-to-Text**: The system starts by first recording the user's speech input in Hausa using the microphone. The recorded audio in `.wav` format is then sent via the API as an input to the [Spitch model](https://spi-tch.com/) for transcription into Hausa text.
- **Translation**: The model then translates the transcribed Hausa text into English text.
- **Text-to-Speech**: Finally, the translated English text is then converted back into an audio file in `.wav` format, which is played aloud through the speaker using an agent's voice (lucy). The translated text is also displayed on the LCD screen for visual interaction.

Other Agent Voices Available Include: john, lina, and jude.

For more detailed information on the API, its features, please refer to the [Spitch Documentation](https://docs.spi-tch.com/getting-started/welcome).

---

## 🏁 Conclusion

The Speech-to-Speech Language Translator is a prototype that enables real-time translation from Hausa to English. While this is the first version, there is great potential for future improvements, such as adding support for more languages, improving translation accuracy, and reducing the overall size. This project showcases the possibility of using readily available hardware to overcome language barriers, opening up many exciting opportunities for future development.

---

## 👥 Contributors

- **Rizama Victor Samuel**  [GitHub: Rizama03](https://github.com/Rizama03)
- **Ifeoluwa Omole**  [GitHub: andy-ife](https://github.com/andy-ife)
- **Ahmad Abubakar Sadiq**  [GitHub: Dantama022](https://github.com/Dantama022)
- **Yero Muhammad Bunuyaminu**  [GitHub: MubarakYero](https://github.com/MubarakYero)
- **Abdulaziz Ahmad Ibrahim**  [GitHub: Abdul-ahmad](https://github.com/Abdul-ahmad)
  
---
