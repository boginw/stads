class GradesPrinter:
    def print(self, grades):
        lengthOfLongestName = max([len(x.name) for x in grades])
        md = (("| {:" + str(lengthOfLongestName) + "} | When       | Grade | ECTS |\n").format("Name"))
        md = md + (("|:{:-<" + str(lengthOfLongestName) + "}-|-----------:|------:|-----:|\n").format(""))

        for grade in grades:
            md = md + (("| {:" + str(lengthOfLongestName) + "} | {} | {:>5} | {:>4} |\n").format(
                grade.name, grade.when, grade.grade, grade.ects))
        return md + "\nWeighted Average: {}".format(self.wavg(grades))
    
    def wavg(self, grades):
        runningTotal = 0
        ectsTotal = 0

        for grade in grades:
            if grade.grade == "B":
                continue
            ectsTotal = ectsTotal + float(grade.ects)
            runningTotal = runningTotal + (float(grade.grade) * float(grade.ects))

        return runningTotal / ectsTotal
