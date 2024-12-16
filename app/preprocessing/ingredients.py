import re


def preprocess_ingredients(ingredients):
    text = ' '.join(ingredients)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    
    return text
