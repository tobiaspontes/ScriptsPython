# remove fundo de imagens


from rembg import remove
from PIL import Image

imagem_inicial = r'.\imagens\foto_inicial.png'
imagem_final = '.\imagens\foto_final.png'

inp = Image.open(imagem_inicial)
out = remove(inp)
out.save(imagem_final)