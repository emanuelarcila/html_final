# Proyecto Final y Examen 1: Café Altiplano
## Sitio Web Adaptable con HTML5 y CSS3 (Implementación de Talleres y Eventos)

**Estudiante:** Emanuel Steven Arcila Gómez  
**Proyecto:** Café Altiplano — Cafetería de Especialidad  
**Rama de trabajo:** `examen-01`  
**Tecnologías:** HTML5 semántico, CSS3, CSS Grid (Mobile First)  
**Restricciones cumplidas:** Cero JavaScript, cero Flexbox, cero animaciones, sin estilos inline ni `!important`.

---

## 1. Mapa del Sitio

El sitio web está estructurado en cinco páginas enlazadas mediante una barra de navegación consistente y accesible:

1. **`index.html` (Inicio):** Presenta la identidad de la cafetería con una cabecera temática, portada (*hero banner*) con imagen de fondo y llamada a la acción, reseña de café de origen, proceso artesanal en lista ordenada (`ol`), servicios en barra lateral (`aside`), galería de productos destacados en cuadrícula autoajustable y glosario en lista de definición (`dl`).
2. **`carta.html` (Carta y Menú):** Detalla la oferta gastronómica dividida en tres categorías principales accesibles mediante un índice con anclas internas (`#calientes`, `#frias`, `#acompanamientos`). Contiene tres tablas semánticas de precios con encabezados accesibles (`th scope="col/row"`), filas alternas con `:nth-child()`, cita de autoría (`blockquote` y `cite`), y galería visual de repostería.
3. **`sedes.html` (Nuestras Sedes):** Muestra las tres sedes de la cafetería (Centro Histórico, Chapinero Norte y Terraza El Jardín). Cada sede cuenta con una tarjeta independiente, fotografía estructurada con `figure` y `figcaption`, direcciones, horarios detallados, datos de contacto ficticios y sección lateral de políticas de visita.
4. **`reservas.html` (Reservas de Mesa):** Formulario accesible y estructurado con `fieldset` y `legend`, campos asociados con `label for`, controles de tipo `text`, `email`, `tel`, `date`, `time`, `number`, menú desplegable `select`, grupo de botones de opción `radio`, casillas `checkbox`, área de texto `textarea` y validaciones nativas `required` y `placeholder`. Acompañado de pasos del servicio, glosario de políticas y preguntas frecuentes.
5. **`talleres.html` (Talleres y Eventos - Examen 1):** Página dedicada a las experiencias y talleres presenciales de café. Incluye portada temática con gradiente y llamada a la acción, fotografía destacada con `figure` y `figcaption` (`.figura-taller`), tabla accesible de agenda con precios y cupos alineados a la derecha (`.tabla__celda--precio` y `.tabla__celda--cupos`), contenedor seguro con desplazamiento horizontal (`.tabla-contenedor`), galería adaptable de 6 tarjetas de talleres (`.galeria-talleres` con `repeat(auto-fit, minmax(16rem, 1fr))`), lista ordenada de inscripción (`ol`), lista sin orden de materiales y beneficios (`ul`), lista de definiciones de niveles (`dl`), y formulario completo de inscripción con `fieldset`, `legend`, `label for`, `input`, `select`, `radio`, `checkbox` y `textarea`.

---

## 2. Comportamiento Adaptable (Responsive)

El contenedor principal (`.maqueta`) utiliza CSS Grid bajo la estrategia móvil primero (*Mobile First*), garantizando fluidez sin desbordamiento horizontal:

- **Móvil (< 600 px):** Diseño en 1 sola columna. Menú apilado verticalmente en 1 columna (`grid-template-columns: 1fr`).
- **Tableta (>= 600 px):** Cuadrícula a 2 columnas (`repeat(2, 1fr)`). Menú horizontal en 5 columnas (`repeat(5, auto)`). Bloque de agenda ocupando 2 columnas (`bloque--doble` con `span 2`).
- **Escritorio (>= 900 px):** Cuadrícula a 3 columnas (`repeat(3, 1fr)`). Bloque de agenda en 2 columnas (`span 2`), barra lateral en 1 columna (`span 1` con `align-self: start`), y galería autoajustable con `auto-fit`.

---

## 3. Justificación de Cinco Unidades CSS

1. **`rem` (Unidad relativa a la raíz):** Utilizada para todos los tamaños de texto (`font-size`), espaciados internos (`padding`), márgenes (`margin`) y separaciones de cuadrícula (`gap`). Al fijar `html { font-size: 100%; }`, 1 rem equivale a los 16 px base del navegador pero respeta plenamente las preferencias de accesibilidad del usuario si decide agrandar o reducir el texto del sistema.
2. **`px` (Unidad absoluta):** Empleada exclusivamente para trazos y bordes finos (`1px solid`, `2px solid`, `4px solid`) y sombras (`box-shadow`). En elementos de 1 a 4 píxeles se busca una nitidez exacta en la pantalla sin distorsión por escala.
3. **`ch` (Unidad de ancho de carácter '0'):** Utilizada en `p { max-width: 65ch; }` y `.hero__bajada { max-width: 55ch; }`. Permite limitar la longitud de las líneas de texto a un promedio de 65 caracteres, lo cual constituye el estándar tipográfico recomendado para evitar la fatiga visual en la lectura.
4. **`%` (Porcentaje relativo al contenedor padre):** Utilizada en `img { max-width: 100%; }`, `.contenedor { width: 100%; }` y `.tabla { width: 100%; }`. Asegura que los elementos fluidos se contraigan o expandan dinámicamente con respecto al ancho disponible del contenedor sin generar desbordamientos.
5. **`vh` (Unidad de altura de ventana):** Utilizada en la sección hero `.hero { min-height: 50vh; }`. Garantiza que la portada ocupe al menos la mitad de la altura de la pantalla del usuario en cualquier resolución, generando impacto visual y bienvenida cálida tanto en móviles como en monitores de escritorio.

---

## 4. Decisiones Técnicas: Mobile First y Puntos de Ruptura

- **Estrategia Mobile First:** La mayoría de clientes que consultan cartas, horarios o reservan en una cafetería acceden desde teléfonos móviles. Por ello, la hoja de estilo base define el diseño apilado en una sola columna limpia y ligera. El código para dispositivos más grandes se incorpora progresivamente mediante `@media (min-width: ...)`.
- **Punto de ruptura 600 px:** Marca la transición entre teléfonos grandes en orientación vertical y tabletas pequeñas u orientación horizontal. A partir de 600 px el contenedor principal pasa a 2 columnas y el menú de navegación se distribuye horizontalmente en 5 columnas (`repeat(5, auto)`).
- **Punto de ruptura 900 px:** Marca la transición hacia pantallas medianas y de escritorio. Permite una distribución completa a 3 columnas en la cuadrícula principal, situando el contenido destacado en 2 columnas (`bloque--doble`) y la barra lateral de información complementaria en 1 columna (`barra-lateral`).
- **Galería con auto-fit:** Para las tarjetas de productos y las 6 tarjetas de talleres se implementó `repeat(auto-fit, minmax(16rem, 1fr))`, lo cual permite que las tarjetas se reorganicen fluidamente sin necesidad de añadir reglas `@media` manuales adicionales.

---

## 5. Dificultad Encontrada y Solución

- **Dificultad:** La integración de 5 enlaces en la cabecera móvil y tablet sin romper el contenedor, sumado a tablas de 6 columnas (agenda de talleres) que en pantallas móviles tienden a desbordar horizontalmente la pantalla.
- **Solución implementada:**
  1. Para la navegación, se utilizó CSS Grid (`display: grid`) configurando `grid-template-columns: 1fr` en móvil y `grid-template-columns: repeat(5, auto)` con `gap: 0.375rem` a partir de 600 px, garantizando que los 5 botones queden perfectamente alineados sin desborde.
  2. Para la tabla de agenda, se envolvió el elemento `<table>` dentro de un contenedor `.tabla-contenedor` con `overflow-x: auto; width: 100%;`. De este modo, en pantallas de 500 px la tabla permite un desplazamiento horizontal interno táctil sin romper ni expandir el ancho de la página web completa, garantizando que el diseño se mantenga 100% adaptable.

