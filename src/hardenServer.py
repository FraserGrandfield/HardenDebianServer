import argparse
import subprocess

if __name__ == "__main__":
    #Parser to get flags.
    parser = argparse.ArgumentParser(description="Harden Debian server.")
    parser.add_argument("-v", "--verbose", help="Print verbose", dest="verbose", action="store_true")
    parser.add_argument("-q", "--qq", help="Print verbose", dest="yeet", action="store_true")
    args = parser.parse_args()    

    print("Hello World")