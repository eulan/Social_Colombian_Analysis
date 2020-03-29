# Análisis de la estructura social de Colombia desde datos Abiertos-Colombia

<h3> Violencia de Pareja 2015 </h3>

<p>La violencia dentro de las parejas es un evento que está en continuo aumento, en donde las mujeres son las que se ven más claramente afectadas. En un conjunto de 47.248 casos de abuso, 40.943 corresponde a mujeres, con una edad que oscila entre los 20 y 34 años. Si se hace un clustering se obtiene 4 segmentos, claramente enmarcados, en donde los puntos verdes corresponde a los evento en donde son más frecuentes los actos de violencia entre los 25 y 35 años, correspondiendo a matrimonios jovenes. Dicho cluster esta constituido unicamente por mujeres, lo que es muy preocupante. Hay otro cluster, contituido por dos conjuntos, de personas, con edades de 20 a 25 y 35 a 55 años. A pesar de que el la violencia es alta y frecuente, este cluster esta constitudo por hombre y mujeres. Es interesante notar, que se presenta maltrato por edades incluso menores a los 20 y años y en ancianos. Lo que muestra que la violencia ocurre durante toda la vida de un Colombiano desde su nucleo familiar.</p> 

<p>Con respecto a la tasa de maltrato, en mujeres esta tasa supera por mucho a la de los hombres, sigo el caso del maltrato al genero femenino el de mayor ocurrencia en el País. Se puede observar que la violencia crece rápidamente para edades menores a los 20 años, y llegar a un máximo bien definido. disminuyendo de suavemente en la cola de la derecha indicando que los casos de violencia dentro de un hogar de adultos mayor es menos frecuente.</p> 

<p>En este análisis se usaron, métodos de fitting y no supervisados, extrayendo aspecto importantes de la geometría interna de los datos, y una caraterización detallada, de las similitudes entre grupos dentro de la socidad Colombiana. Los datos fueron extraídos de eventos ocurridos en el 2015 (URL: https://lnkd.in/dQtBvNY), y el Agglomerative Clustering fue hecho con el método "Ward" y con una métrica típica euclideana.</p>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/index.png" align=middle width=700pt height=500pt/></p>

<h4>Ver código: <a href = "https://github.com/eulan/Social_Colombian_Analysis/blob/master/violencia.py"> link</a> </h4>
____________________________________________________________________________________________
<h3> Trata de personas al extranjero </h3>

<p>La trata de personas es una problemática que se sigue presentando en nuestra Colombia. Por tanto, se hizo un pequeño análisis del como se esta ejecutando en nuestro País dicha practica, y una pequeña clasificación de los departamentos por un unsupervised method de ML. Los datos fueron obtenidos de "https://lnkd.in/dmwxK77". En primer lugar, en términos globales, los departamentos en lo que ocurre la mayor cantidad de eventos de trata de personas hacia el exterior es en el Valle del Cauca y Bogotá, desde el 2016 hasta el 2019. En lo que respecta a Bogotá, se observa un claro pico, que indica un aumento de esta practica los últimos dos años, por el lado del Valle del Cauca, la tendencia a sido la disminución, y en Antioquía la dinámica a sido más o menos constante. También se observa según el clustering que el comportamiento de Bogotá y la trata en el extranjero, tiene cierta similaridad.</p>


<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/trata_ext.png" align=middle width=800pt height=500pt/></p>

<h4>Ver código: <a href = "https://github.com/eulan/Social_Colombian_Analysis/blob/master/trata.py"> link</a> </h4>
____________________________________________________________________________________________
<h3> Sobre las zonas contaminandas de Colombia </h3>


<p>Visualización  de los lugares más contaminados del País. El material, con un aporte más importante es el PM10, el cual afecta directamente la salud, produciendo enfermedades cardíacas o pulmonares. Datos extraídos de: "https://lnkd.in/eD4vZKr".</p>  

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/folium.png"  align=middle width=400pt height=500pt/></p>
<h4>Ver código: <a href = "https://github.com/eulan/Social_Colombian_Analysis/blob/master/folium.py"> link</a> </h4>
____________________________________________________________________________________________

<h3>Análisis de la Caracterización del Empleo Público</h3>

<p>De lo que se puede ver, es que existe con respecto al clustering una anomalía, que indica la existencia de un pequeño cluster hecho por mujeres, que tiene el salario más alto del País, cercano a los 37 millones de pesos. Esta anomalía es también mostrada como un circulo amarillo, en el mapa. Por otro lado, se puede observar que los salarios más grandes pertenecen a unas minorías, mostrando desigualdad.</p>

<p>Con respecto a las poblaciones, el sector publico tiende a dar empleo con mayor frecuencia a las personas con nivel de bachiller y especialización. La experiencia laboral, preferente va desde 1 a 10 años, con una edad entre los 50 y 62 años, siendo las mujeres más frecuentes en cargos públicos.</p>

<p>La contratación ocurre con mayor frecuencia en las alcaldías, concejos y personerías, como entidades municipales es de esperar, siendo Bogotá, el de mayor demanda y mejor salario.</p>

<p>Esta información es respecto a la caracterización de los servidores públicos registrados en SIGEP de la Rama Ejecutiva Orden Nacional (https://lnkd.in/dDqPbXY).</p>


<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/c1.png" align=middle width=400pt height=300pt/></p>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/c2.png" align=middle width=400pt height=300pt/></p>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/c3.png" align=middle width=400pt height=400pt/></p>

<h4>Ver código: <a href = "https://github.com/eulan/Social_Colombian_Analysis/blob/master/caracterizacion.py"> link</a> </h4>

____________________________________________________________________________________________

<h3>Colombian Population</h3>


<p>The classical models of population consist of considering rate equation where the base approximation is exponential kind. However, the increase of Colombian population shows to other behavior, it is more, that is lineal due to the conflicting history.</p>


<p>The most frequent population is between 0 to 24 years, implicating that Colombia is a young country, where the majority of people are men. After the 24 years the population experiments a transition (as phase transition), the female population begins to grow and overcomes the men.</p>


<p>Finally, the data system can be separated in four clusters cleanly, where the most important population in Colombia are young. The older adults are more women than men, implicating that the women have a longest life, other possible explication is the armed conflict where the men are more affected.</p>


<p>The information was obtained of "datos Abiertos Colombia" and the URL was "https://www.datos.gov.co/Mapas-Nacionales/PROYECCIONES-POBLACI-N-Poblaci-n-por-municipio-y-d/grgp-6bef".</p>


<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/pob1.png" align=middle width=400pt height=400pt/></p>



<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/pob2.png" align=middle width=400pt height=400pt/></p>



<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/pob3.png" align=middle width=400pt height=400pt/></p>

<h4>Ver código: <a href = "https://github.com/eulan/Social_Colombian_Analysis/blob/master/poblacion.ipynb"> link</a> </h4>

____________________________________________________________________________________________

<h3>Análisis de las obras de Gabriel García Márquez</h3>

<h4>"Cien años de soledad", "El amor en los tiempos del cólera", "Del amor y otros demonios" y "Crónicas de una muerte anunciada"</h4>

<p>El Machine Learning es una herramienta estadística muy interesante que nos ha permitido incluso ver los patrones detras del lenguaje humano, hoy se va a utilizar un modelo pre-trained de trabajos previos para la clasificación de sentimientos de estas cuatro importantes novelas del famoso autor ¿Qué crees que pasaría un computador al estas obras? ¿Pensaría que son obras muy positivas o negativas? Bueno, hoy vamos a saberlo.</p>

<h5>Aplicación de modelos de analysis sentiment a obras de Gabo</h5>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/model_appCien%20a%C3%B1os%20de%20soledad.png" align=middle width=400pt height=400pt/></p>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/model_appCr%C3%B3nicas%20de%20una%20muerte%20anunciada.png" align=middle width=400pt height=400pt/></p>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/model_appDel%20amor%20y%20otros%20demonios.png" align=middle width=400pt height=400pt/></p>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/model_appEl%20amor%20en%20los%20tiempos%20del%20c%C3%B3lera.png" align=middle width=400pt height=400pt/></p>

<p>Los modelos clasifican las obras de Gabo como neutras o negativas, lo que es lógico por su alto contenido trágico.</p>

<h5>Wordclouds</h5>

<p align="center"><img src="https://github.com/eulan/Social_Colombian_Analysis/blob/master/wordcloud.png" align=middle width=400pt height=400pt/></p>

<p>La palabras más frecuentes además de los conectores, son los nombres de sus personales.</p>

<h4>Ver código: <a href = "https://github.com/eulan/Social_Colombian_Analysis/blob/master/poblacion.ipynb"> link</a> </h4>
