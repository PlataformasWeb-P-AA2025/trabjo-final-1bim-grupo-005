from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#8   Consultar el número de reacciones por tipo de emoción de un usuario específico.
# Primero, definimos el usuario específico del que queremos obtener las reacciones.
usuario_especifico = "Hunter"
# Luego, realizamos la consulta para contar las reacciones por tipo de emoción del usuario específico.
reacciones = session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion)).join(Publicacion).join(Usuario).filter(Usuario.nombre == usuario_especifico).group_by(Reaccion.tipo_emocion).all()


for r in reacciones:
    print(f"{r[0]}: {r[1]} veces")
