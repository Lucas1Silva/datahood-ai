import os
from dotenv import load_dotenv
from src.scripts.generate_script import generate_script

# Carrega as variáveis de ambiente
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_movie_script(topic):
    """
    Gera um roteiro de filme com base no tópico fornecido.

    Args:
        topic (str): O tópico do filme.

    Returns:
        str: O roteiro gerado.
    """
    script = generate_script(topic)  # Chama a função do generate_script.py
    print("Generated Movie Script:")
    print(script)
    return script


def create_movie_from_script(script):
    """
    Cria um filme a partir do roteiro fornecido.

    Args:
        script (str): O roteiro do filme.
    """
    # Este seria o código para criar o 'movie', como processar vídeos, etc.
    pass


def main():
    """
    Função principal para executar o script.
    """
    topic = input("Enter a movie topic: ")
    script = generate_movie_script(topic)
    create_movie_from_script(script)


if __name__ == "__main__":
    main()
