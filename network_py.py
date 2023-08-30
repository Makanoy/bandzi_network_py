import os
import socket
import port_scanner, network_scanner, mac_changer
import subprocess
from colorama import Fore
from datetime import datetime
import getpass
import time

white = Fore.WHITE
cyan = Fore.CYAN
red = Fore.RED
yellow = Fore.YELLOW

username = getpass.getuser()
hostname = socket.gethostname()
user_ip = socket.gethostbyname(hostname)

if os.getuid() != 0:
    exit("you need to run code with sudo!")

def printBanner():
    os.system("clear")
    print(cyan)
    subprocess.call(["figlet", "NetWork PY"])
    print(f"\t\t\t\t\tAutor{white}: ttkak\n\t\t\t\t\t{cyan}Start Time{white}: {datetime.now()}\n")

def main():
    while True:
        printBanner()
        print(f"""
        {cyan}1{white}) Port Scanner
        {cyan}2{white}) Network Scanner
        {cyan}3{white}) MAC Changer
        {cyan}4{white}) Exit!

        """)
        choice = int(input(f"{white}({cyan}{username}{white}/{cyan}{user_ip}{white})-$ {red}"))
        if choice == 1:
            ip = input(f"\n{white}[{cyan}*{white}] IP: {red}")
            max_ports = int(input(f"{white}[{cyan}*{white}] Max Ports: {red}"))
            time.sleep(1)
            print(f"\n{white}[{yellow}!{white}] Scanning {ip} host...")
            ports = port_scanner.port_scanner(ip, max_ports)
            print(f"\n{white}[{cyan}V{white}] Open Ports:", end=' ')
            for port in ports:
                print(f"{cyan}{port}", end=' ')
            ask = input(f"\n\n{white}[{cyan}?{white}] Do you want to save open ports?: {cyan}Y{white}/{cyan}N{white}: ").lower()
            if ask == 'y':
                with open('open_ports.txt', 'a') as f:
                    f.write("------------------------\n")
                    f.write(f" Scaned: {ip}\n")
                    f.write(" Open Ports: ")
                    for port in ports:
                        f.write(f"{port} ")
                    f.write("\n-----------------------\n")
        elif choice == 2:
            ip = input(f"\n{white}[{cyan}*{white}] IP: {red}")
            print(f"\n{white}[{yellow}!{white}] Scanning {ip} host...")
            time.sleep(1)
            answer_list = network_scanner.network_scanner(ip)
            print(f"       {cyan}IP\t\t   MAC Address\n{white}-------------------------------------------")
            for element in answer_list:
                print("  " + element[1].psrc + "\t\t" + element[1].hwdst)
            ask = input(f"\n\n{white}[{cyan}?{white}] Do you want to save open ports?: {cyan}Y{white}/{cyan}N{white}: ").lower()
            if ask == 'y':
                with open('scaned_host.txt', 'a') as f:
                    f.write("-------------------------------------------\n")
                    f.write(f"\t     Host: {ip}\n")
                    f.write("\t\t   |\n")
                    f.write("\t\t   |\n")
                    f.write("\t\t   |\n")
                    f.write("\t\t  \ /\n")
                    f.write(f"       IP\t\t   MAC Address\n-------------------------------------------\n")
                    for element in answer_list:
                        f.write("  " + element[1].psrc + "\t\t" + element[1].hwdst + "\n")
                    f.write("-------------------------------------------\n")
        elif choice == 3:
            interface = input(f"\n{white}[{cyan}*{white}] Interface: {red}")
            new_mac = input(f"\n{white}[{cyan}*{white}] New MAC Address: {red}")
            time.sleep(1)
            mac_changer.change_mac(interface, new_mac)
            print(f"\n{white}[{cyan}V{white}] New MAC Change Success")
        else:
            os.system("clear")
            exit()


if __name__ == '__main__':
    main()
