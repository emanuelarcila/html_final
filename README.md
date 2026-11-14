# Proyecto Final: Café Altiplano
## Sitio Web Adaptable con HTML5 y CSS3

**Estudiante:** Emanuel Steven Arcila Gómez  
**Proyecto:** Café Altiplano — Cafetería de Especialidad  
**Tecnologías:** HTML5 semántico, CSS3, CSS Grid (Mobile First)  
**Restricciones cumplidas:** Cero JavaScript, cero Flexbox, cero animaciones, sin estilos inline ni `!important`.

---

## 1. Mapa del Sitio

El sitio web está estructurado en cuatro páginas enlazadas mediante una barra de navegación consistente:

1. **`index.html` (Inicio):** Presenta la identidad de la cafetería con una cabecera temática, portada (*hero banner*) con imagen de fondo y llamada a la acción, reseña de café de origen, proceso artesanal en lista ordenada (`ol`), servicios en barra lateral (`aside`), galería de productos destacados en cuadrícula autoajustable y glosario en lista de definición (`dl`).
2. **`carta.html` (Carta y Menú):** Detalla la oferta gastronómica dividida en tres categorías principales accesibles mediante un índice con anclas internas (`#calientes`, `#frias`, `#acompanamientos`). Contiene tres tablas semánticas de precios con encabezados accesibles (`th scope="col/row"`), filas alternas con `:nth-child()`, cita de autoría (`blockquote` y `cite`), y galería visual de repostería.
3. **`sedes.html` (Nuestras Sedes):** Muestra las tres sedes de la cafetería (Centro Histórico, Chapinero Norte y Terraza El Jardín). Cada sede cuenta con una tarjeta independiente, fotografía estructurada con `figure` y `figcaption`, direcciones, horarios detallados, datos de contacto ficticios y sección lateral de políticas de visita.
4. **`reservas.html` (Reservas de Mesa):** Formulario accesible y estructurado con `fieldset` y `legend`, campos asociados con `label for`, controles de tipo `text`, `email`, `tel`, `date`, `time`, `number`, menú desplegable `select`, grupo de botones de opción `radio`, casillas `checkbox`, área de texto `textarea` y validaciones nativas `required` y `placeholder`. Acompañado de pasos del servicio y preguntas frecuentes.

---

## 2. Comportamiento Adaptable (Responsive)

El contenedor principal (`.maqueta`) utiliza CSS Grid bajo la estrategia móvil primero (*Mobile First*), garantizando fluidez sin desbordamiento horizontal:

| Página | 500 px (Móvil) | 800 px (Tableta) | 1200 px (Computador) |
|---|---|---|---|
| **index.html** | 1 columna, sin scroll | 2 columnas, sin scroll | 3 columnas, sin scroll |
| **carta.html** | 1 columna, sin scroll | 2 columnas, sin scroll | 3 columnas, sin scroll |
| **sedes.html** | 1 columna, sin scroll | 2 columnas, sin scroll | 3 columnas, sin scroll |
| **reservas.html** | 1 columna, sin scroll | 2 columnas, sin scroll | 3 columnas, sin scroll |

---

## 3. Justificación de Cinco Unidades CSS (RF-06.5)

1. **`rem` (Unidad relativa a la raíz):** Utilizada para todos los tamaños de texto (`font-size`), espaciados internos (`padding`), márgenes (`margin`) y separaciones de cuadrícula (`gap`). Al fijar `html { font-size: 100%; }`, 1 rem equivale a los 16 px base del navegador pero respeta plenamente las preferencias de accesibilidad del usuario si decide agrandar o reducir el texto del sistema.
2. **`px` (Unidad absoluta):** Empleada exclusivamente para trazos y bordes finos (`1px solid`, `2px solid`, `4px solid`) y sombras (`box-shadow`). En elementos de 1 a 4 píxeles se busca una nitidez exacta en la pantalla sin distorsión por escala.
3. **`ch` (Unidad de ancho de carácter '0'):** Utilizada en `p { max-width: 65ch; }`. Permite limitar la longitud de las líneas de texto a un promedio de 65 caracteres, lo cual constituye el estándar tipográfico recomendado para evitar la fatiga visual en la lectura.
4. **`%` (Porcentaje relativo al contenedor padre):** Utilizada en `img { max-width: 100%; }`, `.contenedor { width: 100%; }` y `.tabla { width: 100%; }`. Asegura que los elementos fluidos se contraigan o expandan dinámicamente con respecto al ancho disponible del contenedor sin generar desbordamientos.
5. **`vh` (Unidad de altura de ventana):** Utilizada en la sección hero `.hero { min-height: 50vh; }`. Garantiza que la portada ocupe al menos la mitad de la altura de la pantalla del usuario en cualquier resolución, generando impacto visual y bienvenida cálida tanto en móviles como en monitores de escritorio.

---

## 4. Decisiones Técnicas: Mobile First y Puntos de Ruptura

- **Estrategia Mobile First:** La mayoría de clientes que consultan cartas, horarios o reservan en una cafetería acceden desde teléfonos móviles. Por ello, la hoja de estilo base define el diseño apilado en una sola columna limpia y ligera. El código para dispositivos más grandes se incorpora progresivamente mediante `@media (min-width: ...)`.
- **Punto de ruptura 600 px:** Marca la transición entre teléfonos grandes en orientación vertical y tabletas pequeñas u orientación horizontal. A partir de 600 px el contenedor principal pasa a 2 columnas y el menú de navegación se distribuye horizontalmente.
- **Punto de ruptura 900 px:** Marca la transición hacia pantallas medianas y de escritorio. Permite una distribución completa a 3 columnas en la cuadrícula principal, situando el contenido destacado en 2 columnas (`bloque--doble`) y la barra lateral de información complementaria en 1 columna (`barra-lateral`).
- **Galería con auto-fit:** Para las tarjetas de productos se implementó `repeat(auto-fit, minmax(16rem, 1fr))`, lo cual permite que las tarjetas se reorganicen fluidamente sin necesidad de añadir reglas `@media` manuales adicionales.

---

## 5. Dificultad Encontrada y Solución

- **Dificultad:** La restricción estricta de no utilizar Flexbox para la barra de navegación ni para los botones alineados, sumada a la necesidad de presentar tablas de precios con 4 columnas que en pantallas móviles de 500 px tienden a desbordar la ventana horizontalmente.
- **Solución implementada:**
  1. Para la navegación y los botones, se utilizó CSS Grid (`display: grid`) configurando `grid-template-columns: 1fr` en móvil y `grid-template-columns: repeat(4, auto)` a partir de 600 px, demostrando el dominio de Grid en componentes pequeños sin requerir Flexbox.
  2. Para las tablas de precios, se envolvió cada elemento `<table>` dentro de un contenedor `.tabla-contenedor` con `overflow-x: auto; width: 100%;`. De este modo, en pantallas de 500 px la tabla permite un desplazamiento horizontal interno táctil sin romper ni expandir el ancho de la página web completa, cumpliendo el requisito RF-05.5 y RF-07.7.

