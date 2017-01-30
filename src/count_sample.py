import twittercrawler
from collections import defaultdict


class WordCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def clean_word(self, word):
        temp = word.lower()
        return temp

    def custom_handler(self, crawler, tweet):
        if hasattr(tweet, "text"):
            words = tweet.text.split()
            for word in words:
                cleaned_word = self.clean_word(word)
                self.counts[cleaned_word] += 1


def count_words(query):
    wc = WordCounter()
    crawler = twittercrawler.TwitterCrawler(
                query=query,
                max_depth=20,
                handler=wc.custom_handler
            )
    crawler.crawl()
    print(wc.counts)
