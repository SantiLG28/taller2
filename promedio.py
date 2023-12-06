import numpy as np

def crear_archivo_notas(nombre_archivo, num_estudiantes, num_materias):
    np.random.seed(42)  # Para reproducibilidad

    # Generar nombres de materias
    nombres_materias = [f"Materia-{i + 1}" for i in range(num_materias)]

    with open(nombre_archivo, 'w') as file:
        # Escribir la primera línea con los nombres de las materias
        file.write("Estudiante," + ",".join(nombres_materias) + '\n')

        # Escribir las notas de cada estudiante
        for _ in range(num_estudiantes):
            notas_estudiante = np.round(np.random.uniform(1, 5, num_materias), 1)  # Notas aleatorias entre 1 y 5 con 1 decimal
            nombre_estudiante = f"Estudiante-{_ + 1}"
            file.write(f"{nombre_estudiante}," + ','.join(map(str, notas_estudiante)) + '\n')

def cargar_notas_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        nombres_materias = header[1:]  # Excluir el primer elemento que es "Estudiante"

        notas = []

        for line in lines[1:]:
            clean_line = line.strip()
            if not clean_line:
                continue

            try:
                elementos = clean_line.split(',')
                nombre_estudiante = elementos[0]
                valores = [float(valor) for valor in elementos[1:]]
                notas.append((nombre_estudiante, valores))
            except ValueError as e:
                print(f"Error al convertir las notas: {e}")
                print(f"Línea problemática: {clean_line}")

    return nombres_materias, notas

def calcular_promedios(notas):
    promedios_estudiantes = np.mean([nota[1] for nota in notas], axis=1)
    promedios_materias = np.mean([nota[1] for nota in notas], axis=0)
    return promedios_estudiantes, promedios_materias

def obtener_mejor_estudiante(promedios_estudiantes):
    mejor_estudiante = np.argmax(promedios_estudiantes)
    mejor_promedio_estudiante = promedios_estudiantes[mejor_estudiante]
    return mejor_estudiante, mejor_promedio_estudiante

def obtener_materias_destacadas(promedios_materias):
    materia_mas_perdida = np.argmin(promedios_materias)
    materia_mas_ganada = np.argmax(promedios_materias)
    return materia_mas_perdida, materia_mas_ganada

def imprimir_resultados(nombres_materias, notas, promedios_estudiantes, promedios_materias, mejor_estudiante,
                        mejor_promedio_estudiante, materia_mas_perdida, materia_mas_ganada):
    # Obtener nombres de estudiantes
    nombres_estudiantes = [nota[0] for nota in notas]

    print("Promedio de cada estudiante:")
    for nombre_estudiante, promedio in zip(nombres_estudiantes, promedios_estudiantes):
        print(f"{nombre_estudiante}: {promedio:.1f}")

    print("\nPromedio del grupo en cada materia:")
    for nombre_materia, promedio in zip(nombres_materias, promedios_materias):
        print(f"{nombre_materia}: {promedio:.1f}")

    print(f"\nMejor estudiante: {nombres_estudiantes[mejor_estudiante]} con promedio {mejor_promedio_estudiante:.1f}")
    print(f"Materia más perdida: {nombres_materias[materia_mas_perdida]}")
    print(f"Materia más ganada: {nombres_materias[materia_mas_ganada]}")

    estudiantes_ordenados = sorted(range(len(promedios_estudiantes)), key=lambda x: promedios_estudiantes[x])
    print(f"\nLista ordenada de estudiantes por promedio: {estudiantes_ordenados}")

def main():
    nombre_archivo = 'Notas.txt'
    num_estudiantes = 5
    num_materias = 3  # Modifica el número de materias según tus necesidades

    # Crear archivo de notas
    crear_archivo_notas(nombre_archivo, num_estudiantes, num_materias)

    # Cargar notas desde el archivo
    nombres_materias, notas = cargar_notas_desde_archivo(nombre_archivo)

    # Calcular promedios
    promedios_estudiantes, promedios_materias = calcular_promedios(notas)

    # Obtener mejor estudiante
    mejor_estudiante, mejor_promedio_estudiante = obtener_mejor_estudiante(promedios_estudiantes)

    # Obtener materias destacadas
    materia_mas_perdida, materia_mas_ganada = obtener_materias_destacadas(promedios_materias)

    # Imprimir resultados
    imprimir_resultados(nombres_materias, notas, promedios_estudiantes, promedios_materias, mejor_estudiante, mejor_promedio_estudiante,
                        materia_mas_perdida, materia_mas_ganada)

if __name__ == "__main__":
    main()