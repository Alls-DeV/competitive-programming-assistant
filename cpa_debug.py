import os
import threading as th

import cpa_constants

def single_testcase(testcase, problem_name, inp, out, ans):
    print("Testcase", testcase)
    TLE = False
    t = th.Thread(target = lambda: os.system(f"./{problem_name} < {inp} > {out}"))
    t.start()
    t.join(5)
    if t.is_alive():
        TLE = True
        os.system(f"killall {problem_name}")

    # check if the output is correct excluding white space and endline redirecting the diff output to a file
    os.system(f"diff -B -i -w {ans} {out} > diff.out")
    if os.path.getsize("diff.out") == 0 and TLE == False:
        print("========== in ===========")
        os.system(f"cat {inp}")
        print("========== out ==========")
        os.system(f"cat {out}")
        print("=========================")
        print(f"{cpa_constants.colors.GREEN}Passed!{cpa_constants.colors.NC}")
        return 1
    else:
        # for each line in $out and in $ans, if they are different, print out in $FAILURE color and ans in $SUCCESS color
        print("========== in ===========")
        os.system(f"cat {inp}")
        print("========== out ==========")
        if TLE:
            print("=========================")
            print(f"{cpa_constants.colors.RED}Failed! (Time limit exceeded){cpa_constants.colors.NC}")
            return 0
        with open(out, "r") as f:
            out_text = f.readlines()
        with open(ans, "r") as f:
            ans_text = f.readlines()
        out_with_diff = ""
        ans_with_diff = ""

        for line_index in range(max(len(out_text), len(ans_text))):
            if line_index >= len(out_text):
                for line in ans_text[line_index:]:
                    ans_with_diff += f"{cpa_constants.colors.GREEN}{line}{cpa_constants.colors.NC}"
                break
            if line_index >= len(ans_text):
                for line in out_text[line_index:]:
                    out_with_diff += f"{cpa_constants.colors.RED}{line}{cpa_constants.colors.NC}"
                break
            if out_text[line_index].strip() != ans_text[line_index].strip():
                out_with_diff += f"{cpa_constants.colors.RED}{out_text[line_index]}{cpa_constants.colors.NC}"
                ans_with_diff += f"{cpa_constants.colors.GREEN}{ans_text[line_index]}{cpa_constants.colors.NC}"
            else:
                out_with_diff += out_text[line_index]
                ans_with_diff += ans_text[line_index]

        print(out_with_diff, end = "")
        print("\n========== ans ==========")
        print(ans_with_diff, end = "")
        print("=========================")
        print(f"{cpa_constants.colors.RED}Failed!{cpa_constants.colors.NC}")
        return 0

def debug(problem_name : str, k = False, testcase = -1, DEBUG = False):
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
    
    if k:
        print("Enter your input manually")
        os.system(f"./{problem_name}")

    elif testcase == -1:
        total = 0
        passed = 0

        for testcase in range(0, 1000):
            # redirect the output to a file with the same ending number as the input
            testcase = str(testcase)
            inp = f"{problem_name}.in{testcase}"
            out = f"{problem_name}.out{testcase}"
            ans = f"{problem_name}.ans{testcase}"
            if not os.path.exists(inp):
                break
            total += 1
            passed += single_testcase(testcase, problem_name, inp, out, ans)
            print('\n')

        print()
        os.system("rm -rf diff.out")
        if passed == total:
            c = cpa_constants.colors.GREEN
        else:
            c = cpa_constants.colors.RED
        print(f"{c}{passed} / {total} passed!{cpa_constants.colors.NC}")

    else:
        testcase = str(testcase)
        inp = f"{problem_name}.in{testcase}"
        out = f"{problem_name}.out{testcase}"
        ans = f"{problem_name}.ans{testcase}"
        if not os.path.exists(inp):
            print(f"{cpa_constants.colors.RED}Testcase {testcase} does not exist{cpa_constants.colors.NC}")
            return
        single_testcase(testcase, problem_name, inp, out, ans)
