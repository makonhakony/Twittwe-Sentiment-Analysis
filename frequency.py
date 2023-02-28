import sys
import json

uniqueTerm={}

def load_data(fin):
    with open(fin, 'r') as data_file:
        json_data = data_file.read()
    
    return json.loads(json_data)

def count_all_terms(data):
    global uniqueTerm
    count = 0

    for item in data:
        texts = item['Tweets'].split(' ')
        for text in texts:
            if text not in uniqueTerm.keys():
                uniqueTerm[text] = 1
                count += 1
            else:
                uniqueTerm[text] += 1
    
    return count

def calc_freq(total):
    for item in uniqueTerm:
        print(item, uniqueTerm[item] / total)

def main():
    data = load_data(sys.argv[1])

    totalTerm = count_all_terms(data)
    calc_freq(totalTerm)

if __name__ == '__main__':
    main()