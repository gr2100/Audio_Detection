# Audio_Detection
The objective of audio detection in online examinations is to maintain the integrity of the exam process and prevent cheating by ensuring that all candidates are evaluated based on their own knowledge and abilities.

## Introduction
Proctoring in remote online examinations has evolved significantly with the implementation of video and audio detections to prevent malpractice by test takers. However, certain aspects of audio detection need improvement to ensure fairness and accuracy in online assessments. One critical issue is the immediate identification of any audio as malpractice without considering whether the sound indicates cheating or simply external noise beyond the test taker's control. This can lead to unjust consequences for test takers and negatively impact both the individuals taking the exam and the institutions conducting the assessments.

This project aims to address this challenge by enhancing audio detection in AI proctored online examination portals. The primary goal is to determine whether the detected audio signifies malpractice or not. The system achieves this by recording audio, cross-referencing it with the text from exam questions, identifying whispering or mumbling, and even alerting exam administrators of potential cheating. The focus is on maintaining the integrity of the examination process and ensuring a fair assessment of the test taker's skills and knowledge.

## Features
- **Audio Detection:** The system utilizes audio recognition technology to identify and analyze sounds during online examinations.

- **Cross-Referencing:** It cross-checks the detected audio with the text from the exam questions to identify any potential cheating attempts.

- **Alert System:** In case of suspicious audio activity, the system alerts exam administrators to take appropriate action.

## Code
The code for implementing this audio detection system is provided in the Python script. It uses libraries such as tkinter for the graphical user interface, speech_recognition for audio processing, PIL for image handling, and mysql.connector for database management. The code also includes functionalities for user registration and login, ensuring a secure and user-friendly experience.

Please note that this code is intended for educational purposes and may require customization and integration into a larger software ecosystem to be used in a real-world examination environment.

## Usage
1. **User Registration:** To use the system, users can register with their credentials, including a unique code, username, email, password, and gender. This registration process helps maintain user accounts securely.

2. **User Login:** Registered users can log in using their username and password to access the audio detection system.

3. **Audio Detection:** After logging in, users can start the audio detection process by clicking the "User" button on the main screen.

4. **System Alert:** If the system detects any suspicious audio activity during the examination, it will alert the exam administrators to take necessary actions.

## Installation and Dependencies
Before running the code, make sure you have the following dependencies installed:

- Python (>= 3.6)
- tkinter
- speech_recognition
- Pillow (PIL)
- mysql.connector
- OpenCV (cv2)

You can install these dependencies using pip:
```bash
pip install tkinter pillow SpeechRecognition mysql-connector-python opencv-python
