15 Comandos:

1. pwd: Muestra la ubicación del directorio actual
2. ls: Lista los elementos del directorio actual
3. ls -a: Lista los elementos ocultos dentro del directorio actual
4. ls -R: lista los directorios, subdirectorios y archivos a partir de la ubicación actual
5. cd: Navegar entre directorios
6. mkdir: Crear carpetas
7. mkdir -p: Crear carpetas y subcarpetas
8. touch: Crear archivos
9. cat: Visualizar contenido de los archivos o concatenarlos
10. head: Consultar las primeras "n" lineas de un archivo
11. find: Buscar archivos o carpetas
12. grep: Buscar texto dentro de archivos
13. wc -l: Contar lineas dentro de un archivo
14. rm: Eliminar archivos
15. rm -r: Eliminar archivos o directorios y su contenido

Respuestas puntos de control:

P 1. Una ruta absoluta va desde la raíz del sistema hasta la ruta deseada, mientras que una ruta relativa va desde la ubicación actual hasta la ruta deseada.
Ej.
Ruta absoluta: home/cohorte8/Documents/Riwi_JD/clientes
Ruta relativa desde Documents/: ./Riwi_JD/clientes

P 2. Este archivo no aparece en el listado normal pues el . a la hora de crearlo hace que se oculte y solo pueda visualizarse mediante ls -a.
Para manejar nombres con espacios se hace mediante el uso de comillas, por ejemplo: "lista de pendientes".txt.

P 3. > Lo utilizaría para escribir la primera línea de un archivo o para sobreescribir la información de un archivo existente; >> lo utilizaría para añadir una línea de texto a un archivo sin modificar nada de lo que ya existe. Todo lo anterior acompañado del comando "echo".

P 4. 

P 5. El comando mv permite mover archivos con la estructura: mv [nombre_archivo_origen] [carpeta_destino], y permite cambiar el nombre con la estructura: mv [nombre_original] [nombre_nuevo].

P 6. Para copiar un archivo se usa el comando "cp", para copiar carpetas que contiene información (otras carpetas), se usa el comando "cp -r", -r indica que se copia de manera "recursiva" es decir, contiene la información de la carpeta.

P 7. Para buscar por nombre de archivo se usa el comando "find" y solo se encuentra el nombre del archivo pero nada de la información que contenga, para buscar dentro de archivos, se usa el comando "grep" y aquí solo busca texto dentro de los archivos, omitiendo el nombre de estos mismos.

P 8. Al usar "rmdir" con una carpeta que contiene información, el comando falla, pues este solo sirve para carpetas vacías, para solucionarlo se usa "rm -r", el -r indica que se maneja de manera "recursiva", esto es, maneja también la información dentro del directorio, en este caso, la borra.
