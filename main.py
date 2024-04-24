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
    
try:
    if get_os()=="Windows":
        os.system("pip uninstall urllib3 -y &&  pip install urllib3")
        os.system("python assest\\windows\\main.py")
    elif get_os()=="Linux":
        os.system("python assest/linux/main.py")
    elif get_os()=="Termux":
        os.system("python assest/linux/main.py")
    else:
        print("OS not supported..")
except:
    print("Soon we will create tool for your system")