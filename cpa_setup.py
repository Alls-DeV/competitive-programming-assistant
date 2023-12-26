import os

import cpa_constants

def setup(contest_name : str, problems : list):
    full_path = contest_name
    current_dir = os.path.basename(os.getcwd())
    # check if problems contains '-F' and remove it
    folders = False
    if "-F" in problems:
        problems.remove("-F")
        folders = True

    # create contest folder if it doesn't exist and move to it
    if current_dir != contest_name:
        if not os.path.isdir(full_path):
            os.mkdir(full_path)
            print(f"{cpa_constants.colors.GREEN}Created {contest_name} folder{cpa_constants.colors.NC}")
        os.chdir(full_path)

    if cpa_constants.TEMPLATE_PATH is None:
        template = ""
    else:
        with open(cpa_constants.TEMPLATE_PATH, 'r') as f:
            template = f.read()

    for problem in problems:
        # create problem folder if it doesn't exist and move to it
        if folders:
            if not os.path.isdir(problem):
                os.mkdir(problem)
                print(f"{cpa_constants.colors.GREEN}Created {problem} folder{cpa_constants.colors.NC}")
            os.chdir(problem)
        # create problem file if it doesn't exist
        if not os.path.isfile(problem + ".cpp"):
            with open(problem + ".cpp", 'w') as f:
                f.write(template)
                print(f"{cpa_constants.colors.GREEN}Created {problem}.cpp{cpa_constants.colors.NC}")
        
        # go to previous folder
        if folders:
            os.chdir("..")
            
    
    # go to previous folder
    os.chdir("..")