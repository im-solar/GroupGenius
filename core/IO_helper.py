# Input output helper.
from rich import console
from colorama import Fore, Style, init
import random, os
from tkinter import filedialog

console = console.Console()
init()
class IO_Helpers():
    test = 1
    logos = [
        
        """
            _  .-')                              _ (`-.                      ('-.       .-') _                      .-')    
           ( \( -O )                            ( (OO  )                   _(  OO)     ( OO ) )                    ( OO ).  
  ,----.    ,------.  .-'),-----.  ,--. ,--.   _.`     \        ,----.    (,------.,--./ ,--,' ,-.-') ,--. ,--.   (_)---\_) 
 '  .-./-') |   /`. '( OO'  .-.  ' |  | |  |  (__...--''       '  .-./-')  |  .---'|   \ |  |\ |  |OO)|  | |  |   /    _ |  
 |  |_( O- )|  /  | |/   |  | |  | |  | | .-') |  /  | |       |  |_( O- ) |  |    |    \|  | )|  |  \|  | | .-') \  :` `.  
 |  | .--, \|  |_.' |\_) |  |\|  | |  |_|( OO )|  |_.' |       |  | .--, \(|  '--. |  .     |/ |  |(_/|  |_|( OO ) '..`''.) 
(|  | '. (_/|  .  '.'  \ |  | |  | |  | | `-' /|  .___.'      (|  | '. (_/ |  .--' |  |\    | ,|  |_.'|  | | `-' /.-._)   \ 
 |  '--'  | |  |\  \    `'  '-'  '('  '-'(_.-' |  |            |  '--'  |  |  `---.|  | \   |(_|  |  ('  '-'(_.-' \       / 
  `------'  `--' '--'     `-----'   `-----'    `--'             `------'   `------'`--'  `--'  `--'    `-----'     `-----'  
                                                    (Group Creation Tool)
                                Made by Cj GH: im-solar https://github.com/im-solar/GroupGenius
        """
        
        
    ]
    
    
    def pre_import(Input: str) -> str: return filedialog.askopenfile()
    def single_inp(Input: str) -> str: return console.input(f"[purple3] {Input}")
    def yn_inp(Input: str) -> str: return str(console.input(f"[purple3] {Input} [Y/N]").upper())
    def backcheck(Input: int):
        if Input == "":
            return True
        else:
            return False
    

    def print_logo(logos) -> str:
        
        logo = random.choice(logos)
        for _ in logo.splitlines():
            print(Fore.RED + _)
            
        
        
    def print_info(Info:str) -> str: return console.print(f"[blue] {Info}")
    def warning_out(Warning: str) -> str: return console.print(f"[yellow3] [Warning] - {Warning}")
    def err_out(Error: str) -> str: return console.print(f'[red1] Oops something went wrong:sad:. {Error}')
    
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def print_groups(groups, num_of_groups):
        for x in range(num_of_groups):
            for i in range(len(groups[x])):
                # Will turn this into graphs later
                console.print(f"[blue] Group {x + 1}: {groups[x][i]}")

