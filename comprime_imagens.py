# faz a compressão de imagens, diminuindo-lhe o tamanho

from PIL import Image

# abre a imagem original
img = Image.open(r'.\imagens\paisagem.jpg')

# salva imagem comprimida
img.save(r'.\imagens\paisagem_comprimida.jpg', 'JPEG', optimize=True, quality=10)