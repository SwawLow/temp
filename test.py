"""
Tests fournis pour la mission 9; Compléter par des étudiants.
@author Kim Mens, sebastian et ayoub
@version 26 novembre 2025
"""

from mission9 import *

#
# FOURNI DE BASE
#

playliste1 = ListeLecture("Minecraft")

medias = [
        Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1)),
        Media("Sweden", "C418", Duree(0, 3, 36)),
        Media("Revenge", "CaptainSparklez", Duree(0, 4, 24)),
        Media("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21))
        ]

for media in medias:
    playliste1.ajouter(media)

medias = [
        Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1)),
        Media("Sweden", "C418", Duree(0, 3, 36)),
        Media("Revenge", "CaptainSparklez", Duree(0, 4, 24)),
        Media("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21))
        ]

playliste2 = ListeLecture("Livres audio Minecraft")

livres_audio = [
        LivreAudio("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21), editeur="404 Éditions"),
        ]

for livre_audio in livres_audio:
    playliste2.ajouter(livre_audio)

playliste3 = ListeLecture("Chanson Minecraft")

medias = [
        Chanson("Sweden", "C418", Duree(0, 3, 36),'False', 'Minecraft OST'),
        Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24), False, 'Fallen Kingdoms', ['Villageois', 'Herobrine']),
        ]

playliste3.ajouter(medias)

playliste4 = ListeLecture("Video Minecraft")

medias = [
        Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '720P'),
        ]

playliste4.ajouter(medias)

def afficher_playliste(playliste):
    print(playliste)

if __name__ == "__main__":
    def Media_test():
        assert_error = 0
        #intentionally wrong
        try:
            assert Media(5, "LeCrafteur", Duree(0, 10, 1)), "Test 1 Media init"
        except:
            assert_error += 1
        try:
            assert Media("Tuto installation Minecraft (100% gratuit!!)", [5], Duree(0, 10, 1)), "Test Media init"
        except:
            assert_error += 1
        try:
            assert Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", {}), "Test 3 Media init"
        except:
            assert_error += 1
        #correct
        try:
            assert Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1)), "Test 4 Media init"
        except:
            assert_error += 1
        print(f"Media_test's assertion errors {assert_error}, nombre attendu: 3")

    def LivreAudio_test():
        assert_error = 0
        #intentionally wrong
        try:
            assert LivreAudio([], "Cube Kid", Duree(2, 36, 21),"404 Éditions"), "Test 1 LivreAudio init"
        except:
            assert_error += 1
        try:
            assert LivreAudio("Journal d'un noob (tome 1)", 5, Duree(2, 36, 21),"404 Éditions"), "Test 1 LivreAudio init"
        except:
            assert_error += 1
        try:
            assert LivreAudio("Journal d'un noob (tome 1)", "Cube Kid", {},"404 Éditions"), "Test 2 LivreAudio init"
        except:
            assert_error += 1
        try:
            assert LivreAudio("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21),True), "Test 3 LivreAudio init"
        except:
            assert_error += 1
        #correct
        try:
            assert LivreAudio("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21),"404 Éditions"), "Test 4 LivreAudio init"
        except:
            assert_error += 1
        print(f"LivreAudio_test's assertion errors {assert_error}, nombre attendu: 4")

    def Chanson_test():
        assert_error = 0
        #intentionally wrong
        try:
            assert Chanson([], "CaptainSparklez", Duree(0, 4, 24),"album","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 1 Chanson init"
        except:
            assert_error += 1
        try:
            assert Chanson("Revenge", False, Duree(0, 4, 24),"album","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 2 Chanson init"
        except:
            assert_error += 1
        try:
            assert Chanson("Revenge", "CaptainSparklez", 120,"album","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 3 Chanson init"
        except:
            assert_error += 1
        try:
            assert Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"cpu","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 4 Chanson init"
        except:
            assert_error += 1
        try:
            assert Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"album",{},["Villageois", "Herobrine"]), "Test 5 Chanson init"
        except:
            assert_error += 1
        try:
            assert Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"album","Fallen Kingdoms",[6, 9]), "Test 6 Chanson init"
        except:
            assert_error += 1
        #correct
        try:
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"album","Fallen Kingdoms"), "Test 7 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"album","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 8 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"albu","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 9 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"alb","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 10 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"al","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 11 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"a","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 12 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"no","Fallen Kingdoms"), "Test 13 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"n","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 14 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),False,"Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 15 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"False","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 16 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"false","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 17 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"fals","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 18 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"fal","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 19 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"fa","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 20 Chanson init"
            Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24),"f","Fallen Kingdoms",["Villageois", "Herobrine"]), "Test 21 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "single", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 22 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "singl", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 23 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "sing", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 24 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "sin", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 25 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "si", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 26 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "s", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 27 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), True, "randomBullshit. Go!!!!", ['Mix Williams']), "Test 28 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "True", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 29 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "true", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 30 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "tru", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 31 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "tr", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 32 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "t", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 33 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "yes", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 34 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "ye", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 35 Chanson init"
            Chanson('Bet', 'Daddyphatsnaps', Duree(0,3,3), "s", "randomBullshit. Go!!!!", ['Mix Williams']), "Test 36 Chanson init"
        except:
            assert_error += 1
        print(f"Chanson_test's assertion errors {assert_error}, nombre attendu: 5")

    def Video_test():
        assert_error = 0
        #intentionally wrong
        try:
            assert Video(5, "LeCrafteur", Duree(0, 10, 1), '4K'), "Test 1 Video init"
        except:
            assert_error += 1
        try:
            assert Video("Tuto installation Minecraft (100% gratuit!!)", [5], Duree(0, 10, 1), '4K'), "Test Video init"
        except:
            assert_error += 1
        try:
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", {}, '4K'), "Test 3 Video init"
        except:
            assert_error += 1
        try:
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), "randomBullshit. Go!!!!"), "Test 4 Video init"
        except:
            assert_error += 1
        #correct
        try:
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '4K'), "Test 5 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '4k'), "Test 6 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '1080p'), "Test 7 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '1080P'), "Test 8 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '720p'), "Test 9 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '720P'), "Test 10 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '480p'), "Test 11 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '480P'), "Test 12 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '360p'), "Test 13 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '360P'), "Test 14 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '240p'), "Test 15 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '240P'), "Test 16 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '144p'), "Test 17 Video init"
            assert Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '144P'), "Test 18 Video init"
        except:
            assert_error += 1
        
        print(f"Video_test's assertion errors {assert_error}, nombre attendu: 4")

    def main():
        print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE Media ***\n")
        afficher_playliste(playliste1)
        print("TEST TAILLE")
        playliste1.print_taille()
        print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE LivreAudio ***\n")
        afficher_playliste(playliste2)
        print("TEST TAILLE")
        playliste2.print_taille()
        print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE Chanson ***\n")
        afficher_playliste(playliste3)
        print("TEST TAILLE")
        playliste3.print_taille()
        print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE Video ***\n")
        afficher_playliste(playliste4)
        print("TEST TAILLE")
        playliste4.print_taille()

        Media_test()
        LivreAudio_test()
        Chanson_test()
        Video_test()

    main()
