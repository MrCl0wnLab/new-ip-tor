import os
import datetime
import requests
import threading
import time

IP_HOST_TOR = '127.0.0.1'
IP_PORT_TOR = '9050'
HOST_TEST_TOR = 'http://ifconfig.me'
DEBUG = False

CONFIG_PROXY_TOR = {
    'http':  f'socks5://{IP_HOST_TOR}:{IP_PORT_TOR}',
    'https': f'socks5://{IP_HOST_TOR}:{IP_PORT_TOR}'
}


def view_new_ip(url):
    datetime_now = datetime.datetime.now()
    html = requests.get(url, proxies=CONFIG_PROXY_TOR)
    print(f"[{datetime_now}] [ RESULT REQUEST ] {html.text}")


def kill_tor():
    # REF https://github.com/googleinurl/SCANNER-INURLBR/blob/master/inurlbr.php#L1450
    os.system("[ -z 'pidof tor' ] || pidof tor | xargs sudo kill -HUP;")


def new_ip_tor():
    while threading.active_count() > 1:
        time.sleep(0.1)
    threading.Thread(target=kill_tor).start()
    if DEBUG:
        threading.Thread(target=view_new_ip, args=(HOST_TEST_TOR,)).start()

