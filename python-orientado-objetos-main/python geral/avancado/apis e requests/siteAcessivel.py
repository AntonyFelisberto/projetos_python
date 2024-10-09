import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('erro ao abrir site')
else:
    print('conseguil acessar site')
    print(site.read())