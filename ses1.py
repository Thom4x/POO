class Libro:
    #atributo de la clase: globales
    pasta_dura = "azul"

    # constructor o metodo inicializador con sus parametros
    def __init__(self, autor, titulo, pag):
        #atributos de instancia
        self.titulo = titulo
        self.autor = autor
        self.paginas = pag
        self.tipo = "Papel"
    
    def leer_libro(self, pag):
        print(f"estamos leyendo la {pag} página.")



    def __str__(self):
        return f"{self.titulo} - {self.autor}"
        


#Se debe agregar esta condicion siempre
if __name__ == "__main__":
    
    #crear objetos o instancias
    #instanciacion de la clase Libro
    p1 = Libro ("Stardos", "titanic", 400)
    print(p1)
    print(f"El libro es: {p1.titulo} con el autor de: {p1.autor} que tiene {p1.paginas} paginas...")
    
    #se puede llamar sin print
    p1.leer_libro(8)

#Listas en py

biblioteca = []
biblioteca.append(Libro("Carles Perez" , "Galaxia" , 100))
biblioteca.append(Libro("Carles Perez" , "Galaxia" , 110))
print(biblioteca)

for libro in biblioteca:
    print(libro)

print(":) "*90)