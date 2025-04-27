import os
from dotenv import load_dotenv
import openai


def load_api_key():
    """Carrega a chave da API do arquivo .env."""
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")


def generate_script(topic):
    """
    Gera um roteiro de vídeo explicativo sobre um tópico.

    Args:
        topic (str): O tópico para o roteiro.

    Returns:
        str: O roteiro gerado.
    """
    prompt = f"Crie um roteiro de vídeo explicativo sobre o seguinte tópico: {topic}"

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Usando o modelo gpt-3.5-turbo
            prompt=prompt,
            max_tokens=2000,
        )
        script = response['choices'][0]['text']
        return script.strip()
    except Exception as error:
        return f"Erro ao gerar o roteiro: {error}"


def main():
    """Função principal para executar o script."""
    openai.api_key = load_api_key()
    if not openai.api_key:
        print("Erro: OPENAI_API_KEY não encontrada no arquivo .env.")
        return

    topic = input("Enter a topic: ").strip()
    if not topic:
        print("Erro: Nenhum tópico foi fornecido.")
        return

    script = generate_script(topic)
    print("Generated Script:")
    print(script)


if __name__ == "__main__":
    main()