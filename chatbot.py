import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

lastQuestions = []
lastAnswers = []


def ask(prompt, model="text-davinci-002"):
  response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    n=1,
    max_tokens=150,
    temperature=0.5,
  )

  return response['choices'][0]['text'].strip()

print("Bienvenido a nuestro chatbot básico. Escribe 'salir' cuando quieras terminar la conversación.")

while True:
  history = ""
  prompt = input(">> ")
  if prompt.lower() == "salir":
    break

  for  question, answer in zip(lastQuestions, lastAnswers):
    history += f"El usuario pregunta: {question}\nEl bot responde: {answer}\n"

  prompt = "El usuario pregunta: " + prompt
  response = ask(history + prompt)

  print(f"{response}")

  lastQuestions.append(prompt)
  lastAnswers.append(response)