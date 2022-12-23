import os
import sys
import shutil
import cursor

cursor.hide()

class bcolors:
    OKBLACK = '\033[30m'
    OKPURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKGOLD = '\033[93m'
    OKBROWN = '\033[33m'
    OKRED = '\033[91m'
    OKWHITE = '\033[37m'
    BKWHITE = '\033[47m'
    OKSNOW = '\033[37m\033[47m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    if len(sys.argv) < 2:
         OKXMAS = '\033[37m\033[40m'
    elif sys.argv[1].lower() == 'show':
         OKXMAS = '\033[37m\033[40m'
    elif sys.argv[1].lower() == 'hide':
         OKXMAS = OKBLACK
    else:
         OKXMAS = '\033[37m\033[40m'

cols = shutil.get_terminal_size().columns

def start():

	xtree = f'''

                    {bcolors.OKGOLD}@{bcolors.ENDC}
                    {bcolors.OKGREEN}*{bcolors.ENDC}
                   {bcolors.OKGREEN}***{bcolors.ENDC}
                  {bcolors.OKGREEN}**{bcolors.OKRED}o{bcolors.OKGREEN}**{bcolors.ENDC}
                 {bcolors.OKGREEN}*****{bcolors.OKBLUE}o{bcolors.OKGREEN}*{bcolors.ENDC}
                {bcolors.OKGREEN}*********{bcolors.ENDC}              {bcolors.OKXMAS}HAPPY HOLIDAYS!!!{bcolors.ENDC}
               {bcolors.OKGREEN}**{bcolors.OKGOLD}o{bcolors.OKGREEN}***{bcolors.OKRED}o{bcolors.OKGREEN}****{bcolors.ENDC}                   {bcolors.OKXMAS}from{bcolors.ENDC}
              {bcolors.OKGREEN}*************{bcolors.ENDC}       {bcolors.OKXMAS}Tramell Software Development{bcolors.ENDC}      
             {bcolors.OKGREEN}**{bcolors.OKPURPLE}o{bcolors.OKGREEN}******{bcolors.OKRED}o{bcolors.OKGREEN}*****{bcolors.ENDC}
            {bcolors.OKGREEN}******{bcolors.OKGOLD}o{bcolors.OKGREEN}*******{bcolors.OKPURPLE}o{bcolors.OKGREEN}**{bcolors.ENDC}
           {bcolors.OKGREEN}************{bcolors.OKBLUE}o{bcolors.OKGREEN}******{bcolors.ENDC}
          {bcolors.OKGREEN}***{bcolors.OKRED}o{bcolors.OKGREEN}*************{bcolors.OKGOLD}o{bcolors.OKGREEN}***{bcolors.ENDC}
                   {bcolors.OKBROWN}###{bcolors.ENDC}
                   {bcolors.OKBROWN}###{bcolors.ENDC}
                   {bcolors.OKBROWN}###{bcolors.ENDC}
{bcolors.OKSNOW}========================================================================{bcolors.ENDC}'''

	os.system('clear')
	print(f'{xtree}'.center(cols))
	input();os.system('clear')

start()