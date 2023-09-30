import subprocess, time, pkg_resources, os
from os import name
from pkg_resources import DistributionNotFound, VersionConflict

reqs = [
    'colorama>=0.4.6',
    'google_api_python_client>=2.95.0',
    'google_auth_oauthlib>=1.0.0',
    'passlib>=1.7.4',
    'protobuf>=4.24.3',
    'rich>=13.6.0',
    'setuptools>=65.5.0'
]

cmds = [
    "colorama",
    "google_api_python_client",
    'google_auth_oauthlib',
    'passlib',
    'protobuf',
    'rich',
    'setuptools'
]


try:
    pkg_resources.require(reqs)
except DistributionNotFound as distro_err:
    print("Whoops! Looks like your missing a few things.")
    time.sleep(1.5)
    print("Dont worry you sit back and let me do all the work.")
    time.sleep(1.5)
    print("You will see text pop up on the cmd dont worry its all fine its installing the needed packages to run the program!")
    time.sleep(1.5)
    for i in range(5,0,-1):
        print(f"Installing requirements in: {i} second(s).", end='\r')
        time.sleep(1)
    for cmd in cmds:
        subprocess.run(f"pip install {cmd}")
    print("All done! you will be put into the welcome screen in just a moment please wait.")
    time.sleep(5)
    if name == "nt": # nt is for windows
        os.system('cls') # windows uses the cmd cls to clear prompt
    else: # this is getting anything besides windows aka like mac or linux
        os.system('clear') # mac and linux use the cmd clear to clear prompt
    subprocess.run(["python", "main.py"], check=True)
except VersionConflict as ver_err:
    print("Whoops! Looks like your a little outdated.")
    time.sleep(1.5)
    print("Dont worry you sit back and let me do all the work.")
    time.sleep(1.5)
    print("You will see text pop up on the cmd dont worry its all fine its updating your already installed packages!")
    time.sleep(1.5)
    for i in range(5,0,-1):
        print(f"Installing requirements in: {i} second(s).", end='\r')
        time.sleep(1)
    for cmd in cmds:
        subprocess.run(f"pip install {cmd}")
    print("All done! you will be put into the welcome screen in just a moment please wait.")
    time.sleep(5)
    if name == "nt": # nt is for windows
        os.system('cls') # windows uses the cmd cls to clear prompt
    else: # this is getting anything besides windows aka like mac or linux
        os.system('clear') # mac and linux use the cmd clear to clear prompt
    subprocess.run(["python", "main.py"], check=True)
else:
    print("Wow! All requirements already satisfied good job!")
    print("Bringing you to the welcome screen in a moment. Please wait!")
    time.sleep(4)
    if name == "nt": # nt is for windows
        os.system('cls') # windows uses the cmd cls to clear prompt
    else: # this is getting anything besides windows aka like mac or linux
        os.system('clear') # mac and linux use the cmd clear to clear prompt
    subprocess.run(["python", "main.py"])


