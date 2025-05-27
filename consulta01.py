from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import cadena_base_datos
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas_arte = session.query(Entrega).all()

for entrega in entregas_arte:
    tarea = entrega.tarea
    curso = tarea.curso
    departamento = curso.departamento

    if departamento.nombre == "Arte":
        estudiante = entrega.estudiante
        instructor = curso.instructor

        print(f"Tarea: {tarea.titulo}")
        print(f"Estudiante: {estudiante.nombre}")
        print(f"Calificación: {entrega.calificacion}")
        print(f"Instructor: {instructor.nombre}")
        print(f"Departamento: {departamento.nombre}")
        print("-" * 40)
