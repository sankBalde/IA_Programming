# Assistant Vocal Jarvis

Ce projet est un exemple d'assistant vocal Jarvis développé en utilisant la bibliothèque Kivy pour l'interface utilisateur, la bibliothèque Azure Cognitive Services Speech pour la reconnaissance vocale et la synthèse vocale, ainsi que l'API OpenAI GPT-3 pour l'interaction conversationnelle.

![plot](png/Jarvis_interface.gif)

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés:

- [Python](https://www.python.org/downloads/) (version 3.10 ou supérieure)
- [Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html)
- [Bibliothèque Azure Cognitive Services Speech](https://pypi.org/project/azure-cognitiveservices-speech/)
- [OpenAI Python](https://pypi.org/project/openai/)

## Configuration

1. Assurez-vous d'avoir les clés d'accès nécessaires pour Azure Cognitive Services Speech et OpenAI. Vous devrez les ajouter dans le code pour permettre l'accès à ces services.
2. Modifiez les paramètres tels que les langues utilisées et les noms des voix selon vos préférences.

## Fonctionnalités

L'assistant vocal Jarvis propose les fonctionnalités suivantes:

- Reconnaissance vocale à l'aide de la bibliothèque Azure Cognitive Services Speech.
- Interaction conversationnelle avec l'API OpenAI GPT-3 pour des réponses contextuelles.
- Synthèse vocale pour répondre à l'utilisateur.

## Utilisation

1. Exécutez le programme en utilisant la commande `python main.py`.
2. Appuyez sur le bouton en forme d'orbe planetaire pour activer la reconnaissance vocale et commencez à parler.
3. Lorsque vous relâchez le bouton, l'assistant envoie votre question à l'API OpenAI pour obtenir une réponse.
4. L'assistant vous répondra vocalement en utilisant la synthèse vocale.

## Remarques

- Assurez-vous d'avoir une connexion Internet active pour que l'assistant puisse interagir avec l'API OpenAI.
- N'hésitez pas à personnaliser le comportement de l'assistant en modifiant le code selon vos besoins.


## Auteur

 Abdoulaye Baldé

