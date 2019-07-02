#!/usr/bin/env python

import time, os
from dotenv import load_dotenv

import boto3
from botocore.exceptions import ClientError

from src.grade_fetcher import StadsGradesFetcher
from src.grade_sender import GradesSender

class LoopingGradeChecker:
    sender = None
    fetcher = None
    grades = None
    sleepTime = 0
    iteration = 0

    def __init__(self, sender, fetcher, sleepTime):
        self.sender = sender
        self.fetcher = fetcher
        self.sleepTime = sleepTime

    def start(self):
        while(True):
            print("{}: ".format(self.iteration), end = "")
            self.iteration = self.iteration + 1
            try:
                print("Fetching Grades...", end = "")
                newGrades = self.fetcher.fetch()
            except Exception as err:
                print(" Failed to fetch grades: {}".format(err))
                time.sleep(self.sleepTime)
                continue
            
            if not self.gradesEqual(self.grades, newGrades) and self.grades != None:
                print(" New grades! Sending...", end = "")
                self.sender.send(newGrades)
                print(" Sent!")
            elif self.grades != None and len(self.grades) > 0:
                print(" Nothing new, latest: {} {}".format(self.grades[0].name, self.grades[0].grade))
            elif newGrades != None and len(newGrades) > 0:
                print(" First is checked. Latest: {} {}".format(newGrades[0].name, newGrades[0].grade))
            else:
                print(" First is checked.")

            self.grades = newGrades
            
            time.sleep(self.sleepTime)

    def gradesEqual(self, g1, g2):
        if (g1 == None and g2 != None) or (g1 != None and g2 == None):
            return False

        if len(g1) != len(g2):
            return False

        for i in range(len(g1)):
            if not g1[i].equals(g2[i]):
                return False

        return True

def main(email, stadsUsr, stadsPsw, awsID, awsKey, awsRegion, interval):
    print("Checking Credentials... ", end = "")

    try:
        client = boto3.client("ses",
            aws_access_key_id = awsID,
            aws_secret_access_key = awsKey,
            region_name = awsRegion
        )
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        exit()

    sender = GradesSender(email, email, client)
    fetcher = StadsGradesFetcher(stadsUsr, stadsPsw)

    # Check credentials
    fetcher.setup()

    print("Done\nStarting event loop\n------------------------")

    LoopingGradeChecker(sender, fetcher, interval).start()

load_dotenv()

main(
    os.getenv("NOTIFICATION_EMAIL"),
    os.getenv("STADS_USER"), 
    os.getenv("STADS_PASS"),
    os.getenv("AWS_ID"), 
    os.getenv("AWS_SECRET"), 
    os.getenv("AWS_REGION"),
    int(os.getenv("NOTIFICATION_INTERVAL"))
)
