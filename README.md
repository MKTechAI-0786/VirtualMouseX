# VirtualMouseX
This project leverages Mediapipe, OpenCV, and PyAutoGUI to create a virtual mouse controlled by hand gestures and add various features.The application enables intuitive and hands-free computer control.

#Features
  Hand Gesture Control:
    Move the mouse cursor using hand gestures.
    Perform left-click, right-click, double-click, and scrolling using specific gestures.
    Take screenshots by extending all fingers.
    
  Gesture-Based Commands:
    Scroll up/down using thumb and ring or pinky fingers.
    App switching using swipes.
    
  Dynamic Recognition:
    All gestures are detected in real-time using Mediapipe’s hand tracking module.

#Software Requirements

  Python 3.7 or later
  Required Python libraries:
    opencv-python
    mediapipe
    pyautogui
    pynput

  You can install the dependencies by running the following command:
    pip install opencv-python mediapipe pyautogui pynput

#Hardware Requirements
  Webcam or any external camera for real-time hand tracking.
  A system capable of running Python 3 smoothly.

#Procedure to Run the Project
  1. Clone this repository:
    git clone https://github.com/your-username/facial-emotion-recognition.git
    cd facial-emotion-recognition
  2. Install the required dependencies:
    pip install -r requirements.txt
  3. Run the script:
    python gesture_mouse_control.py
Ensure that the webcam is active and your hand gestures are visible to the camera. The application will process the hand gestures in real time and perform corresponding actions.

#How It Works
  1. Hand Tracking:
    Uses Mediapipe’s hand detection and tracking module to capture real-time hand landmarks.
    Calculates the position and distance between landmarks to detect gestures.
  2. Gesture Recognition:
    Predefined gestures are mapped to mouse and system actions like scrolling, clicking, and volume control.
  3. System Interaction:
    PyAutoGUI is used to simulate mouse and keyboard actions based on detected gestures.

#Conclusion
This project demonstrates the potential of combining computer vision and system automation for hands-free interaction. It offers a convenient alternative to traditional input devices and can be further extended for accessibility applications and advanced gesture control in smart environments.

#Acknowledgements
Mediapipe for the robust hand tracking framework.
OpenCV for video processing.
PyAutoGUI for system control integration.
