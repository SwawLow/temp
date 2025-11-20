class Duree :
    def __init__(self,h,m,s):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro)
            m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        def convert_to_int(e)-> None:
            try:
                if isinstance(e, str):
                    try:
                        e = int(e)
                    except:
                        e = int(float(e))
            except:
                raise TypeError("a wrong type was assigned; int or str must be assigned")
            
            return e
    
        h = convert_to_int(h)
        m = convert_to_int(m)
        s = convert_to_int(s)

        self.hour = h
        if not (m > 60 or s > 60):
            self.minute = m
            self.second = s
        else:
            raise ValueError(f"{m} and {s} cannot exceed 60")
        
        if self.second > 59:
                self.second = self.second-60
                self.minute = self.minute+1
        if self.minute > 59:
            self.minute = self.minute-60
            self.hour = self.hour+1

    
    def to_secondes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """

        hours = self.hour
        minutes = self.minute
        seconds = self.second
        
        total_time = hours*60*60+minutes*60+seconds

        return total_time


    def delta(self,d) :
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
            et la durée d passée en paramètre.
            Cette valeur renovoyée est positif si cette durée (self)
            est plus grand que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """

        if isinstance(d, Duree):
            return self.to_secondes()-d.to_secondes()
        else:
            raise ValueError("An instance of the 'Duree' class must be used as a parametre")
        

    def apres(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
            d passée en paramètre; retourne False sinon.
        """

        if isinstance(d, Duree):
            if self.to_secondes() > d.to_secondes():
                return True
            else:
                return False
        else:
            raise ValueError("An instance of the 'Duree' class must be used as a parametre")

        

    def ajouter(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
            corrigée de manière à ce que les minutes et les secondes soient
            dans l'intervalle [0..60[, en reportant au besoin les valeurs
            hors limites sur les unités supérieures
            (60 secondes = 1 minute, 60 minutes = 1 heure).
            Ne retourne pas une nouvelle durée mais modifié la durée self.
        """

        if isinstance(d, Duree):            
            self.hour += d.hour
            self.minute += d.minute
            self.second += d.second

            if self.second > 59:
                self.second = self.second-60
                self.minute = self.minute+1
            if self.minute > 59:
                self.minute = self.minute-60
                self.hour = self.hour+1

            result = str(self)

            return result
        else:
            raise ValueError("An instance of the 'Duree' class must be used as a parametre")

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
    """
        hours = self.hour
        minutes = self.minute
        seconds = self.second

        if len(str(hours)) == 1:
            hours = f"0{hours}"
        if len(str(minutes)) == 1:
            minutes = f"0{minutes}"
        if len(str(seconds)) == 1:
            seconds = f"0{seconds}"

        return f"{hours}:{minutes}:{seconds}"

class Chanson :
    def __init__(self,t,a,d):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
                un auteur a et une durée d.
        """

        if isinstance(t, str):
            self.title = t
        else:
            raise TypeError("a wrong type was assigned; str must be assigned")
        if isinstance(a, str):
            self.author = a
        else:
            raise TypeError("a wrong type was assigned; str must be assigned")
        if isinstance(d, Duree):
            self.time = d
        else:
            raise TypeError("a wrong type was assigned; an instance of the 'Duree' class must be used as a parametre")

    def get_time(self):
        """
        @pre:  -
        @post: Retourne le temp du chanson
        """

        return self.time

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return f"{self.title} - {self.author} - {self.time}"

class Album :
    def __init__(self, numero):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
            et avec une liste de chansons vide.
        """

        self.chanson = []
        self.time = Duree(0, 0, 0)
        if isinstance(numero, int) or isinstance(numero, str):
            self.id = str(numero)
        else:
            raise TypeError("a wrong type was assigned, int or str must be assigned")


    def add(self,chanson):
        """
        @pre:  chanson une chaine de caracter.
        @post: Ajoute un chanson a un album predefinit.
        """
        if self.time.delta(Duree(1, 15, 0)) > 0 or len(self.chanson) > 99:
            return False
        
        if isinstance(self, Album):
            if isinstance(chanson, Chanson):
                self.chanson.append(chanson)
                self.time.ajouter(chanson.get_time())
                return True
            else:
                raise TypeError("An instance of the 'Chanson' class must be used as a parametre")
        else:
            raise TypeError("An instance of the 'Album' class must be attached to an Album object")

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        chanson_plurel = "chansons" if len(self.chanson) > 1 or len(self.chanson) == 0 else "chanson"
        return_string = f"Album {self.id} ({len(self.chanson)} {chanson_plurel}, {self.time})\n"

        for chanson_nb in range(0,len(self.chanson)):
            return_string += f"{f'0{chanson_nb+1}' if chanson_nb+1 < 10 else f'{chanson_nb+1}'}: {self.chanson[chanson_nb]}\n"

        return return_string

if __name__ == '__main__':
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    def main():
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

    main()