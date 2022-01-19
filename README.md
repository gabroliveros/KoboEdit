# KoboEdit
Modify the value and status of the records KoboToolbox.

Modica el valor y status de los registros de KoboToolbox.

Ante todo debes asegurarte de utilizar el servidor correcto en que se encuentra tu formulario, que puede ser:

https://kobo.humanitarianresponse.info  o
https://kf.kobotoolbox.org/

¿Cómo obtener el asset de un formulario Kobo?

Para obtener el código del asset para la URL: (forma más simple)
	- Abrir la tabla de Datos del formulario
	- Tomar en la barra de dirección el código antes de la palabra "/data" como se indica abajo
                                                     [  código del asset  ]
https://kobo.humanitarianresponse.info/api/v2/assets/aBmZ793qCNjbqYuP5uULp9/data/bulk

Otra forma de obtener el código del asset:
	- Abrir   https://kc.humanitarianresponse.info/api/v1/data
	- GET  xlsx
	- Abrir el archivo descargado y obtener el "id_string" del formulario deseado

Otra forma de obtener el código del asset:
    - Se  abre la tabla de datos del formulario
    - Herramientas Desarrollador / Network /
    - Actualizar página
    - Ubicar "URL de la solicitud" con indicación del assets

