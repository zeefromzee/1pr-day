import secrets
import sys
from Crypto.Util.number import *
from colorama import Fore, Style, init

init(autoreset=True)

# s = "label"
# p = [ord(char) for char in s]
# # int(s)

# print("".join(chr(o ^ 13) for o in p))
# # print(long_to_bytes(p))
plaintext = "cookies"
length = len(plaintext)
p = [ord(char) for char in plaintext]
# a = long_to_bytes(p)
p1 = bytes(p)
key = secrets.token_bytes(length)
title = f"{Style.BRIGHT}{Fore.CYAN} OTP XOR DEMO {Style.RESET_ALL}"
line = f"{Fore.BLUE}{'-' * 56}{Style.RESET_ALL}"

print(line)
print(title)
print(line)
print(f"{Fore.MAGENTA}Plaintext:{Style.RESET_ALL} {Style.BRIGHT}{plaintext}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Length:{Style.RESET_ALL} {length}")
print(f"{Fore.GREEN}Key bytes:{Style.RESET_ALL} {Style.BRIGHT}{key.hex()}{Style.RESET_ALL}")
# print("\n")
result = []
for i, j in zip(p1, key):
    xor = i ^ j
    result.append(xor)

print(f"{Fore.CYAN}Cipher list:{Style.RESET_ALL} {result}")
print(f"{Fore.WHITE}Cipher hex:{Style.RESET_ALL} {Style.BRIGHT}{bytes(result).hex()}{Style.RESET_ALL}")
print(line)