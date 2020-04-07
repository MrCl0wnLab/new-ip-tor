import os
import datetime
import requests
import threading
import time


IP_HOST_TOR = '127.0.0.1'
# tor control port as defined in torrc file
IP_PORT_TOR = '9050'
# host test request "new identity" IP
HOST_TEST_TOR = 'http://ifconfig.me'
# flag debug "new identity" IP
DEBUG = False
# config socks5 ip + port default tor
CONFIG_PROXY_TOR = {
    'http':  f'socks5://{IP_HOST_TOR}:{IP_PORT_TOR}',
    'https': f'socks5://{IP_HOST_TOR}:{IP_PORT_TOR}'
}

# view result "new identity" IP
def view_new_ip(url):
    try:
        datetime_now = datetime.datetime.now()
        html = requests.get(url, proxies=CONFIG_PROXY_TOR)
        print(f"[{datetime_now}] [ RESULT REQUEST ] {html.text}")
    except:
        return False


# reboot execution of the TOR service.
# tor daemon re-read configurations files and make "new identity".
def kill_tor():
    try:
        # REF https://github.com/googleinurl/SCANNER-INURLBR/blob/master/inurlbr.php#L1450
        os.system("[ -z 'pidof tor' ] || pidof tor | xargs sudo kill -HUP;")
    except:
        return False


def new_ip_tor():
    while threading.active_count() > 1:
        time.sleep(0.5)
    threading.Thread(target=kill_tor).start()
    if DEBUG:
        threading.Thread(target=view_new_ip, args=(HOST_TEST_TOR,)).start()
