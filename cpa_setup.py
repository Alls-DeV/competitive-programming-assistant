import os

import cpa_constants

def setup(contest_name : str, problems : list):
    full_path = cpa_constants.CONTEST_PATH + contest_name
    current_dir = os.path.basename(os.getcwd())

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
        with open(problem + ".cpp", 'w') as f:
            f.write(template)
        print(f"{cpa_constants.colors.GREEN}Created {problem}.cpp{cpa_constants.colors.NC}")
    
    # go to previous folder
    os.chdir("..")
    
    # modify all the names of the problems, appending .cpp at the and contest_name/ at the beginning
    problems = [contest_name + "/" + problem + ".cpp" for problem in problems]
    
    # open all files in nvim
    if cpa_constants.EDITOR is not None:
        os.system(f"{cpa_constants.EDITOR} {' '.join(problems)}")