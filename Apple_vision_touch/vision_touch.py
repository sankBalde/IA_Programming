import cv2
import mediapipe as mp
import time
import numpy as np
import math
import random

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils

hands = mphands.Hands()
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
new_background = np.zeros((1080, 1920, 3), dtype=np.uint8)
while True:
    success, img = cap.read()
    H, W, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    landmarks = results.multi_hand_landmarks

    if landmarks:
        min_x, min_y = 0,0
        max_x, max_y = 0,0
        for hand_landmarks in landmarks:
            # Récupérer les coordonnées des points clés de la main
            landmarks1 = hand_landmarks.landmark

            # Calculer les coordonnées de la boîte englobante
            x_values = [landmark.x for landmark in landmarks1]
            y_values = [landmark.y for landmark in landmarks1]
            min_x, min_y = min(x_values), min(y_values)
            max_x, max_y = max(x_values), max(y_values)

        for handLms in landmarks:
            x1, y1 = 0, 0
            x2, y2 = 0, 0
            for id, lm in enumerate(handLms.landmark):
                x , y = int(lm.x * W), int(lm.y * H)
                if id == 4:
                    x1, y1 = x, y
                if id == 8:
                    x2, y2 = x, y
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            length = math.hypot(x2-x1, y2-y1)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                # Générer une couleur de fond aléatoire
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            else:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            new_background[:] = random_color

            # Extraire la région de la main de l'image d'origine
            hand_region = img[int(min_y * H):int(max_y * H), int(min_x * W):int(max_x * W)]
            new_background[int(min_y * H):int(max_y * H), int(min_x * W):int(max_x * W)] = hand_region

            # Dessiner la boîte englobante sur l'image
            cv2.rectangle(new_background, (int(min_x * new_background.shape[1]), int(min_y * new_background.shape[0])),
                          (int(max_x * new_background.shape[1]), int(max_y * new_background.shape[0])), (0, 255, 0), 2)
            cv2.line(new_background, (x1, y1), (x2, y2), (255, 0, 255), 3)
            mpdraw.draw_landmarks(new_background, handLms, mphands.HAND_CONNECTIONS)

    # Affichez l'image avec le fond noir et la pose dessinée
    cv2.imshow("Image", new_background)
    cv2.waitKey(1)
