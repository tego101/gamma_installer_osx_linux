import os, subprocess, time

os.system('clear')
print('\n')
print('########################################################')
print('#   ###########################                        #')
print('#   http://github.com/tego101                          #')
print('#   ####################################               #')
print('#   # IF THIS HELPED, PLEASE DONATE :) #               #')
print('#   ####################################               #')
print('#   BITCOIN -> 1KouUcQ7o4rVh8gTg6W3HPUDsBBdoC6G1K      #')
print('#   CASHAPP -> $redtvme                                #')
print('########################################################')
print('(C) FASTCOMMWW@protonmail.com')
print('\n')

print('\n')
os.system('adb disconnect')
print('\n')
#   Questions
question_ip = 'Please Enter the LOCAL IP ADDRESS: '
question_model = 'Please Enter the MODAL (4k, FIRE TV, ANDROID): '
#   Firesitck Properties.
#   @model, @ip
firestick = {
    'ip': question_ip,
    'model': question_model 
}

class GAMMA:
    def do_install():
        time.sleep(1)
        fsip = input(question_ip)
        print('\n')

        try:
            os.system('adb connect {ip}'.format(ip=fsip))
        except:
            print('ox_x')

        print('\n')
        print('==================>>>> Authorizing... \n')
        print('\a')
        print('\n Select ALWAYS ALLOW FROM THIS COMPUTER and ALLOW/ACCEPT/OK \n')
        time.sleep(1)
        input('\n Press ENTER to continue....')
        time.sleep(1)        
        print('==================>>>> Connecting...') 
        print('\a')   

        try:
            os.system('adb connect {ip}'.format(ip=fsip))
            os.system('adb devices')
        except:
            print('ox_x')

        time.sleep(1)
        print('==================>>>> Installing Launcher.')
        print('\a')
        try:
            os.system('adb install launcher.apk')
        except:
            print('ox_x')    
        time.sleep(1)
        print('==================>>>> Installing AUTO launcher.')
        print('\a')
        try:
            os.system('adb install launchx.apk')
        except:
            print('ox_x')           
        time.sleep(1)
        print('==================>>>> Uploading data payload (BACKGROUND, Launcher Settings).')
        print('\a')
        print('\a')
        try:
            os.system('adb push gamma.jpg /storage/emulated/0/Download/')
            os.system('adb push TV_LAUNCHER_BACKUP.ttv2 /storage/emulated/0/Download/')
        except:
            print('ox_x')           
        time.sleep(1)
        os.system('clear')
        print('\a')
        print('\n OPEN TVLauncher')
        print('\n ** OK now go into the settings in the launcher and restore the back up file. \n')
        print('\n ** PRESS DOWN HIT THE TV LAUNCHER icon select import settings')
        print('\n They are located in =======> /Download \n')
        print('\n')
        input('PRESS ENTER when you did that...')
        os.system('clear')
        print('Now we are going to set the permissions to the autolauncher.')
        print('Open another window and type adb connect {ip}'.format(ip=fsip) + '\n')
        print('\n Next type -> adb shell')
        print('\n Next type -> pm grant de.codefaktor.ftvlaunchx android.permission.WRITE_SECURE_SETTINGS')
        print('\n Next type -> settings put secure enabled_accessibility_services de.codefaktor.ftvlaunchx/de.codefaktor.ftvlaunchx.HomeService')
        print('\n Next type -> exit')
        input('PRESS ENTER to finish')
        print('\n Next open LaunchX')
        print('\n In the center menu select TVLauncher as the app you want to auto launch.')
        print('\n Lets Test this!')
        print('\n Then, REBOOT your firestick ---> settings --> device ---> REBOOT \n')
        time.sleep(1)
        input('\n Press ENTER to continue when you\'re DONE....')
        time.sleep(1)        
        print('==================>>>> ALL SET BOSS!!! ')
        time.sleep(1)        
        print('PEACE!')

    #   Prefix for installing gamma. 
    #   Welcome Screen, ETC.
    def start_install_gamma():
        fsm = input(question_model)
        if str(fsm):
            GAMMA.do_install()
        else:
            os.system('clear')
            print('======> You didn\'t select anything! <======')
            retry = input('\n Try again yes/no: ')

            if 'yes' in retry:
                os.system('clear')
                GAMMA.start_install_gamma()

GAMMA.start_install_gamma()
