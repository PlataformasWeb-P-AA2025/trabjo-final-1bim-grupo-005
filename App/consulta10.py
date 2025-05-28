from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#10¿Cuáles son los tres tipos de emoción más usados en toda la plataforma?
#se hace un query del tipo de emocion de la tabla de reaccion y la cantidad de veces que hay y luego se agrupa por tipo de emocion para posteriormente ordenarlos de menor a mayor y sacar los 3 primeros
reacciones = session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion)).group_by(Reaccion.tipo_emocion).order_by(func.count(Reaccion.tipo_emocion).desc()).limit(3).all()
#for para presentarS
for r in reacciones:
    print(f"{r[0]}: {r[1]} veces")