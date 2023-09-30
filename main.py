

# Current Version: 1.0.0  released: 9/30/23
# Made by GH: im-solar https://github.com/im-solar/GroupGenius
# Note: This is the first version of the program bugs will occur and somethings may not be as polished.
# Note: This is COMMAND PROMPT ONLY a gui version will be worked on but for now you get the windows console enjoy. 


import re, time, os, datetime, csv, random, json, configparser
import core.core as core
from core.IO_helper import IO_Helpers
from google_main.google_auth import google_auth


# To DO: Please add suggestions if you have them in the discussions page
# get google classes if logged in an no preset is active to append names from certain class
# get google classes if logged in an a preset is active to either choose names to append or just append all
# More not listed here



# Data that is being worked with
preset_con = {
    'num_of_groups': None,
    'student_names': None,
    'black_list': None,
    'stared': {'1': [], '2': [], '3': []},
}
session = {
    'preset_active': False,
    'logged_in': False,
    'pre_path': None,
    'amount_changed':  0,
    'last_changed': None,
    'saved': None,
    'last_saved': None
}
con_parse = configparser.ConfigParser()


class main():
    
    def menu():    
        IO_Helpers.print_info("This tool will allow you to make fully customizable groups this is great if your a teacher, coach, or anybody who needs to sort names into fair groups!")
        time.sleep(2)
        login = str(IO_Helpers.yn_inp("Would you like to login with google this way you can get names right from your classes?"))
        if login == "Y":
            if session['logged_in'] == True:
                IO_Helpers.print_info("Already logged into google taking you back to the main menu")
                main_running = True
            else: main.log_in()
            
        preset_in = str(IO_Helpers.yn_inp("Would you like to use a preset? (yes or no)"))
        if preset_in == "Y":
            time.sleep(.2)
            main.import_pre()
            main.main_menu()
            
        if preset_in == "N":
            IO_Helpers.print_info("Sounds good not using a preset")
            # no_pre_check = main
            
            if main.create_preset() == True:
                print("Taking you back to the main menu [DEBUG]")
                main.main_menu()
                
                
            else:
                print("Something went really wrong restart the program and try again.")
                
    def main_menu():
                main_running = True
                while main_running == True:
                    IO_Helpers.clear()
                    IO_Helpers.print_info("Welcome to the program you have loaded a preset please choose what you would like to do next.")
                    # Need work in order to look good.
                    # IO_Helpers.print_info(f"\t\tCurrent Preset Data: \n Names: {preset_con['student_names']}\tNumber Of Groups To Generate: {preset_con['num_of_groups']}\tCurrent Exclusion's (Cannot be in groups with eachother): {preset_con['black_list']}\tStared Names: {preset_con['stared']} ")
                    # List the current preset to show users what they are working with since some come from not using a preset
                    option_choice = int(IO_Helpers.single_inp("[1] = Start generating groups \n [2] = Edit preset \n [3] = Login With Google"))
                    if option_choice == 1:
                        IO_Helpers.print_info("generating groups based off of loaded preset please wait")
                        time.sleep(2)
                        main.main_generation(preset_con)
                        # create a generator function and call it here with all data needed
                    if option_choice == 2:
                        a = main.edit_pre()
                        option_choice = a

                    else:
                        main_running = True
            
    def log_in():
        IO_Helpers.print_info("Welcome to the google login page")
        main_auth = True
        
        while main_auth == True:
            IO_Helpers.print_info("Taking you to the google login!")
            time.sleep(2)
            authed = google_auth.main_auth()
            
            if authed == False:
                yn = str(IO_Helpers.yn_inp("Looks like the google login failed do you want to try again?"))
                if yn == "Y":
                    IO_Helpers.print_info("Sounds good sending you back to the login page.")
                    time.sleep(2)
                    main_auth = True
                elif yn == "NO":
                    IO_Helpers.print_info("Sounds good taking you back to the main page")
                    time.sleep(2)
                    break

            if authed == True:
                IO_Helpers.print_info("Logged into google taking you back to the main menu!")
                time.sleep(2)
                session.update({'logged_in': True})
                main_auth = False
                break
                
            
        
    def import_pre():
        path  = os.getcwd()
        pre_path = path + "\\database\\Presets"
        pre_in_running = True
        
        while pre_in_running == True:
            preset_files = core.pre_handle.get_presets(pre_path) 
            pre_choice = int(IO_Helpers.single_inp("Please choose a preset."))
            
            if pre_choice in range(len(preset_files)):
                pre_chosen = preset_files[pre_choice]
                read_pre = con_parse.read(pre_path + '\\' + pre_chosen)
                con_settings = con_parse['DEFAULT']
                preset_con.update({'num_of_groups': con_settings['num_of_groups'], 'student_names': json.loads(con_settings['student_names']), 'black_list': [json.loads(con_settings['black_list'])], 'stared': json.loads(con_settings['stared'])})
                session.update({'preset_active': True})
                return session.update({'pre_path': pre_path + '\\' + pre_chosen})
            else:
                IO_Helpers.err_out("Not a good file path please try a differnt folder")
                preset_files.clear()
                pre_in_running == True
                
    # Not done but have to link with preset_con dict in order to save correctly
    def create_preset():
        IO_Helpers.print_info("Looks like you opted out of using a preset time to put everything in")
        IO_Helpers.print_info("First add all the names you want to be in the list (one at a time)")
        running = True
        while running == True:
            if session['logged_in'] == True:
                choice = str(IO_Helpers.yn_inp("Looks like you are logged into google would you like to see a list of your current classrooms in order to get the names from your student list?"))
                if choice == "Y":
                    IO_Helpers.print_info("Getting classroom list now")
                    class_names = google_auth.get_classes()
                    IO_Helpers.print_info("Got all names from classroom adding them to the list")
                    preset_con.update({'student_names': class_names})
                    num_check = True
                    while num_check:
                        num_of_groups = int(IO_Helpers.single_inp("Please enter the amount of groups you would like to create."))
                        if core.pre_handle.g_div(num_of_groups, preset_con['student_names']) == True:
                            choice = IO_Helpers.yn_inp(f"Are you sure you want to make {num_of_groups}?")
                            if choice == "Y":
                                IO_Helpers.print_info(f"Sounds good when you run the generator it will make {num_of_groups} group(s)\nTaking you to the main menu. ")
                                time.sleep(1.5)
                                return True
                            elif choice == "N":
                                IO_Helpers.print_info("Sounds good taking you back to choose a new number")
                                num_check = True
                    
                    
                    
                elif choice == "N":
                    print("sounds good not getting your classrooms")
            else:
                
                names = []
                ui = input("Please enter the name you want (type -1 to save what you have entered and goto the next option.)")
                if ui == -1 and len(names) >= 1:
                    print("taking you to the next option")
                else:
                    if len(ui) > 1:
                        stripped = ui.strip()
                        print(stripped, 'is being added to the list of names')
                        preset_con.update({'student_names': stripped})
            
                
    def edit_pre():
        IO_Helpers.print_info("Welcome to the preset editor! \n Please choose one of the options below.")
        main_editor = True
        # Main Preset editor 
        while main_editor == True:
            # Main Edit Choice / what they want to do
            me_choice = int(IO_Helpers.single_inp("[1] = Student Editor. \n [2] = Group Editor \n [3] = Back To Main Screen"))
            # Goes into the student editor loop
            if me_choice == 1:
                IO_Helpers.print_info("Welcome to the student editor! \n please choose one of the options below!")
                student_editor = True
                names = preset_con['student_names']
                while student_editor == True:
                    edit_choice  = int(IO_Helpers.single_inp("[1] = Delete Student Name. \n [2] = Edit Student Name. \n [3] = Edit black-listed names. \n [4] = Edit Stared Students \n [0] = Back to editor seletor."))
                    
                    def edit_choice1():
                        stu_delete = True
                        while stu_delete == True:
                            
                            print("Welcome to the deletion menu. Names are listed with numbers.")
                            IO_Helpers.print_info("Welcome to the deletion menu here you can delete a name thats in your preset!")
                            core.pre_handle.name_print(preset_con)
                            u_in = int(IO_Helpers.single_inp("Please enter the number that corrispondes to the name you want to delete. or type [-1] to go back to the student editor"))
                            # u_in = int(input("Please enter the number that corrispondes to the name you want to delete. or type [-1] to go back to the student editor"))
                            if u_in in range(len(preset_con['student_names'][0])):
                                IO_Helpers.warning_out(f"You are about to delete the name {preset_con['student_names'][u_in]} from this preset.")
                                y_n_in = IO_Helpers.yn_inp("Are you sure you want to do this? [Y/N] ").upper()
                                if y_n_in == 'Y':
                                    print(f"deleting {preset_con['student_names'][u_in]} from group!")
                                    preset_con['student_names'].pop(u_in)
                                    IO_Helpers.print_info(f"New list: {preset_con['student_names']}")
                                    IO_Helpers.print_info('Taking you back to the deletion main screen')
                                    session['amount_changed'] += 1
                                    stu_delete = True
                                elif y_n_in == "N":
                                    IO_Helpers.print_info("Keeping name in group! \n Bringing you back to the deletion menu.")
                                    stu_delete = True
                            if u_in == -1:
                                IO_Helpers.print_info("Taking you back to the student editor!")
                                return False
                    # Name editor function       
                    def edit_choice2():
                        name_edit = True
                        while name_edit == True:
                            IO_Helpers.print_info("Welcome to the name editor menu! \n Here you can change names already in your preset.")
                            core.pre_handle.name_print(preset_con)
                            inp = int(IO_Helpers.single_inp("Please enter the number that corrispondes to the name you want to change. \n Or type [-1] to go back the the student editor."))
                            if inp in range(len(preset_con['student_names'])):
                                IO_Helpers.print_info(f"Name being edited: {preset_con['student_names'][inp]}")
                                str_inp = str(IO_Helpers.single_inp("Please enter the new name you want (Note: names must be more than 1 character)"))
                                if len(str_inp) <= 1:
                                    IO_Helpers.warning_out("New name must be atleast 2 charcters long")
                                    name_edit = True
                                elif any(check.isdigit() for check in str_inp) == True:
                                    IO_Helpers.warning_out("New name cannot contain any numbers. \n Taking you back to the editor menu")
                                    name_edit = True
                                new_name = preset_con['student_names'][inp] = str_inp
                                print(f'Student name updated: {new_name}')
                                session['amount_changed'] += 1
                                name_edit = True
                            else:
                                IO_Helpers.err_out("No student matches the number entered, please follow the numbers listed infront of the name.")
                                name_edit = True
                            if inp == -1:
                                IO_Helpers.print_info("Taking you back to the student editor")
                                time.sleep(1.5)
                                return False
                            
                    def edit_choice3():
                        bl_main = True
                        while bl_main == True:
                            IO_Helpers.print_info("Welcome to the blacklist tab!\n Names of students will pop up with numbers next to their names type the number according to the students you want to exclude from being in a group together.")
                            core.pre_handle.name_print(preset_con)
                            n1 = int(IO_Helpers.single_inp("Enter the number for the first student you want to select.\n Or type [-1] to go to the main menu."))
                            
                            if n1 == -1:
                                IO_Helpers.print_info("Taking you back to the student editor menu")
                                time.sleep(1.5)
                                return False 
                            
                            n2 = int(IO_Helpers.single_inp("Please enter the second number for the other student you want to exclude from being in a group together.\n Or type [-1] to go to the main menu."))
                            if n2 == -1:
                                print("Taking you back to the student editor menu")
                                time.sleep(1.5)
                                return False

                            elif n1 in range(len(preset_con['student_names'])) and n2 in range(len(preset_con['student_names'])):
                                IO_Helpers.warning_out(f"You are about to exclude {preset_con['student_names'][n1]}, {preset_con['student_names'][n2]} from being put in a group together. \n Are you sure you want to do this?")
                                choice = IO_Helpers.yn_inp("Type Y for yes or N for no")
                                if choice == "Y":
                                    IO_Helpers.print_info("Exluding names from being in the same group together.")
                                    time.sleep(1.5)

                                    # Stage 1 split: Splits the pairs of names into the same list
                                    if len(preset_con['black_list'][0]) <= 1:
                                        
                                        s1_split = preset_con['black_list'][0].split(', ') 
                                        sf_split = [x.split(' ') for x in s1_split]
                                        for i in sf_split:
                                            try:
                                                index = i.index('''''')
                                                sf_split.pop(index)
                                                break
                                                
                                            except ValueError as not_found:
                                                pass
                                    else:
                                        sf_split = preset_con['black_list'][0]
                                       
                                    sf_split.append([preset_con['student_names'][n1], preset_con['student_names'][n2]])
                                    preset_con.update({'black_list': sf_split})
                                    count = 1
                                    for i in preset_con['black_list']:
                                            IO_Helpers.print_info(f"Blacklist group #{count}: {i}")
                                            count += 1
                                    session['amount_changed'] += 1
                                    IO_Helpers.print_info("Taking you back to the blacklist menu.")
                                    bl_main = True

                                elif choice == "N":
                                    IO_Helpers.print_info("Sounds good taking you back to the blacklist menu in case you change your mind.")
                                    bl_main = True
                                    
                    def edit_choice4():
                    # stared Students
                    # 3 ranks 1,2,3 
                    # 1 is the highest 3 is lowest 
                    #allow person to choose the person and number they want. (not all students need to be stared)
                        star_main = True
                        temp_dict = {'1': [], '2': [], '3': []}
                        shesh_changes_made = 0
                        take_back = None
                        while star_main == True:
                            take_back = None
                            IO_Helpers.print_info("Welcome to the star student section!\n Names will appear with numbers in front of them please select the number that corresponds to the name you would like to choose.")
                            core.pre_handle.name_print(preset_con)
                            stu_inp = int(IO_Helpers.single_inp("Enter number corresponding to the name you want"))
                            if stu_inp in range(len(preset_con['student_names'][0])):
                                IO_Helpers.print_info("Which group wold u like to put this student in? \n [1] being the highest level and [3] being the lowest (This just means there will be more 3's than 1's in the group)")
                                sg_inp = int(IO_Helpers.single_inp("[1] = Group 1 (highest group) \n [2] = Group 2 \n [3] = Group 3"))
                                for i in preset_con['stared'].values():
                                     for x in preset_con['stared'].keys():
                                        if preset_con['student_names'][stu_inp] in i and preset_con['student_names'][stu_inp] in preset_con['stared'][f'{sg_inp}']:
                                            IO_Helpers.err_out(preset_con['student_names'][stu_inp], f"is already in group: {x}")
                                            IO_Helpers.print_info("Taking you back to the star section")
                                            time.sleep(1.5)
                                            take_back = True
                                            break
                                        # Checks if user is in a group already but not the one defined by user 
                                        if preset_con['student_names'][stu_inp] in i and preset_con['student_names'][stu_inp] not in preset_con['stared'][f'{sg_inp}']:
                                            IO_Helpers.warning_out(f"Students name is already in group {x} would you like to remove them from that group and put them into group {sg_inp}?")
                                            inp = input("Y = [Yes] or N = [No]").upper()
                                            
                                            if inp == 'Y':
                                                IO_Helpers.print_info(f"Moving {preset_con['student_names'][stu_inp]} to group {sg_inp}")
                                                # Not sure why im formating it and putting it into a str will prob change later
                                                index = preset_con['stared'][f'{x}'].index(preset_con['student_names'][stu_inp])
                                                preset_con['stared'][f'{x}'].pop(index)
                                                preset_con['stared'][f'{sg_inp}'].append(preset_con['student_names'][stu_inp])
                                                IO_Helpers.print_info(f"{preset_con['student_names'][stu_inp]} Was moved to star group {sg_inp}")
                                                session['amount_changed'] += 1
                                                take_back = True
                                            elif inp == 'N':
                                                print('not changing anything')
                                                take_back = True
                                            
                                                
                                                # print(temp_dict[f'{x}']
                                
                                if take_back == True:
                                    star_main = True
                                    
                                elif sg_inp == 1:
                                    IO_Helpers.warning_out(f"are u sure u want to add {preset_con['student_names'][stu_inp]} to star group 1?")
                                    yn_in = IO_Helpers.yn_inp("Y or N")
                                    if yn_in == "Y":
                                        preset_con['stared']['1'].append(preset_con['student_names'][stu_inp])
                                        IO_Helpers.print_info(f"Added {preset_con['student_names'][stu_inp]} to star group 1.")
                                        time.sleep(1.5)
                                        session['amount_changed'] += 1
                                        star_main = True
                                elif sg_inp == 2:
                                    IO_Helpers.warning_out(f"are u sure u want to add {preset_con['student_names'][stu_inp]} to group 2?")
                                    yn_in = IO_Helpers.yn_inp("Y or N")
                                    if yn_in == "Y":
                                        preset_con['stared']['2'].append(preset_con['student_names'][stu_inp])
                                        session['amount_changed'] += 1
                                        IO_Helpers.print_info(f"Added {preset_con['student_names'][stu_inp]} to star group 2.")
                                        time.sleep(1.5)
                                        star_main = True
                                
                                elif sg_inp == 3:
                                    IO_Helpers.warning_out(f"are u sure u want to add {preset_con['student_names'][stu_inp]} to star group 3?")
                                    yn_in = IO_Helpers.yn_inp("Y or N")
                                    if yn_in == "Y":
                                        preset_con['stared']['3'].append(preset_con['student_names'][stu_inp])
                                        IO_Helpers.print_info(f"Added {preset_con['student_names'][stu_inp]} to star group 3.")
                                        time.sleep(1.5)
                                        session['amount_changed'] += 1
                                        star_main = True
                            if stu_inp == -1:
                                IO_Helpers.print_info("Taking you back to student editor")
                                time.sleep(1.5)
                                return False
                    def bad_inp():
                        IO_Helpers.err_out("Sorry that wasnt a valid option please try a differnt number.")

                    options: dict = {
                        1:edit_choice1,
                        2:edit_choice2,
                        3:edit_choice3,
                        4:edit_choice4
                    }
                    run = options.get(edit_choice, bad_inp)
                    run()
                    if edit_choice == 0:
                        main_editor = True
                        student_editor = False
                        
            # Group Editor        
            if me_choice == 2:
                IO_Helpers.print_info("Welcome to the group editor!\n Here you can edit the settings for your groups!")
                group_editor = True
                names = preset_con['student_names']
                while group_editor == True:
                    edit_choice  = int(IO_Helpers.single_inp("[1] = Edit Amount Of Groups \n [2] = Back to editor seletor."))
                    if edit_choice == 1:
                    # Goes to edit amount loop
                        IO_Helpers.print_info("Welcome to the group amount editor!\n Here you can edit the amount of groups you would like to generate!")
                        num_of_groups = int(IO_Helpers.single_inp('Please enter the amount of groups you would like.'))
                        if core.pre_handle.g_div(num_of_groups, names) == True:
                            choice = IO_Helpers.yn_inp(f"Are you sure you want to make {num_of_groups}?")
                            if choice == "Y":
                                IO_Helpers.print_info("Changes applied!\n Taking you back to the group editor")
                                time.sleep(1.5)
                                session['amount_changed'] += 1
                                group_editor = True  
                            elif choice == "N":
                                IO_Helpers.print_info("Sounds good taking you back to the group amount editor to choose a new number")
                                group_editor = True 
                        else:
                            IO_Helpers.warning_out("The amount of groups you entered will not have even members be warned some groups may contain more students than others.")
                            temp = []
                            for i in range(1, 100):
                                if num_of_groups % i == 0:
                                    temp.append(i)
                            IO_Helpers.print_info(f"These are sum nums you can use that will make an even amount of groups: {temp}")
                            temp.clear()
                            inp = IO_Helpers.yn_inp("Would you like to enter a new number of groups?")
                            if inp == "Y":
                                print('Taking you back to the total group editor')
                                group_editor == True
                            elif inp == "N":
                                IO_Helpers.print_info(f"Sounds good keeping the group num of {num_of_groups}")
                                preset_con['num_of_groups'] = num_of_groups
                                session['amount_changed'] += 1
                                # Takes user back to the pre edit
                                group_editor = True
                                
                                
                    elif edit_choice == 2:
                        IO_Helpers.print_info("Taking you back to the main selection menu")
                        main_editor = True
                        group_editor = False
         # Saving if any changes were made
            if me_choice == 3:
                # asking if they want to save changes (they are using a preset)
                saving = True 
                while saving:
                    if session['amount_changed'] != 0 and session['preset_active'] == True:
                        IO_Helpers.warning_out(f"Wait before you goto the main menu, you have {session['amount_changed']} changes that need to be saved what would you like to do?")
                        save_inp = int(input("[1] = Save changes to current preset file \n [2] = Save changes to a new preset file \n [3] = Dont save changes and just use for this session."))
                        if save_inp == 1:
                            date = datetime.datetime.now()
                            saved_date = date.strftime('%A') +",",date.strftime('%B'), date.strftime('%d')+",", date.year
                            con_parse['DEFAULT'] = {'num_of_groups': preset_con['num_of_groups'],
                                                    'student_names': json.dumps(preset_con['student_names']), # Add changes to student names ()
                                                    'black_list': json.dumps(preset_con['black_list']),
                                                    'stared': json.dumps(preset_con['stared']),
                                                    'last_saved': json.dumps(saved_date)}     
                            path = session['pre_path']
                            with open(path, 'w') as pre_file:
                                con_parse.write(pre_file)
                                IO_Helpers.print_info("Saved preset file!")
                                time.sleep(1.5)
                        elif save_inp == 2:
                            date = datetime.datetime.now()
                            saved_date = date.strftime('%A') +",",date.strftime('%B'), date.strftime('%d')+",", date.year 
                            con_parse['DEFAULT'] = {'num_of_groups': preset_con['num_of_groups'],
                                                    'student_names': json.dumps(preset_con['student_names']), # Add changes to student names ()
                                                    'black_list': json.dumps(preset_con['black_list']),
                                                    'stared': json.dumps(preset_con['stared']),
                                                    'last_saved': json.dumps(saved_date)}
                            file_name = str(IO_Helpers.single_inp("What Would you like to call the file? [Note: spaces are not allowed the only special characters allowed are _ and -"))
                            
                            path  = os.getcwd()
                            path = path + "\\database\\Presets"
                            path = f"{path}\\{file_name}"
                            with open(path, 'w') as pre_file:
                                con_parse.write(pre_file)
                                IO_Helpers.print_info("Saved preset file!")
                                time.sleep(1.5)  
                            
                            
                        elif save_inp == 3:
                            last_chance = IO_Helpers.yn_inp("Are you sure you dont want to save your changes to a preset file? Y/N")
                            if last_chance == "Y":
                                print("Sounds good taking you to the main menu")
                            elif last_chance == "N":
                                print("Sounds good taking you back to the save option menu")
                                saving = True
                            else:
                                print("Invalid option")
                                saving = True
                # asking if they want to save the changes to a new preset file as they didnt use one 
                    if session['amount_changed'] != 0 and session['preset_active'] == False:
                        IO_Helpers.warning_out("Wait! looks like you have some setting changed but no preset would you like to create one with the setting currently being used?")
                        inp = IO_Helpers.yn_inp("Y/N")
                        if inp == "Y":
                            IO_Helpers.print_info("Sounds good creating a preset file now!")
                            # As of right now there are no checks or fail checks on this so if someone messes it up oh well. for now
                            file_name = IO_Helpers.single_inp("What Would you like to call the file? [Note: spaces are not allowed the only special characters allowed are _ and -")
                            path  = os.getcwd()
                            path = path + "\\database\\Presets"
                            path = f"{path}\\{file_name}"
                            with open(path, 'w') as pre_file:
                                con_parse.write(pre_file)
                                IO_Helpers.print_info("Saved preset file!")
                                time.sleep(1.5)  
                                
                        elif inp == "N":
                            IO_Helpers.print_info("Sounds good taking you to the menu and not saving the changes.")
                            return False
                        
                    if session['amount_changed'] == 0:
                      IO_Helpers.print_info("Taking you back to the main menu")
                      time.sleep(1)
                      return False  
                
                        
                IO_Helpers.print_info("Taking you back to the main menu")
                time.sleep(1)
                return False
      # Done 9/14/23      
    def main_generation(preset):
        
        if len(preset_con['black_list']) >=1 and len(preset_con['stared']) > 3:
            temp_groups = []
            num_per_group = len(preset_con['student_names']) // int(preset_con['num_of_groups'])
            temp_names = preset['student_names'].copy()
            main = True
            fail_count = 0
            for _ in range(int(preset_con['num_of_groups'])):
                temp_groups.append([])
            while main:
                fail_count = 0
                for x, val in enumerate(temp_groups):
                    running = True
                    while running:   
                        if len(temp_groups[x]) == num_per_group:
                            if x + 1 == int(preset_con['num_of_groups']):
                                IO_Helpers.print_groups(temp_groups, int(preset_con['num_of_groups']))
                                time.sleep(5)
                            main = False
                            break
                             
                        # run check function on temp groups if it passes append the groups to main list if not restart and make new groups
                        ran_name = random.choice(temp_names)
                        star_check = core.gen_help.stared_check(preset_con, ran_name, temp_groups[x], num_per_group)
                        bl_check = core.gen_help.bl_check(preset_con, ran_name, temp_groups[x], num_per_group, temp_names)
                        
                        if fail_count >= 100:
                            for x in range(int(preset_con['num_of_groups'])):
                                temp_groups[x].clear()
                            temp_names = preset['student_names'].copy()
                            fail_count = 0  
                            main = True 
                            break
                        
                        if star_check == False:
                            fail_count += 1
                            running = True
                        
                        elif bl_check == False:
                            # Last sort of fail check if for some reason the generator gets caught in and inf loop it will restart the full generation after a certain amount of iterations.
                            fail_count += 1
                            running = True
   
                        else:
                            temp_groups[x].append(ran_name)
                            index = temp_names.index(ran_name)
                            temp_names.pop(index)
                        
                        
                 
        elif len(preset_con['black_list']) > 2 and len(preset_con['stared']) <= 3:
            print("stared is not filled blacklist is [DEBUG ]")
            temp_groups = []
            num_per_group = len(preset_con['student_names']) // int(preset_con['num_of_groups'])
            temp_names = preset['student_names'].copy()
            print(temp_names, 'temp names')
            print(preset['student_names'])
            main = True
            fail_count = 0
            for x in range(int(preset_con['num_of_groups'])):
                temp_groups.append([])
            while main:
                fail_count = 0
                for x, _ in enumerate(temp_groups):
                    running = True
                    while running:   
                        if len(temp_groups[x]) == num_per_group:
                            if x + 1 == int(preset_con['num_of_groups']):
                                IO_Helpers.print_groups(temp_groups, int(preset_con['num_of_groups']))
                                time.sleep(5)
                            main = False
                            break
                        
                        ran_name = random.choice(temp_names)
        
                        bl_check = core.gen_help.bl_check(preset_con, ran_name, temp_groups[x], num_per_group, temp_names)
                        
                        if fail_count >= 100:
                            for x in range(int(preset_con['num_of_groups'])):
                                temp_groups[x].clear()
                            temp_names = preset['student_names'].copy()
                            fail_count = 0  
                            main = True 
                            break
                     
                        if bl_check == False:
                            fail_count += 1
                            running = True
                        else:
                            temp_groups[x].append(ran_name)
                            index = temp_names.index(ran_name)
                            temp_names.pop(index)
            
        elif len(preset_con['stared']) >= 3 and len(preset_con['black_list']) <= 2:
            
            temp_groups = []
            num_per_group = len(preset_con['student_names']) // int(preset_con['num_of_groups'])
            temp_names = preset['student_names'].copy()
            print(temp_names, 'temp names')
            print(preset['student_names'])
            main = True
            fail_count = 0
            for x in range(int(preset_con['num_of_groups'])):
                temp_groups.append([])
            while main:
                fail_count = 0
                for x, _ in enumerate(temp_groups):
                    running = True
                    while running:   
                        if len(temp_groups[x]) == num_per_group:
                            if x + 1 == int(preset_con['num_of_groups']):
                                IO_Helpers.print_groups(temp_groups, int(preset_con['num_of_groups']))
                                done = int(IO_Helpers.yn_inp("Are you done looking at these groups?"))
                                if done == "Y":
                                    IO_Helpers.print_info("Sounds good taking you back to the main menu.")
                                    main = False
                                    break
                                else:
                                    IO_Helpers.warning_out("You can only say yes to this prompt")
                                    
                        ran_name = random.choice(temp_names)
                        star_check = core.gen_help.stared_check(preset_con, ran_name, temp_groups[x], num_per_group)
                        
                        if fail_count >= 100:
                            for x in range(int(preset_con['num_of_groups'])):
                                temp_groups[x].clear()
                            temp_names = preset['student_names'].copy()
                            fail_count = 0  
                            main = True 
                            break
                     
                        if star_check == False:
                            fail_count += 1
                            running = True
                        else:
                            temp_groups[x].append(ran_name)
                            index = temp_names.index(ran_name)
                            temp_names.pop(index)


if __name__ == '__main__':
    IO_Helpers.print_logo(IO_Helpers.logos)
    time.sleep(5)
    main.menu()