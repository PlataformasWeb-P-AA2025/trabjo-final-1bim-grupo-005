from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#6 ¿Cuántas publicaciones ha realizado cada usuario y cuántas reacciones totales han recibido en sus publicaciones?

# accedemos a los usuarios y las unimos con las publicaciones
reporte_publicaciones_reacciones = session.query(Usuario).join(Publicacion).all()
# Recorremos cada usuario y contamos sus publicaciones y reacciones
total = 0
for r in reporte_publicaciones_reacciones:
    print(f"Usuario: {r.nombre} -> Publicaciones Realizadas: {len(r.publicaciones)}")
    sum = 0
    publicaciones = session.query(Publicacion).filter(Publicacion.usuario_id == r.id).all()

    for p in publicaciones:
        reacciones = session.query(Reaccion).filter(Reaccion.publicacion_id == p.id).all()
        sum += len(reacciones)
        total += len(reacciones)
    print(f"                        -> Reacciones Totales Realizadas: {sum}")

    print('-' * 50)

print(f"Total de reacciones: {total}")
