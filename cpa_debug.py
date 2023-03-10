import os
import sys
import threading as th

class colors:
    RED   = "\033[0;31m"
    GREEN = "\033[0;32m"
    NC    = "\033[0m" # no color

def single_testcase(testcase, folder, inp, out, ans):
    print("Testcase", testcase)
    TLE = False
    t = th.Thread(target = lambda: os.system(f"./{folder} < {inp} > {out}"))
    t.start()
    t.join(5)
    if t.is_alive():
        TLE = True
        os.system(f"killall {folder}")

    # check if the output is correct excluding white space and endline redirecting the diff output to a file
    os.system(f"diff -B -i -w {ans} {out} > diff.out")
    if os.path.getsize("diff.out") == 0 and TLE == False:
        print("---------------")
        print("Input")
        os.system(f"cat {inp}")
        print("---------------")
        print("Output")
        os.system(f"cat {out}")
        print("---------------")
        print(f"{colors.GREEN}Passed!{colors.NC}")
        return 1
    else:
        # for each line in $out and in $ans, if they are different, print out in $FAILURE color and ans in $SUCCESS color
        print("---------------")
        print("Input")
        os.system(f"cat {inp}")
        print("---------------")
        print("Output")
        if TLE:
            print("---------------")
            print(f"{colors.RED}Failed! (Time limit exceeded){colors.NC}")
            return 0
        outFile = open(out, "r")
        ansFile = open(ans, "r")
        out_new_text = ""
        ans_new_test = ""
        for line_out, line_ans in zip(outFile, ansFile):
            if line_out.strip() != line_ans.strip():
                out_new_text += colors.RED + line_out + colors.NC
                ans_new_test += colors.GREEN + line_ans + colors.NC
            else:
                out_new_text += line_out
                ans_new_test += line_ans
        outFile.close()
        ansFile.close()
        print(out_new_text, end = "")
        print("---------------")
        print("Expected")
        print(ans_new_test, end = "")
        print("---------------")
        print(f"{colors.RED}Failed!{colors.NC}")
        return 0

def debug(k = False, testcase = -1, DEBUG = False):
    folder = os.getcwd()[os.getcwd().rfind('/') + 1:]

    # remove the executable file if it exists
    if os.path.exists(folder):
        os.system(f"rm -rf {folder}")
    
        os.system(f"g++ -std=gnu++20 -Wall -Wextra -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -O2 -DDEBUG -o {folder} {folder}.cpp")
    if DEBUG:
    else:
        os.system(f"g++ -std=gnu++20 -Wall -Wextra -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -O2 -o {folder} {folder}.cpp")

    # check if the compilation is successful
    if not os.path.exists(folder):
        return
    
    if k:
        print("Enter your input manually, press ctrl+D to finish your input")
        print("---------------")
        print("Input")
        os.system("cat > tmp.txt")
        print("---------------")
        print("Output")
        t = th.Thread(target = lambda: os.system(f"./{folder} < tmp.txt"))
        t.start()
        t.join(5)
        if t.is_alive():
            print(f"{colors.RED}Failed! (Time limit exceeded){colors.NC}")
            os.system(f"killall {folder}")
        os.system("rm -rf tmp.txt")

    elif testcase == -1:
        total = 0
        passed = 0

        for testcase in range(0, 1000):
            # redirect the output to a file with the same ending number as the input
            testcase = str(testcase)
            inp = f"{folder}.in{testcase}"
            out = f"{folder}.out{testcase}"
            ans = f"{folder}.ans{testcase}"
            if not os.path.exists(inp):
                break
            total += 1
            passed += single_testcase(testcase, folder, inp, out, ans)
            print('\n')

        print()
        os.system("rm -rf diff.out")
        if passed == total:
            c = colors.GREEN
        else:
            c = colors.RED
        print(f"{c}{passed} / {total} passed!{colors.NC}")

    else:
        testcase = str(testcase)
        inp = f"{folder}.in{testcase}"
        out = f"{folder}.out{testcase}"
        ans = f"{folder}.ans{testcase}"
        if not os.path.exists(inp):
            print(f"{colors.RED}Testcase {testcase} does not exist{colors.NC}")
            return
        single_testcase(testcase, folder, inp, out, ans)
