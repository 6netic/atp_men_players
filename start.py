from tennisPlayer import tennisPlayer


# Defining Urls for Men and Women Tennis players
atpMenRankingUrl = "https://www.flashscore.fr/tennis/classements/atp/"
atpWomenRankingUrl = "https://www.flashscore.fr/tennis/classements/wta/"

print("******************* Get Tennis Players Ranking *************************")
print("1 - ATP Men Ranking")
print("2 - ATP Women Ranking")
print("************************************************************************")
loop_menu = True
while loop_menu:
    myChoice = input("Choose 1 or 2: ")
    try:
        myChoice = int(myChoice)
        if myChoice == 1:
            urlRanking = atpMenRankingUrl
            loop_menu = False
        if myChoice == 2:
            urlRanking = atpWomenRankingUrl
            loop_menu = False
    except:
        pass

# Creating object to instantiate the class
players = tennisPlayer(urlRanking)

if urlRanking == atpMenRankingUrl:
    # Getting ranking of tennis players into HTML page
    players.getAtpRanking("men")
    # Creating csv file containing the 300 first atp men players
    players.createRankingCsvFile("ranking/atp_rank_men.html", "men")
    # Getting urls for match results
    htmlFile = "ranking/atp_rank_men.html"
    # Getting urls of all match results for those 300 tennis players
    matchResultUrls = players.getUrlOfMatchResultForAllPlayers(htmlFile)
    # Creating csv file containing match results of the 300 first ATP men players
    players.getScoreResults(matchResultUrls, "men")
if urlRanking == atpWomenRankingUrl:
    players.getAtpRanking("women")
    players.createRankingCsvFile("ranking/atp_rank_women.html", "women")
    htmlFile = "ranking/atp_rank_women.html"
    matchResultUrls = players.getUrlOfMatchResultForAllPlayers(htmlFile)
    players.getScoreResults(matchResultUrls, "women")
