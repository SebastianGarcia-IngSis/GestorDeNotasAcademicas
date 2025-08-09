<<<<<<< HEAD
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
        
    elif opcion == "2":
        print("► Mostrar todos los cursos")
        
    elif opcion == "3":
        print("► Calcular promedio general")
        
    elif opcion == "4":
        print("► Contar cursos aprobados y reprobados")
        
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
    
=======
print ("Hola mundo")
>>>>>>> origin/main
