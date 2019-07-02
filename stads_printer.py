import os
from dotenv import load_dotenv

from src.grade_printer import GradesPrinter
from src.grade_fetcher import StadsGradesFetcher

def main(stadsUsr, stadsPsw):
    print("Checking Credentials... ")

    fetcher = StadsGradesFetcher(stadsUsr, stadsPsw)

    # Check credentials
    fetcher.setup()

    grades = fetcher.fetch()

    print(GradesPrinter().print(grades))

load_dotenv()

main(
    os.getenv("STADS_USER"), 
    os.getenv("STADS_PASS")
)
