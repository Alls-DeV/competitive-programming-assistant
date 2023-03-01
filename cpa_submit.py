import requests
import json
import os
import sys
import webbrowser

from getpass import getpass
from bs4 import BeautifulSoup

class colors:
    RED   = "\033[0;31m"
    GREEN = "\033[0;32m"
    NC    = "\033[0m" # no color

class Submitter:
    def __init__(self, contest_path : str, problem_name : str):
        if len(contest_path.split('/')[-1]) < 3 or contest_path.split('/')[-1][:2] != "cf":
            print(f"{colors.RED}You are not in a codeforces' problem directory{colors.NC}")
            sys.exit(1)
        self.contest_path = contest_path
        self.problem_name = problem_name
        self.contest_number = contest_path.split('/')[-1][2:]
        self.url_submission = "https://codeforces.com/contest/" + self.contest_number + "/my"
    
    def login(self, s : requests.Session):
        URL_LOGIN = "https://codeforces.com/enter?back=%2F"
        login_data = {
            "action" : "enter",
            "_tta" : "654"
        }
        r = s.get(URL_LOGIN)
        soup = BeautifulSoup(r.content, "html.parser")
        login_data["csrf_token"] = soup.find("input", attrs={"name": "csrf_token"})["value"]
        login_data["ftaa"] = soup.find("input", attrs={"name": "ftaa"})["value"]
        login_data["bfaa"] = soup.find("input", attrs={"name": "bfaa"})["value"]
        if os.path.isfile(self.contest_path + "/data.json"):
            with open(self.contest_path + "/data.json", "r") as f:
                data = json.load(f)
                login_data["handleOrEmail"] = data["handleOrEmail"]
                login_data["password"] = data["password"]
        else:
            login_data["handleOrEmail"] = input("Enter your codeforces handle: ")
            login_data["password"] = getpass("Enter your codeforces password: ")
        r = s.post(URL_LOGIN, data = login_data)
        if "logout" not in r.content.decode():
            print(f"{colors.RED}Login failed{colors.NC}")
            return False 
        with open(self.contest_path + "/data.json", "w") as f:
            tmp_data = {
                "handleOrEmail": login_data["handleOrEmail"],
                "password": login_data["password"]
            }
            f.write(json.dumps(tmp_data))
        print(f"{colors.GREEN}Successfully logged in as " + login_data["handleOrEmail"] + f"{colors.NC}")
        return True

    def submit(self):
        s = requests.Session()
        if not self.login(s):
            return
        URL_SUBMIT = "https://codeforces.com/problemset/submit"
        submit_data = {
            "action": "submitSolutionFormSubmitted",
            "tabSize": "4",
            "sourceFile": "",
            "_tta": "655"
        }
        r = s.get(URL_SUBMIT)
        soup = BeautifulSoup(r.content, "html.parser")
        submit_data["csrf_token"] = soup.find("input", attrs={"name": "csrf_token"})["value"]
        submit_data["ftaa"] = soup.find("input", attrs={"name": "ftaa"})["value"]
        submit_data["bfaa"] = soup.find("input", attrs={"name": "bfaa"})["value"]
        submit_data["submittedProblemCode"] = self.contest_number + self.problem_name
        lang = self.problem_name[self.problem_name.find('.') + 1:]
        dir_name = self.contest_path + '/' + self.problem_name[:self.problem_name.find('.')]
        if self.problem_name in os.listdir(dir_name):
            with open(dir_name + '/' + self.problem_name, "r") as f:
                submit_data["source"] = f.read()
        else:
            print(f"{colors.RED}File not found{colors.NC}")
            return
        match lang:
            case lang if lang in ["cpp", "cc", "cxx", "c++"]:
                submit_data["programTypeId"] = "73"
            case "c":
                submit_data["programTypeId"] = "43"
            case "py":
                submit_data["programTypeId"] = "41"
            case "java":
                submit_data["programTypeId"] = "60"
            case "rs":
                submit_data["programTypeId"] = "49"
            case _:
                print(f"{colors.RED}Language not supported{colors.NC}")
                return
        r = s.post(URL_SUBMIT, data = submit_data)
        print(f"{colors.GREEN}Submission successful{colors.NC}")
        webbrowser.open(self.url_submission)