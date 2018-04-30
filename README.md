# Ecologica

Esta es una Actividad Educativa desarrollada en Python para Fundación Zamora
Terán y el proyecto "Una laptop por niño" con el objetivo de educar y
concientizar a los niños en edades de educación primaria sobre temas como el
desarrollo sostenible, preservación del medioambiente y el uso racional de los
recursos naturales.

## Ambiente de desarrollo

Esta es una guía de los pasos a seguir para instalar los requerimientos de
sistema necesarios para tener un ambiente de desarrollo homogéneo para la
creación de Actividades Educativas con Python y PyGame.

* Esto garantiza ambientes de desarrollos portables y reproducibles.

### Instalando `virtualenv` and `pip`.

> Fedora

```sh
su -c 'dnf install python2-virtualenv.noarch python3-virtualenv.noarch'
```

```sh
su -c 'dnf install python2-pip.noarch python3-pip.noarch'
```

### Crear un directorio para proyectos.

```sh
cd ~
mkdir .virtualenvs
cd .virtualenvs
```

### Crear un virtualenv para PyGame

Usando el comando `virtualenv-3` o el comando `virtualenv-3.6` creamos un
ambiente aislado para PyGame. Debemos especificar que por defecto se debe usar
Python 2 como alias para `python`.

```sh
virtualenv-3 --no-site-packages -p python2 pygame
```

Nos movemos al directorio `pygame`.

```sh
cd pygame
```

### Activamos el entorno recién creado.

```sh
source bin/activate
```

### Instalamos/Actualizamos `setuptools` y `pip`.

```sh
pip install --upgrade setuptools pip
```

### Instalamos PyGame.

```sh
pip install --upgrade pygame
```

### Clonamos el repo desde Github.

```sh
git clone https://github.com/FundacionZamoraTeran/Ecologica.git
```

Instalamos `git` en caso de no estar instalado.

```sh
su -c 'dnf install git'
```

### Para deshabilitar el ambiente cada vez que dejemos de trabajar en él.

```sh
deactivate
```

### Para habilitar nuevamente.

```sh
source .virtualenvs/pygame/bin/activate
```
