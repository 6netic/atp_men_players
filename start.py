from MenTennisPlayer import MenTennisPlayer


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
# Getting match results
htmlFile = "ranking/atp_men_rank.html"
# Getting urls of all match results for those 300 men tennis players
matchResultUrls = menAtpPlayer.getUrlOfMatchResultForAllMenPlayers(htmlFile)
#print(matchResultUrls)
# Creating csv file containing match results of the 300 first ATP men players
menAtpPlayer.getScoreResults(matchResultUrls)




'''
24.07. 08:45Djokovic N. (Srb)Dellien H. (Bol)206262V
--------------------------------------------------------------
# Get result of matches for each tennis player
resultList = self.scrapeLocal("matches/" + str(j) + ".html")
line = []
field = resultList.find("span", "event__title--name").parent.text
#print("field vaut:", field)
rank = int(resultList.find("span", "participant-detail-rank") \
        .text.replace("ATP: ", "").replace(".", ""))
player1 = resultList.select(".event__participant.event__participant--home")[0].text
player2 = resultList.select(".event__participant.event__participant--away")[0].text
#print(field, rank, player1, player2)
line.append(field)
line.append(rank)
line.append(player1)
line.append(player2)
allResultList.append(line)
print(allResultList) # ajouté pour tests
j += 1

'''


