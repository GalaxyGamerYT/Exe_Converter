import PyInstaller.__main__ as py
from os import rmdir, remove, listdir, system, path, rename, getcwd
from time import sleep
from colorama import Fore, init

init(autoreset=True)

def clear():
    system("cls")

def main():
    run = True
    iconRun = True

    while run:
        while run:
            clear()
            print(Fore.BLUE+"Name of file to convert:")
            file = input()+".py"
            if path.isfile(file):
                sleep(0.5)
                while run:
                    clear()
                    print(Fore.BLUE+"Window or Console:")
                    type = (input().lower())[0]
                    if type == "w" or type == "c":
                        sleep(0.5)
                        clear()
                        print(Fore.BLUE+"Exe file name:")    
                        name = input()
                        
                        sleep(0.5)
                        while iconRun:
                            clear()
                            print(Fore.BLUE+"Do you have an icon image?[y/n]")
                            icon = (input().lower())[0]
                            if icon == "y":
                                while iconRun:
                                    clear()
                                    print(Fore.BLUE+"Path of the .ico icon file:")
                                    icon = input()
                                    if path.isfile(icon):
                                        py_args = [file, '--onefile', '--clean', f"-{type}", f"-n{name}", f"--icon {icon}"]
                                        iconRun = False
                                    else:
                                        print(Fore.RED+icon+" doesn't exist")
                                        sleep(1)
                            elif icon == "n":
                                py_args = [file, '--onefile', '--clean', f"-{type}", f"-n{name}"]
                                iconRun = False
                            else:
                                print(Fore.RED+icon+" isn't an option")
                                sleep(1)
                        
                        sleep(0.5)
                        clear()
                        print(Fore.MAGENTA+"Making EXE file")
                        sleep(0.5)
                        
                        py.run(py_args)
                        
                        clear()
                        print(Fore.MAGENTA+"EXE file made")
                        sleep(0.25)
                        
                        content = listdir(f"build\\{name}")
                        for f in content:
                            remove(f"build\\{name}\\{f}")
                        rmdir(f"build\\{name}")
                        rmdir("build")
                        remove(f"{name}.spec")
                        
                        sleep(0.25)
                        print(Fore.MAGENTA+"extra files removed")
                        
                        sleep(0.25)
                        print(Fore.MAGENTA+"Moving Exe file to current working directory")
                        rename(f"{getcwd()}\\dist\\{name}.exe", f"{getcwd()}\\{name}.exe")
                        rmdir(f"{getcwd()}\\dist")
                        
                        sleep(0.5)
                        clear()
                        print(Fore.GREEN+"\n\n--Done--")
                        run = False
                    else:
                        print(Fore.RED+type+" Isn't an option")
                        sleep(1)
            else:
                print(Fore.RED+file+" Doesn't exist")
                sleep(1)

if __name__ == "__main__":
    main()
