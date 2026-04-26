import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if not os.path.exists(self.filename):
            print(f"Error: {self.filename} not found.")
            return False
        else:
            print(f"File found: {self.filename}")
            return True

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")

        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Output folder created: output/")
        else:
            print("Output folder already exists: output/")



class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")

        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)

            print("Data loaded successfully:", len(self.students), "students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview(self, n=5):
        print("First", n, "rows:")
        print("------------------------------")

        for s in self.students[:n]:
            print(s["student_id"], "|", s["age"], "|", s["gender"], "|", s["country"], "| GPA:", s["GPA"])

        print("------------------------------")



class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        low = []
        high = []

        for s in self.students:
            try:
                sleep = float(s["sleep_hours"])
                gpa = float(s["GPA"])
            except:
                continue

            if sleep < 6:
                low.append(gpa)
            else:
                high.append(gpa)

        avg_low = round(sum(low) / len(low), 2)
        avg_high = round(sum(high) / len(high), 2)
        diff = round(avg_high - avg_low, 2)

        self.result = {
            "total_students": len(self.students),
            "low_sleep": {
                "students": len(low),
                "avg_gpa": avg_low
            },
            "high_sleep": {
                "students": len(high),
                "avg_gpa": avg_high
            },
            "gpa_difference": diff
        }

        return self.result

    def print_results(self):
        print("------------------------------")
        print("Sleep vs GPA Analysis")
        print("------------------------------")

        print("Students sleeping < 6 hours :", self.result["low_sleep"]["students"])
        print("Average GPA (< 6 hours) :", self.result["low_sleep"]["avg_gpa"])

        print("Students sleeping >= 6 hours :", self.result["high_sleep"]["students"])
        print("Average GPA (>= 6 hours) :", self.result["high_sleep"]["avg_gpa"])

        print("GPA difference :", self.result["gpa_difference"])
        print("------------------------------")


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w") as f:
                json.dump(self.result, f, indent=4)

            print("Result saved to output/result.json")

        except Exception as e:
            print("Error saving file:", e)


fm = FileManager("students.csv")

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()

dl.load = DataLoader("wrong_file.csv").load
dl.load()
