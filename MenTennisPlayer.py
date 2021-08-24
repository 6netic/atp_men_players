import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import codecs
import csv


class MenTennisPlayer():
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


    def scrapeUrl(self, url):
        """ This method gets an url webpage to be scrapped """

        htmlPage = requests.get(url).content
        scrappedPage = BeautifulSoup(htmlPage, "lxml")
        return scrappedPage


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
        """ This method gets the rank of the first 300 atp men players.
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
        """ This method creates a csv file containing the first 300 atp men players """

        resultList = self.scrapeLocal(htmlFile)
        entireList = []
        # Here we choose the 300 first players
        for i in range(300):
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











































