import subprocess
import os
import sys

def helpmenu():
    print("Use 'install' to install Certipy if not already done.")
    print("Use 'help' to print this help menu!")

def install():
    print("[-] Installation will create a Python virtual environment in your current directory and install Certipy!")
    print("[!] Installation assumes you are running a Debian/Ubuntu/Kali machine with apt as your package manager!")
    print("[-] You may exit while you have the chance!")
    input("[-] Press Enter to continue or Crtl+C to exit: ")

    
    # installation commands
    subprocess.run(["sudo", "apt", "update"], stdout=True) 
    subprocess.run(["sudo", "apt", "upgrade", "-y"], stdout=True) 
    subprocess.run(["sudo", "apt", "install", "-y", "python3", " python3-pip"], stdout=True) 
    subprocess.run(["python3", "-m", "venv", "certipy-venv"], stdout=True) 
    subprocess.run(["source", "certipy-venv/bin/activate"], stdout=True)
    subprocess.run(["pip", "install", "certipy-ad"], stdout=True)

    print("[+] Installation complete!")

def main():
    while True:
        esc = str(input("[-] Select an exploit (1-16): "))
        match esc:
            case "1":
                print("[+] ESC1 selected!")
                # call some function to exploit w/ certipy
                break
            case "2":
                print("[+] ESC2 selected!")
                # call some function to exploit w/ certipy
                break
            case "3":
                print("[+] ESC3 selected!")
                # call some function to exploit w/ certipy
                break
            case "16":
                print("[+] ESC16 selected!")
                # call some function to exploit w/ certipy
                break
            case _:
                print("[!] You either entered an incorrect, unavailable or non-existent exploit number!")
                continue

def args():
    print("Chroma v1.0.0 by nubb (nubbsterr). Built on Certipy by ly4k.")
    if os.name != "posix":
        print("[!] Chroma is built for Linux machines!")
        sys.exit(0)
    try:
        match sys.argv[1]:
            case "install":
                install()
            case "help":
                helpmenu()
            case _:
                print("[!] You passed an invalid argument!")
                helpmenu()
    except IndexError:
        main()
args()
