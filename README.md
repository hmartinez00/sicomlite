# sicomlite

Aplicacion para gestionar procesos de generacion de archivos VRSS-2.

## Descripcion

Es una herramiento en linea de comando en la version actual. Consiste en un proyecto simplificado, proveniente del proyecto padre bajo el nombre SUGICOM, en el que se ha separado y rehubicado buena parte del codigo en aras de la eficiencia.

### El codigo 

Se encuentra distribuido en tres secciones principales:

* modulos generales: Los cuales levantan las estructuras XML.
* modulos especificos: Los cuales controlan la generacion de los archivos.
* scripts: Los cuales permiten ejecutar la generacion, sirviendose de la informacion almacenada en los modulos especificos.

### La ejecucion

A su vez, todas las ejecuciones son controladas mediante un sistema de control de rutas a traves de un archivo json, donde a su vez se encuentra registradas las opciones de los menues y submenues, asi como la ruta de recursos de donde se extrae y a donde se envia la informacion.

### La Base de datos

Finalmente la aplicacion cuenta con una Base de datos, muy simplificada, heredada del proyecto padre, donde se aloja la tabla de control de procesos, que permite indexar la generacion de archivos para asegurar un seguimiento apropiado de las etapas de cada generacion, sin comprometer la posibilidad de repetir generacions cuando sea necesario.