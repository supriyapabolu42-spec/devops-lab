from openai import OpenAI
OLLAMA_BASE_URL="https//localhost:11434/v1"
ollama=OpenAI(base_url=OLLAMA_BASE_URL,api_key="OLLAMA")
response=ollama.chat.completions.create(mode="llama3.2",messages=[{"role":"user","content":"what is 2+2"}])
print(response.choices[0].message.content)