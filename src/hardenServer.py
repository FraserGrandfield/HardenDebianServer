import argparse
import subprocess
from tabnanny import check

#Text colours
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

def output_progress(output):
    print(bcolors.OKBLUE + output + bcolors.ENDC)

#Print what is happening to terminal
def output_info(process, output):
    if is_error(process):
        if args.verbose:
            print(process.stderr.strip().decode('utf-8'))
        else:
            print(bcolors.WARNING + "An error has occured, use [-v] to see more info" + bcolors.ENDC)
    else:
        if args.verbose:
            print(process.stdout.strip().decode('utf-8'))
            print(bcolors.OKGREEN + output + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + output + bcolors.ENDC)

#Check if there is an error in a command
def is_error(process):
    if process.returncode > 0:
        return True
    else:
        return False

#TEST print ls
def print_ls():
    output_progress("Running 'ls'")
    completedProcess = subprocess.run(["ls"], capture_output=True)
    output_info(completedProcess, "ran 'ls'")

#TEST ipconfig
def print_ip():
    output_progress("Running 'ipconfig'")
    completedProcess = subprocess.run(["ipconfig"], capture_output=True)
    output_info(completedProcess, "ran 'ipconfig'")

#Update and upgrade packages
def update_upgrade():
    output_progress("Starting update")
    completedProcess = subprocess.run(["sudo", "apt-get", "update"], capture_output=True)
    output_info(completedProcess, "Update complete")
    output_progress("Starting upgrade")
    completedProcess = subprocess.run(["sudo", "apt-get", "upgrade"], capture_output=True)
    output_info(completedProcess, "Upgrade complete")

#Install and setup the firewall UFW
def firewall_setup():
    output_progress("Installing firewall")
    completedProcess = subprocess.run(["sudo", "apt-get", "install", 'ufw'], capture_output=True)
    output_info(completedProcess, "Firewall installed")

if __name__ == "__main__":
    #Parser to get flags.
    parser = argparse.ArgumentParser(description="Harden Debian server.")
    parser.add_argument("-v", "--verbose", help="Print verbose", dest="verbose", action="store_true")
    parser.add_argument("-q", "--qq", help="Print verbose", dest="yeet", action="store_true")
    global args
    args = parser.parse_args()
    
    #TESTS
    #print_ip()
    #print_ls()
    
    #Update and upgrade packeges
    update_upgrade()
    #Install firewall
    firewall_setup()