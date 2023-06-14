import rich
from rich.console import Console
import random
from core.IO_helper import IO_Helpers as i_help



class pre_handle():
    def g_div(num_of_groups, names):
            c1_running = True
            if names % num_of_groups != 0:
                # ask if they want to redo
                return False
            elif names % num_of_groups == 0:
                return True
                    # response = i_help.yn_inp("Would you like to enter a different number of groups? [Y for yes or N for no]")
                    # # will be used for a check either in a func or just here
                    # if len(response) != 1:
                    #     print("please only enter y or n")

                    # if response == 'N':
                    #     print('Sounds good taking you back to the main prompt')
                    #     return False
                    # if response == 'Y':
                    #     print("Sounds good restarting prompt")
                    #     c1_running == True
                    # if names % num_of_groups == 0:
                    #         print("Even amount of students for amount of groups you want")
                    # else:
                    #     print('everything looks good! Taking you back to the main prompt.')
                    #     return True
                        # option_choice == 

    def name_print(preset_con):
        for x in range(len(preset_con['student_names'][0])):
                i = preset_con['student_names'][0][x]
                print('[',x,']', i)

    def pre_save(*changes):
        with open(r'database\all_pre.json', 'a') as wrt_to:
            pass
            
    def all_pre_read():
        pass


    # def change_check():
        