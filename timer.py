import time


def timer_func(queue_packet, queue_count_done):
    while True:
        counter = 0
        if queue_packet.get():
            while queue_packet.empty():
                time.sleep(1)
                counter += 1
                if counter > 60:
                    queue_count_done.put(True)
                    break
