import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com/')
except urllib.request.URLError:
    print('O site Facebook não está acessível no momento.')
else:
    print('Consegui acessar o site Facebook.')
