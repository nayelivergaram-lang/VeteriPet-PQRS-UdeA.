# MANUAL DE USUARIO
## Sistema de Gestión de PQRS - VeteriPet UdeA

### 1. Introducción 

VeteriPet UdeA es un sistema desarrollado para gestionar las peticiones, quejas, reclamos, sugerencias (PQRS) relacionadas con los servicios veterinarios dirigidos a perros y gatos en la Universidad de Antioquia. Su propósito es facilitar el registro, consulta y seguimiento e las solicitudes, además de generar reportes estadísticos que permitan conocer su comportamiento.

Este manual tiene como finalidad orientar al usuario en el manejo del sistema, explicando como ejecutarlo y utilizar cada una de las opciones disponibles en el menú principal.

### 2. Requisitos para utilizar el programa 

Para ejecutar VeteriPet UdeA se necesita:
-  Un dispositivo con acceso a internet (computador, tablet o celular).
-  Una cuenta de Google para utilizar Google Colab.
-  El código fuente del proyecto.

**Importante:** No es necesario crear manualmente las carpetas, los moódulos ni los archivos del sistema, ya que el código se encarga de generarlos automáticamente durante su ejecución.

### 3. Inicio del programa 

Para iniciar VeteriPet UdeA desde GitHUB, se puede acceder al código de dos maneras:

**Opcion 1. Abrir directamente en Gogle Colab**

1. Ingresar al repositOrio de VeteriPet UdeA en GitHUb.
2. Buscar el archivo del proyecto que contiene el código fuente. (*Abrir codigo_VETERIPET_UDEA_en colab.py*).
3. Abrir el archivo y seleccionar el botón **Open in Colab (Abrir en Colab).**
4. Esperar a que Google Colab abra el archivo.
5. Ejecutar la celda que tiene el código completo del proyecto.

**Opción 2. Descargar el archivo y abrirlo en Google Colab.**

1. Ingresar al repositOrio de VeteriPet UdeA en GitHUb.
2. Buscar el archivo del proyecto y descargarlo.(*Abrir codigo_VETERIPET_UDEA_en colab.py*).
3. Ingresar a Google Colab.
4. Seleccionar la opción para subir un archivo y cargar el archivo descragado.
5. Abrirlo y ejecutar la celda que tiene el código completo del proyecto.

**Importante:** En cualquiera de las dos opciones, al ejecutar el código, el programa genera automáticamente las carpetas, los módulos y los archivos necesarios. Una vez finaliza este proceso, se inicia el menú principal de VeteriPet UdeA.

### 4. Menú principal 

Al iniciar el programa, aparece el siguiente menú en consola:

```text
======================================================================
VETERIPET-PQRS-UDEA
======================================================================
1. Registrar PQRS
2. Consultar PQRS
3. Registrar cambio en PQRS
4. Estadísticas
5. Imprimir radicado
6. Exportar estadísticas
7. Salir
```
Para utilizar una opción, se debe escribir el número correspondiente y presionar Enter.

### 5. Funciones del sistema 

### 5.1 Registrar PQRS 

Esta opción permite ingresar una nueva petición, queja, reclamo o sugerencia.

El sistema solicita los datos del solicitante:

- Nombre completo.
- Tipo y número de documento.
- Tipo y número de teléfono.
- Correo electrónico.
- Dirección (opcional).

Posteriormente, solicita la información de la PQRS:

- Tipo de solicitud.
- Fecha de registro.
- Canal de recepción.
- Asunto.
- Descripción detallada.
- Tipo de mascota (perro o gato).
- Sede o campus.

El programa valida la información ingresada y calcula automáticamente la fecha máxima de respuesta, que corresponde a 30 días calendario después de la fecha de registro.

Al finalizar, la solicitud queda almacenada con estado inicial «Registrada», se le asigna un número de identificación independiente según su tipo y se genera su respectivo radicado.

#### 5.2. Consultar PQRS

Permite visualizar las solicitudes que todavía no han sido solucionadas.

El sistema muestra información como:

- Número de identificación.
- Tipo de PQRS.
- Nombre del solicitante.
- Estado actual.
- Fecha máxima de respuesta.

Las solicitudes se presentan organizadas por fecha de registro.

#### 5.3. Registrar cambio en PQRS

Esta opción permite actualizar el estado de una solicitud previamente registrada.

Para realizar el cambio, se debe seleccionar el tipo de PQRS e ingresar su número de identificación.

El sistema permite avanzar entre los siguientes estados:

- Registrada.
- En proceso.
- Solucionada.

Cuando una solicitud pasa al estado «Solucionada», se registra la fecha en que fue resuelta.

#### 5.4. Estadísticas

Esta opción permite consultar información general sobre las PQRS almacenadas en el sistema.

Se presentan seis indicadores:

1. Cantidad de solicitudes por tipo de PQRS.
2. Cantidad de solicitudes según el tipo de mascota.
3. Cantidad de solicitudes según su estado.
4. Promedio entero de días de respuesta de las solicitudes solucionadas.
5. Cantidad de solicitudes pendientes cuya fecha máxima de respuesta está dentro de los próximos cinco días.
6. Las cinco solicitudes más antiguas.

#### 5.5. Imprimir radicado

Permite consultar y generar nuevamente el comprobante de una PQRS.

Para ello, se debe seleccionar el tipo de solicitud e ingresar su número de identificación.

El sistema genera un archivo de texto con los datos principales del registro, como el número de radicado, la fecha de registro, el estado, la fecha máxima de respuesta y la información del solicitante.

#### 5.6. Exportar estadísticas

Esta opción permite guardar los resultados estadísticos en un archivo de texto llamado `Estadisticas.txt`, facilitando su consulta posterior.

#### 5.7. Salir

Finaliza la ejecución del programa de manera segura.

### 6. Almacenamiento de la información

El sistema genera automáticamente una estructura de carpetas y archivos para organizar su funcionamiento.

La información de las solicitudes se almacena en cuatro archivos independientes:

- `Peticion.txt`
- `Queja.txt`
- `Reclamo.txt`
- `Sugerencia.txt`

Cada tipo de PQRS maneja su propia numeración consecutiva.

Además, el sistema genera carpetas para almacenar los radicados, organizados según el tipo de solicitud. También puede generar un archivo de estadísticas cuando se utiliza la opción de exportación.

### 7. Recomendaciones de uso

- Ingresar información real y completa en los campos obligatorios.
- Respetar el formato solicitado por el programa.
- Verificar los datos antes de finalizar el registro.
- Conservar los archivos generados por el sistema para mantener la información almacenada.
- Utilizar correctamente las opciones del menú para consultar y actualizar las solicitudes.

### 8. Consideraciones finales

VeteriPet UdeA facilita la gestión de las PQRS relacionadas con los servicios veterinarios para perros y gatos, mediante el registro organizado de solicitudes, el seguimiento de sus estados y la generación de información estadística.

Este manual sirve como guía para que los usuarios puedan ejecutar el programa y aprovechar sus funcionalidades de manera adecuada.


