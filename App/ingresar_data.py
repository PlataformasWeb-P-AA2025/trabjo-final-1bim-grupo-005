import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

csv1 = "../DATA/usuarios_red_x.csv"

with open(csv1, mode='r', encoding='utf-8', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    
    for row in csv_reader:
        usuario = Usuario(nombre=row[0].strip())
        session.add(usuario)
    session.commit()


csv2 = "../DATA/usuarios_publicaciones.csv"
with open(csv2, mode='r', encoding='utf-8', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter="|")
    next(csv_reader)
    
    for row in csv_reader:
        usuario = session.query(Usuario).filter(Usuario.nombre==row[0].strip()).one()
        publicacion = Publicacion(usuario=usuario, publicacion=row[1])
        session.add(publicacion)
    session.commit()


csv3 = "../DATA/publicaciones_liga_premier.csv"
with open(csv2, mode='r', encoding='utf-8', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    
    for row in csv_reader:
        usuario = Usuario(nombre="Premier League")
        session.add(usuario)
        publicacion = Publicacion(usuario=usuario, publicacion=row[0])
        session.add(publicacion)
    session.commit()