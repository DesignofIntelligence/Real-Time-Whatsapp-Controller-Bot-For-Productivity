import os
def kill_whatsapp_connection():
    os.system("netsh advfirewall firewall add rule name=\"BLOCK Whatsapp\" dir=in action=block remoteip=102.132.97.54")
    os.system("netsh advfirewall firewall add rule name=\"BLOCK Whatsapp\" dir=out action=block remoteip=102.132.97.54")
    return False  # whatsapp alive is false


def resurrect_whatsapp_connection():
    os.system("netsh advfirewall firewall delete rule name=\"BLOCK Whatsapp\" dir=in")
    os.system("netsh advfirewall firewall delete rule name=\"BLOCK Whatsapp\" dir=out")
    return True  # whatsapp alive is false
