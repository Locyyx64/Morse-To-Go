#!/bin/python3

from morsedicts import morse_text, text_morse
from greetings import rnd_greet
from rich import print
from pyperclip import copy
from time import sleep

print("[blue] \n          __  __                           _____              ___      \n \
        |  \/  | ___  _ _  ___ ___       |_   _| ___        / __| ___ \n \
        | |\/| |/ _ \| '_|(_-// -_)        | |  / _ \      | (_ |/ _ \ \n \
        |_|  |_|\___/|_|  /__/\___|        |_|  \___/       \___|\___/\n [/blue]")

print(f"\n\n[bold blue]{rnd_greet()}[/bold blue] :detective: \n")

def auth_txt(text: str) -> bool:
    for char in text:
        if char not in morse_text.keys():
            print(f"\n:prohibited: [bold red]   Invalid character '{char}'  [/bold red] :prohibited:\n")
            return False
    return True

def auth_mrs(morse: str) -> bool:
    split_morse = morse.split(" ")
    for code in split_morse:
        if code not in text_morse:
            print(f"\n:prohibited: [bold red]   Invalid morse code '{code}'  [/bold red] :prohibited:\n")
            return False
    return True
def operate():
    option = int(input("\n\nChoose A Translator: \n   1 - Text To Morse\n   2 - Morse To Text (N/A)\n\n> "))
    if option == 1:
        text = input("\nTranslatable Text: ").lower().replace(" ", "")
        if auth_txt(text):
            code = [morse_text[text[i]] for i in range(len(text)-1)]
            code.append(morse_text[text[len(text)-1]])

            complete_morse = " ".join(code)
            print(f"\n[blue]{complete_morse}[/blue]")
            
            if input("\nCopy to Clipboard? (y/n)  ").lower() == "y":
                copy(complete_morse)
                print("     ", end="")
                for i in range(3):
                    print("[i].[/i]", end="")
                    sleep(0.5)
                print("[i]Copied![/i]")
    elif option == 2:
        print("[blue][i]\n   -> Supported Morse Format: ..-. --- --- [/i][/blue]")
        morse_code = input("\nTranslatable Morse Code: ")
        if auth_mrs(morse_code):
            text = "".join([text_morse[code] for code in morse_code.split(" ")])
            print(f"\n[blue][i]{text}[/i][/blue]")
    if input("\nDo you want to continue? (y/n)  ").lower() == "y":
        operate()
operate()
