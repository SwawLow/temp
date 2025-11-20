Ayoub
Sebastian

Duree, from select values, can:
    Will convert any str/float parametre to int:__init__(self,h,m,s)
    Initialised values:
        h = hours
        m = minutes
        s = seconds
    Convert hours and minutes into seconds: to_seconds(self)
    Calculate the difference of two different times: delta(self,d)
    Checks which of two values who's bigger and returns a bool (bigger = True): apres(self,d)
    Add two times together: ajouter(self,d)
    Appears in this form when printed, 'h:m:s' if length of the values exceed 1 else, '0h:0m:0s':__str__(self)

Chanson, from select values, can:
    Initialised values:
        t = title
        a = author
        d = time
    Returns the time inputed as a parametre under this form, 00:00:00:get_time(self)
    Appears in this form when printed, 't - a - d':__init__(self)

Album, from select values, can:
    Initialised values:
        *chanson = []
        *time = Duree(0, 0, 0)
        id = numero

    adds a song to a defined album, 00:00:00:add(self,chanson):
        -Album can have up to 100 songs
    Appears in this form when printed, 'Album 0 (100 chanson, 00:00:00)\n01: title - author - time\n'...100: title - author - time\n':__init__(self)

*Not parametres