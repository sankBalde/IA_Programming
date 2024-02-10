import cv2
import numpy as np

def create_keybord(height : int=900, width: int=1500):

    # Nombre de rangées et de colonnes de touches sur le clavier AZERTY
    rows, cols = 4, 12

    # Calcul des dimensions des touches en fonction de la taille de l'image
    key_width = width // cols
    key_height = height // rows

    # Création de l'image blanche de fond
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Positions des touches du clavier
    keys_positions = [(x, y, key_width, key_height) for y in range(0, height, key_height) for x in range(0, width, key_width)]

    # Libellés des touches du clavier AZERTY
    keys_labels = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'DEL'],
        ['Tab', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['UP', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M'],
        ['Space', 'W', 'X', 'C', 'V', 'B', 'N', ',', ';', ':', ')']
    ]

    key_rect_dict = {}

    # Dessiner les touches sur l'image
    for i, (x, y, w, h) in enumerate(keys_positions):
        # Calculer l'indice de la ligne et de la colonne actuelle
        row_index = (i) // cols
        col_index = (i) % cols
        # Vérifier si l'indice de la ligne est dans la plage des libellés des touches
        if row_index < len(keys_labels):
            # Vérifier si l'indice de la colonne est dans la plage des libellés des touches pour cette ligne
            if col_index < len(keys_labels[row_index]):
                label = keys_labels[row_index][col_index]
                key_rect_dict[label] = [x, y, w, h]
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                cv2.putText(img, label, (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)
    return img, key_rect_dict