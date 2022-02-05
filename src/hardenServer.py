import argparse
import subprocess
from tabnanny import check

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def output_info(process, output):
    if is_error(process):
        if (args.verbose):
            print(process.stderr.strip().decode('ascii'))
        else:
            print(bcolors.WARNING + "An error has occured, use [-v] to see more info" + bcolors.ENDC)
    else:
        if (args.verbose):
            print(process.stdout.strip().decode('ascii'))
            print(bcolors.OKGREEN + output + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + output + bcolors.ENDC)

def is_error(process):
    if (process.returncode > 0):
        return True
    else:
        return False

#TEST print ls
def print_ls():
    print(bcolors.OKBLUE + "Running 'ls'" + bcolors.ENDC)
    completedProcess = subprocess.run(["ls"], capture_output=True)
    output_info(completedProcess, "ran 'ls'")

#TEST ipconfig
def print_ip():
    print(bcolors.OKBLUE + "Running 'ipconfig'" + bcolors.ENDC)
    completedProcess = subprocess.run(["ipconfig"], capture_output=True)
    output_info(completedProcess, "ran 'ipconfig'")

def update_upgrade():
    print(bcolors.OKBLUE + "Starting update" + bcolors.ENDC)
    completedProcess = subprocess.run(["sudo", "apt-get", "update"], capture_output=True)
    output_info(completedProcess, "Update complete")

if __name__ == "__main__":
    #Parser to get flags.
    parser = argparse.ArgumentParser(description="Harden Debian server.")
    parser.add_argument("-v", "--verbose", help="Print verbose", dest="verbose", action="store_true")
    parser.add_argument("-q", "--qq", help="Print verbose", dest="yeet", action="store_true")
    global args
    args = parser.parse_args()
    
    #TESTS
    print_ip()
    #print_ls()
    
    #Update and upgrade packeges
    #update_upgrade()