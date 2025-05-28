from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()



#3Mostrar en qué publicaciones reaccionó un usuario.

listar_reacionesXusuario = session.query(Publicacion).join(Reaccion).all()
for u in listar_reacionesXusuario:
    print(f"Publicacion: {u.publicacion}")