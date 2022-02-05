import argparse
import subprocess
from tabnanny import check

def output_info(process, output):
    if check_error(process):
        if (args.verbose):
            print(process.stdout.strip().decode('ascii'))
        else:
            print(output)
    else:
        if (args.verbose):
            print(process.stderr.strip().decode('ascii'))
        else:
            print("An error has occured, use [-v] to see more info")

def check_error(process):
    if (process.returncode > 0):
        return False
    else:
        return True

#TEST print ls
def print_ls():
    completedProcess = subprocess.run(["ls"], capture_output=True)
    print(completedProcess.stdout.strip().decode('ascii'))

#TEST ipconfig
def print_ip():
    print("Running 'ipconfig'")
    completedProcess = subprocess.run(["ipconfig"], capture_output=True)
    check_error(completedProcess)
    output_info(completedProcess, "ran 'ipconfig'")

def update_upgrade():
    completedProcess = subprocess.run(["sudo", "apt-get", "update"], capture_output=True)
    print(completedProcess)

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
    #update_upgrade()