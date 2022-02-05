import argparse
import subprocess

#TEST print ls
def print_ls():
    completedProcess = subprocess.run(["ls"], capture_output=True)
    print(completedProcess.stdout.strip().decode('ascii'))

#TEST ipconfig
def print_tree():
    completedProcess = subprocess.run(["ipconfig"], capture_output=True)
    print(completedProcess.stdout.strip().decode('ascii'))

if __name__ == "__main__":
    #Parser to get flags.
    parser = argparse.ArgumentParser(description="Harden Debian server.")
    parser.add_argument("-v", "--verbose", help="Print verbose", dest="verbose", action="store_true")
    parser.add_argument("-q", "--qq", help="Print verbose", dest="yeet", action="store_true")
    args = parser.parse_args()
    
    #TESTS
    #print_tree()
    #print_ls()
    
    #Update and upgrade packeges
