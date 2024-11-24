from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

lat_teksts = str(input("Ievadiet tekstu: "))
eng_teksts = GoogleTranslator(source='lv', target='en').translate(lat_teksts)

sentiment_obj = SentimentIntensityAnalyzer()
sentiment_dict = sentiment_obj.polarity_scores(eng_teksts)

print (f"Pozitivitāte: {str(sentiment_dict['pos'] * 100)}%")
print (f"Negativitāte: {str(sentiment_dict['neg'] * 100)}%")
print (f"Neitralitāte: {str(sentiment_dict['neu'] * 100)}%")

if sentiment_dict['compound'] >= 0.05:
  print ("Teksts ir pozitīvs")
elif sentiment_dict['compound'] <= - 0.05:
  print ("Teksts ir negatīvs")
else:
  print ("Teksts ir neitrāls")