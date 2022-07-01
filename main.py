import os
import shutil
from PIL import Image, ImageChops

extensoes = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']

fotosParaMover = []


def compararFotos(imgA, imgB):
    fotoA, fotoB = Image.open(imgA), Image.open(imgB)

    try:
        diferenca = ImageChops.difference(fotoA, fotoB)

        if not diferenca.getbbox():
            caminho = "".join(["iguais/", imgA, "/"])
            if not os.path.exists(caminho):
                os.makedirs(caminho)
            adicionadas, k, t = len(fotosParaMover), 0, 1

            if adicionadas > 0:
                while k < adicionadas:
                    if imgB in fotosParaMover[k][0]:
                        t = 0
                    k += 1
            if t == 1:
                fotosParaMover.append([imgB, str(caminho + imgB)])
        else:
            pass
    except ValueError:
        pass


def mover():
    j, quantidade = 0, len(fotosParaMover)

    while j < quantidade:
        shutil.move(fotosParaMover[j][0], fotosParaMover[j][1])
        j += 1

    fotosParaMover.clear()


def fotos():
    fotos = [
        filename for filename in os.listdir(".") if any(filename.endswith(ext) for ext in extensoes)
    ]
    totalFotos, i = len(fotos), 0
    quantidadeFotos = totalFotos
    while i < quantidadeFotos:
        n = i + 1
        while n < quantidadeFotos:
            compararFotos(fotos[i], fotos[n])
            n += 1

        mover()

        fotos = [
            filename for filename in os.listdir(".") if any(filename.endswith(ext) for ext in extensoes)
        ]
        quantidadeFotos = len(fotos)
        print(str(i * 100 / quantidadeFotos) + "%")
        i += 1


fotos()