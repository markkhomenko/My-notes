# -*- coding: utf-8 -*-


class Mascota(object):
    def __init__(self,MNombre=None,MRaza=None,MPeso=None,MCodMascota=None,MDuenio=None):
        self.__MNombre=MNombre
        self.__MRaza=MRaza
        self.__MPeso=MPeso
        self.__MCodMascota=MCodMascota
        self.__MDuenio=MDuenio
        
        
        def get_MNombre(self):
            """Devuelve el nombre de una mascota"""
            return self.__MNombre
        def get_MRaza(self):
            """Devuelve la raza de una Mascota"""
            return self.__MRaza
        def get_MPeso(self):
            """Devuelve el peso de una mascota"""
            return self.__MPeso         
        def get_MCodMascota(self):
            """Devuelve el codigo de una mascota"""
            return self.__MCodMascota
        
        def set_MNombre(self,nom):
            """Modifica el nombre de una MAscota"""
            self.__MNombre=nom
        def set__MRaza(self,nraza):
            """Modifica la raza de una mascota"""
            self.__MRaza=nraza
        def set_MPeso(self,npeso):
            """Modifica el peso de una mascota"""
            self.__MPeso=npeso
        def set_MCodMascota(self,nCodMascota):
            """Modifica el codigo de una mascotA"""
            self.__MCodMascota=nCodMascota 
 

class Prueba_mascota(object):
    def cargar_Mascotas():
        lista_mascotas = []
             
        m1= Mascota()
        m1.set_MNombre("Manchita")
        m1.set_MRaza("Pichichen")
        m1.set_MPeso(7)
        m1.set_MCodMascota(1)
        lista_mascotas.append(m1)
        
        m2= Mascota()
        m2.set_MNombre("Dalton")
        m2.set_MRaza("Golden")
        m2.set_MPeso(10)
        m2.set_MCodMascota(2)
        lista_mascotas.append(m2)
       
        m3= Mascota()
        m3.set_MNombre("Simon")
        m3.set_MRaza("Boxer")
        m3.set_MPeso(13)
        m3.set_MCodMascota(3)
        lista_mascotas.append(m3)      
        
        m4= Mascota()
        m4.set_MNombre("Anita")
        m4.set_MRaza("Pointer")
        m4.set_MPeso(4)
        m4.set_MCodMascota(4)
        lista_mascotas.append(m4)  
        
        m5= Mascota()
        m5.set_MNombre("Corbata")
        m4.set_MRaza("Collie")
        m4.set_MPeso(5)
        m4.set_MCodMascota(5)
        lista_mascotas.append(m5)  
        
        m6= Mascota()
        m6.set_MNombre("Socrates")
        m6.set_MRaza("Dalmata")
        m6.set_MPeso(6)
        m6.set_MCodMascota(6)
        lista_mascotas.append(m6) 
        
        m7= Mascota()
        m7.set_MNombre("Pancho")
        m7.set_MRaza("Bull Terrie")
        m7.set_MPeso(7)
        m7.set_MCodMascota(7)
        lista_mascotas.append(m7) 
       
       
        m=Mascota()
        for m in lista_mascotas:
           print m.get_MNombre()
        return lista_mascotas       
            
        
        
    
    