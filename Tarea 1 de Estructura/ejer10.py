            # GESTOR DE TAREAS
# Bosquejo

    # Tareas a cargar:
    #
    # "Estudiar" → "alta"
    # "Leer" → "baja"
    # "Hacer tarea" → "alta"


    # Guardar las tareas como tuplas:
    #
    # ("Estudiar", "alta")
    # ("Leer", "baja")
    # ("Hacer tarea", "alta")
    #
    # Lista:
    # [
    #     ("Estudiar", "alta"),
    #     ("Leer", "baja"),
    #     ("Hacer tarea", "alta")
    # ]


    # Buscar tareas prioritarias:
    #
    # ¿"Estudiar" tiene prioridad "alta"?
    # "alta" == "alta" → SÍ
    # → agregar ("Estudiar", "alta")
    #
    # ¿"Leer" tiene prioridad "alta"?
    # "baja" == "alta" → NO
    #
    # ¿"Hacer tarea" tiene prioridad "alta"?
    # "alta" == "alta" → SÍ
    # → agregar ("Hacer tarea", "alta")
    #
    # Resultado:
    # [
    #     ("Estudiar", "alta"),
    #     ("Hacer tarea", "alta")
    # ]


    # Eliminar tarea:
    #
    # Descripción a eliminar:
    # "Estudiar"
    #
    # ¿tarea[0] == "Estudiar"?
    # → SÍ
    # → eliminar la tarea
    #
    # Lista final:
    # [
    #     ("Leer", "baja"),
    #     ("Hacer tarea", "alta")
    # ]

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea (self, descripcion, prioridad):
        tarea = (descripcion,prioridad)
        self.tareas.append(tarea)

    def tareas_prioritarias(self):
        prioritarias = []

        for descripcion, prioridad in self.tareas:
            if prioridad == "alta":
                prioritarias.append((descripcion, prioritarias))

        return prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break

#programa inicial

t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Hacer tarea", "alta")

print("Tareas prioritarias:")
print(t.tareas_prioritarias())

t.eliminar_completada("Estudiar")

print("Tareas después de eliminar:")
print(t.tareas)