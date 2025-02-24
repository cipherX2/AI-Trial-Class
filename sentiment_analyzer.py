""" 

TextBlob is a Python library used for natural language processing (NLP). It makes it easy to work with text data by providing tools for:

1. Sentiment analysis (positive, negative, or neutral)
2. Spelling correction
3. Part-of-speech (POS) tagging
4. Word tokenization (splitting text into words)
5. Translation and language detection
6. Noun phrase extraction

"""

from textblob import TextBlob 

print("\n### Welcome To Simple Sentiment Analyzer ###\n")

"""Get the name from the user"""

name = input("Enter your name: ")
print(f"\nNice to meet you, {name}! Let's try to find the sentiment in your sentence.....")
print("Type 'exit' to quit")

while True:
    
    """Get the sentence """
    sentence = input("Enter a sentence: ")
    if sentence == "exit":
        print(f"Goodbye, {name}\n")
        break

    """ Make it a TextBlob object first...... """

    blob = TextBlob(sentence)

    """ Then tap into the sentiment object which has two values polarity and subjectivity """
    """ Polarity measures how positive or negative the text is (ranges from -1 to 1) """
    """ Subjectivity measures how opinion based the text is (ranges from 0 to 1) """

    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        print("Positive sentiment detected....")
    elif sentiment < 0:
        print("Negative sentiment detected....")
    else:
        print("Neutral sentiment detected.....")

