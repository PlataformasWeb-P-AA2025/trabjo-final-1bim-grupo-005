from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from generar_base import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

 #7Listar las publicaciones que han recibido solo un tipo de emoción (por ejemplo, solo 'alegre') y los usuarios que han reaccionado a esa publiacion del id2.
 #accedemos a la tabla publicaciones y luego a la de reaccion despues filtramos despues con el and ponemos las condiciones de algre y el id de 3 y lo agrupamos con el id pubicaciones
listar_publicaciones_un_tipo_emocion = session.query(Publicacion).join(Reaccion).filter(and_(Reaccion.tipo_emocion == 'alegre', Publicacion.id==3)).group_by(Publicacion.id).all()
print("Publicaciones con solo un tipo de emoción (alegre):")
# Recorremos las publicaciones filtradas y mostramos los usuarios que reaccionaron a cada una de ellas
for publicacion in listar_publicaciones_un_tipo_emocion:
    print(f"Publicación: {publicacion.publicacion}")
    # Obtener los usuarios que reaccionaron a esta publicación
    usuarios_reaccionados = session.query(Usuario).join(Reaccion).filter(Reaccion.publicacion_id == publicacion.id).all()
    for usuario in usuarios_reaccionados:
        print(f"   Usuario que reaccionó: {usuario.nombre}")
    print("-" * 50)

