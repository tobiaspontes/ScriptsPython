# gerar QR Code de um link

import pyqrcode
import png
from pyqrcode import QRCode

# link desejado para o QR Code
link = r'https://www.estudonauta.com/meu-painel/'

# monta o QR Code
qrcode = pyqrcode.create(link)

# salva o QR Code
qrcode.png(r'.\imagens\estudonauta.png', scale=8)