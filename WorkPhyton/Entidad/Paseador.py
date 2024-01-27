# -*- coding: utf-8 -*-


class Paseador(object):
    def __init__(self,pApellido=None,pNombre=None,pDNI=None,pTelefono=None):
        self.__pApellido=pApellido
        self.__pNombre=pNombre
        self.__pDNI=pDNI
        self.__pTelefono=pTelefono
        
        def get_pApellido(self):
            """Devuelve el apellido del Paseador"""
            return self.__pApellido
        def get_pNombre(self):
            """Devuelve el nombre del paseador"""
            return self.__pNombre
        def get_pDNI(self):
            """Devuelve el dni del paseador"""
            return self.__pDNI
        def get_pTelefono(self):
            """Devuelve el telefono del paseador"""
            return self.__pTelefono
        
        def set_pApellido(self,nuevoApellido):
            """Modifica el apellido del paseador"""            
            self.__pApellido=nuevoApellido
        def set_pNombre(self,nuevoNombre):
            """Modifica el nombre del paseador"""            
            self.__pNombre=nuevoNombre
        def set_pDNI(self,nuevoDni):
            """modifca el dni del paseador"""
            self.__pDNI=nuevoDni           
        def set_pTelefono(self,nuevoTelefono):
            """modifica el telefono del paseador"""
            self.pTelefono=nuevoTelefono
            
class Prueba_cliente(object):
    def cargar_Clientes():
        lista_paseadores = []
             
        p1 = Paseador()
        p1.set_pApellido("Gomez")
        p1.set_pNombre("Fernando")
        p1.set_pDNI("35.123.112")
        lista_paseadores.append(p1)
          
        
        p2 = Paseador()
        p2.set_pApellido("Perez")
        p2.set_pNombre("Roberto")
        p2.set_pDNI("35.123.223")
        lista_paseadores.append(p2)
        
        p3 = Paseador()
        p3.set_pApellido("Correa")
        p3.set_pNombre("Hernan")
        p3.set_pDNI("32.444.000")
        lista_paseadores.append(p3)
        
        return lista_paseadores
            
       
        
                  