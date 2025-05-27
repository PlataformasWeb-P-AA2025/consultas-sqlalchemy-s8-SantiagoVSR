
from sqlalchemy.orm import sessionmaker  
from sqlalchemy import create_engine, func  
from config import cadena_base_datos  
from clases import Curso, Entrega, Tarea

# 1. Configuración de la base de datos
engine = create_engine(cadena_base_datos)  
Session = sessionmaker(bind=engine)  
session = Session()  

# 2. Obtener todos los cursos
cursos = session.query(Curso).all()  # Consultamos todos los cursos.

# 3. Iterar sobre los cursos y calcular el promedio de calificaciones
for curso in cursos:
    # 4. Obtener las entregas del curso
    # Usamos una relación inversa para acceder a las entregas a través de la tarea
    entregas = []
    for tarea in curso.tareas:
        entregas.extend(tarea.entregas)

    # 5. Calcular el promedio de calificaciones
    if entregas:  # Verificamos si hay entregas
        # Usamos una comprensión de lista para sumar las calificaciones
        # y excluimos las calificaciones que sean None.
        calificaciones = [entrega.calificacion for entrega in entregas if entrega.calificacion is not None]
        if calificaciones:  # Verificamos si hay calificaciones válidas
            promedio_calificaciones = sum(calificaciones) / len(calificaciones)
        else:
            promedio_calificaciones = 0.0  # No hay calificaciones válidas
    else:
        promedio_calificaciones = 0.0  # No hay entregas

    # 6. Imprimir el resultado
    print(f"Curso: {curso.titulo}, Promedio de Calificaciones: {promedio_calificaciones:.2f}")

# 7. Cerrar la sesión (buena práctica)
session.close()