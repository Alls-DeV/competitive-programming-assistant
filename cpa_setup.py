import os

class colors:
    RED   = "\033[0;31m"
    GREEN = "\033[0;32m"
    NC    = "\033[0m" # no color

class Setupper:
    CONTEST_PATH = "/home/alls/CompetitiveProgramming/"
    TEMPLATE_PATH = "/home/alls/CompetitiveProgramming/Library/Template.cpp"

    def setup(self, contest_name : str, problems : list):
        full_path = self.CONTEST_PATH + contest_name
        current_dir = os.path.basename(os.getcwd())

        # create contest folder if it doesn't exist and move to it
        if current_dir != contest_name:
            if not os.path.isdir(full_path):
                os.mkdir(full_path)
                print(f"{colors.GREEN}Created {contest_name} folder{colors.NC}")
            os.chdir(full_path)
        
        with open(self.TEMPLATE_PATH, 'r') as f:
            template = f.read()
        
        for problem in problems:
            with open(problem + ".cpp", 'w') as f:
                f.write(template)
            print(f"{colors.GREEN}Created {problem}.cpp{colors.NC}")