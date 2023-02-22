from datetime import datetime
import os

os.system('cls')

now = datetime.now()

print("Data atual:", now.strftime("%d/%m/%Y"), '\n')
print("Hora atual:", now.strftime("%H:%M:%S"), '\n')