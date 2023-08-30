import subprocess

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])