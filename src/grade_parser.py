from src.grade import Grade
from bs4 import BeautifulSoup

class GradesParser:
    def parse(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        soup = soup.find(id="resultTable")
        grades = []

        for row in soup.find_all("tr")[1:]:
            grades.append(self.__parseRow(row))

        return grades

    def __parseRow(self, row):
        cols = row.find_all("td")
        return Grade(
            cols[0].string.strip(),
            cols[2].string.strip(),
            cols[4].string.strip(),
            cols[1].string.strip()
        )
