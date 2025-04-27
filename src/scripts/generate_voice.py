import os
import pyttsx3
from dotenv import load_dotenv
import openai

# Carrega as variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def text_to_speech(text):
    """
    Converte texto em fala e salva em um arquivo de áudio.
    :param text: Texto a ser convertido em fala.
    """
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output_audio.mp3')
    engine.runAndWait()


def generate_script(topic):
    """
    Gera um script baseado no tópico fornecido.
    Esta função deve ser implementada ou importada de outro módulo.
    :param topic: Tópico para o qual o script será gerado.
    :return: Script gerado como string.
    """
    # Placeholder para a função de geração de script
    return f"Generated script for topic: {topic}"


def generate_script_and_speech(topic):
    """
    Gera um script baseado no tópico e converte o script em fala.
    :param topic: Tópico para o qual o script será gerado.
    """
    script = generate_script(topic)
    print("Generated Script:")
    print(script)
    text_to_speech(script)


def main():
    """
    Função principal que solicita um tópico ao usuário e inicia o processo.
    """
    topic = input("Enter a topic: ")
    generate_script_and_speech(topic)


if __name__ == "__main__":
    main()
