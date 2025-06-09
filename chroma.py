import subprocess
import os

def main():
    print("Chroma v1.0.0 by nubb (nubbsterr). Built on Certipy by ly4k.")
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

main()
