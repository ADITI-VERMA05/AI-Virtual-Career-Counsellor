import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Make sure resources exist
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered = [word for word in tokens if word.isalpha()]
    return filtered

def recommend_career(text):
    words = preprocess(text)

    tech_keywords = ["code", "coding", "computer", "technology", "ai", "software", "data"]
    arts_keywords = ["draw", "drawing", "paint", "painting", "design", "creative", "art"]
    commerce_keywords = ["business", "finance", "economics", "account", "bank", "commerce"]

    if any(word in tech_keywords for word in words):
        return "Suggested Careers: Software Developer, AI Engineer, Data Scientist, Cybersecurity Expert"

    elif any(word in arts_keywords for word in words):
        return "Suggested Careers: Graphic Designer, Animator, Fashion Designer, Fine Artist"

    elif any(word in commerce_keywords for word in words):
        return "Suggested Careers: Chartered Accountant, Investment Banker, Business Analyst, Financial Advisor"

    else:
        return "Please tell me more about your interests."