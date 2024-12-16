import cv2
import mediapipe as mp
import pyautogui
import time  # For unique filename using timestamp

# Initialize Mediapipe and pyautogui
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Function to detect hand gestures and conditions
def detect_gesture(hand_landmarks):
    gestures = {
        "move": False,
        "left_click": False,
        "right_click": False,
        "double_click": False,
        "screenshot": False,
        "scroll_up": False,
        "scroll_down": False
    }

    # Check finger states
    index_extended = hand_landmarks[8].y < hand_landmarks[6].y  # Index finger extended
    middle_extended = hand_landmarks[12].y < hand_landmarks[10].y  # Middle finger extended
    ring_extended = hand_landmarks[16].y < hand_landmarks[14].y  # Ring finger extended
    pinky_extended = hand_landmarks[20].y < hand_landmarks[18].y  # Pinky finger extended
    thumb_extended = hand_landmarks[4].x > hand_landmarks[2].x  # Thumb extended (based on x-axis)

    # Gesture conditions
    gestures["move"] = index_extended and middle_extended  # Move with index or middle finger extended

    # Left-click: Index finger bent
    if not index_extended and middle_extended:
        gestures["left_click"] = True

    # Right-click: Middle finger bent
    if index_extended and not middle_extended:
        gestures["right_click"] = True

    # Double click: Both index and middle fingers bent
    if not index_extended and not middle_extended:
        gestures["double_click"] = True

    # Screenshot: All fingers extended
    if index_extended and middle_extended and ring_extended and pinky_extended and thumb_extended:
        gestures["screenshot"] = True

    # Scroll detection: Thumb and Ring for scroll up, Thumb and Pinky for scroll down
    thumb = hand_landmarks[4]
    ring = hand_landmarks[16]
    pinky = hand_landmarks[20]

    # Calculate distances for scroll gestures
    thumb_ring_distance = ((thumb.x - ring.x) ** 2 + (thumb.y - ring.y) ** 2) ** 0.5
    thumb_pinky_distance = ((thumb.x - pinky.x) ** 2 + (thumb.y - pinky.y) ** 2) ** 0.5

    # Threshold distance for touch (adjust based on camera resolution)
    touch_threshold = 0.05  # A small distance, adjust if needed

    if thumb_ring_distance < touch_threshold:
        gestures["scroll_up"] = True
    elif thumb_pinky_distance < touch_threshold:
        gestures["scroll_down"] = True

    return gestures

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for natural mirroring
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            gestures = detect_gesture(landmarks)

            # Get coordinates for mouse movement
            if gestures["move"]:
                index_finger = landmarks[8]  # Use index finger tip for movement
                x, y = int(index_finger.x * w), int(index_finger.y * h)
                screen_x = int(index_finger.x * screen_width)
                screen_y = int(index_finger.y * screen_height)
                pyautogui.moveTo(screen_x, screen_y)

            # Perform actions based on gestures
            if gestures["left_click"]:
                pyautogui.click()
            elif gestures["right_click"]:
                pyautogui.rightClick()
            elif gestures["double_click"]:
                pyautogui.doubleClick()
            elif gestures["screenshot"]:
                # Save screenshot with timestamp to avoid overwriting
                timestamp = time.strftime("%Y%m%d-%H%M%S")  # Get current time for unique filename
                screenshot_filename = f'screenshot_{timestamp}.png'  # Filename with timestamp
                pyautogui.screenshot(screenshot_filename)
                print(f"Screenshot saved as {screenshot_filename}")

            # Handle scrolling with faster speed
            if gestures["scroll_up"]:
                pyautogui.scroll(200)  # Faster scroll up
                print("Scrolling up...")
            elif gestures["scroll_down"]:
                pyautogui.scroll(-200)  # Faster scroll down
                print("Scrolling down...")

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
