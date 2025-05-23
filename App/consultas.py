from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#1
listar_publicaciones = session.query(Publicacion).join(Usuario).filter(Usuario.nombre == "Premier League").all()

print("Usuario: Premier League")
for p in listar_publicaciones:
    print(f"Publicacion: {p.publicacion}")
#2
listar_reacciones = session.query(Reaccion).join(Publicacion).filter(Publicacion.publicacion == "Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada." ).all()
print("Publicacion: Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada.")
for r in listar_reacciones:
    print(f"Reacciones: {r.tipo_emocion}")
#3
listar_reacionesXusuario = session.query(Publicacion).join(Reaccion).all()
for u in listar_reacionesXusuario:
    print(f"Publicacion: {u.publicacion}")
#4

# https://stackoverflow.com/questions/14754994/why-is-sqlalchemy-count-much-slower-than-the-raw-query
reporte_reacciones_cantidad = session.query(Reaccion.tipo_emocion,func.count(Reaccion.id)).group_by(Reaccion.tipo_emocion).all()
for r in reporte_reacciones_cantidad:
    print(f"Reaccion: {r[0]} -> Cantidad: {r[1]}")

#5
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