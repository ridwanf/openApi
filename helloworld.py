from decouple import config
import openai

# OPENAI_API_KEY = config('OPENAI_API_KEY')

openai.api_key = config('OPEN_API_KEY')
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role":"user", "content":"Hello World"}],
)

print(response["choices"][0]["message"]["content"])