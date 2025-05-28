from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#9 Las publiaciones que no tienen reacciones.
#se obtiene las publicaciones 
publicaciones = session.query(Publicacion).all()
# 
for p in publicaciones:
    #se pone la condicional si la publicacion tine 0 reacciones que se muestre
    if (len(p.reacciones)==0):
        print(f"Publicacion: {p.publicacion} - No tiene reacciones")
    
    print()