import requests     #cheek beng from google library

#funcation to make sure the oc is conncting to internet

def is_connected():
    try:
        requests.get('https://www.google.com')
        return True
    except requests.ConnectionError:
        return False

#if not is_connected():
    # Send toast notification
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    title = 'Tia Voice Assistant'
    message = 'Please check your internet connection.'
    icon = 'icons/nonet.ico'
    toaster.show_toast(title, message,icon,duration=10)
    
def not_connected():
    try:
        requests.get('https://www.google.com')
        return True
    except requests.ConnectionError:
        return False

if not is_connected():
    # Send toast notification
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    title = 'Tia Voice Assistant'
    message = 'Please check your internet connection.'
    icon = 'icons/logo .ico'
    toaster.show_toast(title, message,icon,duration=10)