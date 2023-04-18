import os

import cpa_constants

def run(problem_name : str, DEBUG = False):
    # remove the executable file if it exists
    if os.path.exists(problem_name):
        os.system(f"rm -rf {problem_name}")
    
    if DEBUG:
        os.system(f"g++ -std=gnu++20 -Wall -Wextra -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -O2 {cpa_constants.FLAGS} -o {problem_name} {problem_name}.cpp")
    else:
        os.system(f"g++ -std=gnu++20 -Wall -Wextra -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -O2 -o {problem_name} {problem_name}.cpp")

    # check if the compilation is successful
    if not os.path.exists(problem_name):
        return

    os.system(f"./{problem_name}")
