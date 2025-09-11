
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

cursos = []

while True:
    menu()
    opcion = input("> ")

    if opcion == "1":
        print("► Registrar nuevo curso")
        nombre_curso = input("Ingresa el nombre del curso: ")
        nota_curso = int(input("Ingresa la nota del curso: "))
        cursos.append({"NOMBREE": nombre_curso, "NOTA": nota_curso})
        print(f"Curso '{nombre_curso}' con una nota de: '{nota_curso}' registrado.\n")
        
    elif opcion == "2":
        print("► Mostrar todos los cursos")
        if cursos:
            print("Cursos registrados:")
            for i, curso in enumerate(cursos, start=1):
                print(f"{i}. {curso}")
            print()
        else:
            print("No hay cursos registrados aún.\n")
        
    elif opcion == "3":
        print("► Calcular promedio general")
        if cursos:
            total_suma_notas = 0
            print("El promedio de los cursos registrados son")
            for curso in cursos:
                total_suma_notas += curso["NOTA"]
            promedio = total_suma_notas / len(cursos)
            print(f"El promedio general es: {promedio:.2f}\n")
        else:
            print("No hay cursos registrados aún.\n")
        
    elif opcion == "4":
        print("► Contar cursos aprobados y reprobados")
        if cursos:
            nota_minima=int(input("Ingrese la nota minima de los cursos"))
            aprobados = 0
            reprobados = 0 
            for curso in cursos:
                if curso["NOTA"] < nota_minima:
                    reprobados += 1
                else:
                    aprobados +=1
            print(f"El estudiante ha aprobado '{aprobados}' cursos y reprobados '{reprobados}'")     
        
    elif opcion == "5":
        print("► Buscar curso por nombre")
        
    elif opcion == "6":
        print("► Actualizar nota de un curso")

    elif opcion == "7":
        print("► Eliminar un curso")

    elif opcion == "8":
        print("► Ordenar por nota (burbuja)")

    elif opcion == "9":
        print("► Ordenar por nombre (inserción)")

    elif opcion == "10":
        print("► Buscar por nombre (búsqueda binaria)")

    elif opcion == "11":
        print("► Simular cola de revisión")

    elif opcion == "12":
        print("► Mostrar historial de cambios (pila)")

    elif opcion == "13":
        print("Saliendo del programa. Gracias por usar el Gestor De Notas.")
        break

    else:
        print(" Opción no válida. Ingrese un numero del 1 al 13.Intente de nuevo.")
    
