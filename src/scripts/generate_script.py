import os
from dotenv import load_dotenv
import openai

# Carrega as variáveis do .env
load_dotenv()

# Usa a chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")


def gerar_roteiro(topico):
    prompt = (
        f"Crie um roteiro envolvente, técnico e cativante sobre o tema: {topico}, "
        "narrado por uma IA charmosa chamada Datahood."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    print(gerar_roteiro("Redes Neurais e sua aplicação em carros autônomos"))