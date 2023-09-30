import time, os, random
from core.IO_helper import IO_Helpers 




class pre_handle():
    def g_div(num_of_groups, names):
            c1_running = True
            if len(names) % num_of_groups != 0:
                # ask if they want to redo
                return False
            elif len(names) % num_of_groups == 0:
                return True
            
    def get_presets(pre_path):
        pre_in_running = True
        preset_files = []
        while pre_in_running == True:
            
            for pre in os.listdir(pre_path):
                if pre.endswith('.ini'):
                    preset_files.append(pre)
            IO_Helpers.print_info("please select the config file you would like to use")
            for i in range(len(preset_files)):
                x = preset_files[i]
                IO_Helpers.print_info(f'[{i}], {x}')
                return preset_files
                
                
        
                
                
    # Put into IO helpers
    def name_print(preset_con):
        for x in range(len(preset_con['student_names'])):
                i = preset_con['student_names'][x]
                IO_Helpers.print_info('[',x,']', i)
                
    
class gen_help():   
    def bl_check(preset, ran_name, temp_check, num_per, names):
        for u in range(len(preset['black_list'])):
                            for q,p in preset['black_list'][u]:
                                work_names = names.copy()
                                if q in temp_check and p == ran_name:
                                    # print(f"found blacklisted names in group (first check) {q, p}")
                                    # print("getting a new name to comply with the blacklist")
                                    return False
                                elif q == ran_name and p in temp_check:
                                    # print(f"found blacklisted names in group (second check) {q, p}") 
                                    # print("getting a new name to comply with the blacklist")
                                    return False
                                index = work_names.index(ran_name)
                                work_names.pop(index)
                                if len(temp_check) >= 1 and q in work_names and p in work_names:
                                    # print("The remaining names cant be put into a list due to them being apart of a black list getting a new name now")
                                    return False
                                else:
                                    return True 
    def stared_check(preset, ran_name, temp_check, num_per):
        check = True
        star_1_per = round(num_per * 0.25)
        star_2_per = round(num_per * 0.30)
        star_3_per = round(num_per * 0.50)
        total_star = len(preset['stared']['1']) + len(preset['stared']['2']) + len(preset['stared']['3'])
        num_of_groups = int(preset['num_of_groups'])
        
        while check:
            if star_1_per + star_2_per + star_3_per > num_per:
                # print("Asking for too many stars due to a rounding issue removing ")
                if star_1_per > 1:
                    star_1_per - 1
                    check = False
                else:
                    if star_2_per > 1:
                       star_2_per - 1
                       check = False
                    else:
                        if star_3_per > 1:
                            star_3_per - 1
                            check = False
            else:
                check = False
                
                
        star_1_count = 0
        star_2_count = 0
        star_3_count = 0
            
        # looping through list but once it finds the name thats already a star it runs need a way to count the names in the group without it running with the first name    
            
        for i in temp_check:
            # print(i, "printed i")
            # time.sleep(3)
            if i in preset['stared']['1']:
                star_1_count += 1
                # print("Name is from star 1")
            elif i in preset['stared']['2']:
                star_2_count += 1 
                # print('name in star 2 ')
            elif i in preset['stared']['3']:
                star_3_count += 1
                # print('name in star 3')
            else:
                pass
                # print("Name is not in a star group")
            
        
        # Done [More can be done to it]
        if total_star < num_of_groups:
            # print("Not enough stars to fill each group with atleast one stared name Note:(One group will have all non-stared students due to this)")
            
            if ran_name in preset['stared']['1']:
                if star_1_per < 1:
                    # print("Dont need a star one in group but since its needed adding to group [DEBUG]")
                    return True
                
                elif star_1_count == star_1_per:
                    # print("Have enough star [1] already skipping and getting a new name")
                    return False
                
            elif ran_name in preset['stared']['2']:
                if star_2_count == star_2_per:
                    # print("Have enough star [2] already skipping and getting a new name")
                    return False
            elif ran_name in preset['stared']['3']:
                if star_3_count == star_3_per:
                    # print("Have enough star [3] already skipping and getting a new name")
                    return False
            else:
                # print("Name is not in a star group adding them to group")
                return True
            # elif ran_name not in preset['stared']['1'] and ran_name not in preset['stared']['1'] and ran_name not in preset['stared']['1'] and star_1_count == 0 and star_2_count == 0 and star_3_count == 0:
            #     print()
        
            
            
            
            
        # Done working fine [Best working I think ]
        elif total_star == num_of_groups:
           
            if ran_name in preset['stared']['1'] or ran_name in preset['stared']['2'] or ran_name in preset['stared']['3']:
                # print("Ran name is in a star group")
                ran_star = True
            else:
                # print('ran name is not in a star group')
                ran_star = False
            for i in temp_check:
                if i in preset['stared']['1'] or i in preset['stared']['2'] or i in preset['stared']['3']:
                    # print("Group already has a stared name")
                    if ran_star == True:

                        # print("Since there is only enough names to put one star in each group skipping the name and getting a non stared name. [DEBUG]")
                        # print(ran_name)
                        # time.sleep(3)
                        return False
                elif i not in preset['stared']['1'] or i not in preset['stared']['2'] or i not in preset['stared']['3']:
                    # print("group dosnt have star")
                # if len(temp_check) == num_per - 1 and star_1_count == 0 and star_2_count == 0 and star_3_count == 0 and ran_star == False:
                    if ran_star == False:
                        # print("Since there is enough star names for each group and this group is about to be filled with no star names skipping and getting a star name [DEBUG]")
                        # print(ran_name)
                        # time.sleep(5)
                        return False
                else:
                    # print('looks good [DEBUG]')
                    return True
          
            # if ran_name not in preset['stared']['1'] and ran_name not in preset['stared']['2'] and ran_name not in preset['stared']['3']:
            #   print("Chosen name was not asigned to a star group adding them to the group and counting their value as a 3")
            #   if star_3_count < star_3_per:
            #       return True
            #   else:
            #       print("Already have enought threes this name will be counted as a 2 instead [DEBUG]")
            #       if star_2_count < star_2_per:
            #           return True
            #       else:
            #           print("Already have enought two's this user will not be added to the group and will be put into another [DEBUG]")
            #           return False
                    
        # Done working fine finished 9/12/23
        elif total_star == num_per * num_of_groups:
            # print("group will be filled with only star names [DEBUG]")
            
            if ran_name in preset['stared']['1']:
                
                if star_1_per < 1:
                    # print("Dont need a star one in group but since its needed adding to group [DEBUG]")
                    return True
                
                elif star_1_count == star_1_per:
                    # print("Have enough star [1] already skipping and getting a new name")
                    return False
                
                    
            elif ran_name in preset['stared']['2']:
                if star_2_count == star_2_per:
                    # print("Have enough star [2] already skipping and getting a new name")
                    return False
            elif ran_name in preset['stared']['3']:
                if star_3_count == star_3_per:
                    # print("Have enough star [3] already skipping and getting a new name")
                    return False
            else:
                # print("Name is not in star grouup somehow")
                return False

         # Done [More can be added and optimized] like counting no star names as certain star # or something     finished 9/12/23
        elif total_star > num_of_groups:
            # print("There are more stared names than groups. Making groups as fair as possible.")
        
            if ran_name in preset['stared']['1']:
                if star_1_per < 1:
                    # print("Dont need a star one in group but since its needed adding to group [DEBUG]")
                    return True
                    
                elif star_1_count == star_1_per:
                    # print("Have enough star [1] already skipping and getting a new name")
                    return False
                
            elif ran_name in preset['stared']['2']:
                if star_2_count == star_2_per:
                    # print("Have enough star [2] already skipping and getting a new name")
                    return False
            elif ran_name in preset['stared']['3']:
                if star_3_count == star_3_per:
                    # print("Have enough star [3] already skipping and getting a new name")
                    return False
            else:
                # print("Name is not in a star group adding them to group")
                return True
           