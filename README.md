# SOLID
### Hacia un diseño de software robusto

Para escribir esta entrada me he basado en el curso de Codely: Principios SOLID aplicados disponible en:
https://pro.codely.com/library/principios-solid-aplicados-36875/77070/path/


Con el tiempo la tecnología va creciendo y avanzando y el mundo del desarollo del software no se queda atrás. Cuando ya conocemos los conceptos, herramientas e interacciones que nos ayudan a desarrollar un código funcional el siguiente reto al que nos enfrentamos es la búsqueda de la claridad, mantenibilidad y flexibilidad. Actualmente no nos conformamos con que un código compile y consiga alcanzar una determinada funcionalidad, ahora debemos tener en cuenta que en un futuro dicha funcionalidad puede ampliarse o incluso modificarse y que esto debe causar, en cierta medida, la menor repercusión posible en nuestros programas. 

Para llevar todo esto a cabo debemos huir de STUPID y acercarnos más a SOLID. ¿Qué quieren decir estos acrónimos? De eso vengo a hablarte en esta sección, en la cual iré explicando brevemente la teoría que define a cada principio y montaré un ejemplo muy sencillo para facilitar su entendimiento. 

### STUPID vs SOLID

STUPID es una forma humorística de recoger las malas prácticas del diseño del software que han ido acompañándonos a lo largo de los años. El acrónimo está formado por:

- S: Singleton. El patrón **singleton** se considera bastante útil mientras no se utilice en exceso. Al acoplar fuertemente las clases esto puede traernos problemas en el momento de realizar tests unitarios, por tanto debemos prestar mucha atención para no abusar de su uso.
- T: Tight Coupling (Alto acoplamiento). Cuando nos encontramos en una situación en la que los componentes de un sistema están **fuertemente interconectados** entre sí aplicar una pequeña modificación puede suponernos un esfuerzo desproporcional al cambio que queremos implementar. Un gran acoplamiento nos puede llevar a un código dificil de mantener y probar.
- U: Untestability. En relación al punto anterior, un código que requiere de técnicas complejas para ser probado sólo se lleva nuestro tiempo y esfuerzo dificultando pues la detección de errores.
- P: Premature Optimization. Cuando nos adelantamos a **posibles optimizaciones** futuras lo único que conseguimos es un código dificil de entender y mantener sin proporcionar beneficios tangibles.
- I: Indescriptive Naming. Debemos siempre intentar **representar la funcionalidad** de una variable, clase o función mediante su nombre. Esto nos lleva a poder evitar posibles errores de interpretación.
- D: Duplication. La **duplicidad** del código aumenta la cantidad de trabajo necesario para realizar cualquier tipo modificación necesaria en un futuro.

### Principios SOLID

Ahora por fin podemos recorrer juntos cada uno de los principios SOLID y así aprender a desarrollar un código mucho más robusto y flexible:

*1. S: SRP (Principio de responsabilidad única). Una clase debe representar un único concepto y una única responsabilidad. Una clase debería tener sólo una razón para cambiar. Este principio fomenta la cohesión y facilita el mantenimiento del código.*

Ejercicio: Desarrolla un sistema de gestión de bibliotecas. Una biblioteca está formada por varios libros y el cliente debería poder registrar un nuevo libro, buscar un libro por su titulo u obtener un listado de todos los libros que contiene la biblioteca actualmente. 

Empezaremos con un ejemplo que se aleja completamente de dicho principio:

Libro.py:

```python
    class Libro:
        def __init__(self, titulo, autor, genero, ncopias):
    
            self.titulo  = titulo
            self.autor   = autor
            self.genero  = genero
            self.ncopias = ncopias

        # ------- GET -------
    
        def get_titulo(self):
    
            return self.titulo
    
        def get_autor(self):
            
            return self.autor
    
        def get_genero(self):
            
            return self.genero
    
        def get_ncopias(self):
    
            return self.ncopias

        # ------- SET -------
            
        def set_titulo(self, nuevo_titulo):
    
            self.titulo = nuevo_titulo
    
        def set_autor(self, nuevo_autor):
            
            self.autor = nuevo_autor
    
        def set_genero(self, nuevo_genero):
            
            self.genero = nuevo_genero
    
        def set_ncopias(self, nuevas_ncopias):
            
            self.ncopias = nuevas_ncopias
```

Biblioteca.py:

```python

class Biblioteca:

    def __init__(self):

        self.nlibros = 0
        self.libros  = []

    # ------- GET -------

    def get_nlibros(self):

        return self.nlibros

    def get_libros(self):

        if not self.libros:
            print("No hay libros registrados en la biblioteca.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros:
                print("- Título:", libro.get_titulo())
                print("  Autor:", libro.get_autor())
                print("  Género:", libro.get_genero())
                print("  Número de copias:", libro.get_ncopias())
                print() 

    # ------- SET -------

    def set_nlibros(self, nuevos_nlibros):

        self.nlibros = nuevos_nlibros

    # ------- MÉTODOS -------

    def registrar_libro(self, libro):

        self.libros.append(libro)
        self.nlibros += 1
        print("Libro '{}' registrado correctamente en la biblioteca".format(libro.get_titulo()))

    def baja_libro(self, libro):
        self.libros.remove(libro)
        print("Libro '{}' eliminado correctamente de la biblioteca".format(libro.get_titulo()))
        
    # buscar libro por su titulo
    def buscar_por_titulo(self, titulo):

        for libro in self.libros:
            if libro.get_titulo() == titulo:
                print("Libro '{}' encontrado correctamente en la biblioteca".format(titulo))
                return libro
        return None
    
    # buscar libro por su autor
    def buscar_por_autor(self, autor):

        for libro in self.libros:
            if libro.get_autor() == autor:
                print("Libro '{}' encontrado correctamente en la biblioteca".format(libro.get_titulo()))
                return libro
        return None

```
    
Cliente.py:
```python

from Biblioteca import Biblioteca
from Libro import Libro


biblioteca = Biblioteca()

libro1 = Libro("Harry Potter", "J.K.Rowling", "Fantasia", 6)
libro2 = Libro("La amiga estupenda", "Elena Ferrante", "Amistad", 2)
libro3 = Libro("Film for her", "Carloto", "Fotografia", 16)

biblioteca.registrar_libro(libro1)
biblioteca.registrar_libro(libro2)
biblioteca.registrar_libro(libro3)

biblioteca.get_libros()

biblioteca.buscar_por_titulo("La amiga estupenda")
biblioteca.buscar_por_autor("J.K.Rowling")

```
            
Como podemos comprobar, existe una única clase 'Biblioteca' que recoge toda la funcionalidad que tenga relación con ella. Por tanto, dicha clase va a cambiar cada vez que queremos modificar la forma de registrar un libro o la manera en la que buscamos un libro en la biblioteca. En resumen, tiene más de una razón para cambiar y esto no cumple el principio de responsabilidad única.

Veamos entonces cómo lo adaptaríamos para ser fieles al principio de responsabilidad única:

La clase 'Libro' se mantendría tal cual:

Libro.py: 

```python
    class Libro:
        def __init__(self, titulo, autor, genero, ncopias):
    
            self.titulo  = titulo
            self.autor   = autor
            self.genero  = genero
            self.ncopias = ncopias

        # ------- GET -------
    
        def get_titulo(self):
    
            return self.titulo
    
        def get_autor(self):
            
            return self.autor
    
        def get_genero(self):
            
            return self.genero
    
        def get_ncopias(self):
    
            return self.ncopias

        # ------- SET -------
            
        def set_titulo(self, nuevo_titulo):
    
            self.titulo = nuevo_titulo
    
        def set_autor(self, nuevo_autor):
            
            self.autor = nuevo_autor
    
        def set_genero(self, nuevo_genero):
            
            self.genero = nuevo_genero
    
        def set_ncopias(self, nuevas_ncopias):
            
            self.ncopias = nuevas_ncopias
```

Sin embargo, la biblioteca ahora puede dividirse en dos clases agrupando en ellas las funcionalidades que tienen más relación entre si.

Por un lado tendríamos la clase autenticación que, además de poder ser reutilizada en otros lugares de nuestra aplicación, recoge perfectamente toda la funcionalidad relacionada con el registro o baja de un nuevo libro en nuestra libreria. Por tanto, un cambio en la búsqueda de un libro no tendría por qué afectar a esta clase.

Autenticación.py:
```python

class Autenticacion:

    def __init__(self):
        self.nlibros = 0
        self.libros = []

    def registrar_libro(self, libro):
        self.libros.append(libro)
        self.nlibros += 1
        print("Libro '{}' registrado correctamente en la biblioteca".format(libro.get_titulo()))

    def baja_libro(self, libro):
        self.libros.remove(libro)
        print("Libro '{}' eliminado correctamente de la biblioteca".format(libro.get_titulo()))
```

Por otro lado, la clase Busqueda se encarga de recoger toda la funcionalidad de aplicar filtros a la búsqueda de libros de la librería:

class Busqueda:
```python

class Busqueda:
    def __init__(self, autenticacion):
        self.autenticacion = autenticacion

    def buscar_por_titulo(self, titulo):
        libros_registrados = self.autenticacion.libros
        for libro in libros_registrados:
            if libro.get_titulo() == titulo:
                print("Libro '{}' encontrado correctamente en la biblioteca".format(titulo))
                return libro
        print("Libro '{}' no encontrado en la biblioteca".format(titulo))
        return None

    def buscar_por_autor(self, autor):
        libros_registrados = self.autenticacion.libros
        for libro in libros_registrados:
            if libro.get_autor() == autor:
                print("Libro del autor '{}' encontrado correctamente en la biblioteca".format(autor))
                return libro
        print("No se encontraron libros del autor '{}' en la biblioteca".format(autor))
        return None
    
    def get_libros(self):
        libros_registrados = self.autenticacion.libros
        if not libros_registrados:
            print("No hay libros registrados en la biblioteca.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in libros_registrados:
                print("- Título:", libro.get_titulo())
                print("  Autor:", libro.get_autor())
                print("  Género:", libro.get_genero())
                print("  Número de copias:", libro.get_ncopias())
                print() 
```

Cliente.py

```python

from Autenticacion import Autenticacion
from Busqueda import Busqueda
from Libro import Libro


autenticacion = Autenticacion()
busqueda      = Busqueda(autenticacion)

# Registrando libros
libro1 = Libro("El nombre del viento", "Patrick Rothfuss", "Fantasia", 6)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 4)
autenticacion.registrar_libro(libro1)
autenticacion.registrar_libro(libro2)

# Búsqueda
busqueda.get_libros()
busqueda.buscar_por_titulo("El nombre del viento")
busqueda.buscar_por_autor("Gabriel García Márquez")


```

De esta manera, ya solo de entrada ganamos bastante en organización del código. Además, evitamos que las clases se vayan extendiendo demasiado con el paso del tiempo y perjudique en la claridad. Por si fuera poco, reducimos el acoplamiento de los módulos o clases que componen nuestro programa (es decir, alcanzamos nuestro principal objetivo). 

**Al igual que en el resto de secciones que vienen a continuación el nivel de "casamiento" que debemos tener con estos principios dependerá directamente del contexto. Habrá situaciones en las que aplicar estos principios no nos aporte ningún beneficio y eso también es correcto, debemos tener claro qué beneficio aporta cada principio para así saber cuando procede aplicarlo y cuando no.**

*2. OCP: Princio de Abierto/Cerrado. El software debería estar abierto a extensión y cerrado a modificación. Debemos evitar depender de implementaciones específicas, haciendo uso de clases abstractas o interfaces con la finalidad de facilitar el momento de añadir casos de uso en un futuro en nuestra aplicación.*

Ejercicio: Debemos calcular el sueldo de un empleado dependiendo de si trabaja a tiempo parcial o a tiempo completo.

Inicialmente, podríamos pensar que la solución más sencilla y rápida es la siguiente:

Empleado.py

```python

class Empleado:

    def __init__(self):

        self.tipo       = "completo"
        self.jornada    = 0
        self.euros_hora = 0
    
    def calcular_salario(self, tipo): 

        if ( tipo == "parcial" ):
            self.jornada = 6
            self.euros_hora = 12

        elif ( tipo == "completo" ):
            self.jornada = 8
            self.euros_hora = 15

        return self.jornada * self.euros_hora
```

Cliente.py

```python
from Empleado import Empleado

empleado  = Empleado()

print("El sueldo de un empleado a tiempo parcial es:", empleado.calcular_salario("parcial"))
print("El sueldo de un empleado a tiempo completo es: ", empleado.calcular_salario("completo"))
```

Aunque en algunas situaciones es cierto que esta forma de abordar este ejemplo puede ser la mejor, en contextos que pueden escalar es preferible disponer de un código completamente cerrado a modificación y abierto a extensión. En la mayoría de situaciones el "if else" del método calcular_salario puede repetirse en otros muchos lugares de nuestra aplicación haciendo muy tedioso el momento de implementar una nueva funcionalidad para un nuevo empleado. 

Por tanto, una posible solución despues de aplicar este principio sería:

Empleado.py

```python
from abc import ABC, abstractmethod

class empleado(ABC):

    def __init__(self):
        self.jornada = 0
        self.euros_hora = 0

    @abstractmethod
    def calcular_sueldo(self):
        pass
```

Empleado_parcial.py

```python
from Empleado import empleado

class empleado_parcial(empleado):

    def __init__(self):
        self.jornada = 6
        self.euros_hora = 12

    def calcular_sueldo(self):
        return self.jornada * self.euros_hora
```

Empleado_completo.py

```python
from Empleado import empleado

class empleado_completo(empleado):

    def __init__(self):
        self.jornada = 8
        self.euros_hora = 15

    def calcular_sueldo(self):
        return self.jornada * self.euros_hora
```
Cliente.py

```python

from Empleado_completo import empleado_completo
from Empleado_parcial  import empleado_parcial

empleado_parcial = empleado_parcial()
print("Salario empleado parcial:", empleado_parcial.calcular_sueldo())

empleado_completo = empleado_completo()
print("Salario empleado completo:", empleado_completo.calcular_sueldo())

```

Como podemos observar, hemos implementado una clase abstracta (o la simulación de ella en el caso de estar usando python) 'Empleado' con el método calcular_salario. Finalmente hemos creado los dos tipos de empleados con sus jornadas y salario por hora correspondiente que implementan dicha clase abstracta y por consecuencia el método calcular_salario. Como consecuencia de esta nueva implementación, si llega el momento de añadir un nuevo tipo de empleado en un futuro nos será mucho más fácil hacerlo ya que únicamente debemos añadir una nueva especificación de la clase abstracta 'Empleado' e implementar el método calcular_salario (con las particularidades que consideremos convenientes).  

*3. LSP: Principio de sustitución de Liskov. Si S es un subtipo de T, instancias de T deberían poderse sustituir por instancias de S sin alterar las propiedades del programa. Por tanto, el comportamiento de subclases debe respetar el contrato de la superclase. La finalidad de este principio es mantener la correctitud para poder aplicar el principio de OCP que acabamos de ver.*

Ejercicio: Tenemos varios tipos de pájaros: patos, gorriones y pingüinos. Queremos implementar métodos para comer, tuitear y volar en todos menos en los pingüinos ya que eston no son capaces de volar. 

De primeras, la solución más sencilla que quizás se nos viene a la cabeza es usar la herencia para representar esta situación. Tendríamos una clase padre (Bird) con los métodos de comer, tuitear y volar y varias clases hijas (dependiendo del tipo de pájaro) que implementan dichos métodos de forma mucho más específica. 

Bird.py

```python

class Bird:

    def eat(self):
        pass

    def tweet(self):
        pass

    def fly(self):
        pass


```

Duck.py

```python

from Bird import Bird

class Duck(Bird):

    def eat(self):
        print("Soy un pato y estoy comiendo")

    def tweet(self):
        print("Soy un pato y estoy tuiteando")

    def fly(self):
        print("Soy un pato y estoy volando")

```

Sparrow.py

```python

from Bird import Bird

class Sparrow(Bird):

    def eat(self):
        print("Soy un gorrión y estoy comiendo")

    def tweet(self):
        print("Soy un gorrión y estoy tuiteando")

    def fly(self):
        print("Soy un gorrión y estoy volando")

```

Penguin.py

```python

from Bird import Bird

class Penguin(Bird):

    def eat(self):
        print("Soy un pingüino y estoy comiendo")

    def tweet(self):
        print("Soy un pingüino y estoy tuiteando")

```

Cliente.py

```python

from Duck import Duck
from Penguin import Penguin
from Sparrow import Sparrow

duck = Duck()
duck.fly()

sparrow = Sparrow()
sparrow.fly()

penguin = Penguin()
penguin.fly()

```

El código anterior no cumple, como podemos comprobar, el principio de sustitución de Liskov ya que sería imposible intercambiar la clase Pingüino por la clase Bird. Debemos siempre intentar que las clases hijas implementen todos y cada uno de los métodos de sus respectivos padres para así tener una buena base para que nos sea mucho más sencillo aplicar el principio de OCP (Abierto/Cerrado). 

Si nos damos cuenta, en este caso disponemos de dos tipos de pájaros: los voladores y los no voladores. Podemos crear dos padres distintos y pensar qué hijos deberían pertenecer a cada uno de los padres. 

Bird.py

```python

class Bird:

    def eat(self):
        print("Soy un pájaro y estoy comiendo")

    def tweet(self):
        print("Soy un pájaro y estoy tuiteando")

```

FlyingBird.py

```python

class FlyingBird:

    def eat(self):
        print("Soy un pájaro y estoy comiendo")

    def tweet(self):
        print("Soy un pájaro y estoy tuiteando")

    def fly(self):
        print("Soy un pájaro y estoy volando")

```

Duck.py

```python

from FlyingBird import FlyingBird

class Duck(FlyingBird):

    def eat(self):
        print("Soy un pato y estoy comiendo")

    def tweet(self):
        print("Soy un pato y estoy tuiteando")

    def fly(self):
        print("Soy un pato y estoy volando")

```

Sparrow.py

```python

from FlyingBird import FlyingBird

class Sparrow(FlyingBird):

    def eat(self):
        print("Soy un gorrión y estoy comiendo")

    def tweet(self):
        print("Soy un gorrión y estoy tuiteando")

    def fly(self):
        print("Soy un gorrión y estoy volando")

```

Penguin.py

```python
from Bird import Bird

class Penguin(Bird):

    def eat(self):
        print("Soy un pingüino y estoy comiendo")

    def tweet(self):
        print("Soy un pingüino y estoy tuiteando")
```

Cliente.py

```python

from Duck import Duck
from Sparrow import Sparrow

duck = Duck()
duck.fly()

sparrow = Sparrow()
sparrow.fly()

```

De esta manera respetamos el principio de sustitución de Liskov ya que esta vez Penguin implementa todos y cada uno de los métodos de la clase padre por lo que el intercambio sería completamente posible. Recordemos que el nivel de granularidad que debemos desarrollar dependerá del contexto y de las necesidades de cada proyecto.   

*4. ISP: Principio de segregación de interfaces. Ningún cliente debería verse forzado a depender de métodos que no usa. Debemos definir contratos de interfaces basándonos en los clientes que las usan y no en las implementaciones que pudiéramos tener. Una forma de conseguir esto es usar Role Interfaces en lugar de Header Interfaces*

Ejercicio: Desarrolla un sistema de gestión de usuarios con funcionalidad para iniciar sesión, cerrar sesión, editar perfil y ver el contenido de dicho usuario. Sin embargo, el caso de uso que estamos abordando se basa en permitir a un usuario registrarse, realizar alguna acción y cerrar la sesión al finalizar. 

Al ver este ejercicio de primeras podríamos intentar abordarlo teniendo presente la funcionalidad relacionada con la gestión del usuario y no tanto el caso de uso específico que se nos ha planteado. Por tanto, tendríamos una interfaz que simplemente representa al usuario (junto a la funcionalidad que tiene relación con el mismo) y una clase que implementa cada uno de los métodos de esta interfaz:

Usuario.py

```python
from abc import ABC, abstractmethod

class Usuario(ABC):

    @abstractmethod
    def iniciar_sesion(self, username, password):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass

    @abstractmethod
    def ver_contenido(self):
        pass

    @abstractmethod
    def editar_perfil(self):
        pass
```

GestionUsuario.py

```python
from Usuario import Usuario

class GestionUsuario(Usuario):

    def __init__(self):
        self.username = ""
        self.password = ""

    def iniciar_sesion(self, username, password):
        self.username = username
        self.password = password
        print(f"Iniciando sesión como: {self.username}")

    def cerrar_sesion(self):
        print(f"Cerrando sesión de: {self.username}")

    def editar_perfil(self):
        print("Editando perfil")

    def ver_contenido(self):
        print("Viendo contenido")

```

Cliente.py

```python
from GestionUsuario import GestionUsuario


gestionUsuario = GestionUsuario()
gestionUsuario.iniciar_sesion("mariaurena","123455")
# Todo: realizar x acciones
gestionUsuario.cerrar_sesion()
```

Sin embargo, si tenemos presente el principio de segregación de interfaces y nos enfocamos en el caso de uso que en este caso es iniciar y cerrar la sesión de un usuario, el código quedaría de otra forma:

AutenticacionUsuario.py

```python

from abc import ABC, abstractmethod

class AutenticacionUsuario(ABC):

    @abstractmethod
    def iniciar_sesion(self, username, password):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass
```
GestionUsuario.py

```python
from abc import ABC, abstractmethod

class GestionUsuario(ABC):

    @abstractmethod
    def ver_contenido(self):
        pass

    @abstractmethod
    def editar_perfil(self):
        pass
```

Cliente.py

```python

from AutenticacionUsuario import AutenticacionUsuario

class Cliente(AutenticacionUsuario):

    def __init__(self):
        self.username = ""
        self.password = ""
        
    def iniciar_sesion(self, username, password):
        self.username = username
        self.password = password
        print(f"Iniciando sesión como: {self.username}")

    def cerrar_sesion(self):
        print(f"Cerrando sesión de: {self.username}")



cliente = Cliente()
cliente.iniciar_sesion("mariaurena","3457863")
# Todo: realizar x acciones
cliente.cerrar_sesion()

```
