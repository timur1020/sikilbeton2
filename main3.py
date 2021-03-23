import requests
import json
import time
import sys
import random
import os
import argparse
import colorama
import string
import traceback
import urllib
import pathlib
from colorama import Fore, Back, Style
from random import randint
from datetime import datetime
import pyshorteners
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from os import system, name
from inputimeout import inputimeout, TimeoutOccurred
colorama.init(autoreset=True)

# SET BETSET
parser = argparse.ArgumentParser(
    description='999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk')
parser.add_argument(
    '-c', '--betset',
    default=0,
    help='Enter Your Betset Number (default: 0)'
)
my_namespace = parser.parse_args()

with open('settings.json', 'r') as myfile:
    data = myfile.read()
# PARSE FILE
obj = json.loads(data)


# CONFIG WARNA
res = Style.RESET_ALL
putih = Style.NORMAL+Fore.WHITE
putih2 = Style.BRIGHT+Fore.WHITE
hitam = Style.BRIGHT+Fore.BLACK
hitam2 = Style.BRIGHT+Fore.BLACK
ungu = Style.NORMAL+Fore.MAGENTA
hijau = Style.NORMAL+Fore.GREEN
hijau2 = Style.BRIGHT+Fore.GREEN
merah = Style.NORMAL+Fore.RED
merah2 = Style.BRIGHT+Fore.RED
biru = Style.NORMAL+Fore.BLUE
biru2 = Style.BRIGHT+Fore.BLUE
biru3 = Style.BRIGHT+Fore.LIGHTCYAN_EX
profitcolor = Style.BRIGHT+Back.GREEN+Fore.WHITE
losecolor = Style.BRIGHT+Back.RED+Fore.WHITE
rccolor = Style.BRIGHT+Back.WHITE+Fore.BLACK
rcfontcolor = Style.NORMAL+Fore.BLACK
kuning = Style.NORMAL+Fore.YELLOW
kuning2 = Style.BRIGHT+Fore.YELLOW

c = requests.session()
ua = UserAgent()
proxies = []
proxystatus = False
freeversion = False
linkcode = ""



def timeprocess(sec):
    now = datetime.now()
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    stopwatchx = datetime(now.year, now.month, now.day,
                          int(hours), int(mins), int(sec), 0)

    return stopwatchx


def setmsgbox():

    try:
        msg = client.query(
            q.get(q.match(q.index("param_by_id"), "messagebox")))
        msgbox = msg["data"]["message"]
    except:
        msgbox = "-"

    return msgbox


def banner():
    # BANNER
    banner = "\n\n"
    banner = banner + merah2 + "·▄▄▄▄  ▪   ▄▄· ▄▄▄ .▄▄▄▄·      ▄▄▄▄▄\n"
    banner = banner + "██▪ ██ ██ ▐█ ▌▪▀▄.▀·▐█ ▀█▪▪    •██  \n"
    banner = banner + "▐█· ▐█▌▐█·██ ▄▄▐▀▀▪▄▐█▀▀█▄ ▄█▀▄ ▐█." + putih2 + "▪\n"
    banner = banner + "██. ██ ▐█▌▐███▌▐█▄▄▌██▄▪▐█▐█▌.▐▌▐█▌·\n"
    banner = banner + "▀▀▀▀▀• ▀▀▀·▀▀▀  ▀▀▀ ·▀▀▀▀  ▀█▄▀▪▀▀▀\n"
    banner = banner + "\n"
    banner = banner + putih2 + "Author      : "
    banner = banner + merah2 + "github@beducode\n"
    banner = banner + putih2 + "Advisor     : "
    banner = banner + merah2 + "@riosuyanto\n"
    banner = banner + putih2 + "Contact     : "
    banner = banner + merah2 + "@beduplay / @riosuyanto\n"
    banner = banner + putih2 + "Version     : "
    banner = banner + merah2 + "v.3.0\n" + res
    print(banner)


url = "https://www.999doge.com/api/web.aspx"
uadata = {
    "Origin": "file://",
    "user-agent": ua.random,
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "X-Requested-With": "com.reland.relandicebot"
}

# CLEAN PAGE


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# CONVERT BET & AMOUNT


def konvert(persen, taruhan):
    global high
    global low
    c = str(999999 * float(persen) / 100)
    if taruhan == "Hi" or taruhan == "hi" or taruhan == "HI":
        n = str(c.split(".")[1])
        pangkat = 6 - len(n)
        low = int(int(n) * (10 ** pangkat))
        high = 999999
    if taruhan == "Lo" or taruhan == "LOW" or taruhan == "low" or taruhan == "Low" or taruhan == "LO":
        low = 0
        high = int(c.split(".")[0])

# DECIMAL 8 DIGIT


def rev(num):
    if (len(num) < 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        result = ("0."+num)
    if (len(num) == 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        result = ("0."+num)
    else:
        len_num = len(num)
        end = num[-8:]
        first = num[:len_num-8]
        result = (first+"."+end)
    return (result)

# API INDODAX FOR GET LAST PRICE


def indodax(coin):

    try:
        if coin == "DOGE" or coin == "doge" or coin == "Doge":
            pair = "doge_idr"
        elif coin == "LTC" or coin == "ltc" or coin == "Ltc":
            pair = "ltc_idr"
        else:
            pair = "eth_idr"

        url = 'https://indodax.com/api/' + str(pair) + '/ticker'

        indx = requests.get(url)
        jsindx = json.loads(indx.text)
        pricepair = int(jsindx["ticker"]["last"])
    except:
        if coin == "DOGE" or coin == "doge" or coin == "Doge":
            coinpair = "doge"
        elif coin == "LTC" or coin == "ltc" or coin == "Ltc":
            coinpair = "ltc"
        else:
            coinpair = "eth"

        url = "https://beducode-price.herokuapp.com/price/" + str(coinpair)

        price = c.get(url)
        data = json.loads(price.text)
        pricepair = data["last"]

    return pricepair

# FORMAT VALUE TO IDR


def rupiah_format(angka):
    return 'Rp ' + '{:0,.2f}'.format(angka)

# GENERATE STRING


def stringgen(N):
    resp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return str(resp)


# FIND PROXY
def findproxy():
    # Retrieve latest proxies
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })

    # Choose a random proxy
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]

    for n in range(1, 100):
        req = Request('http://www.999doge.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

        # Every 10 requests, generate a new proxy
        if n % 10 == 0:
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]

        # Make the call
        try:
            print('  Mohon tunggu, sedang mencari proxy sebelum running... ' + Style.BRIGHT+Back.GREEN +
                  Fore.WHITE + ' CHECK SERVER # ' + str(proxy_index) + ' ' + Style.RESET_ALL + ' ', end="\r" + res)
            urlopen(req, timeout=5).read().decode('utf8')
            return proxies[proxy_index]
        except:  # If error, delete this proxy and find another one
            del proxies[proxy_index]
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]


def cekproxymanual(ip, port):
    req = Request('http://www.999doge.com')
    req.set_proxy(ip + ':' + port, 'http')
    try:
        urlopen(req, timeout=5).read().decode('utf8')
        status = True
    except:
        status = False

    return status


def random_proxy():
    return random.randint(0, len(proxies) - 1)


def setProxy():
    if obj["Proxy Manual"]["Toggle"] == "ON" or obj["Proxy Manual"]["Toggle"] == "on" or obj["Proxy Manual"]["Toggle"] == "On":
        ip = str(obj["Proxy Manual"]["Ip"])
        port = str(obj["Proxy Manual"]["Port"])
        proxystatus = cekproxymanual(ip, port)

        if proxystatus is True:
            proxies = dict()

            proxies["ip"] = ip
            proxies["port"] = port
        else:
            proxystatus = False

    else:
        if obj["Account"]["Auto Proxy"] == "ON" or obj["Account"]["Auto Proxy"] == "on" or obj["Account"]["Auto Proxy"] == "On":

            # CLEAR BEFORE RUNNING
            clear()
            banner()

            proxystatus = True
            proxies = findproxy()
        else:
            proxystatus = False


def checkcurr(curr):
    if curr == "DOGE" or curr == "doge" or curr == "Doge":
        currbalance = js[currency]["Balance"]
    elif curr == "LTC" or curr == "ltc" or curr == "Ltc":
        currbalance = js[currency]["Balance"]
    else:
        currbalance = js[currency]["Balance"]

    return currbalance


def checklogin(status):
    if status is True:
        clear()
        banner()

        print(merah2 + "Periksa Kembali Username Atau Password Anda Pada File settings.json" + res)
        sys.exit()
    else:
        pass


# FOR PUBLIC VERSION
def checkccount(balacc, version, curr):

    if curr == "DOGE" or curr == "doge" or curr == "Doge":
        limitbal = 1000000
    elif curr == "LTC" or curr == "ltc" or curr == "Ltc":
        limitbal = 100
    else:
        limitbal = 100

    if version is True:
        if balacc > int(float(limitbal)*(10 ** 8)):
            clear()
            banner()

            print(merah2 + "Anda Hanya Dapat Menggunakan Balance Maksimal " + str(limitbal) + " " +
                  str(curr).upper() + " Pada Versi Ini, Silahkan Hubungi Contact Untuk Informasi Lebih Lanjut" + res)
            sys.exit()
        else:
            pass
    else:
        pass


# CREATE CODE FOR SHORTLINK SERVER

# AUTH FREE VERSION



# CREATE FILE PASSCODE


# AUTH PREMIUM VERSION


# DEK MODE RUN AKTIF


def checkmoderun():
    moderun = 0
    urut = int(my_namespace.betset)
    if obj["Betset"][urut]["Mode1"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode1"]["Toggle"] == "on" or obj["Betset"][urut]["Mode1"]["Toggle"] == "On":
        moderun += 1
    else:
        pass
    if obj["Betset"][urut]["Mode2"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode2"]["Toggle"] == "on" or obj["Betset"][urut]["Mode2"]["Toggle"] == "On":
        moderun += 1
    else:
        pass
    if obj["Betset"][urut]["Mode3"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode3"]["Toggle"] == "on" or obj["Betset"][urut]["Mode3"]["Toggle"] == "On":
        moderun += 1
    else:
        pass
    if obj["Betset"][urut]["Mode4"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode4"]["Toggle"] == "on" or obj["Betset"][urut]["Mode4"]["Toggle"] == "On":
        moderun += 1
    else:
        pass
    if obj["Betset"][urut]["Mode5"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode5"]["Toggle"] == "on" or obj["Betset"][urut]["Mode5"]["Toggle"] == "On":
        moderun += 1
    else:
        pass
    if obj["Betset"][urut]["Dalembert"]["Toggle"] == "ON" or obj["Betset"][urut]["Dalembert"]["Toggle"] == "on" or obj["Betset"][urut]["Dalembert"]["Toggle"] == "On":
        moderun += 1
    else:
        pass
    if obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "ON" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "on" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "On":
        moderun += 1
    else:
        pass

    return moderun

# VALIDASI MODE RUN


def validatemoderun(moderun):
    if moderun > 1:
        clear()
        banner()

        print(biru2 + '\r' + putih2 + '>> ' + res + merah2 + 'Anda Mengaktifkan Lebih Dari 1 Mode!!' +
              res + putih2 + ', Silahkan Cek Kembali File settings.json Anda' + res)
        time.sleep(2)
        sys.exit()
    else:
        pass


def auth2fa():
    # CLEAR BEFORE
    clear()
    banner()

    try:
        inputotp = biru2 + '\r' + putih2 + '>> ' + res + kuning2 + \
            'Silahkan masukan kode google authenticator anda : ' + res
        otpinput = inputimeout(prompt=inputotp, timeout=600)
        if otpinput == "":
            auth2fa()
        else:
            return otpinput

    except TimeoutOccurred:
        auth2fa()


mdcount = checkmoderun()
validatemoderun(mdcount)

username = obj["Account"]["Username"]
password = obj["Account"]["Password"]
# SET UP API AKSES FROM 999DOGE.COM
if obj["Account"]["API Access"] == "OFF" or obj["Account"]["API Access"] == "off" or obj["Account"]["API Access"] == "Off":
    apiAkses = "cd6f9843b05f4042ad1d4060d290b2fd"
else:
    apiAkses = obj["Account"]["API Access"]

if obj["Account"]["2FA"] == "ON" or obj["Account"]["2FA"] == "on" or obj["Account"]["2FA"] == "On":
    otpstatus = True
    otp = auth2fa()
else:
    otpstatus = False


def stopbet(profit, bl, mb, ls, tp):
    clear()
    banner()
    print(putih2 + "Limit Maksimal Bet Telah Terpenuhi, Profit Anda : " +
          res + hijau2 + str(profit) + res)
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + str(rev(str(bl))) + res)
    print(putih2 + "Waktu Yang Di Butuhkan : " +
          res + putih2 + tp.strftime("%H:%M:%S") + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


def stoplimitls(profit, bl, mb, ls, tp):
    clear()
    banner()
    print(putih2 + "Limit Lose Strike Telah Terpenuhi, Profit Anda : " +
          res + hijau2 + str(profit) + res)
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + str(rev(str(bl))) + res)
    print(putih2 + "Waktu Yang Di Butuhkan : " +
          res + putih2 + tp.strftime("%H:%M:%S") + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


def targetprofit(profit, bl, mb, ls, tp):
    clear()
    banner()
    print(putih2 + "Target Profit Telah Tercapai : " +
          res + hijau2 + str(profit) + res)
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + str(rev(str(bl))) + res)
    print(putih2 + "Waktu Yang Di Butuhkan : " +
          res + putih2 + tp.strftime("%H:%M:%S") + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    print(hijau2 + "Restart New Seeds...tunggu 1tahun..")
    time.sleep(5)
    clear()
    dice(int(float(obj["Target Win"])*(10 ** 8)),
     int(float(obj["Lose Target"])*(10 ** 8)))
    


def targetbalance(profit, bl, mb, ls, tp):
    clear()
    banner()
    print(putih2 + "Target Balance Telah Tercapai : " +
          res + hijau2 + str(profit) + res)
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + str(rev(str(bl))) + res)
    print(putih2 + "Waktu Yang Di Butuhkan : " +
          res + putih2 + tp.strftime("%H:%M:%S") + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


def targetlose(profit, bl, mb, ls, tp):
    clear()
    banner()
    print(putih2 + "Target Lose Telah Tercapai, Jumlah Minus : " +
          res + merah2 + str(profit) + res)
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + merah2 + str(rev(str(bl))) + res)
    print(putih2 + "Waktu Yang Di Butuhkan : " +
          res + putih2 + tp.strftime("%H:%M:%S") + res)
    print(merah2 + "STOP!!!" + res + putih2 +
          ", Hitung Kembali Betset Anda & Coba Analisa Kembali" + res)
    time.sleep(1)
    sys.exit()


def fibocal(n):
    if n <= 1:
        return n+1
    else:
        return(fibocal(n-1) + fibocal(n-2))


# CLEAR BEFORE
clear()
banner()

pilcurr = obj["Account"]["Currency"]
if pilcurr == "DOGE" or pilcurr == "doge" or pilcurr == "Doge":
    currency = "Doge"
elif pilcurr == "LTC" or pilcurr == "ltc" or pilcurr == "Ltc":
    currency = "LTC"
elif pilcurr == "ETH" or pilcurr == "eth" or pilcurr == "Eth":
    currency = "ETH"
else:
    print("Tipe currency tidak disupport, silahkan cek kembali file settings.json anda!")
    sys.exit()


def dice(ws, ls):
    if my_namespace.betset == "Auto" or my_namespace.betset == "auto" or my_namespace.betset == "AUTO":
        urut = 0
        jumlahulang = 0
        while True:
            jumlahulang += 1
            try:
                pesan = obj["Betset"][urut]["Name Bet Set"]
            except:
                break
    else:
        urut = int(my_namespace.betset)

    slp = int(obj["Betset"][urut]["Interval"]) / 1000
    limit_a = int(obj["Betset"][urut]["Reset If Win"]) - 1
    konvert(obj["Betset"][urut]["Chance"], obj["Betset"][urut]["Bet"]["Bet"])
    baseBet = int(float(obj["Betset"][urut]["Base Bet"])*(10 ** 8))
    if obj["Betset"][urut]["Mode1"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode1"]["Toggle"] == "on" or obj["Betset"][urut]["Mode1"]["Toggle"] == "On":
        payin = int(float(obj["Betset"][urut]["Mode1"]["Prebet"])*(10 ** 8))
        winGet1 = int(obj["Betset"][urut]["Mode1"]["Start Strike If Win"])
        winGet2 = int(obj["Betset"][urut]["Mode1"]["Limit Strike If Win"])
        Mt1 = float(obj["Betset"][urut]["Mode1"]["Start Multi"])
        Mt2 = float(obj["Betset"][urut]["Mode1"]["Limit Multi"])
        go = False
        tmplose = 0
        
    elif obj["Betset"][urut]["Mode2"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode2"]["Toggle"] == "on" or obj["Betset"][urut]["Mode2"]["Toggle"] == "On":
        payin = int(float(obj["Betset"][urut]["Mode2"]["Prebet"])*(10 ** 8))
        Mtpreroll = float(obj["Betset"][urut]["Mode2"]["Multipler"])
        preroll = int(obj["Betset"][urut]["Mode2"]["Preroll"])
        prerollStatus = True
        
    elif obj["Betset"][urut]["Mode3"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode3"]["Toggle"] == "on" or obj["Betset"][urut]["Mode3"]["Toggle"] == "On":
        payin = int(float(obj["Betset"][urut]["Mode3"]["Prebet"])*(10 ** 8))
        Mtpreroll = float(obj["Betset"][urut]["Mode3"]["Multipler"])
        preroll = int(obj["Betset"][urut]["Mode3"]["Preroll"])
        maxlslimit = int(obj["Betset"][urut]["Mode3"]["Max LS Strike"])
        prerollStatus = True
        maxls = False
        
    elif obj["Betset"][urut]["Mode4"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode4"]["Toggle"] == "on" or obj["Betset"][urut]["Mode4"]["Toggle"] == "On":
        payin = int(float(obj["Betset"][urut]["Mode4"]["Prebet"])*(10 ** 8))
        startfish = int(obj["Betset"][urut]["Mode4"]["Start Fishing"])
        stopfish = int(obj["Betset"][urut]["Mode4"]["Stop Fishing"])
        Mt = float(obj["Betset"][urut]["Mode4"]["Multipler"])
        tmplosefish = 0
        profitpay = 0
        tmpprofit = 0
        
    elif obj["Betset"][urut]["Mode5"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode5"]["Toggle"] == "on" or obj["Betset"][urut]["Mode5"]["Toggle"] == "On":
        payin = baseBet
        loseval = float(obj["Betset"][urut]["Mode5"]["Lose"])
        winval = float(obj["Betset"][urut]["Mode5"]["Win"])
        profitdiv = int(float(obj["Betset"][urut]["Mode5"]["Profit"])*(10 ** 8))
        tmpprofit = 0
        wincount = 0
        
    elif obj["Betset"][urut]["Dalembert"]["Toggle"] == "ON" or obj["Betset"][urut]["Dalembert"]["Toggle"] == "on" or obj["Betset"][urut]["Dalembert"]["Toggle"] == "On":
        payin = baseBet
        profitdiv = int(float(obj["Betset"][urut]["Dalembert"]["Profit"])*(10 ** 8))
        wincount = 0
        tmpprofit = 0
        dllevel = 0
        
    elif obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "ON" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "on" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "On":
        payin = int(float(obj["Betset"][urut]["Fibonacci1"]["Prebet"])*(10 ** 8))
        fibo = False
        fbtmp = 1
        fbcount = 1
        preroll = int(obj["Betset"][urut]["Fibonacci1"]["Preroll"])
        fbmaxlslimit = int(obj["Betset"][urut]["Fibonacci1"]["Max LS Strike"])
        fbmaxls = False
        prerollStatus = True
        
    else:
        payin = baseBet

    amount = payin
    maxbet = 0
    stopmaxbet = False
    stopbetamount = 0

    data = {
        "a": "PlaceBet",
        "s": js["SessionCookie"],
        "PayIn": amount,
        "Low": low,
        "High": high,
        "ClientSeed": randint(0, 999999),
        "Currency": pilcurr,
        "ProtocolVersion": "2"
    }

    try:
        if proxystatus is True:
            r1 = c.post(url, proxies=proxies, headers=uadata, data=data)
        else:
            r1 = c.post(url, headers=uadata, data=data)

        jsn = json.loads(r1.text)
        jumbl = jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount)
        jum = int(jsn["PayOut"]) - int(amount)
        prof = (float(jsn["StartingBalance"] +
                      int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
        n = 0
        burst = False
        stats_rolebet_lose = False
        stats_rolebet_win = False
        menit = datetime.now().strftime('%M')
        menit = int(menit) + int(obj["Interval"])
        no_win = 0
        no_lose = 0
        total_win = 0
        total_lose = 0
        no_rolebet = 0
        rolebet = " H "
        reset_if_profit = obj["Betset"][urut]["Reset If Profit"]
        tot_if_profit = obj["Betset"][urut]["Reset If Profit"]
        # NEW
        rdchange = False
        spin = 0
        start_time = time.time()

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            # ADD STOP MAX BET
            if obj["Betset"][urut]["Stop Max Bet"] == "OFF" or obj["Betset"][urut]["Stop Max Bet"] == "off" or obj["Betset"][urut]["Stop Max Bet"] == "Off":
                pass
            else:
                stopmaxbet = True
                stopbetamount = int(
                    float(obj["Betset"][urut]["Stop Max Bet"])*(10 ** 8))

            if reset_if_profit == "OFF" or reset_if_profit == "Off" or reset_if_profit == "off":
                stats_if_profit = False
            else:
                stats_if_profit = True
            if obj["Betset"][urut]["Max Bet"] == "OFF" or obj["Betset"][urut]["Max Bet"] == "off" or obj["Betset"][urut]["Max Bet"] == "Off":
                sys.stdout.write("")
            else:
                if amount > int(float(obj["Betset"][urut]["Max Bet"])*(10 ** 8)):
                    amount = payin
            if obj["Betset"][urut]["Bet"]["Hi / Low"]["Toggle"] == "On" or obj["Betset"][urut]["Bet"]["Hi / Low"]["Toggle"] == "ON" or obj["Betset"][urut]["Bet"]["Hi / Low"]["Toggle"] == "on":
                no_rolebet += 1
                if stats_rolebet_win is False:
                    if no_rolebet > int(obj["Betset"][urut]["Bet"]["Hi / Low"]["If Win"]) - 1:
                        rolebet = " L "
                    if no_rolebet > int(obj["Betset"][urut]["Bet"]["Hi / Low"]["If Win"]) * 2 - 1:
                        rolebet = " H "
                        no_rolebet = 0
                if stats_rolebet_lose is False:
                    if no_rolebet > int(obj["Betset"][urut]["Bet"]["Hi / Low"]["If Lose"]) - 1:
                        rolebet = " L "
                    if no_rolebet > int(obj["Betset"][urut]["Bet"]["Hi / Low"]["If Lose"]) * 2 - 1:
                        rolebet = " H "
                        no_rolebet = 0
            else:
                rolebet = obj["Betset"][urut]["Bet"]["Bet"]
                if rolebet == "HI" or rolebet == "hi" or rolebet == "Hi" or rolebet == "High" or rolebet == "HIGH" or rolebet == "high":
                    rolebet = " H "
                elif rolebet == "LO" or rolebet == "lo" or rolebet == "Lo" or rolebet == "Low" or rolebet == "LOW" or rolebet == "low":
                    rolebet = " L "
                else:
                    print(
                        "Terjadi kesalahan pada settings.json, silahkan cek kembali file settings anda")
                    sys.exit()

            if my_namespace.betset == "Auto" or my_namespace.betset == "AUTO" or my_namespace.betset == "auto":
                waktu = datetime.now().strftime('%M')
                if int(waktu) > int(menit - 1):
                    menit = int(menit) + int(obj["Interval"])
                    urut += 1
                    if urut == jumlahulang:
                        urut = 0
                    print("Change Bet Set "+obj["Betset"][urut]
                          ["Name Bet Set"]+"                           ")
                    slp = int(obj["Betset"][urut]["Interval"]) / 1000
                    limit_a = int(obj["Betset"][urut]["Reset If Win"]) - 1
                    payin = int(
                        float(obj["Betset"][urut]["Base Bet"])*(10 ** 8))
                    amount = payin

            else:
                urut = int(my_namespace.betset)

            time.sleep(float(slp))
            amount = int(amount)
            n += 1
            data = {
                "a": "PlaceBet",
                "s": js["SessionCookie"],
                "PayIn": amount,
                "Low": low,
                "High": high,
                "ClientSeed": randint(0, 999999),
                "Currency": currency,
                "ProtocolVersion": "2"
            }

            if prof > float(obj["Target Profit"]):
                # TARGET PROFIT
                bl = int(jsn["StartingBalance"]) + int(jum)
                pf = prof
                tp = timeprocess(int(elapsed_time))
                targetprofit(pf, bl, maxbet, total_lose, tp)

            if proxystatus is True:
                r1 = c.post(url, proxies=proxies, headers=uadata, data=data)
            else:
                r1 = c.post(url, headers=uadata, data=data)

            jsn = json.loads(r1.text)
            prof = (float(jsn["StartingBalance"] +
                          int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
            jum = int(jsn["PayOut"]) - int(amount)

            if jsn["StartingBalance"] > ws:
                # TARGET BALANCE
                bl = int(jsn["StartingBalance"]) + int(jum)
                pf = prof
                targetbalance(pf, bl, maxbet, total_lose, tp)

            if jsn["StartingBalance"] < ls:
                # LOSE TARGET
                bl = int(jsn["StartingBalance"]) + int(jum)
                pf = prof
                targetlose(pf, bl, maxbet, total_lose, tp)

            if obj["Betset"][urut]["Random Chance"]["Toggle"] == "ON" or obj["Betset"][urut]["Random Chance"]["Toggle"] == "On" or obj["Betset"][urut]["Random Chance"]["Toggle"] == "on":
                hasil_chance = round(random.uniform(float(obj["Betset"][urut]["Random Chance"]["Min"]), float(
                    obj["Betset"][urut]["Random Chance"]["Max"])), 2)
                rdchange = True
                panjangrd = len(str(hasil_chance))

                if panjangrd == 3:
                    chancerand = str(hasil_chance) + "   "
                if panjangrd == 4:
                    chancerand = str(hasil_chance) + "  "
                if panjangrd == 5:
                    chancerand = str(hasil_chance) + " "

                konvert(hasil_chance, str(rolebet))
            else:
                konvert(obj["Betset"][urut]["Chance"], str(rolebet))

            if spin == 0:
                marketidx = indodax(pilcurr)

            spin += 1

            if spin == 250:
                marketidx = indodax(pilcurr)
                spin = 1

            # MAIN BET
            if obj["Betset"][urut]["Mode1"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode1"]["Toggle"] == "on" or obj["Betset"][urut]["Mode1"]["Toggle"] == "On":
                # MODE-1
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    go = True
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    # BET SETTING
                    if no_win == winGet1 and go is True:
                        if tmplose != 0:
                            amount = int(tmplose) * Mt1
                        else:
                            amount = int(baseBet) * Mt1

                    if no_win > winGet1 and no_win <= winGet2 and go is True:
                        amount = int(amount) * Mt2

                    if no_win > winGet2 and go is True:
                        tmplose = 0
                        go = False
                        amount = int(payin)

                else:
                    no_win = 0
                    no_lose += 1
                    go = False

                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    if no_lose == 1:
                        if amount > payin:
                            tmplose = int(amount)
                            amount = int(payin)
                        else:
                            amount = int(payin)
                    else:
                        amount = int(payin)
            elif obj["Betset"][urut]["Mode2"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode2"]["Toggle"] == "on" or obj["Betset"][urut]["Mode2"]["Toggle"] == "On":
                # MODE-2 PREROLL COUNT
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    amount = int(payin)
                    preroll = int(obj["Betset"][urut]["Mode2"]["Preroll"])
                    prerollStatus = True

                else:
                    no_win = 0
                    no_lose += 1
                    preroll -= 1
                    i = 0
                    burst = True
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    if preroll == 0:
                        amount = int(baseBet)
                        prerollStatus = False
                    elif preroll < 0:
                        amount = int(amount) * Mtpreroll
                    else:
                        amount = int(payin)

            elif obj["Betset"][urut]["Mode3"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode3"]["Toggle"] == "on" or obj["Betset"][urut]["Mode3"]["Toggle"] == "On":
                # MODE-3 PREROLL COUNT WITH MAX LOSE STRIKE LIMIT
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass

                        if total_lose >= maxlslimit:
                            stoplimitls(prof, bal, maxbet, total_lose, tp)
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    amount = int(payin)
                    preroll = int(obj["Betset"][urut]["Mode3"]["Preroll"])
                    prerollStatus = True

                else:
                    no_win = 0
                    no_lose += 1
                    preroll -= 1
                    i = 0
                    burst = True
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    if preroll == 0:
                        amount = int(baseBet)
                        prerollStatus = False
                    elif preroll < 0:
                        amount = int(amount) * Mtpreroll
                    else:
                        amount = int(payin)
            elif obj["Betset"][urut]["Mode4"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode4"]["Toggle"] == "on" or obj["Betset"][urut]["Mode4"]["Toggle"] == "On":
                # MODE-4
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)
                    tmpprofit = int(prof*(10 ** 8))

                    if prof > 0:
                        if tmpprofit > profitpay:
                            profitpay = tmpprofit
                        else:
                            pass

                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " Balance : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    # BET SETTING
                    if tmpprofit < profitpay:
                        if no_win == startfish or no_win == stopfish:
                            if tmplosefish > 0:
                                amount = int(tmplosefish) * Mt
                            else:
                                amount = int(baseBet) * Mt
                        else:
                            amount = int(payin)
                    else:
                        if no_win == startfish or no_win == stopfish:
                            tmplosefish = 0
                            amount = int(baseBet) * Mt
                        else:
                            tmplosefish = 0
                            amount = int(payin)

                else:
                    no_win = 0
                    no_lose += 1

                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    if no_lose == 1:
                        if amount > payin:
                            tmplosefish = int(amount)
                            amount = int(payin)
                    else:
                        amount = int(payin)
            elif obj["Betset"][urut]["Mode5"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode5"]["Toggle"] == "on" or obj["Betset"][urut]["Mode5"]["Toggle"] == "On":
                # MODE-5
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass
                        
                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    # BET SETTING
                    wincount += 1
                    if(profit > (tmpprofit + profitdiv)):
                        wincount = 0
                        tmpprofit = profit
                        amount = payin
                    else:
                        amount = amount * winval
                        

                else:
                    no_win = 0
                    no_lose += 1

                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    wincount = 0
                    amount = amount * loseval
            
            elif obj["Betset"][urut]["Dalembert"]["Toggle"] == "ON" or obj["Betset"][urut]["Dalembert"]["Toggle"] == "on" or obj["Betset"][urut]["Dalembert"]["Toggle"] == "On":
                # MODE-5
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass
                        
                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    # BET SETTING
                    wincount += 1
                    dllevel -= 1
                    if(profit > (tmpprofit + profitdiv)):
                        dllevel = 0
                        wincount = 0
                        tmpprofit = profit
                        amount = payin + (payin * dllevel)
                    else:
                        if dllevel < 0:
                            dllevel = 0
                        amount = payin + (payin * dllevel)
                    

                else:
                    no_win = 0
                    no_lose += 1

                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    # BET SETTING
                    wincount = 0
                    dllevel += 1
                    
                    amount = payin + (payin * dllevel)
                    

            elif obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "ON" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "on" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "On":
                fibo = True
                # MODE FIBONACCI #1
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    fbcount = 1
                    fbtmp = 1
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if total_lose >= fbmaxlslimit:
                            stoplimitls(prof, bal, maxbet, total_lose, tp)
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    # BET SETTING
                    amount = int(payin)
                    preroll = int(obj["Betset"][urut]["Fibonacci1"]["Preroll"])
                    prerollStatus = True

                else:
                    no_win = 0
                    no_lose += 1
                    go = False

                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:

                        if stopmaxbet is True:
                            if stopbetamount != 0 and amount > stopbetamount:
                                stopbet(prof, bal, maxbet, total_lose, tp)
                            else:
                                pass
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    if no_lose == 1:
                        if amount > payin:
                            tmplose = int(amount)
                            amount = int(payin)
                    else:
                        amount = int(payin)

            else:
                # NORMAL MODE
                if jsn["PayOut"] != 0:
                    no_win += 1
                    no_lose = 0
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if amount > maxbet:
                            maxbet = amount
                        else:
                            pass

                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L" + res + " : " + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + profitcolor + putih2 + str(rolebet) + res + " " +
                                  hijau2+"+"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(profitcolor + putih2 + str(rolebet) + res + " " + hijau2+"+"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    amount = int(amount) * float(obj["Betset"][urut]["If Win"])

                else:
                    no_win = 0
                    no_lose += 1
                    i = 0
                    burst = True
                    bal = int(jsn["StartingBalance"]) + int(jum)
                    profit = bal-currbalance
                    lastprice = marketidx
                    wdbalance = float(int(bal))/(10 ** 8)
                    wd = rupiah_format(lastprice * wdbalance)

                    if prof > 0:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res +
                                  " " + merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + hijau2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                    else:
                        if rdchange is True:
                            print(rccolor + rcfontcolor + chancerand + res + losecolor + putih2 + str(rolebet) + res + " " +
                                  merah2+"-"+str(rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))
                        else:
                            print(res + losecolor + putih2 + str(rolebet) + res + " " + merah2+"-"+str(
                                rev(str(amount))) + res + biru3 + " B4L : " + res + str(rev(str(bal))) + res + merah2 + " Profit" + res + " : " + str(rev(str(profit))) + res + kuning + " Total" + res + " : " + str(wd))

                    amount = int(amount) * \
                        float(obj["Betset"][urut]["If Lose"])

                if stats_if_profit is True:
                    if prof > float(reset_if_profit):
                        amount = payin
                        reset_if_profit = float(prof)+float(tot_if_profit)

                if burst is True:
                    i += 1
                    if i > limit_a:
                        i = 0
                        burst = False
                    else:
                        if n > limit_a:
                            n = 0
                            amount = payin

            if no_win > total_win:
                stats_rolebet_win = True
                stats_rolebet_lose = False
                total_win += 1
            if no_lose > total_lose:
                stats_rolebet_lose = True
                stats_rolebet_win = False
                total_lose += 1

            prTextStatus = res + '' + Style.RESET_ALL

            if obj["Betset"][urut]["Mode3"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode3"]["Toggle"] == "on" or obj["Betset"][urut]["Mode3"]["Toggle"] == "On":
                if total_lose >= maxlslimit:
                    maxls = True
                else:
                    pass

            if obj["Betset"][urut]["Mode2"]["Toggle"] == "ON" or obj["Betset"][urut]["Mode2"]["Toggle"] == "on" or obj["Betset"][urut]["Mode2"]["Toggle"] == "On":
                if prerollStatus is not True:
                    prTextStatus = Style.BRIGHT+Back.RED+Fore.WHITE + \
                        ' PREROLL ' + res + " " + Style.RESET_ALL
                else:
                    prTextStatus = Style.BRIGHT+Back.GREEN + \
                        Fore.WHITE + ' PREROLL ' + res + " " + Style.RESET_ALL

            if obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "ON" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "on" or obj["Betset"][urut]["Fibonacci1"]["Toggle"] == "On":
                prTextStatus = Style.BRIGHT+Back.BLUE+Fore.WHITE + \
                    ' FIBO ' + res + " " + Style.RESET_ALL
                if total_lose >= fbmaxlslimit:
                    fbmaxls = True
                else:
                    pass

            mbTextStatus = res + " " + Style.BRIGHT+Back.RED+Fore.WHITE + \
                ' MB ' + rev(str(maxbet)) + " " + Style.RESET_ALL

            if freeversion is True:
                textVersion = Style.BRIGHT+Back.GREEN+Fore.WHITE + " FREE " + res
            else:
                textVersion = Style.NORMAL+Back.YELLOW+Fore.BLACK + " PREMIUM " + res

            tp = timeprocess(int(elapsed_time))
            timelabel = Style.NORMAL+Back.WHITE+Fore.BLACK + \
                " " + tp.strftime("%H:%M:%S") + " " + res

            sys.stdout.write(res + "   " + profitcolor + putih2 + " WS " + str(total_win) +
                             " " + res + " " + losecolor + putih2 + " LS " + str(total_lose) + " " + res + " " + rccolor + rcfontcolor + " HARGA " + str(rupiah_format(marketidx)) + " " + mbTextStatus + " " + prTextStatus + "" + textVersion + " " + timelabel + "\r")

            if obj["Auto Wd"]["Toggle"] == "On" or obj["Auto Wd"]["Toggle"] == "ON" or obj["Auto Wd"]["Toggle"] == "on":
                if float(rev(str(bal))) > float(obj["Auto Wd"]["If Balance"]):
                    wd = {
                        "a": "Withdraw",
                        "s": js["SessionCookie"],
                        "Amount": int(float(obj["Auto Wd"]["Amount"])*(10 ** 8)),
                        "Address": obj["Auto Wd"]["Wallet Address"],
                        "Totp": "",
                        "Currency": pilcurr
                    }
                    r1 = c.post(url, headers=uadata, data=wd)
                    withdraw = json.loads(r1.text)
                    clear()
                    banner()
                    autowdactive = Style.BRIGHT+Back.GREEN + \
                        Fore.WHITE + " AUTO WITHDRAW ACTIVE \n" + res
                    print(autowdactive)
                    print("Jumlah Withdraw : " +
                          str(rev(str(withdraw["Pending"]))) + " " + str(pilcurr).upper())
                    sys.exit()
    except:
                    print(merah2+"Balance Tidak Mencukupi Untuk Betting")
                    sys.exit()

# WITH OTP
if otpstatus is True:
    datas = {"a": "Login", "Key": apiAkses,
             "Username": username, "Password": password, "Totp": str(otp)}
else:
    datas = {"a": "Login", "Key": apiAkses,
             "Username": username, "Password": password, "Totp": ""}

if proxystatus is False:
    r = c.get(url, headers=uadata, data=datas)
    js = json.loads(r.text)
    loginstatus = "LoginInvalid" in js
    checklogin(loginstatus)
    currbalance = checkcurr(pilcurr)
    checkccount(currbalance, freeversion, pilcurr)
    setProxy()

    print(Style.BRIGHT+Back.RED+Fore.WHITE + ' PROXY TIDAK AKTIF ' + Style.RESET_ALL +
          ' Mari kita mulai..                                                                    \n ', end="\r")

else:
    r = c.get(url, proxies=proxies, headers=uadata, data=datas)
    js = json.loads(r.text)
    loginstatus = "LoginInvalid" in js
    checklogin(loginstatus)
    currbalance = checkcurr(pilcurr)
    checkccount(currbalance, freeversion, pilcurr)
    setProxy()

    print(Style.BRIGHT+Back.GREEN+Fore.WHITE + ' PROXY AKTIF ' + Style.RESET_ALL +
          ' Mari kita mulai..                                                                    \n ', end="\r")

try:
    messagebox = setmsgbox()
    print(profitcolor + putih2 + " B4L ", res + str((float(int(currbalance))/(10 ** 8))) +
          " " + currency + res + " " + rccolor + hitam2 + " Info : " + messagebox + " " + res + " ")
except:
    sys.exit()

dice(int(float(obj["Target Win"])*(10 ** 8)),
     int(float(obj["Lose Target"])*(10 ** 8)))
