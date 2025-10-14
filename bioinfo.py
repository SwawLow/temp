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
    tempListCluster = [s,p]
    tempListClusterLength = len(tempListCluster)

    for j in range(tempListClusterLength):
        if not is_adn(tempListCluster[j]):
            return f"{tempListCluster[j]} is not a valid dna sequence"

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

    tempListCluster = [s1,s2]
    tempListClusterLength = len(tempListCluster)

    for j in range(tempListClusterLength):
        if not is_adn(tempListCluster[j]):
            return f"{tempListCluster[j]} is not a valid dna sequence"

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


print("\nFonction — is adn:")
print(f"{is_adn('AC')} #A et C font partie des 4 caracter autoriser(A,C,G & T)")
print(f"{is_adn('AS')} >>> AS is not a valid dna sequence #S ne peut etre dans l'input")
#is_adn

print("\nFonction — positions:")
print(f"{positions('ACGTACTCAC','AS')} >>> AS is not a valid dna sequence #S ne peut etre dans l'input")
print(f"{positions('ACGTACTCAC','AC')} #a indexe 0, 4 et 8 commence la combinaisons des caracter AC")
#positions

print("\nFonction — distances_h:")
print(f"{distance_h('GACGTAGCTCAC','AGATGTACGACT')} #Est le nombre de distance Hamming")
print(f"{distance_h('GACGTAGCTCACSSS','AGATGTACGACT')} #S ne peut etre dans l'input")
print(f"{distance_h('GACGTAGCTCACTTT','AGATGTACGACT')} #La longeur du premier input est different de la deuxieme")
#distances_h

print("\nFonction — distances_matrice:\n")
fnshdProd = distances_matrice(["AG", "AT", "GT", "ACG", "ACT" ])
for t in range(len(fnshdProd)):
    print(fnshdProd[t])

fnshdProd = distances_matrice("AT")
print("#Ci-dessus represent la matrice de la list ['AG', 'AT', 'GT', 'ACG', 'ACT']\nqui a ete traité par la fonction distances_h()\n")
for t in range(len(fnshdProd)):
    print(fnshdProd[t])
print("#Ci-dessus represent la matrice de 'A' et 'T' qui a ete traité par la fonction distances_h()\n")

print(f"{distances_matrice('AS')} #S ne peut etre dans l'input")
#distances_matrice
