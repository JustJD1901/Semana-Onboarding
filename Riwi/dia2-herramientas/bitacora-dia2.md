# Bitácora · Día 2 · Herramientas de desarrollo

- **Coder: Juan Daniel Ortiz Cadavid**
- **Fecha: 15/10/2026**
- **TL: Johan Alexander Rivera Vasquez**

---

## 1. Mi entorno de desarrollo (Etapa 1)

- Versión de Ubuntu: Ubuntu 26.04.1 LTS
- Versión de Python: Python 3.14.4
- ¿Dónde está instalado Python? (resultado de `which python3`): /usr/bin/python3
- Con mis palabras, la diferencia entre un compilador y un intérprete es: La diferencia es que, un compilador lee y traduce todo el código antes de la ejecución y un interprete lee y va ejecutando el código línea por línea mientras se ejecuta
- ¿Qué pasó con la línea 4 de `hola.py` y por qué?: La línea 4 no se ejecutó pues Python, al ser un lenguaje interpretado, lee línea por línea, y como detectó un error en la línea 3, no ejecutó las siguientes

| Herramienta | ¿Qué es? (sistema operativo, editor, intérprete, compilador o navegador) |
|---|---|
| Ubuntu | Sistema Operativo |
| VS Code | Editor |
| Python | Intérprete |
| Chrome | Navegador |
| gcc | Compilador |

## 2. Reinstalación de VS Code (Etapa 2)

- ¿Cómo estaba instalado VS Code? (snap, .deb o no estaba): VS Code estaba instalado como snap
- Comando que usé para desinstalarlo: El comando usado para desinstalar fue: sudo snap remove code
- Comando que usé para instalarlo: El comando usado para instalar fue: sudo apt install ./code_1.142.0-1792035033_amd64.deb
- ¿Por qué es importante instalar desde la fuente oficial?: Es importante instalar desde una fuente oficial para evitar algún tipo de malware o virus
- ¿Qué pasó con mi configuración al desinstalar? ¿Dónde vive?: La configuración al desinstalar se mantuvo y reside en: ~/.vscode y en ~/.config/Code/

## 3. Perfiles y extensiones (Etapa 3)

- Con mis palabras, un perfil de VS Code es: Es un conjunto de configuraciones personalizadas que permiten trabajar de diferentes maneras según se requiera
- ¿Qué cambia en el Explorador entre un perfil y otro?: Cambian los íconos mostrados
- ¿Por qué VS Code pregunta si confío en el publicador de una extensión?: Porque una extensión de un publicador desconocido puede contener malware

## 4. Duelo de perfiles (Etapa 4)

| Prueba | Perfil2-Basico | Perfil1-Pro |
|---|---|---|
| 1. Auto guardado | No | Sí |
| 2. Auto Rename Tag | No | Sí |
| 3. Error Lens | No | Sí |
| 4. Íconos | Tradicionales | M.I.T. |
| 5. Guías de indentación | Tradicionales | Guides |
| 6. Extensiones corriendo | Menos MS | Más MS |

**Reflexión**

1. ¿Noté diferencias en la experiencia de trabajo entre los dos perfiles? ¿Cuáles?
   - En el perfil 2 es una experiencia más plana y menos personalizada, interfaz más simple, menos ayudas en los errores, en cambio en el perfil 1 todo es un poco más estético, las ayudas visuales son mejores y existe la ayuda de los errores, sin embargo corre un poco más lento
2. ¿Qué ventajas tiene usar múltiples perfiles en VS Code?
   - Permite tener configuraciones distintas dentro del editor sin tener que estar modificando constantemente
3. ¿Cómo influyen las extensiones en la productividad y en el rendimiento del editor?
   - La visualización de los errores antes de ejecutar el código, y las guías visuales son mucho más cómodas y permiten un mejor orden a la hora de escribir. Puede valer la pena siempre y cuando facilite el acceso y optimice el uso o sea más intuitivo de usar
4. ¿Cuándo sería útil usar perfiles distintos en un entorno profesional? (dos ejemplos)
   - Un ejemplo sería para separar y diferenciar entre backend y frontend, con herramientas y extensiones distintas para no sobrecargar la memoria y mantener una interfaz más limpia. Otro ejemplo sería para separar proyectos corporativos de proyectos personales

## 5. Inspección y modificación (Etapa 5)

- Página que usé: riwi.moodle.io
- Cinco etiquetas que encontré y para qué sirven:
  1. <body></body>: Es donde se encuentra el cuerpo y todos los elementos de la página en código HTML
  2. <section></section>: Sirve para delimitar secciones dentro de la página
  3. <footer></footer>: Sirve para marcar el pie de página de la web
  4. <div></div>: Sirve para agrupar varios elementos, como títulos, imágenes, texto, dentro de una misma sección
  5. <h2></h2>: Sirve para escribir títulos de diferentes tamaños, desde h1 hasta h6
- ¿Qué pasó con mis cambios al recargar y por qué?: Los cambios realizados se borraron, pues estos fueron ejercidos dentro del DOM y no en el servidor como tal
- Con mis palabras, el DOM es: Es una copia que se muestra en vivo de la página, que permite experimentar o probar cosas de HTML o JavaScript

## 6. La consola (Etapa 6)

| Operación | Mi predicción | Resultado real |
|---|---|---|
| `2 + 3` | 5 | 5 |
| `10 - 4 * 2` | 2 | 2 |
| `(10 - 4) * 2` | 12 | 12 |
| `10 / 4` | 2,5 | 2.5 |
| `10 % 3` | 1 | 1 |
| `2 ** 8` | 256 | 256 |
| `120000 * 0.19` | 22800 | 19 |
| `365 * 24` | 8760 | 8760 |

- ¿Por qué `0.1 + 0.2` no da exactamente `0.3`?: Porque los números decimales se guardan en binario, por lo que muchos no se pueden representar de una manera exacta, arrojando valores distintos
- Errores o advertencias que encontré en la página (o "ninguno"): Ningún error ni advertencia
- Diferencia entre un error y una advertencia: Un error es una eventualidad que no permite en absoluto la ejecución del código, una advertencia indica que algo no está bien pero se puede seguir ejecutando el código

## 7. La red / Network (Etapa 7)

| Imagen | Formato | Tamaño | Tiempo | Código de estado |
|---|---|---|---|---|
| Diseño de portadas | png | 2 mb | 4,64 s | 200 |
| Imagen1 | png | 354.44 kb | 1,35 s | 200 |
| ic-forward-img | png | 4,61 kb | 323 ms | 200 |

| Experimento | Solicitudes | Transferido | Load |
|---|---|---|---|
| A. Sin caché | 42 | 16.73 mb/14.78 mb | 5.13 s |
| B. Con caché | 18 | 5.60 mb/21.31 kb | 295 ms |
| C. Red lenta | 23 | 11,09mb/9,47mb | 1.63 min |

- Archivo más pesado de la página y su tipo: Se llama first.js y es un archivo de tipo js (JavaScript)
- ¿Por qué la página cargó más rápido con caché?: Porque la caché es una copia de ciertos archivos que se guarda para no tener que descargarlos otra vez y agilizar el proceso de carga de las páginas
- ¿Por qué un desarrollador querría probar con una red lenta?: Para evaluar los tiempos de carga y posibles errores que se pueden desencadenar
- ¿Qué haría para que una imagen pesada cargue más rápido?: Comprimirla bajando un poco la calidad y almacenando la caché en la página

## 8. Dispositivos móviles (Etapa 8)

| Ancho (px) | Dispositivo | ¿Cambia el menú? | ¿Imágenes bien? | ¿Scroll horizontal? | Observación |
|---|---|---|---|---|---|
| 320 | Responsive | Sí | No | Sí | N/a |
| 375 | Responsive | Sí | No | Sí | N/a |
| 768 | Responsive| No | Sí | Sí | N/a |
| 1024 | Responsive | No | Sí | Sí | N/a |
| 1440 | Responsive | No | Sí | Sí | N/a |

- ¿Por qué es importante probar varias resoluciones antes de entregar un proyecto?: Para validar correctamente su compatibilidad en múltiples dispositivos y evitar imagenes cortadas o información faltante

## 9. Laboratorio de errores (Etapa 9)

| # | Tipo | ¿Dónde lo detecté? | Mensaje o síntoma | Causa | Solución aplicada |
|---|---|---|---|---|---|
| 1 | 404 | Consola | css file not found | Dirección relativa mál escrita | Corrección de la dirección del archivo css |
| 2 | 404 | Inspector | can't load the image | La imagen no se cargaba correctamente | Reemplazar la imagen |
| 3 | Uncaught TypeError | Consola | can't access property "addEventListener", boton is null | Las ids del código en JS y HTML no coinciden | corregir el error de escritura |
| 4 | TypeError | VS Code | No funciona el botón | Error de escritura de una variable | Corregir la escritura |

- Uno de los errores, descrito con detalle, y cómo lo resolví: El logo de la página no se cargaba correctamente, la imagen no se cargaba correctamente por lo que tuve que reemplazar la imagen por una que fuera compatible
- ¿Qué vi al pausar con el breakpoint?: Un mensaje que dice Debugger Paused
- ¿Qué pasó al cambiar `visitas` por 99 y al borrarlo?: el contador subió a 99 y luego, al borrarlo, bajó a 1 nuevamente
- ¿Para qué usan el localStorage las páginas reales? ¿Qué NO debería guardar ahí?: Se usa para guardar ciertos datos en el almacenamiento del navegador, preferiblemente que no sean datos o información sensible
- Ancho exacto en el que se apilan las tarjetas y regla de CSS responsable: 600px
- ¿Por qué no basta con mirar solo la consola para encontrar errores?: Porque la consola solo muestra el tipo de error pero no muestra que sucede dentro del código como tal

## 10. Comparación con Firefox (Etapa 10)

| Herramienta | Chrome: nombre y atajo | Firefox: nombre y atajo | Diferencia que noté |
|---|---|---|---|
| Inspeccionar HTML y CSS | Elements (Ctrl + Shift + C) | Inspector (Ctrl + Shift + C) | Ambos permiten inspeccionar y modificar HTML y CSS en tiempo real. |
| Consola | Console (Ctrl + Shift + J) | Consola web (Ctrl + Shift + K) | Ambas permiten ejecutar JavaScript y ver errores, pero la interfaz y algunas opciones son diferentes. |
| Red | Network (Ctrl + Shift + J y seleccionar Network) | Red (Ctrl + Shift + E) | Ambas muestran las solicitudes de red, los tiempos de carga y las respuestas del servidor. |
| Simulación de dispositivos | Device Toolbar (Ctrl + Shift + M) | Modo de diseño adaptable (Ctrl + Shift + M) | Ambas permiten simular dispositivos móviles y cambiar el tamaño de la pantalla. |
| Almacenamiento local | Application > Local Storage | Almacenamiento > Almacenamiento local | Ambas permiten consultar, modificar y eliminar datos guardados en el almacenamiento local. |
| Mensaje del error que reintroduje | Console | Consola web | En ambas herramientas se muestran los errores de JavaScript en rojo y se puede consultar el archivo y la línea donde ocurren. |

- Una característica de Firefox interesante o diferente a Chrome (qué es, para qué sirve y cómo la probé): El inspector de accesibilidad, permite visualizar cómo los lectores de pantalla interpretan una página web y detectar problemas de accesibilidad, como botones sin etiquetas o textos con poco contraste

## 11. Reflexión final (Etapa 11)

- La herramienta que más voy a usar y por qué: El inspector de elementos y la consola, porque permiten identificar errores en el código, modificar elementos visuales en tiempo real y comprobar el funcionamiento de una página web sin tener que modificar directamente los archivos del proyecto
- Lo más difícil del día y cómo lo resolví: Lo más difícil fue identificar y solucionar los errores durante la inspección y depuración de la página web. Lo resolví revisando los mensajes de error en la consola, verificando las rutas de los archivos y comprobando que los nombres de las variables y los identificadores coincidieran entre HTML y JavaScript 
- Las DevTools explicadas para alguien que no programa (3 líneas): Las DevTools son herramientas que permiten inspeccionar una página web y entender cómo funciona por dentro. Sirven para detectar errores, modificar temporalmente la apariencia de una página y analizar su velocidad de carga