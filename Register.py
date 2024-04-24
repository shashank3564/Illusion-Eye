import platform
import os
def get_os():
    if platform.system() == "Linux":
        if os.path.exists('/data/data/com.termux'):
            return "Termux"
        else:
            return "Linux"
    elif platform.system() == "Windows":
        return "Windows"
    else:
        return "Unknown OS"  
    

if get_os()=="Windows":
    os.system("pip uninstall urllib3 -y &&  pip install urllib3")
    os.system("python assest\\windows\\register.py")
elif get_os()=="Linux":
    os.system("python assest/linux/register.py")
elif get_os()=="Termux":
    os.system("python assest/linux/register.py")
else:
    print("OS not supported..")
