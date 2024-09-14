class Animal:
    '''Clase para representar un animal.'''
    def __init__(self, especie:str, edad:str) -> None:
        self.especie = especie
        self.edad = edad

    # def info(self):
    #     print(f'Especie: {self.especie}, Edad: {self.edad}')

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"
    

class Mascota(Animal):
    '''Clase para representar una mascota, heredada de la clase Animal.'''
    def __init__(self, especie: str, edad: str, nombre: str) -> None:
        super().__init__(especie, edad)
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}, Nombre: {self.nombre}]"    

class RegistroMascotas:
    '''Clase para representar un registro de mascotas.'''
    def __init__(self) -> None:
        self.mascotas = []


    def agregar_mascota(self,mascota):
        '''
        Agrega una mascota al registro.
        
        Parameters:
            mascota (Mascota): La mascota a agregar al registro.
        '''
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        '''
            Listar todas las mascotas registradas.
        '''
        if self.mascotas:
            print(" Lista de mascotas \n", '=' *30)
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        else:
            print('No hay mascotas registradas.')        

    def editar_mascota(self, index, nueva_mascota):
        '''
        Editar una mascota en el registro.

        Parameters:
            index (int): El índice de la mascota a editar.
            nueva_mascota (Mascota): La nueva información de la mascota.
        '''
        if index < 0 or index >= len(self.mascotas):
            print('No hay registro con ese indice')
        else:
            self.mascotas[index] = nueva_mascota

    def eliminar_mascota(self, index):
        '''
        Eliminar una mascota
        
        Parameters:
            index (int): El índice de la mascota a eliminar.
        '''
        if index< 0 or index >= len(self.mascotas):
            print('No hay registro con ese indice')
        else:
            del self.mascotas[index]
            print('Mascota eliminada correctamente')