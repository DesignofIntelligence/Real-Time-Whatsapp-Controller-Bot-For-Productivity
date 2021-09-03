import time


def timer_func(queue_packet, queue_count_done):
    while True:
        counter = 0
        if queue_packet.get():
            print("Whatsapp opened")
            while queue_packet.empty():
                time.sleep(1)
                counter += 1
                print(counter)
                if counter > 3:
                    queue_count_done.put(True)
                    break
