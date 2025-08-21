import nltk
from nltk import NaiveBayesClassifier, classify

# create feature extractor
def char_features(text, n=3):
    """Return a dictionary of character n-grams as features"""
    text = text.lower()
    features = {}
    for i in range(len(text) - n + 1):
        ngram = text[i:i+n]
        features[f'char_{ngram}'] = True
    return features

# Read training data
with open("x_train.txt", "r", encoding="utf-8") as f:
    train_texts = [line.strip() for line in f]

with open("y_train.txt", "r", encoding="utf-8") as f:
    train_labels = [line.strip() for line in f]


# Filter for desired languages
languages = {"afr", "bos", "deu", "eng", "fra"} #Afrikaans, Bosnian, German, English, and French
train_data = [(char_features(text), label)
              for text, label in zip(train_texts, train_labels)
              if label in languages]

# Read test data
with open("x_test.txt", "r", encoding="utf-8") as f:
    test_texts = [line.strip() for line in f]

with open("y_test.txt", "r", encoding="utf-8") as f:
    test_labels = [line.strip() for line in f]

test_data = [(char_features(text), label)
              for text, label in zip(test_texts, test_labels)
              if label in languages]

# Train classifier on data
classifier = NaiveBayesClassifier.train(train_data)

# Evaluate classifier
accuracy = classify.accuracy(classifier, test_data)
print(f"Accuracy: {accuracy:.2%}")

# Test that it works on your sentence of choice
print(classifier.classify(char_features("wer zuletzt lacht, lacht am besten")))
