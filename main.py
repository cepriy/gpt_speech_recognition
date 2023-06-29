
import pyttsx3
import openai
import  gradio as gr
import speech_recognition as sr


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def STT():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
       print("Recognizing")
       query = r.recognize_google(audio, language="en-US")
       print("Human said: " + query)
    except Exception as e:
        print(e)
        print("Say this again, please!")
        return "None"
    return query

openai.api_key = "***YOUR API KEY"
prompt = "The following is an application with an assistant"




def get_output(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        temperature = 0.9,
        prompt = prompt,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        stop = ["AI", "Human"]

    )
    speak(response.choices[0].text)


def gpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output = get_output(inp)
    history.append((input, output))
    return history, history


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = "\nAI"
    restart = "\nHuman"
    block = gr.Blocks()
    while(True):
        query = STT()
        get_output(query)

