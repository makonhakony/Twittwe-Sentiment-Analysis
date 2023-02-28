import sys
import json

def calc_sent(texts, points):
    score = 0
    for text in texts:
        if text in points.keys():
                score += points[text]
    return score


htList = {}

def count_hashtag(data):
    global htList

    for item in data:
        hashTags = item["Hashtags"]
        if (hashTags):
            for each in hashTags:
                if each not in htList.keys():
                    htList[each] = 1
                else:
                    htList[each] += 1

def print_hastag():
    top_10 = sorted(htList.items(), key=lambda x: x[1], reverse=True)[:10]

    for item in top_10:
        print(item[0],item[1])

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

def main():
    data = load_data(sys.argv[1])

    count_hashtag(data)
    print_hastag()

if __name__ == '__main__':
    main()