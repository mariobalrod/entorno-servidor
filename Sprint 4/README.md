# Entregable 4

![portada](./docs/portada.jpg)



Desarrollo Web - Entorno Servidor <br>
Ciclo Superior Desarrollo Web <br>
Curso 2020-21 <br>
Cuarta entrega <br>
<br>

#### GRUPO: 2  
<br>

- INTEGRANTE 1:  
    - APELLIDOS, NOMBRE: Ballestero Rodríguez, Mario  
    - DNI: 29533046B  
- INTEGRANTE 2:  
    - APELLIDOS, NOMBRE: Del Junco Pérez, Esperanza  
    - DNI: 49137125V  
- INTEGRANTE 3:  
    - APELLIDOS, NOMBRE: Ávila Chacón, Sergio  
    - DNI: 29498790W

<br>
<br>

### Requerimientos del sistema



**Nota:** Este software ha sido creado inicialmente en Windows 10 por lo cual tiene las librerías correspondientes a Windows 10, se recomienda su ejecución en Windows 10.

- Tener Python 3 actualizado a su ultima versión: [python 3](https://www.python.org/downloads/)

- Se necesita tener Python pip instalado y en su ultima versión:

  ```bash
  python -m pip install
  ```

  ```bash
  python -m pip install --upgrade
  ```

  

### Guía de configuración del Proyecto

<br>

Lo primero será acceder al directorio del sprint 4 y montar un entorno virtual con Python para ello, haremos lo siguiente:

```bash
cd Sprint 4/

py -m venv venv
```



Posteriormente, activaremos el entorno creado, para ello:

* En caso de Ubuntu:

  ```bash
  source venv/bin/activate
  ```

* En caso de Windows:

  ```bash
  source venv/Scripts/activate
  ```



Finalmente, instalaremos todas las dependencias necesarias para el proyecto:

```bash
pip install -r requirements.txt
```

<br>



Para arrancar el servidor Python:

```bash
py server.py
```





## Despliegue

*  [Cliente](https://among-us-voting-server.herokuapp.com/)

*  [Servidor](https://among-us-voting-server.herokuapp.com/)

  

  

Al abrir el cliente se muestra:

![inicio](./docs/inicial.JPG)

Una vez introducido el nombre entramos en la sala de juego en la que estarán todos lo jugadores, que hayan entrado al mismo tiempo, ya que al estar trabajando con socket si pasa mucho tiempo entre el login de un jugador y otro el socket se actualiza y solo quedaría el ultimo jugador.



![lobby](./docs/start.JPG)



Una vez todos los jugadores esten listos comenzamos con "Start game".



![play](./docs/play.JPG)

Una vez haya muerto un jugador, como es obvio no se le permite realizar mas votaciones.

![dead](./docs/muerto.png)



Una vez se ha pillado al impostor se avisa y se termina el juego.

![](./docs/fin.png)
