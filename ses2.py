class Smart:
    def __init__(self, tipo, serial, costo) -> None:
        self.tipo = tipo
        self.serial = serial
        self.costo = costo

    def actualizar_costo(self, costo):
        if costo > 500:
            self.costo = costo
        else:
            print("Costo no válido...")

    def __str__(self) -> str:
        return f"Objeto: {self.serial}"

if __name__ == "__main__":
    dispositivos = []
    print("="*30)
    while True:
                                                        #lower
        op = input("Quiere agrera otro dispositivo S/N: ").upper()
        if op == "S":
            # creacion de objeto y agregar a lista
            tipo = input("Tipo de dispositivos: ")
            serial = input("Serial del dispositivo: ")
            costo = int(input("costo del dispositivo: "))
            obj = Smart(tipo, serial, costo)
            dispositivos.append(obj)
        elif op == "N":
            break
        else:
            pass
    for s in dispositivos:
        print(s)        #Aqui me refiero al objeto completo

    # Resto de Operaciones CRUD
    while True:
        op = int(input("""Que desea hacer: 
                       1. Buscar
                       2. Eliminar
                       3. Salir
                       """))
        if op == 3:
            break
        elif op == 1:
            serial = input("Digite el serial a buscar: ")
            for s in dispositivos:
                if serial == s.serial:
                    print(f"Encontrado: Objeto: {s.tipo} - {s.serial} - {s.costo}")
                    costo = int(input("Digite el nuevo costo: "))
                    s.actualizar_costo(costo)
                    break
                else:
                    print("No encontrado...")
        elif op == 2:
            # eliminar: pop, remove
            tam = len(dispositivos)
            contador = 0
            for s in dispositivos:
                contador += 1
                print(f"Objeto: {s.tipo} - {s.serial} - ${s.costo}")
            borrar = int(input(f"Cual objeto desea eliminar? 1-{tam}: "))
            dispositivos.pop(borrar-1)
        else:
            print("Opcion incorrecta...")
print("Programa Principal...")
