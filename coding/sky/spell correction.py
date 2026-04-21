from textblob import TextBlob
text = TextBlob("I havv a spelinyg errror")
print(text.correct())