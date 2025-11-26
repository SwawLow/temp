Ayoub 
Sebastian

Duree, from select values, can:
    Will convert any str/float parametre to int:__init__(self, h, m, s)
    Initialised values:__init__(self, h, m, s):
        self.h = h - int
        self.m = m - int
        self.s = s - int
    Convert hours and minutes into seconds: to_seconds(self)
    Calculate the difference of two different times: delta(self,d)
    Checks which of two values who's bigger and returns a bool (bigger = True): apres(self,d)
    Add two times together: ajouter(self,d)
    Appears in this form when printed, 'h:m:s' if length of the values exceed 1 else, '0h:0m:0s':__str__(self)

Media function as a mother class to Chanson, Video et LivreAudio:
    Initialised values:__init__(self, title, author, duree):
        self
        self.title = title - str
        self.author = author - str
        self.duree = duree - Duree
    
    Calculates the size of a media based on the return value of taille_par_seconde(self) function in Chanson, Video et LivreAudio:taille(self)
    Returns a NotImplementedError when called/used:taille_par_seconde(self):
    Returns a string that represents this media's type, 'Media':type_media(self):
    Appears in this form when printed,"(DUREE, TYPE) 'TITRE' par AUTEUR":__str__(self)

    Chanson(Media), from select values, can:
        Initialised values:__init__(self, title, author, duree, singleOrAlbum, album, feat):
            self
            Media values(title, author, duree)
            self.single = singleOrAlbum - bool/str
            self.album = album - str
            self.feat = feat - list[str]

        Returns a value(0.01) that will be used in the taille(self) function in media to calculate this media's size:taille_par_seconde(self)
        Returns a string that represents this media's type, 'Chanson':type_media(self)
        Appears in this form when printed, "Media.__str__() (self.feat) [Album]/- Single":__str__(self)

    LivreAudio(Media), from select values, can:
        Initialised values:__init__(self, title, author, duree, editeur):
            self
            Media values(title, author, duree)
            self.editeur = editeur - str

        Returns a value(0.01) that will be used in the taille(self) function in media to calculate this media's size:taille_par_seconde(self)
        Returns a string that represents this media's type, 'Livre Audio':type_media(self)
        Appears in this form when printed, "Media.__str__(), édité par self.editeur":__str__(self)

    Video(Media), from select values, can:
        Initialised values:__init__(self, title, author, duree, resolution):
            self
            Media values(title, author, duree)
            self.resolution(144p, 240p, 360p, 480p, 720p, 1080p, 4K) = resolution - str/int

        Returns a value(0.085, 0.1, 0.12, 0.15. 0.2, 0.5 and 1) that will be used in the taille(self) function in media to calculate this media's size,
        the return value ranges due to the self.resolution value:taille_par_seconde(self)
        Returns a string that represents this media's type, 'Video':type_media(self)
        Appears in this form when printed, "Media.__str__() (self.resolution)":__str__(self)

ListeLecture, from select values, can:
    ListeLecture.__idn__ exist outside all classes and starts with a value of 0.
    Increaments by orders of 1 every time a new ListeLecture class object is created, 
    making the ids created by ListeLecture unique
    Initialised values:__init__(self, name):
        self
        self.id = ListeLecture.__idn__
        self.name = name - str
        self.medias = [] - list
        self.duree = Duree(0, 0, 0) - Duree

    Adds a Media object(Media, Chanson, Video et LivreAudio) to the self.medias list:ajouter(self, media)
    Print the size of every media object in the ListeLecture object and the total,
    appears in this form when printed:print_taille(self):
        """
        [120.20MB] Media Object
        [10.80MB] Media Object
        [13.20MB] Media Object
        [93.81MB] Media Object
        TOTAL : 238.01MB
        """
    
    Appears in this form when printed:__str__(self): 
        [#self.id] self.name (len(self.medias) = number of media in self.media medias)
        01: Media Object
        ...
        20: Media Object
