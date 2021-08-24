from MenTennisPlayer import MenTennisPlayer
import os
import codecs


# Defining Urls
atpMenRankingUrl = "https://www.flashscore.fr/tennis/classements/atp/"

# Instanciating the class
menAtpPlayer = MenTennisPlayer(atpMenRankingUrl)
'''
# Getting ranking page
menAtpPlayer.getAtpMenRanking()
# Creating csv file containing the 300 first atp men players
menAtpPlayer.createRankingCsvFile("ranking/atp_men_rank.html")
'''




