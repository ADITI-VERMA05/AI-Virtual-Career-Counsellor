# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

class ActionRecommendCareer(Action):

    def name(self):
        return "action_recommend_career"

    def preprocess(self, text):
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in tokens if w.isalpha() and w not in stop_words]
        return filtered

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")

        words = self.preprocess(user_message)

        # Keyword Logic
        if any(word in words for word in ["code", "ai", "software", "technology"]):
            response = "💻 Recommended: Software Developer, AI Engineer"
        elif any(word in words for word in ["draw", "design", "animation"]):
            response = "🎨 Recommended: Graphic Designer, Animator"
        elif any(word in words for word in ["finance", "business", "investment"]):
            response = "💼 Recommended: CA, Investment Banker"
        elif any(word in words for word in ["data", "statistics", "math"]):
            response = "📊 Recommended: Data Scientist, Analyst"
        else:
            response = "Please tell me more about your interests."

        dispatcher.utter_message(text=response)

        return []