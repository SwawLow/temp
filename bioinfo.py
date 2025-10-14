def is_adn(s: str) -> bool:
    """
    prerequisite: requires 1 argument: s is a string
    
    post: returns true or false based on if a, t, c, and g are the only characters present
    
    """

    s = s.upper()

    for k in range(len(s)):
        if s[k] != "A" and s[k] != "T" and s[k] != "C" and s[k] != "G":
            return False
    return True

def positions(s: str, p: str) -> list:

    """
    prerequisite: requires 2 arguments: s and p are strings, s is a dna sequence and p is the objective
    
    post: returns the indexes of the where starts the objective  (ex: find p(cg) in s(ACCGACCG) -> [1,5])
    
    """

    s = s.upper()
    p = p.upper()

    tempList = []
    tempListLengthOfp = len(p)
    
    for k in range(len(s)):
        tempVar = tempListLengthOfp
        for n in range(tempListLengthOfp):
            if s[k+n] == p[n]:
                tempVar -= 1
            else:
                break

        if tempVar == 0:
            tempList.append(k)
   
    return tempList

def distance_h(s1: str, s2: str) -> int:

    """
    prerequisite: requires 2 arguments: s1 and s2 are strings, s1 & s2 are dna sequences
    
    post: returns the number of differences in each list (ex: compare s1(ACG) and s2(ACT) -> 1)
    
    """

    s1.upper()
    s2.upper()
    tempVar = 0

    if len(s1) == len(s2):
        tempListLength = len(s1)
        for k in range(tempListLength):
            if s1[k] != s2[k]:
                tempVar += 1

        return tempVar
    
    else:
        return None

def distances_matrice(l: str|list):

    """
    prerequisite: requires 1 argument: l is either a string or a list of strings
    
    post: returns a matrix with all strings being compared with values of the distance_h() function
    
    """

    tempListLength = len(l)
    if type(l) == list:
        for j in range(tempListLength):
            if not is_adn(l[j]):
                return f"{l} is not a valid dna sequence"
            
    elif type(l) == str:
        if not is_adn(l):
                return f"{l} is not a valid dna sequence"
    
    else:
        return f"{l} is not a valid input"

    tempList = [['none' for _ in range(tempListLength)] for _ in range(tempListLength)]

    for k in range(tempListLength):
        for n in range(tempListLength):
          tempList[k][n] = distance_h(l[k],l[n])
    
    return tempList


#["AG", "AT", "GT", "ACG", "ACT" ]
#"AT"

fnshdProd = distances_matrice(["AG", "AT", "GT", "ACG", "ACT" ])

for t in range(len(fnshdProd)):
    print(fnshdProd[t])