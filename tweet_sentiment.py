import sys
import json 

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

def sent_eva(data, points):
    scores = []

    i = 0
    for item in data:
        texts = item['Tweets'].split(' ')

        score = 0
        for text in texts:
            if text in points.keys():
                score += points[text]
        scores.append(score)
        #print(texts)
        print(score)
        # i += 1
        # if (i>10):
        #     break
    jsonString = json.dumps(scores, indent=1)
    jsonFile = open("sentiment.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()


def main():
    sent_file = open(sys.argv[1])
    data = load_data(sys.argv[2])
    points = sent_proc(sent_file)
    
    sent_eva(data, points)

    

if __name__ == '__main__':
    main()
