# Input output helper.

import rich
from rich.console import Console
import random
from tkinter import filedialog

console = Console()
class IO_Helpers():
    def pre_import(Input: str) -> str: return filedialog.askopenfile()
    def single_inp(Input: str) -> str: return int(input(f"{Input}"))
    def yn_inp(Input: str) -> str: return str(console.input(f"{Input} [Y/N]").upper())
    def backcheck(Input: int):
        if Input == "":
            return True
        else:
            return False
    


    def info_print(Info:str) -> str: return console.print(f"[blue] {Info}")
    def warning_out(Warning: str) -> str: return console.print(f"[blue] [Warning] - {Warning}")
    def err_out(Error: str, Exception: str) -> str: return console.print('f[red]Oops something went wrong:sad:. {Error}, {Exception}')
    
    

    

# a = IO_Helpers.pre_import("Input something")
# b = IO_Helpers.info_print('Okok')
# print(b)
# print(a)


class Menu():

    logos = [
        '''
        test
    ''',

    '''test 
            '''
    
    
    
    ]

    def print_logo(logo):
        for i in random.choice(logo):
            print(i)
            break

    # def

logos = [
        '''
        test
    '''

    '''test 
            '''
    
    
    
    ]

# Menu.print_logo(logos)

