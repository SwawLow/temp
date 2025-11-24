def readfile(filename: str) -> list:
    """ Crée une liste des lignes contenues dans un fichier dont le nom est ``filename``

    pre:
        filename: le nom d'un fichier de texte
    post:
        retourne une liste dans laquelle chaque ligne du fichier filename est un élément.
        Si filename n'existe pas, la fonction retourne une liste vide.
    """

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except:
        raise FileNotFoundError

def get_words(line: list) -> list:
    """ Pour une chaîne de caractères donnée, retourne une liste des mots dans
        la chaîne en minuscules et dans l'ordre d'apparence dans le texte. La
        ponctuation et les caractères non-alphabétiques doivent être ignorés et
        retirés des mots.

        Par exemple :
            - Pour la chaîne de caractères :
                "Turmoil has engulfed the Galactic Republic. The taxation of
                trade routes to outlying star systems is in dispute."
              Le résultat est :
                ["turmoil", "has", "engulfed", "the", "galactic", "republic",
                "the", "taxation", "of", "trade", "routes", "to", "outlying",
                "star", "systems", "is", "in", "dispute" ]
            - Pour la chaîne de caractères :
                "These aren't the droids you're looking for."
              Le résultat est :
                ['these', 'arent', 'the', 'droids', 'youre', 'looking', 'for']

        Un caractère est considéré comme une ponctuation ou un
        caractère non-alphabétique si ce n'est pas une lettre, selon la
        fonction string.isalpha().

    pre:
        line: une chaîne de caractères.
    post:
        retourne une liste des mots dans la chaîne, en minuscules, et sans ponctuation.
    """

    if not isinstance(line, list):
        raise TypeError("only list elements may be used")

    
    cleaned_words = []
    for word in line:
        correct_char = ""
        for char in word:
            if char.isalpha():
                correct_char += char.lower()
        cleaned_words.append(correct_char)
    return cleaned_words

def create_index(filename: str) -> dict:
    """ crée un index pour le fichier avec nom ``filename``. L'index se compose
        d'un dictionnaire dans lequel pour chaque mot du fichier ``filename``
        on retrouve une liste des indices des lignes du fichier qui contiennent
        ce mot.

        Par exemple, pour un fichier avec le contenu suivant:

          While the Congress of the Republic endlessly debates
          this alarming chain of events, the Supreme Chancellor has
          secretly dispatched two Jedi Knights.

        Une partie de l'index, representé comme dictionnaire, est:


          {"while": [0], "the": [0,1], "congress": [0], \
           "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

    pre:
        filename: une chaîne de caractères
    post:
        retourne un dictionnaire avec pour chaque mot du fichier (en minuscules)
        la liste des indices des lignes qui contiennent ce mot.
    """    

    contents = readfile(filename)
    
    for line in range(len(contents)):
        contents[line] = get_words(contents[line].split())
    
    dictionary = {}
    for k in range(len(contents)):
        for n in contents[k]:
            if k != 0:
                if n in dictionary:
                    dictionary[n].append(k)
                else:
                    dictionary[n] = [k]
            else:
                dictionary[n] = [k]
                

    return dictionary

def get_lines(words: list, index: dict) -> list:
    """ Détermine les lignes qui contiennent tous les mots indexes dans ``words``,
        selon l'index ``index``.

        Par exemple, pour l'index suivant:

            index = {"while": [0], "the": [0,1], "congress": [0], \
                    "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

        La fonction retourne
            get_lines(["the"], index) -> [0, 1]
            get_lines(["jedi"], index) -> [2]
            get_lines(["the", "of"], index) -> [0, 1]
            get_lines(["while", "the"], index) -> [0]
            get_lines(["congress", "jedi"], index) -> []
            get_lines(["while", "the", "congress"], index) -> [0]

    pre:
        words: une liste de mots, en minuscules
        index: un dictionnaire contenant pour mots (en minuscules) des listes de nombres entiers
    post:
        retourne une liste des nombres des lignes contenant tous les mots indiqués
    """
    if isinstance(words, list):
        for check_nb in range(len(words)):
            if not isinstance(words[check_nb], str):
                raise TypeError("only string elements may be used within the list", "get_lines(list, dict)")
    else:
        raise TypeError("only lists may be used", "get_lines(list, dict)")
    
    if not isinstance(index, dict):
            raise TypeError("only dictionnaries may be used", "get_lines(list, dict)")

    index_list = []
    for word in words:
        for key, value in index.items():
            if key == word:
                if len(words) == 1:
                    return value
                else:
                    index_list.append(value)
    
    similar_occurences = []
    for value_index in range(len(index_list)-1):
        for subsquent in index_list[value_index+1]:
            for first in index_list[0]:
                if first == subsquent and subsquent not in similar_occurences:
                    similar_occurences.append(subsquent)

    return similar_occurences

if __name__ == "__main__":
    def main():
        print(get_lines(["the", "jedi", "congress"], create_index("tp7/text0.txt")))
    
    main()