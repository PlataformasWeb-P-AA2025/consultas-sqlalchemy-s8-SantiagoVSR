from sqlalchemy import func

# Suponiendo que ya tienes una sesión activa llamada 'session'

# Obtener todos los departamentos
departamentos_con_bajas_notas = session.query(Departamento).all()

# Iterar sobre los departamentos
for departamento in departamentos_con_bajas_notas:
    # Inicializar el contador de cursos
    numero_cursos = 0
    
    # Buscar los cursos del departamento
    for curso in departamento.cursos:
        # Buscar las tareas del curso
        for tarea in curso.tareas:
            # Buscar las entregas de la tarea
            for entrega in tarea.entregas:
                # Filtrar las entregas con calificaciones <= 0.3
                if entrega.calificacion is not None and entrega.calificacion <= 0.3:
                    numero_cursos += 1
                    break # Si una entrega cumple la condición, pasar al siguiente curso
            if numero_cursos > 0:
                break # Si un curso tiene una entrega que cumple la condición, pasar al siguiente departamento
    
    # Imprimir los resultados para cada departamento
    if numero_cursos > 0:
        print(f"Departamento: {departamento.nombre}, Número de Cursos con entregas <= 0.3: {numero_cursos}")