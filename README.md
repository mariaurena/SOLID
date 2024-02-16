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
- I: Indescriptive Naming. Debemos siempre intentar representar la funcionalidad de una variable, clase o función mediante su nombre. Esto nos hace poder evitar posibles errores de interpretación.
- D: Duplication. La duplicidad del código aumenta la cantidad de trabajo necesario para realizar cualquier tipo modificación necesaria en un futuro. 
