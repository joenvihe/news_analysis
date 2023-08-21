# Analizador de noticias peruanas:
Objetivo: análizar noticias, de medios peruanos, a través de diferentes gráficos planteados en un dashboard

## Campos utilizados para hacer los análisis:
- Resumen del texto
- p&n: buenas o malas noticias
- Definición de la noticia en 1 palabra
- Listados de ideas principales en la noticia
- Listado de palabras claves
- Categoria de la noticia
- Entidades identificados en la noticias: Nombre, tipo de entidad, descripcion, que se habla de la entidad, propiedades de la entidad
- Nombre del peridico
- La hora de publicación

## Listado de graficos:

- Grafico de barras de medios y cantidad de noticias por medio, en un determinado periodo.
- Grafico de linea de tiempo de cantidad de noticias por fechas y medios.
- Gráfico de Barras Apiladas de Sentimient (positivo, negativo, otros), por entidades, categorias, palabras claves
- Nube de palabras claves.
- Grafos de entidades(personas, organizaciones, ubicaciones, etc.) y como se relacionan entre ellos
- mapa geografico.
- Gráfico de Barras Horizontales de Entidades Más Mencionadas, para resaltar quiénes son los protagonistas más destacados en la colección.
- Gráfico de Tendencias de Palabras Clave, cómo cambia la frecuencia de las palabras clave a lo largo del tiempo
- heatmap de Frecuencia de Palabras Clave, visualizar la frecuencia de las palabras clave en función de la fecha y la categoría. Los colores pueden representar la intensidad de la frecuencia, lo que permite detectar patrones rápidamente
- Gráfico de Relación entre Palabras Clave, encontrar las relaciones.
- Gráfico de sectores para comparar la frecuencia de diferentes entidades (personas, organizaciones) mencionadas en las noticias. 
- Gráfico de Densidad de Noticias por Hora del Día, mostrar cuándo se publican más noticias a lo largo del día
- Mapa de Calor de Entidades Geográficas: Muestra las ubicaciones geográficas mencionadas en las noticias en un mapa de calor. Esto podría ayudar a identificar áreas geográficas clave en las noticias y sus relaciones.
- Gráfico de Flujo de Temas Principales: Muestra cómo los temas principales en las noticias cambian con el tiempo. Puede ayudar a visualizar las tendencias y los eventos relevantes en un período determinado.
- Comparación de Sentimiento por Palabra Clave: Combina el sentimiento con las categorías y las palabras clave para identificar las emociones asociadas con temas específicos en diferentes categorías.
- Diagrama de Árbol de Temas y Subtemas: Visualiza las jerarquías de temas y subtemas en las noticias en un diagrama de árbol. Esto puede revelar la estructura de las historias y cómo se conectan diferentes ideas.
- Comparación de Cobertura de Categorías en Diferentes Medios: Si tienes datos de múltiples medios de noticias, un gráfico de barras puede comparar la cobertura de diferentes categorías en cada medio, lo que permite identificar enfoques diferentes.
- Gráfico de Frecuencia de Hashtags o Etiquetas:
Si las noticias incluyen hashtags o etiquetas, un gráfico de barras puede mostrar la frecuencia de diferentes hashtags en un período de tiempo.
- Comparación de Contenido de Noticias por Categoría:
Utiliza un gráfico de burbujas para comparar el contenido de las noticias en función de diferentes métricas (longitud del contenido, cantidad de entidades, etc.) en diferentes categorías.
- Gráfico tridimensional (3D) que combine varias variables importantes de la noticia para proporcionar una vista completa y profunda de la información. Cada eje del gráfico podría representar una variable diferente, y el tamaño, el color y la forma de los puntos en el gráfico podrían representar otras variables clave.

Por ejemplo, podrías combinar las siguientes variables:
Eje X: Sentimiento: Representa el sentimiento de la noticia en una escala de emociones (positivo, neutral, negativo).
Eje Y: Categoría: Muestra la categoría de la noticia (política, economía, entretenimiento, etc.).
Eje Z: Importancia: Indica la importancia de la noticia en una escala (alta, media, baja).
Tamaño de los Puntos: Representa la longitud del contenido de la noticia.
Color de los Puntos: Codifica el tema principal de la noticia (basado en palabras clave).
Forma de los Puntos: Indica la fuente de la noticia (por ejemplo, medios de comunicación diferentes).
Cada punto en el gráfico tridimensional podría representar una noticia individual. Los usuarios podrían explorar el gráfico moviéndose en tres dimensiones y observando cómo diferentes variables se combinan para representar cada noticia. Un punto grande, de color rojo y en forma de círculo podría representar una noticia negativa, de alta importancia en la categoría política, con un contenido largo y de una fuente específica, por ejemplo.

Nota: generar mapa conceptual con GPT

## Ejemplos de web:

- https://ai-talks.streamlit.app/
- https://bert-keyword-extractor.streamlit.app/
- https://gptflix.streamlit.app/
- https://multichem-mlb-research-tables-streamlit-app-r18mai.streamlit.app/
- https://st-worldle.streamlit.app/?locale=en
- https://cefis-food-indices.streamlit.app/


## Web de base
- https://farolcovid.coronacidades.org/?page=Inicio#
- https://github.com/ImpulsoGov/farolcovid/blob/stable/src/farolcovid.py

## Ejecucion
> streamlit run app.py --server.port 8888






