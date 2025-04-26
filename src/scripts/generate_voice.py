import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def synthesize_voice(text_path:str, output_path="datahood_voice.mp3", voice="nova"):
    # Ler o conteúdo do texto
    with open(text_path, "r", encoding="utf-8") as file:
        content = file.read()

    print("[🔊] Gerando áudio com voz:", voice)

    response = openai.audio.speech.create(
        model="tts-1-hd",
        voice=voice,  # opções: "nova", "alloy", "shimmer", etc.
        input=content
    )

    # Salvar como mp3
    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"[✅] Voz salva em: {output_path}")

# Exemplo de uso direto
if __name__ == "__main__":
    synthesize_voice("scripts/episode_001.txt")
