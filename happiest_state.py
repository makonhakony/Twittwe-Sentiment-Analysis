import sys
import json
import re

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def calc_sent(texts, points):
    score = 0
    for text in texts:
        if text in points.keys():
                score += points[text]
    return score
    

def state_eval(data, afinn):
    stateWithSent = {}

    pattern = r"fullName='[A-Za-z\s]+, ([A-Z]{2})'"
    for item in data:
        texts = item['Tweets'].split(' ')
        place = item["Place"]

        match = re.search(pattern, place)

        if match:
            state_code = match.group(1)
            if state_code in states.keys():
                if state_code not in stateWithSent.keys():
                    stateWithSent[state_code] = calc_sent(texts, afinn)
                else:
                    stateWithSent[state_code] += calc_sent(texts, afinn)
    highestState = max(stateWithSent, key=stateWithSent.get)
    print(highestState, max(stateWithSent.values()))
    #print (stateWithSent)

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
    sent_file = open(sys.argv[1])
    data = load_data(sys.argv[2])
    afinn = sent_proc(sent_file)

    state_eval(data, afinn)

if __name__ == '__main__':
    main()