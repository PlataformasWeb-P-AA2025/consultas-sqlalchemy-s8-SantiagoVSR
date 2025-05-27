from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import cadena_base_datos
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

nombres_estudiantes = [
    "Jennifer Bolton",
    "Elaine Perez",
    "Heather Henderson",
    "Charles Harris"
]

# Obtener los estudiantes filtrando por nombre
estudiantes = session.query(Estudiante).filter(Estudiante.nombre.in_(nombres_estudiantes)).all()

# Usar un diccionario para evitar duplicar tareas
tareas_dict = {}

for estudiante in estudiantes:
    for entrega in estudiante.entregas:
        tarea = entrega.tarea
        if tarea.id not in tareas_dict:
            tareas_dict[tarea.id] = {
                'titulo': tarea.titulo,
                'num_entregas': len(tarea.entregas)
            }

# Mostrar resultados
for tarea_info in tareas_dict.values():
    print(f"Tarea: {tarea_info['titulo']}  --- Número de entregas: {tarea_info['num_entregas']}")
