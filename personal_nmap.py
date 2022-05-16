import socket
import sys
import pyfiglet
import datetime

ascii_banner = pyfiglet.figlet_format("Python For Hacker Series 1 (Nmap)")
print(ascii_banner)

target = input("Hedef Domain Adresi: ")
target_IP = socket.gethostbyname(target)
time = datetime.datetime.now()
tarih = datetime.datetime.ctime(time)

print("_" * 50)
print("Taranan Hedef >> ", str(target))
print("Tarama Başlama Tarihi: ", tarih)
print("_"* 50)

try:
    for port in range(21,445):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        sonuc = sock.connect_ex((target_IP, port))

        if sonuc ==0:
            print("Port {}:   Açık" .format(port))
            sock.close()
except KeyboardInterrupt:
    print("İşlemi İptal Ettiniz!")
    sys.exit()

except socket.gaierror:
    print("Host ismi çözülemedi!")
    sys.exit()

except socket.error:
    print("Bağlantı Kurulamadı!")
    sys.exit()

