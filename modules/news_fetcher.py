from dotenv import load_dotenv
import os
from gnews import GNews
import random


class NewsFetcher:
    def __init__(self):
        load_dotenv(dotenv_path='.venv/.env')
        self.gnews_api_key = os.getenv("GNEWS_API_KEY")

    def fetch_random_topic_gnews(self, topic):

        google_news = GNews()
        gnews = random.choice(google_news.get_news(topic))['description']

        return gnews
