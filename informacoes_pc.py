import wmi   # Windows Management Instrumentation
import os

os.system('cls')

# Carrega informações
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

# Mostra resultados
print()
print(f'Marca: {my_system.Manufacturer}')
print(f'Modelo: {my_system.Model}')
print(f'Nome: {my_system.Name}')
print(f'Qtde CPUs: {my_system.NumberOfProcessors}')
print(f'Arquitetura: {my_system.SystemType}')
print(f'Família: {my_system.SystemFamily}')
print()

# # fornece a percentagem de disco livre
# for disk in c.Win32_LogicalDisk(DriveType=3):
#     print(disk.Caption, "%0.2f%% free" % (100.0 * float((disk.FreeSpace)) / float((disk.Size))))

# # lista todos os processos em execução
# for process in c.Win32_Process():
#   print(process.ProcessId, process.Name)

# # mostra as partições do disco
# for physical_disk in c.Win32_DiskDrive():
#   for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
#     for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
#       print('Disco físico:', physical_disk.Caption, '\nPartição:', partition.Caption, '\nDisco lógico:', logical_disk.Caption)

# # mostra todos os serviços automáticos que não estão em execução
# stopped_services = c.Win32_Service(StartMode="Auto", State="Stopped")
# if stopped_services:
#   for s in stopped_services:
#     print(s.Caption, "service is not running")
# else:
#   print("No auto services stopped")

# # mostra a lista de IP e MAC address
# for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
#   print('Descrição interface:', interface.Description, '\nMACAddress:', interface.MACAddress)
#   for ip_address in interface.IPAddress:
#     print('\nEndereço IP:', ip_address)
#   print

# # o que está rodando na inicialização
# for s in c.Win32_StartupCommand ():
#   print("\nLocal: [%s] \nNome: %s \nComando: <%s>" % (s.Location, s.Caption, s.Command))

# # mostra os drives compartilhados
# for share in c.Win32_Share():
#   print('Nome:', share.Name, '\nDiretório:', share.Path)

# # encontra os tipos de drive
# DRIVE_TYPES = {
#   0 : "Unknown",
#   1 : "No Root Directory",
#   2 : "Removable Disk",
#   3 : "Local Disk",
#   4 : "Network Drive",
#   5 : "Compact Disc",
#   6 : "RAM Disk"
# }

# for drive in c.Win32_LogicalDisk():
#   print('Nome:', drive.Caption, '\nTipo:', DRIVE_TYPES[drive.DriveType])