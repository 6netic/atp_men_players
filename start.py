from MenTennisPlayer import MenTennisPlayer
import os


# Defining Urls
atpMenRankingUrl = "https://www.flashscore.fr/tennis/classements/atp/"

# Instanciating the class
menAtpPlayer = MenTennisPlayer(atpMenRankingUrl)
menAtpPlayer.getAtpMenRank()


#chemin = os.path.abspath("chromedriver")
#print(chemin)

