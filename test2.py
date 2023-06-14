

# for google api https://developers.google.com/identity/protocols/oauth2/native-app


import tkinter
from tkinter import filedialog
import re, time, os
import csv
import json
from tkinter.constants import TRUE
from core import IO_helper
from core.IO_helper import IO_Helpers 
from core.core_helper import pre_handle




# For generating names and not including blacklist:
# 





config = {
    'logged_in': None
}

preset_con = {
    'preset_active': False,
    'num_of_groups': None,
    'student_names': None,
    'black_list': [],
    'stared': {},
    'last_saved': None,
    # css = changes made since last saved
    'css':  None,
    # saved last run? aka yes or no/ True or False
    'slr': None
}
temp_pre = {
    'amount_changed':  0,
    'last_changed': None,
    'saved': None,
    'last_saved': None
}


class presets():
    def import_pre():
        print("time to import your pre-set a file explorer will open soon click on the preset you want to use.")
        pre_in_running = True
        while pre_in_running == True:

            inpt_pre = filedialog.askopenfile()
            exten = inpt_pre.name
            if exten.endswith('.txt'):
                print('text found')
                with open(exten, 'r') as pre_file:
                    kk = pre_file.readlines()
                    raw_group = kk[0]
                    raw_names = kk[1]
                    raw_blk_lst = kk[2]
                    ok = raw_names.splitlines()
                    info = [x.split(', ') for x in ok]
                    print(info)
                    preset_con.update({'preset_active': True, 'num_of_groups': raw_group, 'student_names': info, 'black_list': raw_blk_lst})
                    break

            # --// Not working rn will need a package like pandas or openpyxl \\--
            # elif exten.endswith('.xlsx') or exten.endswith('.xlsm'):
            #     # open excel and read data with csv
            #     print("excel file extension found")
            #     with open(exten, 'r') as pre_file:
            #         print(pre_file)
            #     pass


            else:
                print("not a good file path")
                pre_in_running == True
        # print(kk)
            # raw_group = kk[0]
            # raw_names = kk[1]
            # ok = raw_names.splitlines()
            # info = [x.split(', ') for x in ok]
    def edit_pre():
        print("Welcome to the preset editor what would you like to do?")
        main_editor = True
        # Main Preset editor 
        while main_editor == True:
            # Main Edit Choice / what they want to do
            me_choice = IO_helper.IO_Helpers.single_inp("[1] = Student Editor. \n [2] = Group Editor [3] = Back To Main Screen")
            # Goes into the student editor loop
            if me_choice == 1:
                print("Welcome to the student editor")
                student_editor = True
                names = preset_con['student_names']
                while student_editor == True:
                    edit_choice  = IO_Helpers.single_inp("[2] = Delete Student Name. \n [3] = Edit Student Name. \n [4] = Edit black-listed names. \n [5] = Edit Stared Students \n [6] = Back to editor seletor.")
                    
                    def edit_choice1():
                        stu_delete = True
                        while stu_delete == True:
                            
                            print("Welcome to the deletion menu. Names are listed with numbers.")
                            pre_handle.name_print(preset_con)
                            u_in = int(input("Please enter the number that corrispondes to the name you want to delete. or type [-1] to go back to the student editor"))
                            if u_in in range(len(preset_con['student_names'][0])):
                                print(preset_con['student_names'][0][u_in])
                                IO_Helpers.warning_out(f"You are about to delete the name {preset_con['student_names'][0][u_in]} from this preset.")
                                y_n_in = IO_Helpers.yn_inp("Are you sure you want to do this? [Y/N] ").upper()
                                if y_n_in == 'Y':
                                    print("deleting name!")
                                    preset_con['student_names'][0].pop(u_in)
                                    print(f"New list: {preset_con['student_names'][0]}")
                                    print('Taking you back to the deletion main screen')
                                    stu_delete = True
                                    

                                    # Make it so it can detect when changes were made and see if user saved if not ask them to save
                                    # print("Taking you back to the preset editor dont forget to save your changes at the end!")
                                elif y_n_in == "N":
                                    print("No problem taking you back to the deletion menu")
                                    stu_delete = True
                            if u_in == -1:
                                print("Taking you to the student editor menu")
                                return False
                                # stu_delete = False
                                # student_editor = True
                                
                                
                                
                                
                    def edit_choice2():
                        name_edit = True
                        while name_edit == True:
                            print("Welcome to the name edit menu")
                            pre_handle.name_print(preset_con)
                            inp = int(input("Please enter the number that corrispondes to the name you want to change. or type [-1] to go back the the student editor"))
                            if inp in range(len(preset_con['student_names'][0])):
                                print(preset_con['student_names'][0][inp])
                                str_inp = input("Please enter the new name you want")
                                new_name = preset_con['student_names'][0][inp] = str_inp
                                print(f'Student name updated: {new_name}')
                                name_edit = True
                            else:
                                print("No student matches that number")
                                name_edit = True
                            if inp == -1:
                                print("Taking you back to the student editor")
                                # end function 
                                # student_editor = True
                                return False
                                
                    def edit_choice3():
                        bl_main = True
                        while bl_main == True:
                            print("Welcome to the blacklist tab names of students will pop up with numbers next to their names type the number according to the student you want.")
                            pre_handle.name_print(preset_con)
                            n1 = int(input("Enter the number for the first student you want to select or type [-1] to go to the main menu."))
                            if n1 == -1:
                                print("Taking you back to the student editor menu")
                                time.sleep(1)
                                # student_editor = True
                                return False 
                            n2 = int(input("Please enter the second number for the other student you want to blCKLIST or type [-1] to go to the main menu."))
                            if n2 == -1:
                                print("Taking you back to the student editor menu")
                                time.sleep(1)
                                # student_editor = True
                                return False
                            # IO_Helpers.backcheck(n2)
                            
                                

                            elif n1 in range(len(preset_con['student_names'][0])) and n2 in range(len(preset_con['student_names'][0])):
                                print("Good to go")
                                print(f"Are you sure you want to blacklist these 2 students from being in a group together? Students: {preset_con['student_names'][0][n1]}, {preset_con['student_names'][0][n1]}")
                                choice = IO_Helpers.yn_inp("Type Y or N")
                                if choice == "Y":
                                    print("Adding the 2 students to the blacklist")

                                    # Stage 1 split: Splits the pairs of names into the same list
                                    s1_split = preset_con['black_list'].split(', ')
                                    #splits the pairs of names into a list inside the s1 list to give it its own group aka: [['name1', 'name2'], ['name3', 'name4']]
                                    sf_split = [x.split(' ') for x in s1_split]
                                    sf_split.append([preset_con['student_names'][0][n1], preset_con['student_names'][0][n2]])
                                    preset_con.update({'black_list': sf_split})
                                    count = 1
                                    for i in preset_con['black_list']:
                                        print(f"Blacklist group #{count}: {i}")
                                        count += 1
                                    print("Taking you back to the blacklist menu.")
                                    bl_main = True
                                    # print(f"New blacklist: {preset_con['black_list']}")

                                    # print(preset_con['black_list'])
                                elif choice == "N":
                                    print('Sounds good taking you back to the blacklist menu in case you change your mind.')
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
                            print(temp_dict)
                            print("Welcome to the star student section")
                            print("Names will appear with numbers seect the one u want")
                            pre_handle.name_print(preset_con)
                            stu_inp = int(input("Enter number correspodng to tje name u want"))
                            if stu_inp in range(len(preset_con['student_names'][0])):
                                print("Good inp")
                                
                                print("which group wold u like to put this student in?")
                                sg_inp = int(input("[1] = Group 1 (highest group) \n [2] = Group 2 \n [3] = Group 3"))
                                for i in temp_dict.values():
                                     for x in temp_dict.keys():
                                    # print(i)
                                        # print(i,x)
                                        
                                        if preset_con['student_names'][0][stu_inp] in i and preset_con['student_names'][0][stu_inp] in temp_dict[f'{sg_inp}']:
                                            print("Found same")
                                            print( preset_con[f'student_names'][0][stu_inp], f"is already in group: {x}")
                                            print("Taking you back to the star section")
                                            time.sleep(1)
                                            take_back = True
                                            
                                            # not breaking right still going to next function to add to group
                                            break
                                            
                                        
                                            
                                        # Checks if user is in a group already but not the one defined by user 
                                        if preset_con['student_names'][0][stu_inp] in i and preset_con['student_names'][0][stu_inp] not in temp_dict[f'{sg_inp}']:
                                            print('found diff group')
                                            print(f"Students name is already in group {x} would you like to remove them from that group and put them into group {sg_inp}?")
                                            inp = input("Y or N").upper()
                                            
                                            # Need to do:
                                            # fix they y inp as its not appending to the group and just says none. Once thats done break look when moved to another group
                                            # finish the n inp
                                            
                                            
                                            if inp == 'Y':
                                                print(f"Moving {preset_con['student_names'][0][stu_inp]} to group {sg_inp}")
                                                index = temp_dict[f'{x}'].index(preset_con['student_names'][0][stu_inp])
                                                print(index)
                                                temp_dict[f'{x}'].pop(index)
                                                print('popped')
                                                temp_dict[f'{sg_inp}'].append(preset_con['student_names'][0][stu_inp])
                                                print("Added to new group")
                                                print(temp_dict)
                                                take_back = True
                                            elif inp == 'N':
                                                print('not changing anything')
                                                take_back = True
                                            
                                                
                                                # print(temp_dict[f'{x}']
                                
                                if take_back == True:
                                    star_main = True
                                    
                                elif sg_inp == 1:
                                    print(f"are u sure u want to add {preset_con['student_names'][0][stu_inp]} to group 1? ")
                                    yn_in = IO_Helpers.yn_inp("Y or N")
                                    if yn_in == "Y":
                                        print("Adding student to group.")
                                        temp_dict['1'].append(preset_con['student_names'][0][stu_inp])
                                        print('Added name')
                                        temp_pre['amount_changed'] += 1
                                        # print(temp_pre)
                                        # print(temp_dict)
                                        star_main = True
                                        
                                        # to do print name to see if I need to check if they want to star another person
                                elif sg_inp == 2:
                                    print(f"are u sure u want to add {preset_con['student_names'][0][stu_inp]} to group 2? ")
                                    yn_in = IO_Helpers.yn_inp("Y or N")
                                    if yn_in == "Y":
                                        print("Adding student to group.")
                                        temp_dict['2'].append(preset_con['student_names'][0][stu_inp])
                                        print('Added name')
                                        temp_pre['amount_changed'] += 1
                                        print(temp_pre)
                                        print(temp_dict)
                                        star_main = True
                                
                                elif sg_inp == 3:
                                    print(f"are u sure u want to add {preset_con['student_names'][0][stu_inp]} to group 3? ")
                                    yn_in = IO_Helpers.yn_inp("Y or N")
                                    if yn_in == "Y":
                                        print("Adding student to group.")
                                        temp_dict['3'].append(preset_con['student_names'][0][stu_inp])
                                        print('Added name')
                                        temp_pre['amount_changed'] += 1
                                        star_main = True
                            if stu_inp == -1:
                                print("taking yo back to student editor")
                                return False

                                        
                            
                    
                    def bad_inp():
                        print("Sorry that wasnt an option.")
                        # student_editor = True
                    
                    options: dict = {
                        1:edit_choice1,
                        2:edit_choice2,
                        3:edit_choice3,
                        4:edit_choice4
                    }
                    run = options.get(edit_choice, bad_inp)
                    run()
                    if edit_choice == 5:
                        main_editor = True
                        student_editor = False
                        
                    
                    # if edit_choice5() == True:
                    #     print('Taking you back to the editor selector')
                    #     main_editor = True
                    #     student_editor = False
                    # time.sleep(10)
                    
                    # if edit_choice == 1:
                    #     stu_delete = True
                    #     while stu_delete == True:
                            
                    #         print("Welcome to the deletion menu. Names are listed with numbers.")
                    #         pre_handle.name_print(preset_con)
                    #         u_in = int(input("Please enter the number that corrispondes to the name you want to delete. or type [-1] to go back to the student editor"))
                    #         if u_in in range(len(preset_con['student_names'][0])):
                    #             print(preset_con['student_names'][0][u_in])
                    #             IO_Helpers.warning_out(f"You are about to delete the name {preset_con['student_names'][0][u_in]} from this preset.")
                    #             y_n_in = IO_Helpers.yn_inp("Are you sure you want to do this? [Y/N] ").upper()
                    #             if y_n_in == 'Y':
                    #                 print("deleting name!")
                    #                 preset_con['student_names'][0].pop(u_in)
                    #                 print(f"New list: {preset_con['student_names'][0]}")
                    #                 print('Taking you back to the deletion main screen')
                    #                 stu_delete = True
                                    

                    #                 # Make it so it can detect when changes were made and see if user saved if not ask them to save
                    #                 # print("Taking you back to the preset editor dont forget to save your changes at the end!")
                    #             elif y_n_in == "N":
                    #                 print("No problem taking you back to the deletion menu")
                    #                 stu_delete = True
                    #         if u_in == -1:
                    #             print("Taking you to the student editor menu")
                    #             stu_delete = False
                    #             student_editor = True
                                    
                    # # Student name editor                
                    # if edit_choice == 2:
                    #     name_edit = True
                    #     while name_edit == True:
                    #         print("Welcome to the name edit menu")
                    #         pre_handle.name_print(preset_con)
                    #         inp = int(input("Please enter the number that corrispondes to the name you want to change. or type [-1] to go back the the student editor"))
                    #         if inp in range(len(preset_con['student_names'][0])):
                    #             print(preset_con['student_names'][0][inp])
                    #             str_inp = input("Please enter the new name you want")
                    #             new_name = preset_con['student_names'][0][inp] = str_inp
                    #             print(f'Student name updated: {new_name}')
                    #             name_edit = True
                    #         else:
                    #             print("No student matches that number")
                    #             name_edit = True
                    #         if inp == -1:
                    #             print("Taking you back to the student editor")
                    #             student_editor = True
                    #             name_edit = False
                    
                    # # Blacklist students
                    # # ask for 2 numbers aka student names to blacklist then add the pair to a blacklist - list and check when generating if name 1 and name 2 in generated group swap them.
                    # if edit_choice == 3:
                    #     bl_main = True
                    #     while bl_main == True:
                    #         print("Welcome to the blacklist tab names of students will pop up with numbers next to their names type the number according to the student you want.")
                    #         pre_handle.name_print(preset_con)
                    #         n1 = int(input("Enter the number for the first student you want to select or type [-1] to go to the main menu."))
                    #         n2 = int(input("Please enter the second number for the other student you want to blCKLIST or type [-1] to go to the main menu."))
                    #         if n1 == -1 or n2 == -1:
                    #             print("Taking you back to the student editor menu")
                    #             time.sleep(1.5)
                    #             student_editor = True
                    #             bl_main = False
                                

                    #         elif n1 in range(len(preset_con['student_names'][0])) and n2 in range(len(preset_con['student_names'][0])):
                    #             print("Good to go")
                    #             print(f"Are you sure you want to blacklist these 2 students from being in a group together? Students: {preset_con['student_names'][0][n1]}, {preset_con['student_names'][0][n1]}")
                    #             choice = IO_Helpers.yn_inp("Type Y or N")
                    #             if choice == "Y":
                    #                 print("Adding the 2 students to the blacklist")

                    #                 # Stage 1 split: Splits the pairs of names into the same list
                    #                 s1_split = preset_con['black_list'].split(', ')
                    #                 #splits the pairs of names into a list inside the s1 list to give it its own group aka: [['name1', 'name2'], ['name3', 'name4']]
                    #                 sf_split = [x.split(' ') for x in s1_split]
                    #                 sf_split.append([preset_con['student_names'][0][n1], preset_con['student_names'][0][n2]])
                    #                 preset_con.update({'black_list': sf_split})
                    #                 count = 1
                    #                 for i in preset_con['black_list']:
                    #                     print(f"Blacklist group #{count}: {i}")
                    #                     count += 1
                    #                 print("Taking you back to the blacklist menu.")
                    #                 bl_main = True
                    #                 # print(f"New blacklist: {preset_con['black_list']}")

                    #                 # print(preset_con['black_list'])
                    #             elif choice == "N":
                    #                 print('Sounds good taking you back to the blacklist menu in case you change your mind.')
                    #                 bl_main = True
                            
                        

                    # # stared Students
                    # # 3 ranks 1,2,3 
                    # # 1 is the highest 3 is lowest 
                    # #allow person to choose the person and number they want. (not all students need to be stared)
                    # if edit_choice == 4:
                    #     star_main = True
                    #     temp_dict = {'1': [], '2': [], '3': []}
                    #     shesh_changes_made = 0
                    #     while star_main == True:
                    #         print("Welcome to the star student section")
                    #         print("Names will appear with numbers seect the one u want")
                    #         pre_handle.name_print(preset_con)
                    #         stu_inp = int(input("Enter number correspodng to tje name u want"))
                    #         if stu_inp in range(len(preset_con['student_names'][0])):
                            
                    #         # if preset_con['student_names'][0][stu_inp] in temp_dict['1'] or temp_dict['2'] or temp_dict['3']: 
                    #             # for i in temp_dict.values():
                    #             #      for x in temp_dict.keys():
                    #             #     # print(i)
                    #             #         # print(i,x)
                    #             #         if preset_con['student_names'][0][stu_inp] in i:
                    #             #             print(f"Students name is already in group {x} would you like to remove them from that group and put them into group {stu_inp}?")
                    #             #             inp = input("Y or N")
                    #             #             if inp == 'Y':
                    #             #                 print(f"Moving {preset_con['student_names'][0][stu_inp]}")
                    #             #                 print(temp_dict[f'{x}'])

                    #             #             break
                    #             #         if preset_con['student_names'][0][stu_inp] in i and stu_inp == x:
                    #             #             print(x, "name already in group 1")
                                        
                                    
                    #         # if stu_inp in range(len(preset_con['student_names'][0])):
                                
                            
                                    
                    #             print("Good inp")
                                
                    #             print("which group wold u like to put this student in?")
                    #             sg_inp = int(input("[1] = Group 1 (highest group) \n [2] = Group 2 \n [3] = Group 3"))
                    #             for i in temp_dict.values():
                    #                  for x in temp_dict.keys():
                    #                 # print(i)
                    #                     # print(i,x)
                                        
                    #                     if preset_con['student_names'][0][stu_inp] in i and sg_inp == int(x):
                    #                         print( preset_con[f'student_names'][0][stu_inp], "is already in group: {x}")
                    #                         print("Taking you back to the star section")
                    #                         time.sleep(1)
                    #                         star_main = True
                    #                     if preset_con['student_names'][0][stu_inp] in i:
                    #                         print(f"Students name is already in group {x} would you like to remove them from that group and put them into group {sg_inp}?")
                    #                         inp = input("Y or N").upper()
                                            
                    #                         # Need to do:
                    #                         # fix they y inp as its not appending to the group and just says none. Once thats done break look when moved to another group
                    #                         # finish the n inp
                                            
                                            
                    #                         if inp == 'Y':
                    #                             print(f"Moving {preset_con['student_names'][0][stu_inp]} to group {sg_inp}")
                    #                             index = temp_dict[f'{x}'].index(preset_con['student_names'][0][stu_inp])
                    #                             print(index)
                    #                             temp_dict[f'{x}'].pop(index)
                    #                             print('popped')
                    #                             ng = temp_dict[f'{sg_inp}'].append(preset_con['student_names'][0][stu_inp])
                    #                             print("Added to new group")
                    #                             print(ng)
                                                
                    #                             # print(temp_dict[f'{x}'])

                    #                              break
                                        
                                
                    #             if sg_inp == 1:
                    #                 print(f"are u sure u want to add {preset_con['student_names'][0][stu_inp]} to group 1? ")
                    #                 yn_in = IO_Helpers.yn_inp("Y or N")
                    #                 if yn_in == "Y":
                    #                     print("Adding student to group.")
                    #                     temp_dict['1'].append(preset_con['student_names'][0][stu_inp])
                    #                     print('Added name')
                    #                     changes_made['amount_changed'] += 1
                    #                     print(changes_made)
                    #                     print(temp_dict)
                    #                     star_main = True
                                        
                    #                     # to do print name to see if I need to check if they want to star another person
                    #             elif sg_inp == 2:
                    #                 print(f"are u sure u want to add {preset_con['student_names'][0][stu_inp]} to group 2? ")
                    #                 yn_in = IO_Helpers.yn_inp("Y or N")
                    #                 if yn_in == "Y":
                    #                     print("Adding student to group.")
                    #                     temp_dict['2'].append(preset_con['student_names'][0][stu_inp])
                    #                     print('Added name')
                    #                     shesh_changes_made += 1
                    #                     star_main = True
                                
                    #             elif sg_inp == 3:
                    #                 print(f"are u sure u want to add {preset_con['student_names'][0][stu_inp]} to group 3? ")
                    #                 yn_in = IO_Helpers.yn_inp("Y or N")
                    #                 if yn_in == "Y":
                    #                     print("Adding student to group.")
                    #                     temp_dict['3'].append(preset_con['student_names'][0][stu_inp])
                    #                     print('Added name')
                    #                     shesh_changes_made += 1
                    #                     star_main = True
                    #         if stu_inp == -1:
                    #             print("taking yo back to student editor")
                    #             time.sleep(1)

                                    

                    # # back to main screen or whatever
                    # if edit_choice == 5:
                    #     pass
                        
                    #             
                    # if edit_choice == 2:
                    
            # Group Editor        
            if me_choice == 2:
                print("Welcome to the Group editor")
                group_editor = True
                names = preset_con['student_names']
                while group_editor == True:
                    edit_choice  = IO_Helpers.single_inp("[1] = Edit Amount Of Groups \n [6] = Back to editor seletor.")
                    if edit_choice == 1:
                    # Goes to edit amount loop
                        print("Welcome to the group amount changer")
                        num_of_groups = IO_helper.IO_Helpers.single_inp('Please enter the amount of groups you would like.')
                        if pre_handle.g_div(num_of_groups, names) == True:
                            print("Even amount of groups")
                            print("Changes temp applied. Taking you back to the Student editor")
                            group_editor = True
                            
                        else:
                            print("warning the amount of groups you entered will not have even members be warned some groups may contain more students than others.") 
                            temp = []
                            for i in range(1, 100):
                                if num_of_groups % i == 0:
                                    temp.append(i)
                            print(f"These are sum nums you can use that will make an even amount of groups: {temp}")
                            temp.clear()

                            inp = IO_Helpers.yn_inp("Would you like to enter a new number of groups?")
                            if inp == "Y":
                                print('Taking you back to the number enter thing')
                                group_editor == True
                            elif inp == "N":
                                print(f"Sounds good keeping the group num of  {num_of_groups}")
                                # Takes user back to the pre edit
                                group_editor = True
                    elif edit_choice == 2:
                        print("taking you back to the main selection thing")
                        main_editor = True
                        group_editor = False
            
            #Back To Main menu

            if me_choice == 3:
                print("Taking you back to the main menu")
                time.sleep(1)
                return False
                
                        
                
                        
                
                
            
                    
                    
                    
                    
                    # pre_handle.c1(num_of_groups, names)
                    
                

                    
                    
                            
                        


                            
                        
                    # ask for input to either keep it or make it even.

                # send num of groups and student names
                # if ok % num_of_groups != 0:
                #             # ask if they want to redo
                #     print("warning the amount of groups you entered will not have even members be warned some groups may contain more students than others.")
                #     response = input("Would you like to enter a different number of groups? [yes or no]").upper()
                #     if response == 'No':
                #         print('Sounds good taking you back to the main prompt')
                #     if response == 'YES':
                #         print("Sounds good restarting prompt")
                #         c1_running == True
                #     if ok % num_of_groups == 0:
                #             print("Even amount of students for amount of groups you want")
                #     else:
                #         print('everything looks good! Taking you back to the main prompt.')
                #         return 2
                        # option_choice == 2
        # if choice == 2:
        #     running = True
        #     # for x in range(len(preset_con['student_names'][0])):
        #     #     i = preset_con['student_names'][0][x]
        #     #     print('[',x,']', i)
        #     while running == True:
        #         print("Welcome to the name editor please select what you would like to do.")
        #         inp = int(input("[1] - Delete Name \n, [2] - Edit Name \n [3] - Back To Main Menu"))
        #         if inp == 1:
        #             print("Welcome to the deletion menu. Names are listed with numbers.")
        #             pre_handle.name_print(preset_con)
        #             u_in = int(input("Please enter the number that corrispondes to the name you want to delete."))
        #             if u_in in range(len(preset_con['student_names'][0])):
        #                 print(preset_con['student_names'][0][u_in])
        #                 IO_Helpers.warning_out(f"You are about to delete the name {preset_con['student_names'][0][u_in]} from this preset.")
        #                 y_n_in = IO_Helpers.yn_inp("Are you sure you want to do this? [Y/N] ").upper()
        #                 if y_n_in == 'Y':
        #                     print("deleting name!")
        #                     preset_con['student_names'][0].pop(u_in)
        #                     print(f"New list: {preset_con['student_names'][0]}")
        #                     changes_made

        #                     # Make it so it can detect when changes were made and see if user saved if not ask them to save
        #                     print("Taking you back to the preset editor dont forget to save your changes at the end!")
        #                 elif y_n_in == "N":
        #                     print("No problem taking you back to the Deletion menu")



            

             
        #         elif inp == 2:
        #             pass



                

                # else:
                #     break
            
                






    def save_preset():
        pass



class login_main():
    def weclome():
        print("welcome please type 1 or 2")
        welc_in = int(input())
        return welc_in

    def log_in(welc_in):
        if welc_in == 1:
            print("taking you to google login.")
            config.update({'logged_in': True})

        if welc_in == 2:
            print("taking you into the program")
            config.update({'logged_in': False})

class Main_2():

    # def main_welc():
    
        # if there are logged in give them more options and what no
        
        # if config['logged_in'] == True:
        #     print('Welcome to the main program.')
        #     print("Options:", '\n')
        #     print('[1] = ')
        
        # # if there are not logged in give them limited options.
        
        
        # else:
        #    print('Welcome to the main program.') 
        #    print("Options:", '\n')
        #    print('[1] = Create a list of names yourself. \n, [2] = goto group creator')
        #    user_in = int(input('enter the numbers you see'))
        #    return user_in

        
    def main_welc():
        
        print('welcome to the group creator!')
        print('You will be given some options in order to make this the best for you')
        time.sleep(0.1)
        preset_in = str(input("Would you like to use a preset? (yes or no)")).upper()
        if preset_in == "YES":
            time.sleep(.2)
            presets.import_pre()
            main_running = True
            while main_running == True:
                print('welcome to the program you have loaded a preset please choose what you would like to do next.')
                option_choice = int(input("[1] = Start generating groups \n[2] = Edit preset"))
                if option_choice == 1:
                    print("generating groups based off of loaded preset please wait")

                    # create a generator function and call it here with all data needed

                
                if option_choice == 2:
                    a = presets.edit_pre()
                    option_choice = a
                else:
                    main_running = True


        if preset_in == "NO":
            print("Sounds good not using a preset")
            pass

        
        
   
    # def name_file_create():
    #     names = input("Enter")
       
    #     # Instead of splitting use re
    #     ok = names.split(', ')
    #     if re.search(', ', names) != None:
    #         print('matched something')
    #     if re.search(' ', names) != None:
    #         print('FOUND SPACE ONLY')
    #     else:
    #         print("no sir")
    #     print(ok)
    #     to_use = '\n'.join(ok)
    #     print(to_use)
    #     with open('group_names.txt', 'a') as f:
    #         f.write(to_use)
    #         print('created a new file with names listed please use this file when asked in the dialouge')


           


       
   
    # def file_in():
    #     u_in = filedialog.askopenfilename()
    #     return u_in
   
    # def read(file_name):
    #     if re.search('.txt', file_name):
    #         with open(file_name, 'r') as read_file:
    #             a = read_file.readlines()
    #             test = []
    #             for i in a:
    #                 print(len(i))
    #                 b = i.split()
    #                 test.append(b)
    #             print(test)
               
               
           
    #     if re.search('.csv', file_name):
    #         with csv(file_name, 'r') as read_file:
    #             print(read_file)
           
Main_2.main_welc()
# file_name = Main.file_in()
# Main.read(file_name)



