"""
HuggingFace API teszt szkript.
Az ingyenes HuggingFace API használatát demonstrálja egyszerű szöveggenerálással.
"""

import os
from transformers import pipeline
from dotenv import load_dotenv

def init_huggingface():
    """
    HuggingFace környezet inicializálása.
    Betölti az API kulcsot a környezeti változókból.
    """
    load_dotenv()
    return os.getenv('HUGGINGFACE_API_KEY')

def generate_text(prompt: str) -> str:
    """
    Szöveggenerálás a HuggingFace pipeline segítségével.
    
    Args:
        prompt: A generáláshoz használt kezdő szöveg
        
    Returns:
        A generált szöveg
    """
    # Pipeline létrehozása magyar nyelvű modellel
    generator = pipeline('text-generation', 
                        model='Helsinki-NLP/opus-mt-en-hu',
                        max_length=100)
    
    # Szöveg generálása
    result = generator(prompt)
    
    return result[0]['generated_text']

def main():
    """
    Főprogram: demonstrálja a szöveggenerálást.
    """
    api_key = init_huggingface()
    if not api_key:
        print("Hiba: Nem található HUGGINGFACE_API_KEY környezeti változó!")
        return
    
    test_prompt = "Írj egy rövid mesét egy kis robotról!"
    generated_text = generate_text(test_prompt)
    print(f"Prompt: {test_prompt}")
    print(f"Generált szöveg: {generated_text}")

if __name__ == "__main__":
    main()
