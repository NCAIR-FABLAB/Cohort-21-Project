# Speech-to-Speech 🗣️ Language Translator Using Raspberry Pi

---

## 🚀 Overview

The **Speech-to-Speech Translator** is a system that receives voice input through a microphone, translates it via an [API Spitch](https://spi-tch.com/), and produces the translated output through a speaker. Additionally, the translated text is displayed on an I2C LCD, providing a visual representation of the translation. Built on a Raspberry Pi and housed in a 3D-printed enclosure, the device is both portable and user-friendly. It efficiently handles real-time language translation, making it a practical solution for communication in diverse scenarios such as travel, international meetings, or everyday conversations across language barriers.

---

## 📑 Table of Contents

1. [🌟 Features](#-features)
2. [🛠️ How to Run](#️-how-to-run)
    - [🖥️ Hardware Requirements](#️-hardware-requirements)
    - [💾 Software Requirements](#-software-requirements)
    - [▶️ Running the Program](#️-running-the-program)
3. [🖨️ 3D Printing Process](#️-3d-printing-process)
    - [🖼️ 3D Models](#️-3d-models)
5. [📸 Project Pictures](#-project-pictures)
6. [🔗 API Integration](#-api-integration)
7. [🏁 Conclusion](#-conclusion)
8. [👥 Group Members](#-group-members)

---

## 🌟 Features

- **⚡ Real-Time Language Translation**: Instant speech-to-speech translation for seamless communication.
- **📝 Text Display**: Displays the translated text on a screen, providing both auditory and visual feedback.
- **🌍 Multilingual Support**: Currently supports only translation from Hausa to English. But can easily be extended to Yoruba and Igbo with minimal modifications to the code.
- **📦 Portable Design**: Compact and lightweight with a 3D-printed enclosure.
- **👆 User-Friendly Interface**: Simple operation with a button to start the translation process, designed for easy interaction.

---

## 🛠️ How to Run

To run the **Speech-to-Speech Translator**, both hardware and software components are needed. This section outlines the necessary hardware setup and the software libraries that need to be installed to get the system up and running. Follow the steps below to ensure everything is properly configured before running the program.

## 🖥️ Hardware Requirements

- **🎛️ Raspberry Pi 4B**: The central processing unit that runs the translation software and controls the hardware peripherals.
- **🔌 Connecting Wires**: Used to connect various components, including the microphone, speaker, and LCD.
- **🎤 USB Mini Microphone**: Captures the voice input for translation.
- **🔊 Speaker**: Outputs the translated speech after processing.
- **🖲️ Push Button**: Initiates the translation process when pressed.
- **📺 LCD Screen**: Displays the translated text for visual feedback.
- **🏗️ 3D-Printed Enclosure**: Houses all components securely for a portable and compact design.

## 🔌 Circuit Diagram
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/circuit_diagram.png" alt="Speech-to-Speech Translator Circuit Diagram" width="1500"/>
  <br>
  <em>Device Circuit Diagram</em>
</p>

### 💾 Software Requirements

To run the **Speech-to-Speech Translator** system, the following libraries are required:

- **I2C_LCD_driver_library**  
  Used to interact with the I2C LCD module.  
  Install via cloning the repository:  
  ```bash
  git clone https://github.com/your_I2C_LCD_driver_repo.git
  ```
- **sounddevicer**  
  Handles audio input/output for the system. Install via pip:
  ```bash
  pip3 install sounddevice
  ```
- **scipy**  
  Provides functions to read and write audio data. Install via pip:
  ```bash
    sudo apt-get install python3-gpiozero
  ```
- **gpiozero**  
  Used for handling GPIO pins connected to the button. Install via apt-get (for Raspberry Pi):
  ```bash
    sudo apt-get install python3-gpiozero
  ```
- **numpy**  
  Required for handling audio data as arrays. Install via pip:
  ```bash
    pip3 install numpy
  ```
## ▶️ Running the Program

After installing the required hardware components and software libraries, follow these steps to run the **Speech-to-Speech Translator** system:

### 1. Ensure All Components Are Connected:
Make sure that the Raspberry Pi is properly connected to the microphone, speaker, push button, and I2C LCD screen using the provided connecting wires.

### 2. Install Required Libraries:
If you haven’t already installed the necessary libraries, do so using the commands listed in the [Software Requirements](#software-requirements) section.

### 3. Clone the Project:
Clone the **Speech-to-Speech Translator** repository to your Raspberry Pi:

```bash
git clone https://github.com/your_project_repo.git
cd your_project_repo
```
### 4. Run the Program:
To start the program, execute the Python script:

```bash
python3 speech_translator.py
```
### 5. Using the System:
Press and hold the button to begin recording your speech. After releasing the button, the system will process the translation and output the result through both the speaker and the LCD screen.

### 6. End the Session:
Once you’re finished, press Ctrl+C to stop the program or unplug the Raspberry Pi.

---

# 🖨️ 3D Printing Process

## 🎨 Designing the Enclosure
To design the enclosure, Fusion 360 was used for 3D modeling. The design was printed using the Prusa i3 Mk 3 3D printer, and additional structural parts were laser cut using the Epilog laser cutter.

The final enclosure dimensions are 87.5 mm in height, 140 mm in length, and 100 mm in width. The compact size of the enclosure allows for an easy-to-use interface while housing all components securely, making it portable and user-friendly for everyday use.

# 🖼️ 3D Models
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

---

# 📸 Project Pictures
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/final device.jpg" alt="The Speech-to-Speech Translator Device" width="600"/>
  <br>
  <em>The Speech-to-Speech Translator</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/top_view_3d_printing_1.jpg" alt="Initial Stage of Top View 3D Printing with Prusa i3 mK 3" width="600"/>
  <br>
  <em>Top View 3D Printing (Initial Stage)</em>
</p>
<p align="center">
  <img src="NCAIR Speech-to-Speech Image Collection/top_view_3d_printing_2.jpg" alt="Latter Stage of Top View 3D Printing with Prusa i3 mK 3" width="600"/>
  <br>
  <em>Top View 3D Printing (Latter Stage)</em>
</p>
<video width="600" controls>
  <source src="NCAIR Speech-to-Speech Image Collection/bottom_part2.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

# 🔗 API Integration
The Speech-to-Speech Translator system relies on the [Spitch API](https://spi-tch.com/), which is based on a large language processing model hosted on a backend server. This API provides seamless speech translation through a series of steps involving transcription, translation, and speech synthesis.

### How It Works with the System:
- **Speech-to-Text**: The system records the user's speech input in Hausa using the microphone. The audio is sent to the [Spitch API](https://spi-tch.com/), where it is transcribed into Hausa text.
- **Translation**: The API translates the transcribed Hausa text into English.
- **Text-to-Speech**: The translated English text is then converted back into speech, which is played aloud through the speaker. The translated text is also displayed on the LCD screen for visual feedback.

### Supported Languages:
The API supports transcription and translation for the following languages:
- Hausa
- Yoruba
- Igbo

For more detailed information on the API, its features, please refer to the [Spitch API Documentation](https://docs.spi-tch.com/getting-started/welcome).

---

# 🏁 Conclusion
The Speech-to-Speech Translator is a functional prototype that facilitates real-time translation from Hausa to English. Although it is operational in its first iteration, there is significant potential for future improvements, including expanding language support and enhancing translation accuracy. This project demonstrates the feasibility of using accessible hardware to bridge language barriers, with many exciting opportunities for further development.

---

## 👥 Group Members
- **Rizama Victor Samuel**  [GitHub: Rizama03](https://github.com/Rizama03)
- **Ifeoluwa Omole**  [GitHub: andy-ife](https://github.com/andy-ife)
- **Ahmad Abubakar Sadiq**  [GitHub: Dantama022](https://github.com/Dantama022)
- **Yero Muhammad Bunuyaminu**  [GitHub: MubarakYero](https://github.com/MubarakYero)
- **Abdulaziz Ahmad Ibrahim**  [GitHub: Abdul-ahmad](https://github.com/Abdul-ahmad)
