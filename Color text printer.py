import colorama
from colorama import Back, Fore

# Back is used to change the background colour of the text. while fore changes color of txt

colorama.init(autoreset=True)  # Will reset the colours back to normal after the execution is over

text = input("Type your sentence here: ")
print(Fore.RED + Back.BLUE + text)
print(Fore.BLACK + Back.WHITE + text)
print(Fore.GREEN + Back.MAGENTA + text)
print(Fore.YELLOW + Back.BLUE + text)
print(Fore.BLUE + Back.YELLOW + text)
print(Fore.MAGENTA + Back.GREEN + text)
print(Fore.CYAN + Back.RED + text)
print(Fore.WHITE + Back.BLACK + text)
