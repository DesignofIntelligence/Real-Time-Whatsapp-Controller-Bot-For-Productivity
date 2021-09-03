from firewall_functions import *
from datetime import datetime
from time import sleep


def whatsapp_controller(queue_count_done, notifier):
    counter = 2
    resurrect_whatsapp_connection()
    whatsapp_alive = True
    timer_expired = False
    while 1:
        sleep(2)
        print("whatsapp controller working")
        # helper_check()
        try:
            timer_expired = queue_count_done.get(timeout=1)
        except:
            pass

        if timer_expired:
            counter -= 1
            timer_expired = False
            notifier.show_toast("Whatsapp closed", str(counter) + " Time(s) remaining")

        if counter == 0 and whatsapp_alive:
            whatsapp_alive = kill_whatsapp_connection()

        if datetime.now().minute == 59:
            counter = 2
            whatsapp_alive = resurrect_whatsapp_connection()
