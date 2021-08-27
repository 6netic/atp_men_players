from MenTennisPlayer import MenTennisPlayer


# Defining Urls
atpMenRankingUrl = "https://www.flashscore.fr/tennis/classements/atp/"

# Instanciating the class
menAtpPlayer = MenTennisPlayer(atpMenRankingUrl)

# Getting ranking page
menAtpPlayer.getAtpMenRanking()
# Creating csv file containing the 100 first atp men players
menAtpPlayer.createRankingCsvFile("ranking/atp_men_rank.html")

# Getting match results
htmlFile = "ranking/atp_men_rank.html"
# Getting urls of all match results for those 300 men tennis players
matchResultUrls = menAtpPlayer.getUrlOfMatchResultForAllMenPlayers(htmlFile)
# Creating csv file containing match results of the 100 first ATP men players
menAtpPlayer.getScoreResults(matchResultUrls)

