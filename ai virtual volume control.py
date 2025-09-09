import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ----------------- Pycaw Setup -----------------
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol, max_vol, _ = vol_range  # usually (-65.25, 0.0, 0.03125)

# ----------------- Mediapipe Setup -----------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# ----------------- Webcam -----------------
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    # Flip for mirror effect
    img = cv2.flip(img, 1)

    # Convert to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            h, w, _ = img.shape
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                # Thumb tip = 4, Index tip = 8
                x1, y1 = lm_list[4][1], lm_list[4][2]
                x2, y2 = lm_list[8][1], lm_list[8][2]

                # Draw line & circles
                cv2.circle(img, (x1, y1), 8, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 8, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

                # Find distance
                length = np.hypot(x2 - x1, y2 - y1)

                # Convert distance to volume
                vol = np.interp(length, [30, 200], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

                # Volume bar for display
                vol_bar = np.interp(length, [30, 200], [400, 150])
                vol_perc = np.interp(length, [30, 200], [0, 100])

                # Draw volume bar
                cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
                cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(vol_perc)} %', (40, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    cv2.imshow("Gesture Volume Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
