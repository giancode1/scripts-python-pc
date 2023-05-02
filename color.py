print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color
print('asdasdasd') 

from colorama import Fore, Style

# Mensaje en rojo
print(f"{Fore.RED}Este es un mensaje en rojo{Style.RESET_ALL}")

# Mensaje en verde
print(f"{Fore.GREEN}Este es un mensaje en verde{Style.RESET_ALL}")

print("mensaje normal")
