# -*- coding: utf-8 -*-
import os
from fiunamfs import FIUNAMFS
from tabulate import tabulate

fsimg_path = os.path.join('.', 'fiunamfs v0.8.img')

fs = FIUNAMFS(fsimg_path)
fs.montar()
fs.montar()

l_archivos = fs.listdir()
print(l_archivos)

lEntDir = fs.scandir()
encabezados = ['Cluster\nde inicio', 'Nombre', 'Tamaño', 'Fecha de creación', 'Fecha de modificación']
tabla = []
for entDir in lEntDir:
    tabla.append([
        entDir.cluster_inicial, 
        entDir.nombre, 
        '%i bytes' % entDir.tam_archivo, 
        entDir.f_creacion, 
        entDir.f_modif
    ])
print('\n', tabulate(tabla, encabezados), '\n')

# fs.descargar('README.org', os.path.join('ArchivosDescargados', 'README.org'))
# fs.descargar('logo.png', os.path.join('ArchivosDescargados', 'logo.png'))
# fs.descargar('mensajes.png', os.path.join('ArchivosDescargados', 'mensajes.png'))
# fs.descargar('blackbird.jpg', os.path.join('ArchivosDescargados', 'blackbird.jpg'))

# fs.subir('README.org', 'OtroMas')
# fs.subir('README.org', 'OtroMas\na')
fs.subir(os.path.join('ArchivosParaSubir', 'blackbird.jpg'), 'blackbird.jpg')

fs.subir(os.path.join('ArchivosDescargados', 'README.org'), 'README.org')
# fs.subir('README.org', 'OtroMás')
# fs.subir('README.org', 'Otro Más  ')
# fs.subir('README.org', 'Otro mass largo........  ')
# fs.subir('README.org', 'a'*16)
# fs.subir('README.org', 'b'*17)

l_archivos = fs.listdir()
print('\n', l_archivos, '\n')

fs.desmontar()
fs.desmontar()