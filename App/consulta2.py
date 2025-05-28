from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#2Listar las reacciones a una publicación.

listar_reacciones = session.query(Reaccion).join(Publicacion).filter(Publicacion.publicacion == "Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada." ).all()
print("Publicacion: Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada.")
for r in listar_reacciones:
    print(f"Reacciones: {r.tipo_emocion}")