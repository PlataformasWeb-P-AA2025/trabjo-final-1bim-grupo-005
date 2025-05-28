from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#1Listar publicaciones de un usuario.

listar_publicaciones = session.query(Publicacion).join(Usuario).filter(Usuario.nombre == "Premier League").all()

print("Usuario: Premier League")
for p in listar_publicaciones:
    print(f"Publicacion: {p.publicacion}")