#!/usr/bin/python

import os
func_done = False

while func_done is False:
    print("Welcome to Nitrogen Linux!")
    print("Would you like to (I)nstall (R)epair or enter (S)hell", end=" ")

    option = input()
    if option == "i":
        os.system("nitrogen-install")
        func_done = True
    elif option == "r":
        print("Select disk that Nitrogen has been installed on: ")
        os.system("lsblk -d")
        disk = input("disk: ")
        os.system("lsblk /dev/" + disk)
        print("root partition:")
        root = input("/dev/" + disk)
        os.system("mount /dev/" + disk + "/" + root + " /mnt")
        print("Chroot into it?")
        chroot = input("y/n ")
        if chroot == "y":
            os.system("arch-chroot /mnt")
            print("Would you like to reboot?")
            reboot = input("y/n ")
            if reboot == "y":
                os.system("reboot")
            else:
                func_done = True
                pass
        else:
            func_done = True
            pass

    elif option == "s":
        func_done = True
        pass
    else:
        print("Nitrogen ISO: " + option + ": command not found")