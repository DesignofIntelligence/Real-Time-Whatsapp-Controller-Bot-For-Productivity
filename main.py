from threading import Thread
from queue import Queue
from whatsapp_controller import *
from packet_scapy_sniff import packet_sniff
from timer import timer_func
#from win10toast import ToastNotifier

if __name__ == "__main__":
    # sleep(60)
    #notifier = ToastNotifier()
    q_packet_detector = Queue(maxsize=1)
    q_timer = Queue(maxsize=1)
    whatsapp_detector = Thread(target=packet_sniff, args=(q_packet_detector,))
    whatsapp_controller = Thread(target=whatsapp_controller, args=(q_timer, ))
    timer = Thread(target=timer_func, args=(q_packet_detector, q_timer))
    whatsapp_controller.start()
    whatsapp_detector.start()
    timer.start()
    whatsapp_detector.join()
    print("thread finished...exiting")
