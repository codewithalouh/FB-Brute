import colors
from colorama import Fore, Style

c = colors


logo = f"""

  ______ ____    _____  _     _     _               
 |  ____|  _ \  |  __ \| |   (_)   | |              
 | |__  | |_) | | |__) | |__  _ ___| |__   ___ _ __ 
 |  __| |  _ <  |  ___/| '_ \| / __| '_ \ / _ \ '__|
 | |    | |_) | | |    | | | | \__ \ | | |  __/ |   
 |_|    |____/  |_|    |_| |_|_|___/_| |_|\___|_|   
                                                    
                                                    
                    
                          {c.c + "Author: "+c.y+"Alouh Sperk | PH.PHOENIX"}                                                                                                                                   
"""


def banner():
    print(c.ran + logo)
    print(c.ran + '-' * 65)
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/codewithalouh/ ", "- " * 3+c.ran + "|")
    print(c.ran + '-' * 65)







