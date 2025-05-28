from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#4Obtener un reporte de reacciones en función del número de veces que fueron usadas.


# https://stackoverflow.com/questions/14754994/why-is-sqlalchemy-count-much-slower-than-the-raw-query
reporte_reacciones_cantidad = session.query(Reaccion.tipo_emocion,func.count(Reaccion.id)).group_by(Reaccion.tipo_emocion).all()
for r in reporte_reacciones_cantidad:
    print(f"Reaccion: {r[0]} -> Cantidad: {r[1]}")