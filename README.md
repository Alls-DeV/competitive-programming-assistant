# Competitive programming assistant

It is a tool designed to speed-up competitive programmer's speed during contests by automating various routine tasks like compiling and testing, debugging, cloning testcases, loading template, etc. The console command suits any coding environment (i.e. VSCode, Jetbrains IDEs, Vim, Emacs, Geany, Sublime Text, ...).

## Features

- Automatically parse sample testcases files with corresponding source code files with template loaded into a desired directory
   - `cpa parse` waits for competitive companion plugin to send parsed data for each problem

Run the following commands in the folder of the solution of the problem

- Compile, run, test and debug
   - `cpa debug` compiles and runs the code on all the test cases, highlighting the differences
   - `cpa debug N` it will run only on the N-th test case
   - `cpa debug -k` to use keyboard as input
   - `cpa debug -D` it will compile the code with the -D flag
   - You can combine N or -k with -D

- Stresstest against a bruteforce solution
   - `cpa comparator solution1 solution2 generator numTests` solution1, solution2 and generator are respectively the executables of the two solutions and of the testcases generator. Compares the outputs of two solutions of a problem, checking if they give the same outputs

- Stresstest against a validator
   - `cpa validate solution validator generator numTests` solution, validator and generator are respectively the executables of the solution, validator of a solution and of the testcases generator. Validator should return the string 'OK' or the string that explains the error. Validator first take in input the generator input and next the program output


## Requirements

- [Install competitive companion](https://github.com/jmerle/competitive-companion#readme)
   in your browser.
- Add this repository to your path.
- Make `cpa` executable using `chmod +x cpa`.
- In cpa_parse.py:
   - add CONTEST_PATH in the Parser class, the contests will be parsed in CONTEST_PATH.
   - add TEMPLATE_PATH in the Parser class, cpa will paste the code inside TEMPLATE_PATH in the contests that cpa will parse.

## Supported Languages

- C++
- C
- Rust
- Python
- Java

## Supported Websites

- Codeforces
- CodeChef
- Kattis
- Google Code Jam
- Google Hash Code
- Google Kickstart
