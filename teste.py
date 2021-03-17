from leia import SentimentIntensityAnalyzer

analiser = SentimentIntensityAnalyzer()
final = analiser.polarity_scores("testando o analiser")
print(final['compound'])