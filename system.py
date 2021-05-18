# windows management instrumentation
import wmi
c=wmi.WMI()
my_system=c.win32_computerSystem()[0]
print(f"Manufacturer:{my_system.Manufacturer}")
print(f"Model:{my_system.Model}")
print(f"Name:{my_system.Name}")
print(f"Number of processors:{my_system.Numberofprocessors}")
print(f"System type:{my_system.systemType}")
print(f"system family:{my_system.systemfamily}")

