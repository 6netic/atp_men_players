import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


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


    def scrapeLocal(self):
        """  """

        pass


    def getAtpMenRank(self):
        """ This method gets the rank of the first 300 atp men players.
            User has to click on a link that triggers a JS script to show more match results
            for a specific tennis player. So we use Selenium to do that job.
            Finally that page is saved to a file on the hard drive """

        self.createFolder("ranking")
        self.createFolder("csv")
        # For oneLine in urlList

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











































