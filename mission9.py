"""
Classes fournies pour la mission 9; compléter par des étudiants.
@author Kim Mens, sebastian et ayoub
@version 26 novembre 2025
"""
class Duree:
    """
    Représente une durée dans le temps en format hh:mm:ss
    """    

    def __init__(self, h, m, s):
        """
        @pre:  h est un entier positif.
               m est un entier entre 0 (compris) et 60 (non compris)
               s est un entier entre 0 (compris) et 60 (non compris)
        @post: Une object de type 'Duree' est créé
        """
        self.h = h
        self.m = m
        self.s = s

    def to_secondes(self):
        """
        @post: renvoie la durée convertie en secondes (un entier)
        """
        return self.h*3600 + self.m*60 + self.s

    def delta(self, d):
        """
        Renvoie la différence en secondes entre la durée 'self' et 'd'. 
        Peut être négative si la durée représentée par 'd' est plus
        grande que celle de 'self'.
        @pre:  d est une instance de 'Duree'
        @post: la différence en secondes entre 'self' et 'd'
               (la différence est négative si la durée 'd' est plus
                grande la durée 'self')
        """
        return self.to_secondes() - d.to_secondes()

    def apres(self, d):
        """
        Renvoie l'ordre entre 2 durées.
        @pre:  d est une instance de 'Duree'
        @post: renvoie 'True' si la durée représentée par 'self' est
               strictement plus grande que celle représentée par 'd',
               renvoie 'False' sinon.
        """
        return self.delta(d) > 0

    def ajouter(self, d):
        """
        Ajoute la durée 'd' à 'self'.
        @pre:  d est une instance de 'Duree'
        @post: la durée représentée par 'self' est incrémentée par
               la durée représentée par 'd'
        """
        sum = self.to_secondes()+d.to_secondes()
        self.s = sum % 60
        self.m = sum // 60 % 60
        self.h = sum // 3600

    def __str__(self):
        """
        Revoie la représentation en string de la durée
        en format 'hh:mm:ss'
        """
        return "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)

class Media:
    """
    Représente un média générique, comme une chanson, un livre audio ou une vidéo
    qui peut être 'joué' pour être écouté, lu ou regardé.
    """
    
    def __init__(self, titre, auteur, duree):
        """
        @pre:  titre est un string
               auteur est un string
               duree est une instance de 'Duree'
        @post: un média jouable générique
        """

        if isinstance(titre, str):
            self.titre = titre
        else:
            raise TypeError("a wrong type was assigned; str must be assigned")
        
        if isinstance(auteur, str):
            self.auteur = auteur
        else:
            raise TypeError("a wrong type was assigned; str must be assigned")
        
        if isinstance(duree, Duree):
            self.duree = duree
        else:
            raise TypeError("a wrong type was assigned; an instance of the 'Duree' class must be used as a parametre")

    def taille(self):
        """
        Renvoie la taille du média en méga-octets
        """
        return round(self.taille_par_seconde() * self.duree.to_secondes(),3)

    def taille_par_seconde(self):
        """
        Renvoie la taille du média par seconde de durée en méga-octets
        """
        raise NotImplementedError

    def type_media(self):
        """
        Renvoie un string indiquant le type de média
        """
        return "Media"

    def __str__(self):
        """
        Renvoie un string en format "(hh:mm:ss, Type) 'Titre' par Auteur"
        décrivant les détails de ce média.
        """
        s = "({}, {}) '{}' par {}".format(self.duree, self.type_media(), self.titre, self.auteur)
        return s

class LivreAudio(Media):
    """
    Représente un livre audio. En plus des attributs présents dans 'Media', 
    'LivreAudio' inclu aussi un attribut représentant l'éditeur du livre.
    """

    def __init__(self, titre, auteur, duree, editeur):
        """
        @pre:  titre est un string
               auteur est un string
               duree est une instance de 'Duree'
               editeur est un string
        @post: un livre audio ayant les propriétés demandées
        """
        super().__init__(titre, auteur, duree)
        if isinstance(editeur, str):
            self.editeur = editeur
        else:
            raise TypeError("a wrong type was assigned; str must be assigned")

    def taille_par_seconde(self):
        """
        Renvoie la taille de lecture par défaut d'un livre audio
        en méga-octets par seconde
        """
        return 0.01

    def type_media(self):
        """
        Renvoie un string indiquant le type de média
        """
        return "Livre Audio"

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "(self.self, self.type) 'self.titre' par self.auteur, édité par self.editeur".
            Par exemple: (02:36:21, Livre Audio) 'Journal d'un noob (tome 1)' par Cube Kid, édité par 404 Éditions
        """
        s = super().__str__() + ", édité par " + self.editeur
        return s
    
class Chanson(Media):
    def __init__(self, titre, auteur, duree, singleOrAlbum, album=None, feat=[]):
        """
        @pre:  titre et auteur sont des string, 
                duree est une instance de la classe Duree
                singleOrAlbum est un bool ou un string ('yes' ou 'no','true' or 'false, 'single' or 'album')
                album est none (n'est pas neccesaire sauf si singleOrAlbum est Faux ou faut veux etre rempli)
                feat est list de string
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
                un auteur a et une durée d.
        """
        super().__init__(titre, auteur, duree)
        if isinstance(singleOrAlbum, bool):
            self.single = singleOrAlbum
        elif isinstance(singleOrAlbum, str):
            singleOrAlbum = singleOrAlbum.lower()
            if singleOrAlbum in ['yes','y','ye','true','t','tr','tru','single','singl','sing','sin','si','s']:
                self.single = True
            elif singleOrAlbum in ['no','n','false','f','fa','fal','fals','album','albu','alb','al','a']:
                self.single = False
            else:
                raise ValueError("either yes or no must be provided")
        else:
            raise TypeError("a wrong type was assigned; bool or str(yes or no, single or album) must be assigned")
            
        if not singleOrAlbum:
            if album:
                if not isinstance(album, str):
                    raise TypeError("a wrong type was assigned; str must be assigned")
            else:
                raise ValueError("if the song is not a single. The name album must be provided")
        self.album = album
            
        if feat:
            if isinstance(feat, list):
                for check_nb in range(len(feat)):
                    if not isinstance(feat[check_nb], str):
                        raise TypeError("str must be used in the list of authors")
            else:
                raise TypeError("a wrong type was assigned; str must be assigned")
        self.feat = feat
        
    def taille_par_seconde(self):
        """
        Renvoie la taille de lecture par défaut d'un livre audio
        en méga-octets par seconde
        """
        return 0.05

    def type_media(self):
        """
        Renvoie un string indiquant le type de média
        """
        return "Chanson"

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "(self.self, self.type) 'self.titre' par self.auteur (self.feat) [Album]/- Single".
            Par exemple: (00:03:36, Chanson) 'Sweden' par C418 [Album: Minecraft OST]
                        (00:03:36, Chanson) 'Who's Better?' par Daddyphatsnaps (feat. OmarCameUp) - Single
        """
        singleOrAlbum = "- Single" if self.single else f"[Album: {self.album}]"
        featured = ""
        str(list(f"{k}, " for k in self.feat))
        if self.feat:
            featured = "feat. "
            for f in self.feat:
                featured += f"{f}, "
            featured = f" ({featured.rstrip(', ')})"
            
        s = super().__str__() + f"{featured} {singleOrAlbum}"
        return s
    
class Video(Media):
    def __init__(self, titre, auteur, duree, resolution):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
                un auteur a et une durée d.
        """
        super().__init__(titre, auteur, duree)

        if isinstance(resolution, str):
            resolution = resolution.lower()
            if resolution in ['144p', '240p', '360p', '480p', '720p', '1080p', '4k']:
                for res in ['144p', '240p', '360p', '480p', '720p', '1080p', '4K']:
                    if res.lower() == resolution:
                        self.resolution = res
                        break
            else:
                raise ValueError("144p, 240p, 360p, 480p, 720p, 1080p or 4K must be chosen for resolution values")
        else:
            raise TypeError("a wrong type was assigned; str or int must be assigned")

    def taille_par_seconde(self):
        """
        Renvoie la taille de lecture par défaut d'un livre audio
        en méga-octets par seconde
        """
        for res, mult in [('144p',0.85), ('240p',1), ('360p',1.2), ('480p',1.5), ('720p',2), ('1080p',5), ('4K',10)]:
            if res.lower() == str(self.resolution).lower():
                return 0.1*mult

    def type_media(self):
        """
        Renvoie un string indiquant le type de média
        """
        return "Video"

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "(self.self, self.type) 'self.titre' par self.auteur (self.resolution)".
            Par exemple: (00:10:01, Vidéo) 'Tuto installation Minecraft (100% gratuit!!)' par LeCrafteur (720p)
        """

        s = super().__str__() + f" ({self.resolution})"
        return s
    
class ListeLecture:
    __idn__ = 0
    """
    Représente une compilation nommée de médias.
    """

    def __init__(self, name):
        """
        @pre:  name est un string
               id est un entier
        @post: Une instance de 'ListeLecture' ayant un identifiant unique. 
               Si 'id' est déjà utilisé par une autre instance, 
               alors une erreur 'ValueError' sera levée
        """

        self.id = ListeLecture.__idn__
        ListeLecture.__idn__ += 1
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("a wrong type was assigned; str must be assigned")
        
        self.medias = []
        self.duree = Duree(0, 0, 0)

    def ajouter(self, media):
        """
        Ajoute 'media' à la liste de lecture
        @pre:  media est une instance de 'Media'
        @post: la liste de lecture comprend maintenant 'media'
        """
        if isinstance(media, Media):
            self.medias.append(media)
            self.duree.ajouter(media.duree)
        elif isinstance(media, list):
            for m in media:
                if not isinstance(m, Media):
                    raise TypeError("a Media object must be used in the list")
            for k in media:
                self.medias.append(k)
                self.duree.ajouter(k.duree)
        else:
            raise TypeError("a wrong type was assigned; str or a Media object must be assigned")

    def print_taille(self):
        """Imprime une liste des médias de cette liste avec leurs tailles en méga-octets"""
        total = 0
        for media in self.medias:
            try:
                taille = media.taille()
            except NotImplementedError:
                taille = None
            if taille is None:
                print("[Taille inconnue] " + media.titre)
            else:
                print("[{:.2f}MB] ".format(taille) + media.titre)
                total += taille
        print("TOTAL : {:.2f}MB\n".format(total))

    def __str__(self):
        s = "[#{}] {} ({} medias)\n".format(self.id, self.name, len(self.medias))
        i = 1
        for media in self.medias:
            s += "{:02}: ".format(i) + str(media) + "\n"
            i += 1
        return s

if __name__ == '__main__':
    def main():
        m1 = Chanson('The City', 'Daddyphatsnaps',Duree(0,4,15), "s", 'single')
        m2 = Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "sin", "randomBullshit. Go!!!!", ['Mix Williams'])
        m3 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m4 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m5 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m6 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m7 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m8 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m9 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m10 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m11 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m12 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m13 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m14 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m15 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m16 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m17 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m18 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m19 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        m20 = Video("Venom Rap | \"There Will Be Carnage\" | Daddyphatsnaps (Prod. By Musicality) [Marvel]", 'Daddyphatsnaps \"Daddyphatsnaps\" YouTube', Duree(0,3,38), '4k')
        l1 = ListeLecture('Dps')
        l1.ajouter([m1, m2, m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20])
        print(l1)
        l1.print_taille()

    main()