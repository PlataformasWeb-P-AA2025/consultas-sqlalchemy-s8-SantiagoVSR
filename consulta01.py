from sqlalchemy.orm import sessionmaker  
from sqlalchemy import create_engine  
from config import cadena_base_datos  
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega  

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)  
session = Session()  

entregas_arte = session.query(Entrega).all()  # Realiza una consulta para obtener todas las entregas de la base de datos.

for entrega in entregas_arte:  # Itera sobre cada entrega obtenida.
    tarea = entrega.tarea  # Obtiene la tarea asociada a la entrega.
    curso = tarea.curso  # Obtiene el curso asociado a la tarea.
    departamento = curso.departamento  # Obtiene el departamento asociado al curso.

    if departamento.nombre == "Arte":  # Verifica si el nombre del departamento es "Arte".
        estudiante = entrega.estudiante  # Obtiene el estudiante asociado a la entrega.
        instructor = curso.instructor  # Obtiene el instructor asociado al curso.

        print(f"Tarea: {tarea.titulo}")  # Imprime el título de la tarea.
        print(f"Estudiante: {estudiante.nombre}")  # Imprime el nombre del estudiante.
        print(f"Calificación: {entrega.calificacion}")  # Imprime la calificación de la entrega.
        print(f"Instructor: {instructor.nombre}")  # Imprime el nombre del instructor.
        print(f"Departamento: {departamento.nombre}")  # Imprime el nombre del departamento.
        print("-" * 40)  # Imprime una línea separadora.
