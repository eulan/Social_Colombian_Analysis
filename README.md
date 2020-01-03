# Análisis de la estructura social de Colombia desde datos Abiertos-Colombia

<h3> Violencia de Pareja 2015 </h3>

La violencia dentro de las parejas es un evento que está en continuo aumento, en donde las mujeres son las que se ven más claramente afectadas. En un conjunto de 47.248 casos de abuso, 40.943 corresponde a mujeres, con una edad que oscila entre los 20 y 34 años. Si se hace un clustering se obtiene 4 segmentos, claramente enmarcados, en donde los puntos verdes corresponde a los evento en donde son más frecuentes los actos de violencia entre los 25 y 35 años, correspondiendo a matrimonios jovenes. Dicho cluster esta constituido unicamente por mujeres, lo que es muy preocupante. Hay otro cluster, contituido por dos conjuntos, de personas, con edades de 20 a 25 y 35 a 55 años. A pesar de que el la violencia es alta y frecuente, este cluster esta constitudo por hombre y mujeres. Es interesante notar, que se presenta maltrato por edades incluso menores a los 20 y años y en ancianos. Lo que muestra que la violencia ocurre durante toda la vida de un Colombiano desde su nucleo familiar. 

Con respecto a la tasa de maltrato, en mujeres esta tasa supera por mucho a la de los hombres, sigo el caso del maltrato al genero femenino el de mayor ocurrencia en el País. Se puede observar que la violencia crece rápidamente para edades menores a los 20 años, y llegar a un máximo bien definido. disminuyendo de suavemente en la cola de la derecha indicando que los casos de violencia dentro de un hogar de adultos mayor es menos frecuente. 

En este análisis se usaron, métodos de fitting y no supervisados, extrayendo aspecto importantes de la geometría interna de los datos, y una caraterización detallada, de las similitudes entre grupos dentro de la socidad Colombiana. Los datos fueron extraídos de eventos ocurridos en el 2015 (URL: https://lnkd.in/dQtBvNY), y el Agglomerative Clustering fue hecho con el método "Ward" y con una métrica típica euclideana.

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/index.png" align=middle width=700pt height=500pt/></p>
____________________________________________________________________________________________
<h3> Trata de personas al extranjero </h3>

La trata de personas es una problemática que se sigue presentando en nuestra Colombia. Por tanto, se hizo un pequeño análisis del como se esta ejecutando en nuestro País dicha practica, y una pequeña clasificación de los departamentos por un unsupervised method de ML. Los datos fueron obtenidos de "https://lnkd.in/dmwxK77". En primer lugar, en términos globales, los departamentos en lo que ocurre la mayor cantidad de eventos de trata de personas hacia el exterior es en el Valle del Cauca y Bogotá, desde el 2016 hasta el 2019. En lo que respecta a Bogotá, se observa un claro pico, que indica un aumento de esta practica los últimos dos años, por el lado del Valle del Cauca, la tendencia a sido la disminución, y en Antioquía la dinámica a sido más o menos constante. También se observa según el clustering que el comportamiento de Bogotá y la trata en el extranjero, tiene cierta similaridad.


<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/trata_ext.png" align=middle width=400pt height=500pt/></p>
____________________________________________________________________________________________
<h3> Sobre las zonas contaminandas de Colombia </h3>


Visualización  de los lugares más contaminados del País. El material, con un aporte más importante es el PM10, el cual afecta directamente la salud, produciendo enfermedades cardíacas o pulmonares. Datos extraídos de: "https://lnkd.in/eD4vZKr".  

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/folium.png"  align=middle width=700pt height=500pt/></p>
