import os
from pathlib import Path
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

BASE_PROMPT = """
You are Datahood — an AI with charm, humor and deep technical knowledge.
You love coffee, explaining things clearly, and making people smile.
You're preparing a script for a YouTube video about: "{topic}"
Make it informal, playful, flirty but insightful. Use metaphors, analogies and good storytelling.
Length: Around 1200 words.
"""


def generate_script(topic: str, save_path: str = "scripts") -> None:
    """
    Generates a script for a given topic and saves it to a file.

    Args:
        topic (str): The topic for the script.
        save_path (str): The directory where the script will be saved.
    """
    prompt = BASE_PROMPT.format(topic=topic)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=2000,
    )

    script = response["choices"][0]["message"]["content"]
    Path(save_path).mkdir(exist_ok=True, parents=True)
    file_path = os.path.join(save_path, f"{topic.replace(' ', '_')}.md")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(script)

    print(f"Script saved to {file_path}")


def main() -> None:
    """
    Main function to prompt the user for a topic and generate a script.
    """
    topic = input("Enter a topic: ").strip()
    if topic:
        generate_script(topic)
    else:
        print("Topic cannot be empty.")


if __name__ == "__main__":
    main()
