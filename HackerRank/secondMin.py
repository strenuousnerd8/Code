#Alphabetically sort the students name and print the students with second least score
if __name__ == '__main__':
    lis = []
    scores = []
    res = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name, score])
        scores.append(score)
    secondleast = min(list(filter((min(scores)).__ne__, scores)))
    for data in lis:
        if data[1] == secondleast:
            res.append(data[0])
    res = sorted(res)
    for i in res:
        print(i)