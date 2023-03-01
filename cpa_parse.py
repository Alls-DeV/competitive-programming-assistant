import socket
import json
import os
from threading import Thread, Semaphore
import subprocess

class colors:
    RED   = "\033[0;31m"
    GREEN = "\033[0;32m"
    NC    = "\033[0m" # no color
    
class Parser:
    HOST = "127.0.0.1"
    PORT = 1327 
    CONTEST_PATH = "/home/alls/CompetitiveProgramming/"
    TEMPLATE_PATH = "/home/alls/CompetitiveProgramming/Library/Template.cpp"

    def create(self, x : str, sem : Semaphore):
        try:
            dic = json.loads(x[x.find('{'):])
            url = dic["url"]

            if dic["group"][:10] == "Codeforces":
                tmp = url[url.find("contest") + 8: ]
                contest_name = "cf" + tmp[:tmp.find('/')]
                problem_name = tmp[tmp.rfind('/') + 1:]
            elif dic["group"][:8] == "CodeChef":
                contest_name = "cc" + dic["group"][dic["group"].find('-') + 2:]
                problem_name = url[url.rfind('/') + 1:]
            elif dic["group"][:6] == "Google":
                contest_name = "".join(dic["group"][dic["group"].find('-') + 2: dic["group"].rfind('-') - 1].split())
                problem_name = dic["languages"]["java"]["taskClass"]
            elif dic["group"][:6] == "Kattis":
                tmp = url[url.find("contest") + 9: ]
                contest_name = "kt" + tmp[:tmp.find('/')]
                problem_name = dic["name"][dic["name"].find("Problem") + 8: dic["name"].find('-') - 1]
            else:
                print(f"{colors.RED}Unknown contest{colors.NC}")
                return

            full_path = self.CONTEST_PATH + contest_name
            current_dir = os.path.basename(os.getcwd())

            # create contest folder if it doesn't exist and move to it
            if current_dir != contest_name:
                if not os.path.isdir(full_path):
                    os.mkdir(full_path)
                os.chdir(full_path)

            # create problem folder if it doesn't exist and move to it
            if not os.path.isdir(problem_name):
                os.mkdir(problem_name)
            else:
                with sem:
                    ans = input(problem_name + " folder already exists, do you want to overwrite it? (y/n)")
                Y = ('y', 'Y', "yes", "Yes", "YES")
                if ans in Y:
                    subprocess.run(["rm", "-rf", problem_name])
                    os.mkdir(problem_name)
                else:
                    print(problem_name + " not parsed")
                    return
            os.chdir(os.path.join(full_path, problem_name))
            
            # create problem file with url of the problem
            with open(self.TEMPLATE_PATH, 'r') as f:
                template = f.read()
            with open(problem_name + self.TEMPLATE_PATH[self.TEMPLATE_PATH.rfind('.'):], 'w') as f:
                f.write(template)

            # create input and answer files
            testcases = dic["tests"]
            for i, case in enumerate(testcases):
                file_input = problem_name + ".in" + str(i)
                file_output = problem_name + ".ans" + str(i)
                with open(file_input, 'w') as f_in:
                    f_in.write(case["input"])
                with open(file_output, 'w') as f_out:
                    f_out.write(case["output"])
            with sem:
                print(f"{colors.GREEN}Parsed problem " + problem_name + f"{colors.NC}")
            
        except:
            pass

    def parse(self):
        flag = False
        sem = Semaphore(1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            print("Listening...")
            timeout = 20
            ok = True
            while ok:
                try :
                    s.listen()
                    s.settimeout(timeout)
                    timeout = 2
                    conn, addr = s.accept()
                    with conn:
                        while True:
                            data = conn.recv(4096)
                            result = (data.decode("utf-8"))
                            if not data:
                                break
                            else:
                                flag = True
                                t = Thread(target=self.create, args=(result, sem))
                                t.start()
                except :
                    ok = False
        return flag