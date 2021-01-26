import os

os.system('pip3 install -r requirements.txt')


def setting_sleep_watcher():
    try:
        os.system('sudo rm -rf /Library/StartupItems/SleepWatcher')
        os.system('sudo cp ./sleepwatcher_2.2.1/sleepwatcher /usr/local/sbin')
        os.system(
            'sudo cp ./sleepwatcher_2.2.1/sleepwatcher.8 /usr/local/share/man/man8')
        os.system('sudo cp ./sleepwatcher_2.2.1/config/de.bernhard-baehr.sleepwatcher-20compatibility.plist /Library/LaunchDaemons/de.bernhard-baehr.sleepwatcher.plist')
        os.system('sudo cp ./sleepwatcher_2.2.1/config/rc.* /etc')
        os.system(
            'sudo launchctl load /Library/LaunchDaemons/de.bernhard-baehr.sleepwatcher.plist')
    except Exception as e:
        print(e)


def train():
    try:
        os.system('python3 ./train_dataset_getter.py')
        os.system('python3 ./train_LBPH.py')
    except Exception as e:
        print(e)


setting_sleep_watcher()
train()
