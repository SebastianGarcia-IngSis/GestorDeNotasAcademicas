# Función para mostrar el menú principal
def menu():
    print("▬▬▬▬▬▬▬▬▬▬GESTOR DE NOTAS ACADEMICAS▬▬▬▬▬▬▬▬▬▬")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir") 
    print("Seleccione una opción:")

# Lista principal de cursos
cursos = []

# Pila para guardar historial de cambios
historial = []

# Bucle principal del programa1

while True:
    menu()  # Mostrar menú principal
    opcion = input("> ")

    # OPCIÓN 1: Registrar nuevo curso
    if opcion == "1":
        print("► Registrar nuevo curso")
        nombre_curso = input("Ingresa el nombre del curso: ").upper()
        nota_curso = int(input("Ingresa la nota del curso: "))
        cursos.append({"NOMBREE": nombre_curso, "NOTA": nota_curso})
        print(f"Curso '{nombre_curso}' con una nota de {nota_curso} registrado.\n")

    # OPCIÓN 2: Mostrar todos los cursos
    elif opcion == "2":
        print("► Mostrar todos los cursos")
        if cursos:
            print("Cursos registrados:")
            for i, curso in enumerate(cursos, start=1):
                print(f"{i}. {curso}")
            print()
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 3: Calcular promedio general
    elif opcion == "3":
        print("► Calcular promedio general")
        if cursos:
            total_suma_notas = 0
            for curso in cursos:
                total_suma_notas += curso["NOTA"]
            promedio = total_suma_notas / len(cursos)
            print(f"El promedio general es: {promedio:.2f}\n")
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 4: Contar cursos aprobados y reprobados
    elif opcion == "4":
        print("► Contar cursos aprobados y reprobados")
        if cursos:
            nota_minima = int(input("Ingrese la nota mínima para aprobar: "))
            aprobados = 0
            reprobados = 0
            for curso in cursos:
                if curso["NOTA"] < nota_minima:
                    reprobados += 1
                else:
                    aprobados += 1
            print(f"El estudiante ha aprobado {aprobados} cursos y reprobado {reprobados}.\n")
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 5: Buscar curso por nombre (búsqueda lineal)
    elif opcion == "5":
        print("► Buscar curso por nombre")
        if cursos:
            nombre = input("Ingrese el nombre del curso que desea buscar: ").upper()
            encontrado = False
            for curso in cursos:
                if curso["NOMBREE"] == nombre:
                    print(f"El curso '{nombre}' está registrado con nota {curso['NOTA']}.\n")
                    encontrado = True
                    break
            if not encontrado:
                print("El curso que desea buscar no ha sido registrado.\n")
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 6: Actualizar nota de un curso
    elif opcion == "6":
        print("► Actualizar nota de un curso")
        if cursos:
            nombre = input("Ingrese el nombre del curso que desea actualizar: ").upper()
            encontrado = False
            for curso in cursos:
                if curso["NOMBREE"] == nombre:
                    nota_anterior = curso["NOTA"]
                    print(f"Nota actual de '{nombre}': {nota_anterior}")
                    nueva_nota = int(input("Ingrese la nueva nota: "))
                    curso["NOTA"] = nueva_nota
                    print(f"Nota del curso '{nombre}' actualizada a {nueva_nota}.\n")
                    historial.append(f"Se actualizó: {nombre} - Nota anterior: {nota_anterior} → Nueva nota: {nueva_nota}")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró ningún curso con ese nombre.\n")
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 7: Eliminar un curso
    elif opcion == "7":
        print("► Eliminar un curso")
        if cursos:
            nombre = input("Ingrese el nombre del curso que desea eliminar: ").upper()
            encontrado = False
            for curso in cursos:
                if curso["NOMBREE"] == nombre:
                    historial.append(f"Se eliminó: {curso['NOMBREE']} - Nota: {curso['NOTA']}")
                    cursos.remove(curso)
                    print(f"El curso '{nombre}' ha sido eliminado correctamente.\n")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró ningún curso con ese nombre.\n")
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 8: Ordenar cursos por nota (burbuja)
    elif opcion == "8":
        print("► Ordenar cursos por nota ")
        if cursos:
            n = len(cursos)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if cursos[j]["NOTA"] > cursos[j + 1]["NOTA"]:
                        cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
            print("Cursos ordenados por nota de menor a mayor.\n")
            for i, curso in enumerate(cursos, start=1):
                print(f"{i}. {curso['NOMBREE']} → {curso['NOTA']}")
            print()
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 9: Ordenar cursos por nombre (inserción)
    elif opcion == "9":
        print("► Ordenar cursos por nombre ")
        if cursos:
            for i in range(1, len(cursos)):
                actual = cursos[i]
                j = i - 1
                while j >= 0 and cursos[j]["NOMBREE"] > actual["NOMBREE"]:
                    cursos[j + 1] = cursos[j]
                    j -= 1
                cursos[j + 1] = actual
            print("Cursos ordenados alfabéticamente por nombre.\n")
            for i, curso in enumerate(cursos, start=1):
                print(f"{i}. {curso['NOMBREE']} → {curso['NOTA']}")
            print()
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 10: Buscar curso por nombre (búsqueda binaria)
    elif opcion == "10":
        print("► Buscar curso por nombre")
        if cursos:
            cursos.sort(key=lambda x: x["NOMBREE"])
            nombre = input("Ingrese el nombre del curso que desea buscar: ").upper()
            inicio = 0
            fin = len(cursos) - 1
            encontrado = False
            while inicio <= fin:
                medio = (inicio + fin) // 2
                if cursos[medio]["NOMBREE"] == nombre:
                    print(f"El curso '{nombre}' fue encontrado con nota: {cursos[medio]['NOTA']}.\n")
                    encontrado = True
                    break
                elif cursos[medio]["NOMBREE"] < nombre:
                    inicio = medio + 1
                else:
                    fin = medio - 1
            if not encontrado:
                print("No se encontró ningún curso con ese nombre.\n")
        else:
            print("No hay cursos registrados aún.\n")

    # OPCIÓN 11: Simular cola de solicitudes de revisión
    elif opcion == "11":
        print("► Simular cola de solicitudes de revisión")
        from collections import deque
        cola_revision = deque()

        while True:
            print("\n--- MENÚ DE COLA DE REVISIÓN ---")
            print("1. Agregar solicitud de revisión")
            print("2. Atender siguiente solicitud")
            print("3. Ver solicitudes pendientes")
            print("4. Salir de la simulación")
            opcion_cola = input("> ")

            if opcion_cola == "1":
                nombre_curso = input("Ingrese el nombre del curso a revisar: ").upper()
                cola_revision.append(nombre_curso)
                print(f"Solicitud para '{nombre_curso}' agregada a la cola.")

            elif opcion_cola == "2":
                if cola_revision:
                    curso_atendido = cola_revision.popleft()
                    print(f"Se ha atendido la solicitud del curso '{curso_atendido}'.")
                else:
                    print("No hay solicitudes pendientes.")

            elif opcion_cola == "3":
                if cola_revision:
                    print("Solicitudes pendientes:")
                    for i, curso in enumerate(cola_revision, start=1):
                        print(f"{i}. {curso}")
                else:
                    print("No hay solicitudes en espera.")

            elif opcion_cola == "4":
                print("Saliendo de la simulación de cola...\n")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

    # OPCIÓN 12: Mostrar historial de cambios(pila)
    elif opcion == "12":
        print("► Mostrar historial de cambios")
        if historial:
            print("Historial de cambios recientes (último cambio arriba):")
            for i, cambio in enumerate(reversed(historial), start=1):
                print(f"{i}. {cambio}")
            print()
        else:
            print("No hay cambios registrados aún.\n")

    # OPCIÓN 13: Salir del programa
    elif opcion == "13":
        print("Saliendo del programa...")
        print("Gracias por usar el Gestor de Notas Académicas.")
        print("Desarrollado por: SebastianGarcia-IngSis")
        break

    else:
        print("Opción no válida. Ingrese un número del 1 al 13.\n")
