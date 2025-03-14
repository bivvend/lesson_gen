#Basic test to check if the openai model is working
import pytest
from utils import generate_text

def test_generate_text():
    prompt = "Write a 100 word description of a GCSE physics lesson on waves." # Example prompt    
    text = generate_text.generate_text(prompt)
    assert text is not None # Check if text is generated    
    print(text)


