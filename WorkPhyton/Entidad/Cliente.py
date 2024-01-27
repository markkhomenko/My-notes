# -*- coding: utf-8 -*-


class Cliente(object):
    
        def __init__(self,dApellido=None,dNombre=None,dDireccion=None,dDNI=None,dTelefono=None):
            self.__dApellido=dApellido
            self.__dNombre=dNombre
            self.__dDireccion=dDireccion
            self.__dDNI=dDNI
            self.__dTelefono=dTelefono
        
        def get_dApellido(self):
            """Devuelve el apellido del dueño"""
            return self.__dApellido
        def get_dNombre(self):
            """Devuelve el nombre del dueño"""
            return self.__dNombre
        def get_dDireccion(self):
            """Devuelve la direccion del dueño"""
            return self.__dDireccion
        def get_dDNI(self):
            """Delvuelve el DNI del dueño"""
            return self.__dDNI
        def get_dTelefono(self):
            """Delvuelve el telefono del dueño"""
            return self.__dTelefono
        def get_dDuenio(self):
            return self.__dApellido,self.__dNombre,self.__dDireccion,self.__dDNI,self.__dTelefono
        
        def set_dApellido(self,nuevoApellido):
            """Modifica el apellido del dueño"""
            self.__dApellido=nuevoApellido
        def set_dNombre(self,nuevoNombre):
            """Modifica el nombre del dueño"""
            self.__dNombre=nuevoNombre
        def set_dDireccion(self,nuevaDireccion):
            """Modifica la direccion del dueño"""
            self.__dDireccion=nuevaDireccion
        def set_dDNI(self,nuevoDni):
            """Modifica el DNI del dueño"""
            self.__dDNI=nuevoDni    
        def set_dTelefono(self,nuevoTelefono):
            """Modifica el telefono del dueño"""
            self.__dTelefono=nuevoTelefono   
        
     
        
       
        
class Prueba_cliente(object):
    def cargar_Clientes():
        lista_cliente = []
             
        d1=Cliente()
        d1.set_dApellido("Garcia")
        d1.set_dNombre ("Francisco")
        d1.set_dDireccion ("Alvear y Gouchon")
        d1.set_dTelefono ("03447-15432211")
        d1.set_dDNI("1")
        lista_cliente.append(d1)
          
        d2=Cliente()
        d2.set_dApellido("PiedraBuena")
        d2.set_dNombre ("Roberto")
        d2.set_dDireccion("J.J Paso 213")
        d2.set_dTelefono("03447-1543450")
        d2.set_dDNI("2")
        lista_cliente.append(d2)
            
        d3=Cliente()
        d3.set_dApellido ("Ciano")
        d3.set_dNombre  ("Omar")
        d3.set_dDireccion("M. Fernandez 009")
        d3.set_dTelefono( "03447-15401256")
        d3.set_dDNI("3")
        lista_cliente.append(d3)
            
        d4=Cliente()
        d4.set_dApellido("Fisio")
        d4.set_dNombre("Eddy")
        d4.set_dDireccion( "San Martin 92")
        d4.set_dTelefono("03447-15456788")
        d4.set_dDNI("4")
        lista_cliente.append(d4)
            
        d5=Cliente()
        d5.set_dApellido("Menta")
        d5.set_dNombre ("Aitor")
        d5.set_dDireccion("Las Acacias 14")
        d5.set_dTelefono= ("03447-15455567")
        d5.set_dDNI("5")
        lista_cliente.append(d5)
        
        
        return lista_cliente
   