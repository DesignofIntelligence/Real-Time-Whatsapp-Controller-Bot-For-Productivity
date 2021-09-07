from scapy.all import *
import time
from functools import partial
from notifier import notify

def print_summary(whatsapp_detected, pkt):
    if (pkt["IP"].src == "102.132.97.54") or (pkt["IP"].dst == "102.132.97.54"):
        whatsapp_detected[0] = True


def packet_sniff(out_q):
    while True:
        time.sleep(0.4)
        whatsapp_detected = [False]
        sniff(filter="tcp", prn=partial(print_summary, whatsapp_detected), timeout=0.1, store=0)
        if whatsapp_detected[0] and out_q.empty():
            try:
                notify("Whatsapp Opened", "Make it quick")
            except:
                pass
            out_q.put(True)
