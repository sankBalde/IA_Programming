from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os
import azure.cognitiveservices.speech as speechsdk
import openai

# This example requires environment variables named "OPEN_AI_KEY" and "OPEN_AI_ENDPOINT"
# Your endpoint should look like the following https://YOUR_OPEN_AI_RESOURCE_NAME.openai.azure.com/
openai.api_key = os.getenv("OPEN_AI_KEY")

# This will correspond to the custom name you chose for your deployment when you deployed a model.
deployment_id='text-davinci-003'

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region=os.getenv("SPEECH_REGION"))
audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

# Should be the locale for the speaker's language.
speech_config.speech_recognition_language="fr-FR"
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# The language of the voice that responds on behalf of Azure OpenAI.
speech_config.speech_synthesis_voice_name='fr-FR-JeromeNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)

# The model history
history = [{"role": "system", "content": f"Tu es Jarvis,une IA et en meme temps mon meilleur partenaire.je veux des reponses courtes à mes questions de maniere consise et precise. Par contre apres chaque reponse,tu dois me poser une question pertinente. si tu as compris, dit OK."},
           {"role": "assistant", "content": f"OK"}]


def chat(question):
    history.append({"role":"user", "content":question})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )
    response_text = completion.choices[0].message.content
    history.append({"role":"assistant", "content":response_text})
    return response_text

def text_to_speech(text):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region=os.getenv("SPEECH_REGION"))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='fr-FR-JeromeNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")


class JarvisScreen(Screen):
    def __init__(self, **kwargs):
        super(JarvisScreen, self).__init__(**kwargs)
        self.reconize_text = ""

    def on_button_jarvis_press(self):
        # Add your custom function here for button press event
        self.start_listening()

    def on_button_jarvis_release(self):
        # Add your custom function here for button release event
        self.stop_listening()


    def start_listening(self):
        # Function to start listening for speech input and interact with Azure OpenAI
        print("Azure OpenAI is listening. Say 'Stop' or press Ctrl-Z to end the conversation.")
        try:
            # Get audio from the microphone and then send it to the TTS service.
            speech_recognition_result = speech_recognizer.recognize_once_async().get()

            # If speech is recognized, send it to Azure OpenAI and listen for the response.
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                if speech_recognition_result.text == "Stop.":
                    print("Conversation ended.")
                print("Recognized speech: {}".format(speech_recognition_result.text))
                self.reconize_text = speech_recognition_result.text
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))

        except EOFError:
            pass

    def stop_listening(self):
        # Function to stop the conversation when the button is released
        self.ask_openai(self.reconize_text)
        # Implement any additional actions you want when the button is released here.

    def ask_openai(self, prompt):
        # Function to ask Azure OpenAI
        response = chat(prompt)
        print('Azure OpenAI response:' + response)
        # Add any actions you want to perform with the OpenAI response here.
        text_to_speech(response)


class MainApp(App):
    def build(self):
        return GUI

if __name__ == '__main__':
    GUI = Builder.load_file("main.kv")
    MainApp().run()
