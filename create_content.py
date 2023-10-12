import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def create_content(subject, tokens, temperature, model="text-davinci-002"):
  prompt = f"Por favor escribe un articulo corto sobre el tema {subject}.\n\n"
  response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    n=1,
    max_tokens=tokens,
    temperature=temperature,
  )

  return response['choices'][0]['text'].strip()

def summarize_text(text, tokens, temperature, model="text-davinci-002"):
  prompt = f"Por favor resume el siguiente texto en español: {text}\n\n"
  response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    n=1,
    max_tokens=tokens,
    temperature=temperature,
  )

  return response['choices'][0]['text'].strip()

# subject = input("Por favor ingresa el tema del articulo: ")
# tokens = int(input("Por favor ingresa el numero de palabras del articulo: "))
# temperature = int(input("Del 1 al 10, que tan creativo quieres que sea el articulo: ")) / 10

# content = create_content(subject, tokens, temperature)
# print(content)

original_text = input("Por favor ingresa el texto a resumir: ")
tokens = int(input("Por favor ingresa el numero de palabras del resumen: "))
temperature = int(input("Del 1 al 10, que tan creativo quieres que sea el resumen: ")) / 10

summary = summarize_text(original_text, tokens, temperature)
print(summary)