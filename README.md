# OTW

## Introducción

**OTW** es una Herramienta que permite la obtención automatizada de Información a través de Fuentes Abiertas, tomando como base la utilización de diferentes API’s proporcionadas por las fuentes de datos de mayor reputación y fiabilidad del mercado. Partiendo de un enfoque modular específicamente diseñado para mostrar información pertinente, permite al usuario interactuar con módulos que proporcionan información diferenciada a partir de un input de entrada único.
Desarrollada en Python 3, la Versión Alpha de OTW está ideada para un uso ágil e intuitivo, con una presentación de resultados limpia y ordenada, a través de Línea de Comandos.

## Scope

**OTW** puede ser de utilidad tanto para Organizaciones que quieran conocer el grado de exposición de sus Sistemas y Tecnologías de la Información, como para Empresas de Ciberseguridad, Pentesters y Analistas de inteligencia, como punto de partida para la realización de Auditorías / Investigaciones. 

## Características técincas

-	Desarrollada en Python 3 
-	Versión Alpha diseñada para ser utilizada en CLI
-	Modularidad: Más de 20 Módulos 
-	Escalabilidad: Posibilidad de incorporar nuevos Módulos fácilmente
-	Conexión mediante API’s con las plataformas OSINT de mayor prestigio del Mercado
- Almecenamiento de API's en archivo "config.py"
-	Resultados limpios, claros, concisos, filtrados y veraces
-	Documentación detallada para cada uno de los Módulos

## Módulos 

- Censys

  -[Documentación API](https://censys.io/api)

  -[Creación de Cuenta y Generación de API_KEY](https://censys.io/register)
  
- Shodan 

  -[Documentación API](https://developer.shodan.io/api)

  -[Creación de Cuenta y Generación de API_KEY](https://account.shodan.io/login)

- Virus Total

  -[Documentación API](https://developers.virustotal.com/reference)

  -[Creación de Cuenta y Generación de API_KEY](https://www.virustotal.com/gui/join-us)
  
- IBM X-Force Exchange

  -[Documentación API](https://exchange.xforce.ibmcloud.com/api/doc/?)

  -[Creación de Cuenta y Generación de API_KEY](https://www.ibm.com/account/reg/us-en/signup?formid=urx-30243)
  
- RiskIQ

  -[Documentación API](https://api.passivetotal.org/index.html)

  -[Creación de Cuenta y Generación de API_KEY](https://community.riskiq.com/registration/signupforfree?utm_content=riqcom&utm_term=register)
  
- Fraudguard

  -[Documentación API](https://docs.fraudguard.io/)

  -[Creación de Cuenta y Generación de API_KEY](https://app.fraudguard.io/register)
  
- Botscout

  -[Documentación API](https://botscout.com/api.htm)

  -[Creación de Cuenta y Generación de API_KEY](https://botscout.com/getkey.htm)
  
- Clearbit

  -[Documentación API](https://clearbit.com/docs)

  -[Creación de Cuenta y Generación de API_KEY](https://dashboard.clearbit.com/signup?)
  
- Dehased

  -[Documentación API](https://www.dehashed.com/docs)

  -[Creación de Cuenta y Generación de API_KEY](https://www.dehashed.com/register)
  
- Scylla

  -[Documentación API](https://scylla.sh)

  - Scylla es un Proyecto que alberga una considerable cantidad de "Data Leaks", desarrollado exclusivamente para Investigadores de Seguridad. En la actualidad, se encuentra disponible únicamente bajo autorización de su creador, Alejandro Cáceres. Para obtener las credenciales básicas de acceso a su API, podéis contactar con él vía Twitter: @_hyp3ri0n
  
- Libreborme

  -[Documentación API](https://libreborme.readthedocs.io/es/latest/api/)

- UserChecker

  - No se hacen necesarias ni doumentación ni credenciales. Introducir un Nick y a buscar!

- Blockchain.info

  -[Documentación API](https://www.blockchain.com/es/api/blockchain_api)

## Inputs de Entrada admitidos

- IP
- Dominio
- URL
- Certificados SSL
- Hashes
- Transacciones / Direcciones de Bitcoin
- Emails
- Nombres de personas
- Nombres de Empresas
- Passwords, Números de teléfono
- Nombres de Usuario


## Usus y Funcionalidades 

**OTW** se ha desarrollado de forma Modular, permitiendo, dado un Input determinado, elegir el Módulo a lanzar en función de las necesidades de información requeridas. La información que OTW aporta para cada uno de los nueve Inputs de Entrada que permite, se detalla a continuación.

BLOQUE IP
-	Extracción de Subdominios, Puertos, Servicios y Vulnerabilidades 
-	Extracción de muestras de Malware (Hashes, URL’s…)
-	Extracción de Metadatos y Bloque OSINT
-	Detección de Subredes y Registros DNS
-	Detección del Nivel de Riesgo de una IP
-	Vinculación de IP’s con Botnets
-	Enumeración de Certificados
-	Geolocalización de IP’s
-	Whois completo 

BLOQUE DOMINIOS
-	Descripción, Rankings
-	Extracción de Información Corporativa
-	Extracción de muestras de Malware (Hashes, URL’s…)
-	Extracción de Subdominios, Puertos, Servicios y Vulnerabilidades
-	Detección de Subredes y Registros DNS
-	Enumeración de Certificados
-	Geolocalización 
-	Whois completo 

BLOQUE URL’s
-	Análisis de Riesgos CTI
-	Detección por Principales AV’s
-	Detección y asignación a Familias de Malware
-	Enumeración de Registros DNS
-	Whois completo 

BLOQUE CERTIFICADOS
-	Búsqueda por certificado (sha256 y sha1)
-	Información General
-	Claves Públicas
-	Validez
-	Entidad Certificadora

BLOQUE MALWARE
-	Búsqueda por Hashes (sha256, sha1 y MD5)
-	Asignación de Niveles de Riesgo
-	Detección por Principales AV’s
-	Detección y asignación a Familias de Malware
-	Plataformas expuestas
-	Información Criptográfica
-	
BLOQUE BLOCKCHAIN
-	Extracción de información sobre Transacciones en la Blockchain de Bitcoin: Destinos, importes…
-	Extracción de información sobre Direcciones de Bitcoin: Saldos, Transacciones

BLOQUE EMAIL
-	Extracción de Información Personal 
-	Extracción de Información Profesional
-	Detección de presencia en Leaks de Información
-	Enumeración de fuentes filtradas
-	Extracción de Passwords a través de múltiples Inputs
-	Detección de Bots a partir de un email

BLOQUE PERSONAS Y EMPRESAS
-	Extracción de Información sobre Personas (a partir de un email)
-	Extracción de Información sobre Empresas (a partir de un email)
-	Búsqueda de Personas y Empresas inscritas en el Registro Mercantil
-	Extracción de Información de Cargos en Empresariales
-	Extracción de Información Societaria

BLOQUE NICKS & USERNAMES
-	Detección de presencia de Usuarios en Plataformas Sociales 
-	Detección de Usuarios en Leaks de Información
-	Detección de Bots

## Autores 

Isabel Muñoz Alfonso 

Jorge Iturria Fernández de Pinedo 

CONTACTO: pyproject@protonmail.com

## Descarga e Instalación

```
git clone https://github.com/McintProject/OTW.git 
cd OTW
pip3 install -r requeriments.txt

```
## Uso 

**OTW** requiere para su funcionamiento de la introducción de las API_KEY de cada uno de los Módulos, editando el archivo _"config.py"_, a excepción de los Módulos de BlockChain, LibreBorme y UserChecker, funcionales sin necesidad de credenciales. **Todas las API_KEY  necesarias son Gratuítas**, a excepción del Módulo de _Dehased_. **El acceso a las API_KEY de cada Módulo, así como a la documentación de cada API, los podeís encontrar en el Apartado "Módulos" de este README**.

Una vez introducidas las Claves de API, y dentro de la Carpeta OTW...

```
otw.py
```
... Rocks!

## Licencia

**OTW** se distribuye como Software Open Source con Licencia GNU V3, permitiendo al usuario adaptar el Código Fuente a sus propias necesidades, y pudiendo ser complementada con módulos adicionales, gracias a la escalabilidad en la que se ha basado su desarrollo.
