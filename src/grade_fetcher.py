import requests
from src.grade_parser import GradesParser

class StadsGradesFetcher:
    __usr = None
    __psw = None
    __cookies = None
    __response = None
    
    __loginPage = "https://sb.aau.dk/sb-ad/sb/"
    __loginUrl = "https://sb.aau.dk/sb-ad/sb/index.jsp"
    __resultsPage = "https://sb.aau.dk/sb-ad/sb/resultater/studresultater.jsp"

    __loginSuccessDiscriminator = "Velkommen til STADS-Selvbetjening på Aalborg Universitet"
    __resultsSuccessDiscriminator = "Her vises samtlige resultater"

    def __init__(self, usr, psw):
        self.__usr = usr
        self.__psw = psw

    def setup(self):
        if not self.__fetchCookies():
            raise Exception("Could not fetch cookies")

        if not self.__login():
            raise Exception("Could not login")

    def fetch(self):
        if self.__cookies == None or not self.__fetchResults():
            self.setup()
            self.__fetchResults()
        
        return GradesParser().parse(self.__results.text)

    def __fetchCookies(self):
        response = requests.get(self.__loginPage)
        
        if response.status_code == 200:
            self.__cookies = response.cookies
            return True
        return False

    def __login(self):
        response = requests.post(self.__loginUrl, cookies = self.__cookies, data = {
            "lang": "null",
            "submit_action": "login",
            "brugernavn": self.__usr,
            "adgangskode": self.__psw
        })
    
        if response.status_code == 200 and self.__loginSuccessDiscriminator in response.text:
            return True
        return False

    def __fetchResults(self):
        self.__results = None
        response = requests.get(self.__resultsPage, cookies = self.__cookies)

        if response.status_code == 200 and self.__resultsSuccessDiscriminator in response.text:
            self.__results = response
            return True
        return False