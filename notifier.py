from win10toast import ToastNotifier


def notify(title, description):
    notifier = ToastNotifier()
    try:
        notifier.show_toast(title, description)
    except:
        pass
