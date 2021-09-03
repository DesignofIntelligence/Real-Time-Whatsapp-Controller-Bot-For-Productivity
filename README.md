# Real-Time-Whatsapp-Controller-Bot-For-Productivity

A software that controls the number of times per hour whatsapp could be opened.

The software has 3 main modules running in parallel threads, The first module (packet_scapy_sniff.py) is a packet sniffer that detects the IP address of whatsapp in the incoming/outgoing packets. 
If whatsapp was detected, a semaphore is sent to the second module, which is a counter that starts counting 60 seconds. Everytime the first module sends the semaphore, the counting gets restarted, so that the 60 seconds are counted after the last packet was sent/ received to make sure that whatsapp was closed.
After the count is finished, a semaphore is sent to the third module, which decrements a counter(responsible for the number of times whatsapp could be opened in an hour), checks if the counter was 0, if so then it calls a function that creates firewall blocks. if an hour mark is passed, the counter gets restarted by this module.


