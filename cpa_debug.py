import os
import sys

class colors:
    RED   = "\033[0;31m"
    GREEN = "\033[0;32m"
    NC    = "\033[0m" # no color

def debug(k = False, testcase = -1, A = False):
    folder = os.getcwd()[os.getcwd().rfind('/') + 1:]

    # remove the executable file if it exists
    if os.path.exists(folder):
        os.system(f"rm -rf {folder}")
    
    print("Compiling...")
    
    if k or testcase != -1:
        os.system(f"g++ -std=gnu++20 -Wall -Wextra -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -O2 -DDEBUG -o {folder} {folder}.cpp")
    else:
        os.system(f"g++ -std=gnu++20 -Wall -Wextra -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -O2 -o {folder} {folder}.cpp")

    # check if the compilation is successful
    if not os.path.exists(folder):
        return
    
    if k:
        print("Enter your input manually, press ctrl+D to finish your input")
        print("\nInput")
        os.system("cat > tmp.txt")
        print("\nOutput")
        os.system(f"./{folder} < tmp.txt")
        os.system("rm tmp.txt")

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
            os.system(f"./{folder} < {inp} > {out}")

            # check if the output is correct excluding white space and endline redirecting the diff output to a file
            os.system(f"diff -B -i -w {ans} {out} > diff.out")
            if os.path.getsize("diff.out") == 0:
                passed += 1
                print(f"\n{colors.GREEN}Testcase {testcase} passed{colors.NC}")
                # if -A is passed print testcase
                if A:
                    print("\nInput")
                    os.system(f"cat {inp}")
                    print("\nOutput")
                    os.system(f"cat {out}")
            else:
                # for each line in $out and in $ans, if they are different, print out in $FAILURE color and ans in $SUCCESS color
                print(f"\n{colors.RED}Testcase {testcase} failed{colors.NC}")
                print("Input")
                os.system(f"cat {inp}")
                print("\nOutput")
                # open out and ans and compare line by line, if they are different, print out in $RED color and ans in $GREEN color
                out = open(out, "r")
                ans = open(ans, "r")
                for line_out, line_ans in zip(out, ans):
                    if line_out != line_ans:
                        if len(line_out) + 10 > 70:
                            line_to_print = colors.RED + line_out.strip() + colors.GREEN + '\n' + line_ans.strip() + colors.NC
                        else:
                            line_to_print = colors.RED + line_out.strip() + colors.GREEN + ' ' * 10 + line_ans.strip() + colors.NC
                        print(line_to_print)
                    else:
                        print(line_out, end="")
                out.close()
                ans.close()

        print()
        #  do the same for the summary
        if passed == total:
            print(f"{colors.GREEN}All testcases passed {colors.NC}")
        elif total - passed == 1:
            print(f"{colors.RED}{total - passed} testcase failed {colors.NC}")
        else:
            print(f"{colors.RED}{total - passed} testcases failed {colors.NC}")

    else:
        testcase = str(testcase)
        inp = f"{folder}.in{testcase}"
        out = f"{folder}.out{testcase}"
        ans = f"{folder}.ans{testcase}"
        if not os.path.exists(inp):
            print(f"{colors.RED}Testcase {testcase} does not exist{colors.NC}")
            return
        os.system(f"./{folder} < {inp} > {out}")

        print("\nInput")
        os.system(f"cat {inp}")
        if A:
            print("\nAnswer")
            os.system(f"cat {ans}")
        print("\nOutput")
        os.system(f"cat {out}")
