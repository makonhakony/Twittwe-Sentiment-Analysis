import sys
import json
from sklearn.naive_bayes import MultinomialNB
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

def load_data(fin):
    with open(fin, 'r') as data_file:
        json_data = data_file.read()
    
    return json.loads(json_data)

def sent_proc(sent_file):
    points = {}
    for line in sent_file:
        sent,point = line.split("\t")
        points[sent] = int(point)
    return points

def extract_features(text,afinn):
    blob = TextBlob(text.lower())
    words = blob.words.lemmatize()
    vectorizer = CountVectorizer(vocabulary=afinn.keys(), lowercase=False)
    features = vectorizer.fit_transform(words).toarray().sum(axis=0)
    return features

def train_classifier(afinn):
    X = []
    y = []
    for sent, point in afinn.items():
        X.append(extract_features(sent,afinn))
        y.append(int(point > 0))
    classifier = MultinomialNB()
    classifier.fit(X, y)
    return classifier

def compute_new_term_sentiment(text, afinn, clf):
    features = extract_features(text,afinn)
    sentiment_score = clf.predict_proba([features])[0, 1] - clf.predict_proba([features])[0, 0]
    return sentiment_score

def term_eva(data, afinn):
    clf = train_classifier(afinn)

    newTerm = {}

    for item in data:
        texts = item['Tweets'].split(' ')
        print(texts)
        for text in texts:
            if text not in afinn.keys():
                if text not in newTerm.keys():
                    sent = compute_new_term_sentiment(text, afinn, clf)
                    newTerm[text] = round(sent,3)
                    print(text,round(sent,7))

def main():
    sent_file = open(sys.argv[1])
    data = load_data(sys.argv[2])
    afinn = sent_proc(sent_file)

    term_eva(data, afinn)

if __name__ == '__main__':
    main()
