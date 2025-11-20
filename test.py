##############################
# Tests pour la classe Duree #
##############################
# Kim Mens, 30-10-2021, à compléter par les étudiants

# Pour le moment, pour tester votre programme orienté objet
# vous allez encore utiliser les instructions "assert" comme
# dans les missions 5 à 7. 
# (Dans une mission futur nous introduirons le nouveau mécanisme
#  des tests unitaires qui est encore mieux approprié pour tester
#  du code orienté objet.)

# D'abord on doit importer les classe à tester
from mission8 import Duree, Chanson, Album

# CREATION DE QUELQUES OBJETS DE LA CLASSE Duree A TESTER
d0 = Duree( 0, 0, 0)
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)

# FONCTION POUT TESTER LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str() :
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS
    
# FONCTION POUR TESTER LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes() :
    assert d0.to_secondes() == 0, "Test 1 Duree toSecondes"
    assert d1.to_secondes() == 37259, "Test 2 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 1 Duree toSecondes"

# FONCTION POUR TESTER LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    assert d0.delta(d1) == -37259, "Test 1 Duree toSecondes"
    assert d1.delta(d0) == 37259, "Test 1 Duree toSecondes"
    
# FONCTION POUR TESTER  LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert d1.apres(d2),     "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"
    
# FONCTION POUR TESTER LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    # A COMPLETER PAR LES ETUDIANTS
    assert d1.ajouter(d2) == "19:02:24", "Test 1 Duree apres"
    assert d1.ajouter(d0) == "19:02:24", "Test 2 Duree apres"
    assert d1.ajouter(d2) == "27:43:49", "Test 2 Duree apres"

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

################################
# Tests pour la classe Chanson #
################################

# CREATION DE QUELQUES OBJETS DE LA CLASSE Chanson A TESTER
c = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Chanson_str(chanson) :
    # A COMPLETER PAR LES ETUDIANTS
    assert str(chanson) == "Let's Dance - David Bowie - 00:04:05", "Test 1 Chanson str"

def test_Chanson_get_time(chanson) :
    # A COMPLETER PAR LES ETUDIANTS
    assert str(chanson.get_time()) == "00:04:05", "Test 1 Chanson get_time"

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c)
test_Chanson_get_time(c)

##############################
# Tests pour la classe Album #
##############################

# CREATION D'UN OBJET DE LA CLASSE Album A TESTER
a1 = Album(1)
a2 = Album(69)
c1 = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))
c2 = Chanson("The City", "Daddyphatsnaps", Duree("0.99999999","4","0"))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Album_str1(album) :
    # A COMPLETER PAR LES ETUDIANTS
    print()
    assert str(album) == "Album 1 (0 chansons, 00:00:00)\n", "Test 1.1 Album str"

def test_Album_add1(album, chanson) :
    # A COMPLETER PAR LES ETUDIANTS
    assert album.add(chanson) == True, "Test 1.1 Album add"


def test_Album_add2(album, chanson) :
    # A COMPLETER PAR LES ETUDIANTS
    assert album.add(chanson) == True, "Test 1.2 Album add"

def test_Album_str2(album) :
    # A COMPLETER PAR LES ETUDIANTS
    assert str(album) == "Album 69 (1 chanson, 00:04:00)\n01: The City - Daddyphatsnaps - 00:04:00\n", "Test 1.2 Album str"

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Album_str1(a1)
test_Album_add1(a1, c1)

test_Album_add2(a2, c2)
test_Album_str2(a2)

#####################################
# Test du comportement du programme #
#####################################

f = open("tp8\music-db-txt","r")
lines = f.readlines()
f.close()

line_list = []
for l in lines:
    line_list.append(l.strip().split())

i = 1
di = {}
di[i] = Album(i)
for ll in line_list:
    time = [ll[2]]
    try:
        time.append(ll[3])
    except:
        pass

    try:
        time.append(ll[4])
    except:
        pass
    
    match len(time):
        case 1:
            #minutes
            m = int(ll[2])
            duree = Duree(0, m, 0)
        case 2:
            #minutes seconds
            m = int(ll[2])
            s = int(ll[3])
            duree = Duree(0, m, s)
        case 3:
            #hours minutes secondes
            h = int(ll[2])
            m = int(ll[3])
            s = int(ll[4])
            duree = Duree(h, m, s)

    song = Chanson(ll[0],ll[1],duree)
    if not di[i].add(song):
        i += 1
        di[i] = Album(i)

for i in di.values():
    print(f"{i}")