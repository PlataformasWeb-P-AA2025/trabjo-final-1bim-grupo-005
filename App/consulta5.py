from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#5Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" que sean de usuarios que cuyos nombre no inicien con vocal.

emociones = ["alegre","enojado","pensativo"]

listar_reacciones_like = session.query(Reaccion).join(Usuario) \
    .filter(Reaccion.tipo_emocion.in_(emociones)) \
    .filter( not_(or_(Usuario.nombre.ilike("a%"),Usuario.nombre.ilike("e%"),Usuario.nombre.ilike("i%"),Usuario.nombre.ilike("o%"),Usuario.nombre.ilike("u%")))).all()
            
for f in listar_reacciones_like:
    print(f"Nombre: {f.usuario.nombre} -> Emocion: {f.tipo_emocion}")
    
#5.1
emociones = ["alegre","enojado","pensativo"]
listar_reacciones_like = session.query(Reaccion).join(Usuario).filter(and_(Usuario.nombre.not_like('A%'),Usuario.nombre.not_like('E%'),Usuario.nombre.not_like('I%'),Usuario.nombre.not_like('O%'),Usuario.nombre.not_like('U%')),Reaccion.tipo_emocion.in_(emociones)).all()
for r in listar_reacciones_like:
    print(f"Usuario: {r.usuario.nombre} -> Emocion: {r.tipo_emocion}")
    
print(listar_reacciones_like.size())