# Sistema de inicio de sesión con verificación facial

Este proyecto corresponde a la actividad de Visión por Computadora.  
Se desarrolló un sistema de inicio de sesión seguro utilizando verificación facial con la librería DeepFace.

## Descripción del proyecto

El sistema compara dos imágenes:

- `rostros/usuario_registrado.jpg`: imagen del usuario autorizado.
- `rostros/intento_login.jpg`: imagen de la persona que intenta iniciar sesión.

Si ambos rostros coinciden, el sistema muestra el mensaje:

```text
ACCESO PERMITIDO
