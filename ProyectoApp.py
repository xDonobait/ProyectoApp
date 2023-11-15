class Tarea:
    def __init__(self, descripcion, materia, fecha_entrega):
        self.descripcion = descripcion
        self.materia = materia
        self.fecha_entrega = fecha_entrega
        self.siguiente = None


class ListaTareas:
    def __init__(self):
        self.head = None

    def agregar_tarea(self, tarea):
        if not self.head:
            self.head = tarea
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = tarea

    def mostrar_tareas(self):
        current = self.head
        while current:
            print(f"Descripción: {current.descripcion}")
            print(f"Materia: {current.materia}")
            print(f"Fecha de entrega: {current.fecha_entrega}")
            print("------")
            current = current.siguiente

    def buscar_tarea(self, descripcion):
        current = self.head
        while current:
            if current.descripcion == descripcion:
                return current
            current = current.siguiente
        return None

    def actualizar_tarea(self, descripcion, nueva_descripcion, nueva_materia, nueva_fecha_entrega):
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            tarea.descripcion = nueva_descripcion
            tarea.materia = nueva_materia
            tarea.fecha_entrega = nueva_fecha_entrega
            print("Tarea actualizada exitosamente.")
        else:
            print("Tarea no encontrada.")

    def eliminar_tarea(self, descripcion):
        current = self.head
        if current and current.descripcion == descripcion:
            self.head = current.siguiente
            print("Tarea eliminada exitosamente.")
            return
        while current and current.siguiente:
            if current.siguiente.descripcion == descripcion:
                current.siguiente = current.siguiente.siguiente
                print("Tarea eliminada exitosamente.")
                return
            current = current.siguiente
        print("Tarea no encontrada.")


def menu():
    lista_tareas = ListaTareas()

    while True:
        print("\nMenú:")
        print("1. Crear tarea")
        print("2. Actualizar tarea")
        print("3. Eliminar tarea")
        print("4. Ver todas las tareas")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            materia = input("Ingrese la materia de la tarea: ")
            fecha_entrega = input("Ingrese la fecha de entrega de la tarea: ")
            nueva_tarea = Tarea(descripcion, materia, fecha_entrega)
            lista_tareas.agregar_tarea(nueva_tarea)

        elif opcion == "2":
            descripcion = input("Ingrese la descripción de la tarea a actualizar: ")
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nueva_materia = input("Ingrese la nueva materia: ")
            nueva_fecha_entrega = input("Ingrese la nueva fecha de entrega: ")
            lista_tareas.actualizar_tarea(descripcion, nueva_descripcion, nueva_materia, nueva_fecha_entrega)

        elif opcion == "3":
            descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
            lista_tareas.eliminar_tarea(descripcion)

        elif opcion == "4":
            lista_tareas.mostrar_tareas()

        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()