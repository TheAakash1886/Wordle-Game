import csv
rankDict = {}
with open('wordRank.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        rankDict[row[0].split(',')[0]] = row[1].split(',')[0]
rankDict.pop('Rank')

def rankedWords(correctWords, incorrectWords):
    myList = []
    defaultList = []
    if correctWords == None and incorrectWords == None:
        for i in range(1,51):
            defaultList.append(rankDict[str(i)])
        return defaultList
    if correctWords != None:
        for key in range(1,len(rankDict)):
            flag = 0
            for letter in correctWords:
                if letter not in rankDict[str(key)]:
                    flag = 1
            if flag == 0:
                myList.append(rankDict[str(key)])
    else:
        for key in rankDict:
            myList.append(rankDict[key])
    if incorrectWords != None:
        for word in myList:
            flag = 0
            for letter in incorrectWords:
                if letter in word:
                    flag = 1
            if flag == 1:
                myList.remove(word)
    return myList

#testcall to check the function is working right
print(rankedWords(['j','k'],['z','y','b']))