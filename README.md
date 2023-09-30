# Group Genius
## (Group Creation Tool)


# Note: This tool is in early stages of its development and is currently being worked on more updates will be posted if you encounter any bugs or have feature requests please leave them in the issues page.
Run auto_setup in order to use the program as it downloads the requirements needed

## 1.0.0 Introduction
### What is Group Genius?
Group Genius is a command-line interface group creation tool designed for educators, sports teams, and various other applications. It serves as an advanced group generator, offering a multitude of customization options while maintaining user-friendly functionality.
This tool aims to facilitate the creation of highly customizable groups, allowing for the efficient sorting of students and other individuals into well-suited group configurations.

### Current Features
- [x] Ability to create and import presets
- [x] Manage and save presets
- [x] Choose number of groups to make
- [x] Add restrictions so students cant be in the same group as each other
- [x] Add certain users into higher level groups based on their skill level and let the program sort them into fair-even groups
- [x] Google Login and ability to grab student names from a certain classroom and then add all the names into a list you can use
- [x] Generation of groups


### Future Features
- [ ] Functional Interface
- [ ] Save created groups into a file
- [ ] Save presets to db so the user dosnt have to import a file
- [ ] + Much More

## How To Run
- Open command prompt and cd onto the desktop
```bash
~$ cd Desktop
```

### Download or clone the code from github
- Cloning Code:
```bash
~$ git clone https://github.com/im-solar/GroupGenius
```
### Downloading the code:
- Goto the main github page find the green button that says code click on it and download as zip once downloaded unzip it with winrar or 7zip and drag to desktop/prefered directory.

### Intall the necessary requirements
### Option 1:
Open the group genius folder find the auto_setup.py file and run it
After that you only have to run the main.py file not the setup file

### Option 2:
- Cd into the directory
```bash
~$ cd GroupGenius
```

- Install needed requirements
```bash
~$ pip install -r requirements.txt
```
- Run the program
```bash
~$ python3 main.py
```

## If you would like to use google login read this
For the time being until I find out if its possible I cannont provide the credentials used for the api application this means you will have to do this yourself you can do this easily by going to the google.txt file there you will find a tutorial on how to set it up. Again I dont want to do this but as of right now I have no way of securly storing the credentials.
