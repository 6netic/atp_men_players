import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import codecs
import csv


class MenTennisPlayer:
    """ Class representing ATP men players """

    def __init__(self, atpMenRankingUrl):
        """ Initializes the url """

        self.atpMenRankingUrl = atpMenRankingUrl


    def createFolder(self, directory):
        """ This method creates a directory given as a parameter """

        try:
            os.mkdir(directory)
        except:
            pass


    def scrapeLocal(self, htmlFile):
        """ This method gets the local webpage that will be scrapped """

        with open(htmlFile) as file:
            soup = BeautifulSoup(file, 'lxml')
        return soup


    def saveToCsv(self, filename, chart, labels):
        """ Saves the chart to a csv file """

        # Writing to csv file
        with open(filename, mode='w') as players:
            entry = csv.writer(players, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            entry.writerow(labels)
            entry.writerows(chart)


    def getAtpMenRanking(self):
        """ This method gets the ranking of ATP men players.
            User has to click on a link that triggers a JS script to show more match results
            for a specific tennis player. So we use Selenium to do that job.
            Finally that page is saved to a file on the hard drive """

        self.createFolder("ranking")
        self.createFolder("csv")
        # Get absolute path of chromedriver file
        chromePath = os.path.abspath("chromedriver")
        driver = webdriver.Chrome(executable_path=chromePath)
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        # Gets the url and opens it in Chrome navigator
        driver.get(self.atpMenRankingUrl)
        # click on "I accept" button
        python_button = driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']")
        python_button.click()
        time.sleep(2)
        # click on "show more" button
        python_button = driver.find_element_by_xpath("//*[@id='live-table']/div[1]/div[4]/a")
        python_button.click()
        time.sleep(3)
        # Get path of ranking folder and create html file
        rankingPath = os.path.dirname(os.path.abspath("ranking"))
        rankingFile = os.path.join(rankingPath, "ranking", "atp_men_rank.html")
        htmlRankingFile = codecs.open(rankingFile, "w", "utf−8")
        driverContent = driver.page_source
        htmlRankingFile.write(driverContent)
        print("File 'atp_men_rank.html' has been saved to '/ranking' folder.")
        # close browser
        driver.quit()


    def createRankingCsvFile(self, htmlFile):
        """ This method creates a csv file containing the first 100 atp men players """

        resultList = self.scrapeLocal(htmlFile)
        entireList = []
        # Here we choose the 100 first players
        for i in range(100):
            line = []
            number = resultList.select(".rank-column-rank")[i + 1].text
            number = int(number.replace(".", ""))
            line.append(number)
            name = resultList.select(".rankingTable__player")[i].text
            line.append(name)
            points = resultList.select(".rank-column-points")[i + 1].text
            points = int(points.replace(",", ""))
            line.append(points)
            print(line)
            entireList.append(line)
        # Save ranking list to csv file
        self.saveToCsv("csv/ranking.csv", entireList, ["RANK", "PLAYER", "POINTS"])
        print("File 'csv/ranking.csv' has been saved successfully !")


    def getUrlOfMatchResultForAllMenPlayers(self, file):
        """ This method gets the url of each tennis men players's page """

        urlOfMenPlayersResultList = []
        scraped = self.scrapeLocal(file)
        url = scraped.select(".rankingTable__player")
        # Getting urls for each of the 100 first players
        for i in range(0, 100):
            urlOfMenPlayersResultList.append("https://www.flashscore.fr" + url[i].a['href'] + "/resultats/")
        return urlOfMenPlayersResultList


    def getScoreResults(self, urlList):
        """ This method creates a csv file containing some matches of the 100 first men players """

        allResults = []
        j = 1
        self.createFolder("matches")
        for oneLine in urlList:

            chromePath = os.path.abspath("chromedriver")
            driver = webdriver.Chrome(executable_path=chromePath)
            driver.implicitly_wait(0.5)
            driver.maximize_window()
            # Opens each url in a chrome navigator
            driver.get(oneLine)
            # click on "J'accepte" button
            python_button = driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']")
            python_button.click()
            time.sleep(2)
            # click on "show more" button
            python_button = driver.find_element_by_xpath("//*[@id='live-table']/div[1]/div[2]/div/a")
            python_button.click()
            time.sleep(3)
            # Getting file path to save page
            matchResultsPath = os.path.dirname(os.path.abspath("matches"))
            matchResultFile = os.path.join(matchResultsPath, "matches", str(j) + ".html")
            htmlResultFile = codecs.open(matchResultFile, "w", "utf−8")
            # Obtaining page source
            driverContent = driver.page_source
            # Saving the webpage in a file
            htmlResultFile.write(driverContent)
            print("File" + str(j) + ".html has been saved to current path.")
            # close the browser
            driver.quit()

            # Getting result of matches for each tennis player
            resultList = self.scrapeLocal("matches/" + str(j) + ".html")
            # data = resultList.find("span", "event__title--name") or the following:
            data = resultList.select(".icon--flag.event__title.fl_3473162")[0]
            # The number in following range is to get enough match results
            try:
                for i in range(750):
                    lineResults = []
                    val = data.text

                    if len(val) > 40 and "dur" not in val and "gazon" not in val and "terre battue" not in val:
                        ranking = int(resultList.find("span", "participant-detail-rank") \
                                      .text.replace("ATP: ", "").replace(".", ""))
                        firstPlayerIndexStart = 12
                        firstPlayerIndexEnd = val.index(")")
                        player1 = val[firstPlayerIndexStart:firstPlayerIndexEnd + 1]
                        secondPlayerIndexStart = firstPlayerIndexEnd + 1
                        secondPlayerIndexEnd = val.index(")", secondPlayerIndexStart, len(val))
                        player2 = val[secondPlayerIndexStart:secondPlayerIndexEnd + 1]
                        setP1 = val[secondPlayerIndexEnd + 1]
                        setP2 = val[secondPlayerIndexEnd + 2]
                        matchResult = val[-1]

                        field = data.find_previous("span", "event__title--name").text
                        if "dur" in field:
                            field = "dur"
                        if "gazon" in field:
                            field = "gazon"
                        if "terre battue" in field:
                            field = "terre battue"
                        # print(field, player1, player2, setP1, setP2, matchResult)
                        lineResults.append(ranking)
                        lineResults.append(field)
                        lineResults.append(player1)
                        lineResults.append(player2)
                        lineResults.append(setP1)
                        lineResults.append(setP2)
                        lineResults.append(matchResult)
                        allResults.append(lineResults)
                        # print(lineResults)
                    # Going forward to next 'div'
                    data = data.find_next("div")
            except ValueError:
                pass

            j += 1
        #print(allResults)
        # Saving to csv file
        self.saveToCsv(
            "csv/results.csv",
            allResults,
            ['RANKING', 'FIELD', 'PLAYER1', 'PLAYER2', 'SET_P1', 'SET_P2', 'RESULT']
        )
        print("End of processing ! - csv file populated")
