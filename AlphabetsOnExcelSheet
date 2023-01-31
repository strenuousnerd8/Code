#IBM Question

def findPrecedingAlphabets(rows, alphabet):
    res = []
    ind = []
    restr = ""
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == alphabet:
                res.append(rows[i][0: j])
                ind = [i, j]
                
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if i <= (ind[0] - 1):
                if j == ind[1]:
                    restr += rows[i][j]
            else:
                break
            
    res.append(restr)
    return res

if __name__ == '__main__':
        
    rows = [
        "AXDER",
        "SUJQW",
        "YTMBC",
        "OLFGH"
        ]
        
    alphabet = "M"
    
    print(findPrecedingAlphabets(rows, alphabet))
