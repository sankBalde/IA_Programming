import cv2
import mediapipe as mp
from keybord_creation import *
import time

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils

hands = mphands.Hands()

text_to_write = ""

# Initialisation du temps de début et du rectangle précédent
start_times = {'0': 0, '1': 0}  # '0' et '1' représentent les ID des mains
prev_rect_labels = {'0': None, '1': None}
prev_letter = ''
wrong_letters = ['Tab', 'DEL', 'UP', 'Space']
bool_upercase = False
while True:
    success, img = cap.read()
    # Inverser l'image horizontalement
    img = cv2.flip(img, 1)
    H, W, _ = img.shape
    H_key = int(H * 0.9)
    W_key = W
    img_key, rect_dict = create_keybord(height=H_key, width=W_key)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    landmarks = results.multi_hand_landmarks

    # Créez un fond noir de la même taille que l'image
    black_background = np.zeros_like(img)
    black_background[int(0.10 * H):int(H), :] = img_key
    writeTextframe = black_background[:int(0.10 * H), :]
    if landmarks:
        number = 0
        for handLms in landmarks:
            x2, y2 = 0, 0
            for id, lm in enumerate(handLms.landmark):
                x, y = int(lm.x * W), int(lm.y * H)
                if id == 8:
                    x2, y2 = x, y
            # Dessiner les repères et les points d'intérêt
            cv2.circle(black_background, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

            # Vérifier si le point est dans un rectangle
            for label, rect in rect_dict.items():
                x, y, w, h = rect
                y += int(0.10 * H)
                if x < x2 < x + w and y < y2 < y + h:
                    if prev_rect_labels[str(number)] and (label not in prev_rect_labels[str(number)]):
                        start_times[str(number)] = time.time()
                    end_time = time.time()
                    diff = end_time - start_times[str(number)]
                    if diff >= 1:
                        cv2.rectangle(black_background, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        if prev_letter != label and label not in wrong_letters:
                            if bool_upercase:
                                text_to_write += label.upper()
                            else:
                                text_to_write += label.lower()
                            prev_letter = label
                        if label == 'DEL':
                            text_to_write = text_to_write[:-1]
                        if label == 'Space':
                            text_to_write += ' '
                        if label == 'UP':
                            if bool_upercase:
                                bool_upercase = False
                            else:
                                bool_upercase = True
                            #print(bool_upercase)

                        start_times[str(number)] += 1
                    else:
                        cv2.rectangle(black_background, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Mettre à jour le rectangle précédent pour chaque main
                    prev_rect_labels[str(number)] = label
            number += 1
            mpdraw.draw_landmarks(black_background, handLms, mphands.HAND_CONNECTIONS)
    # Écrire le texte sur la partie writeTextframe
    cv2.putText(writeTextframe, text_to_write, (0, int(0.10 * H) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 2, cv2.LINE_AA)
    black_background[:int(0.10 * H), :] = writeTextframe
    # Affichez l'image avec le fond noir et la pose dessinée
    cv2.imshow("Image", black_background)
    cv2.waitKey(1)
