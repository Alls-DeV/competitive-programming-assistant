import socket
import json
import os
import threading

import cpa_constants
    
class Parser:
    def create(self, x : str):
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
            elif dic["group"][:7] == "AtCoder":
                tmp = url[url.find("contests") + 9: ]
                contest_name = "at" + tmp[:tmp.find('/')]
                problem_name = dic["url"][-1]
            else:
                print(f"{cpa_constants.colors.RED}Unknown contest{cpa_constants.colors.NC}")
                return

            full_path = cpa_constants.CONTEST_PATH + contest_name
            current_dir = os.path.basename(os.getcwd())

            # create contest folder if it doesn't exist and move to it
            if current_dir != contest_name:
                if not os.path.isdir(full_path):
                    os.mkdir(full_path)
                    print(f"{cpa_constants.colors.GREEN}Created {contest_name} folder{cpa_constants.colors.NC}")
                os.chdir(full_path)

            with open(cpa_constants.TEMPLATE_PATH, 'r') as f:
                template = f.read()

            # if problem wasn't already parsed
            if not os.path.isfile(problem_name + ".cpp"):
                with open(problem_name + ".cpp", 'w') as f:
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
            print(f"{cpa_constants.colors.GREEN}Parsed problem " + problem_name + f"{cpa_constants.colors.NC}")
            
        except:
            pass

    def parse(self):
        flag = False
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((cpa_constants.HOST, cpa_constants.PORT))
            print("Listening...")
            timeout = 60
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
                            if not data:
                                break
                            else:
                                flag = True
                                t = threading.Thread(target=self.create, args=(data.decode("utf-8"),))
                                t.start()
                except :
                    ok = False
        return flag
