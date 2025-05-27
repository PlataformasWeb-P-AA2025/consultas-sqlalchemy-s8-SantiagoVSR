from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import cadena_base_datos  # Asegúrate de que la ruta y el nombre del archivo sean correctos

# Importamos las clases
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

# Configuración de la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta: Obtener entregas de estudiantes de cursos del departamento de Arte
entregas_arte = session.query(
    Tarea.titulo.label("titulo_tarea"),
    Estudiante.nombre.label("nombre_estudiante"),
    Entrega.calificacion,
    Instructor.nombre.label("nombre_instructor"),
    Departamento.nombre.label("nombre_departamento")
).join(Tarea, Entrega.tarea) \
 .join(Estudiante, Entrega.estudiante) \
 .join(Curso, Tarea.curso) \
 .join(Departamento, Curso.departamento) \
 .join(Instructor, Curso.instructor) \
 .filter(Departamento.nombre == "Arte") \
 .all()

# Mostrar los resultados
for entrega in entregas_arte:
    print(f"Tarea: {entrega.titulo_tarea}")
    print(f"Estudiante: {entrega.nombre_estudiante}")
    print(f"Calificación: {entrega.calificacion}")
    print(f"Instructor: {entrega.nombre_instructor}")
    print(f"Departamento: {entrega.nombre_departamento}")
    print("-" * 40)
