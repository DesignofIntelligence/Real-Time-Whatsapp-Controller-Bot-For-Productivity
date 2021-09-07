import psutil
import os


def get_pid(name):
    for proc in psutil.process_iter():
        if name in proc.name():
            pid = proc.pid
    return pid


def whatsapp_process_opened():
    if "WhatsApp.exe" in [x.name() for x in psutil.process_iter()]:
        return True
    else:
        return False


def kill_whatsapp_process():
    pid = get_pid("WhatsApp.exe")
    p = psutil.Process(pid)
    print("Closing")
    p.terminate()


def helper_check():
    if "helper.exe" not in [x.name() for x in psutil.process_iter()]:
        os.system('shutdown -s')
