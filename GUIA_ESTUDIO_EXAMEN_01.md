# GUÍA DE ESTUDIO COMPLETA: EXAMEN 1 — CAFÉ ALTIPLANO
## Implementación de Talleres y Eventos (Unidades 01 a 07)

**Estudiante:** Emanuel Steven Arcila Gómez  
**Proyecto:** Café Altiplano — Cafetería de Especialidad  
**Rama de trabajo:** `main` (fusión de `examen-01`)  
**Página desarrollada:** `talleres.html`  
**Tecnologías:** HTML5 Semántico y CSS3 Puro (Grid Layout, Mobile First)  
**Restricciones académicas:** Cero JavaScript, cero Flexbox, cero animaciones, sin estilos inline ni `!important`.

---

## 1. Estructura General del Proyecto

El proyecto web de **Café Altiplano** está organizado bajo una arquitectura modular limpia donde se separa la estructura semántica (HTML), el diseño visual (CSS) y los recursos multimedia (imágenes).

```text
trabajo_entrega_final_html.css/
├── index.html                   (Página de Inicio - Enlace a Talleres en cabecera y pie)
├── carta.html                   (Página de Carta y Menú - Enlace a Talleres en cabecera y pie)
├── sedes.html                   (Página de Sedes - Enlace a Talleres en cabecera y pie)
├── reservas.html                (Página de Reservas - Enlace a Talleres en cabecera y pie)
├── talleres.html                (Página NUEVA - Examen 1: Talleres y Eventos)
├── README.md                    (Documentación técnica del proyecto - Actualizado)
├── GUIA_ESTUDIO_EXAMEN_01.md    (Esta guía didáctica de estudio y sustentación)
├── css/
│   ├── base.css                 (Variables en :root, reset de caja, html y body)
│   ├── tipografia.css           (Fuentes, encabezados, párrafos a 65ch y enlaces)
│   ├── cajas.css                (Contenedor 75rem, tarjetas, figuras y glosarios)
│   ├── componentes.css          (Botones, menús, tablas, formularios y celdas)
│   └── layout.css               (Grilla Mobile First, breakpoints 600px y 900px)
└── imagenes/
    ├── hero-cafe.jpg            (Foto de portada hero)
    ├── cappuccino.jpg           (Foto de latte art utilizada en figura de talleres)
    ├── espresso.jpg             (Foto de espresso)
    ├── filtrado.jpg             (Foto de método filtrado)
    └── ...                      (Demás fotos de productos y sedes)
```

### Función de cada archivo nuevo o modificado

1. **`talleres.html` (NUEVO):** Es la quinta página del sitio. Presenta la agenda de talleres en una tabla semántica, una figura ilustrativa (`.figura-taller`), las tres listas requeridas (`ol`, `ul`, `dl`), una galería autoajustable de seis tarjetas de talleres (`.galeria-talleres`) y el formulario completo de inscripción.
2. **`index.html`, `carta.html`, `sedes.html`, `reservas.html` (MODIFICADOS):** Se actualizó el menú de cabecera (`.menu__lista`) y el listado de navegación del pie (`.pie__lista`) para incorporar el enlace hacia `talleres.html`, manteniendo el enlace activo exacto en cada una sin romper la navegación.
3. **`css/layout.css` (MODIFICADO):** Se actualizó el breakpoint de 600 px (`@media (min-width: 600px)`) para que `.menu__lista` distribuya 5 columnas horizontales (`repeat(5, auto)`) con espaciado cómodo (`gap: 0.375rem`), garantizando que los 5 botones quepan perfectamente en tabletas y computadores.
4. **`css/componentes.css` (MODIFICADO):** Se agregó la clase semántica `.tabla__celda--cupos` para alinear números y cupos a la derecha con su propia variable, complementando la clase existente `.tabla__celda--precio`.
5. **`css/cajas.css` (MODIFICADO):** Se agregó la clase `.figura-taller` con su imagen y pie de foto para mantener nombres 100% representativos e independientes.
6. **`css/base.css` (MODIFICADO):** Se agregaron variables independientes para cupos (`--color-tabla-cupos`) y figura de talleres (`--color-taller-figura-*`).
7. **`README.md` (ACTUALIZADO):** Se documentó la nueva página `talleres.html`, su integración con el mapa del sitio y la justificación de las decisiones técnicas.
8. **`GUIA_ESTUDIO_EXAMEN_01.md` (NUEVO):** Guía pedagógica exhaustiva para comprender, modificar y defender cada línea de código ante el docente evaluador.

---

## 2. HTML Explicado (Paso a Paso de Arriba hacia Abajo)

A continuación, recorremos el archivo `talleres.html` bloque por bloque, explicando qué hace cada etiqueta, por qué se usó y qué pasaría si se modifica o elimina.

### A. Metadatos y Encabezado del Documento (`<head>`)

```html
<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Talleres y Eventos - Café Altiplano | Cafetería de Especialidad</title>

  <!-- Hojas de estilo externas -->
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/tipografia.css">
  <link rel="stylesheet" href="css/cajas.css">
  <link rel="stylesheet" href="css/componentes.css">
  <link rel="stylesheet" href="css/layout.css">
</head>
```

- **`<!DOCTYPE html>`:** Declara que el documento sigue la especificación HTML5 estándar. Si se elimina, los navegadores antiguos entran en "modo quirks" (modo de compatibilidad), interpretando el modelo de caja de forma errónea.
- **`<html lang="es">`:** Indica que el idioma principal del contenido es español. Es vital para la accesibilidad (los sintetizadores de voz para personas invidentes leen con pronunciación española) y para motores de búsqueda.
- **`<meta charset="UTF-8">`:** Codificación de caracteres universal. Permite mostrar tildes (á, é, í, ó, ú), eñes (ñ) y signos sin que aparezcan símbolos extraños (`Ã¡`).
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`:** **Regla de oro del Responsive Design.** Hace que el ancho visible de la página coincida con el ancho de la pantalla del dispositivo (`width=device-width`) y que el zoom inicial sea 100% (`initial-scale=1.0`). Sin esta etiqueta, los celulares muestran la página miniaturizada como si fuera un monitor de escritorio.
- **`<title>`:** Define el título que aparece en la pestaña del navegador y en los resultados de Google. Debe ser único y descriptivo para cada página.
- **`<link rel="stylesheet" href="...">`:** Enlaza las cinco hojas CSS en un orden lógico: primero variables y reset (`base.css`), luego fuentes (`tipografia.css`), contenedores (`cajas.css`), elementos interactivos (`componentes.css`) y finalmente la cuadrícula y breakpoints (`layout.css`).

---

### B. Cabecera y Menú de Navegación (`<header>` y `<nav>`)

```html
  <!-- Cabecera principal -->
  <header class="cabecera">
    <div class="contenedor cabecera__interior">
      <a href="index.html" class="cabecera__logotipo">
        <span class="cabecera__marca">Café Altiplano</span>
        <span class="cabecera__subtitulo">Cafetería de Especialidad</span>
      </a>

      <!-- Menu de navegacion principal -->
      <nav class="menu" aria-label="Navegación principal">
        <ul class="menu__lista">
          <li class="menu__item"><a href="index.html" class="menu__enlace">Inicio</a></li>
          <li class="menu__item"><a href="carta.html" class="menu__enlace">Carta</a></li>
          <li class="menu__item"><a href="sedes.html" class="menu__enlace">Sedes</a></li>
          <li class="menu__item"><a href="reservas.html" class="menu__enlace">Reservas</a></li>
          <li class="menu__item"><a href="talleres.html" class="menu__enlace menu__enlace--activo">Talleres</a></li>
        </ul>
      </nav>
    </div>
  </header>
```

- **`<header class="cabecera">`:** Contenedor semántico superior del sitio. Ocupa todo el ancho (`width: 100%`) y tiene el gradiente marrón café característico de la marca.
- **`<div class="contenedor cabecera__interior">`:** Limita el contenido a un ancho máximo de `75rem` (1200 px) y lo centra con `margin: 0 auto`.
- **`<nav class="menu" aria-label="Navegación principal">`:** Elemento semántico exclusivo para bloques de navegación. El atributo `aria-label` ayuda a lectores de pantalla a distinguir este menú del menú de enlaces del pie.
- **`<ul class="menu__lista">`:** Lista desordenada que agrupa los 5 ítems. En HTML semántico, los menús siempre deben ser listas `<ul>` de enlaces `<a>`.
- **`class="menu__enlace menu__enlace--activo"`:** Modificador BEM que resalta visualmente en qué página se encuentra el usuario (en este caso, en Talleres).

---

### C. Portada Hero (Requerimiento A)

```html
  <main class="contenedor maqueta">

    <!-- A. Introduccion y portada -->
    <section class="hero bloque--completo">
      <h1 class="hero__titulo">Talleres y Experiencias de Café</h1>
      <p class="hero__bajada">Cada mes abrimos nuestras sedes para aprender sobre café: desde probar sin ver la etiqueta hasta dibujar corazones en la espuma. Los cupos son limitados.</p>
      <div class="hero__acciones">
        <a href="#agenda" class="boton boton--primario">Ver Agenda</a>
        <a href="#inscripcion" class="boton boton--secundario">Inscribirme Ahora</a>
      </div>
    </section>
```

- **`<main class="contenedor maqueta">`:** Engloba el contenido principal de la página. La clase `.maqueta` aplica `display: grid`.
- **`<section class="hero bloque--completo">`:** Bloque de impacto visual. `bloque--completo` tiene `grid-column: 1 / -1`, lo que hace que abarque todas las columnas de la grilla.
- **`<h1>`:** Título de primer nivel. **Solo debe haber exactamente un `<h1>` por página** para cumplir con la jerarquía semántica y el estándar SEO/accesibilidad.
- **`<p class="hero__bajada">`:** Contiene el texto exacto exigido en el examen.
- **`<div class="hero__acciones">`:** Enlaces con aspecto de botón (`.boton--primario` y `.boton--secundario`) con anclas internas (`#agenda` e `#inscripcion`) que permiten navegar de inmediato a las secciones clave de la página.

---

### D. Agenda de Talleres (Requerimiento B)

```html
    <!-- B. Agenda de talleres (Ocupa dos columnas desde 600px: bloque--doble) -->
    <section id="agenda" class="tarjeta bloque--doble">
      <h2>Agenda de Talleres</h2>
      <p>Consultá las fechas programadas para este mes y apartá tu lugar con anticipación.</p>

      <!-- Tabla estructurada dentro de contenedor con scroll horizontal -->
      <div class="tabla-contenedor">
        <table class="tabla">
          <caption class="tabla__caption">Cronograma de talleres y experiencias cafeteras</caption>
          <thead>
            <tr>
              <th scope="col">Fecha</th>
              <th scope="col">Taller</th>
              <th scope="col">Sede</th>
              <th scope="col">Duración</th>
              <th scope="col" class="tabla__celda--cupos">Cupos</th>
              <th scope="col" class="tabla__celda--precio">Precio</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">7 de marzo</th>
              <td>Cata a ciegas</td>
              <td>Centro</td>
              <td>2 h</td>
              <td class="tabla__celda--cupos">12</td>
              <td class="tabla__celda--precio">$ 30.000</td>
            </tr>
            <!-- (demás filas) -->
          </tbody>
        </table>
      </div>
    </section>
```

- **`class="tarjeta bloque--doble"`:** En pantallas de tableta (>= 600 px) y escritorio (>= 900 px), la clase `.bloque--doble` hace que ocupe **2 columnas** (`grid-column: span 2`), tal como exige el examen.
- **`<div class="tabla-contenedor">`:** Contenedor con `overflow-x: auto;`. Si la tabla es más ancha que la pantalla de un celular (por ejemplo en 500 px), el usuario puede desplazar la tabla con el dedo sin desbordar el resto de la página.
- **`<caption>`:** Título accesible de la tabla. Los lectores de pantalla lo leen antes de entrar a las celdas.
- **`<thead>` y `<tbody>`:** Separan estructuralmente el encabezado de las filas de datos.
- **`<th scope="col">` y `<th scope="row">`:** `<th>` representa una celda de encabezado. El atributo `scope="col"` indica que encabeza una columna vertical; `scope="row"` indica que encabeza la fila horizontal actual (la fecha).
- **`.tabla__celda--cupos` y `.tabla__celda--precio`:** Clases BEM semánticas que alinean los números de cupos y precios a la derecha con `text-align: right;`, cumpliendo la buena práctica contable y el requisito del examen.

---

### E. Barra Lateral: Figura y Listas (Requerimientos A, D, E y F)

```html
    <!-- Barra lateral de informacion complementaria (bloque--completo en móvil, span 1 en desktop) -->
    <aside class="tarjeta tarjeta--destacada barra-lateral">
      <h2>Información de los Talleres</h2>

      <!-- Figura con imagen descriptiva y figcaption (Requerimiento A) -->
      <figure class="figura-taller">
        <img src="imagenes/cappuccino.jpg" alt="Barista vertiendo leche texturizada para crear un corazón en una taza de cappuccino" class="figura-taller__imagen">
        <figcaption class="figura-taller__pie">Práctica guiada de emulsión de leche y vertido en nuestro taller de latte art.</figcaption>
      </figure>

      <!-- D. Cómo inscribirse (Lista ordenada) -->
      <h3>Cómo inscribirse</h3>
      <ol class="lista-pasos">
        <li>Elegí el taller y la fecha.</li>
        <li>Completá el formulario de esta página.</li>
        <li>Recibirás la confirmación por correo en 24 horas.</li>
        <li>Presentate 10 minutos antes en la sede.</li>
      </ol>

      <!-- E. Qué incluye cada taller (Lista sin orden) -->
      <h3>Qué incluye cada taller</h3>
      <ul class="lista-caracteristicas">
        <li>Todos los materiales.</li>
        <li>Degustación de tres cafés.</li>
        <li>Certificado de participación.</li>
        <li>10 % de descuento en la carta ese día.</li>
      </ul>

      <!-- F. Niveles (Lista de definición) -->
      <h3>Niveles</h3>
      <dl class="glosario-lista">
        <dt class="glosario-termino">Básico</dt>
        <dd class="glosario-definicion">No requiere experiencia previa.</dd>
        <dt class="glosario-termino">Intermedio</dt>
        <dd class="glosario-definicion">Conviene haber asistido a un taller básico.</dd>
      </dl>
    </aside>
```

- **`<aside class="barra-lateral">`:** En Grid a 900 px ocupa 1 columna (`grid-column: span 1`) y se ubica al lado de la agenda de 2 columnas (2 + 1 = 3 columnas totales).
- **`<figure class="figura-taller">` y `<figcaption>`:** Elemento semántico para vincular una imagen con su leyenda o pie explicativo de talleres.
- **`<ol class="lista-pasos">`:** Lista **ordenada** con números automáticos. Se usa obligatoriamente aquí porque los pasos de inscripción tienen un orden cronológico estricto (Paso 1, 2, 3 y 4).
- **`<ul class="lista-caracteristicas">`:** Lista **no ordenada** con viñetas. Se usa porque los materiales e inclusiones no dependen de un orden cronológico.
- **`<dl class="glosario-lista">`:** Lista de **descripciones o definiciones** (*description list*). Contiene pares de términos (`<dt>`) y descripciones (`<dd>`), ideal para los niveles Básico e Intermedio.

---

### F. Galería Autoajustable de 6 Tarjetas (Requerimiento C)

```html
    <!-- C. Galería de talleres (6 tarjetas autoajustables) -->
    <section class="bloque--completo">
      <h2>Nuestros Talleres</h2>
      <p>Conocé el contenido de cada experiencia y elegí la que mejor se adapte a tu curiosidad cafetera.</p>

      <div class="galeria-talleres">
        <!-- Tarjeta 1 -->
        <article class="tarjeta">
          <div class="tarjeta__cuerpo">
            <h3>Cata a ciegas</h3>
            <p>Reconocé aromas y sabores sin ver la etiqueta.</p>
            <p><strong>Nivel:</strong> Básico</p>
          </div>
        </article>
        <!-- (tarjetas 2 a 6) -->
      </div>
    </section>
```

- **`<div class="galeria-talleres">`:** Utiliza `repeat(auto-fit, minmax(16rem, 1fr))`. Acomoda automáticamente las 6 tarjetas en 1 columna en celular, 2 columnas en tableta y 3 columnas en escritorio, **sin utilizar ninguna media query**.
- **`<article class="tarjeta">`:** Elemento semántico independiente que representa una unidad de contenido autocontenida (cada taller).

---

### G. Formulario de Inscripción Accesible (Requerimiento G)

```html
    <!-- G. Formulario de inscripcion -->
    <section id="inscripcion" class="bloque--completo tarjeta">
      <h2>Formulario de Inscripción</h2>
      <p>Completá los siguientes datos para reservar tu cupo en el taller de tu interés.</p>

      <form class="formulario" action="#" method="get">
        <fieldset class="formulario__seccion">
          <legend class="formulario__leyenda">Datos Personales y Selección del Taller</legend>

          <!-- Fila 1: Nombre y Correo -->
          <div class="formulario__fila">
            <div class="formulario__grupo">
              <label for="campo-nombre" class="formulario__etiqueta">Nombre completo:</label>
              <input type="text" id="campo-nombre" name="nombre" class="formulario__campo" placeholder="Ej. Camila Morales Restrepo" required>
            </div>
            <div class="formulario__grupo">
              <label for="campo-correo" class="formulario__etiqueta">Correo electrónico:</label>
              <input type="email" id="campo-correo" name="correo" class="formulario__campo" placeholder="camila.morales@correo.com" required>
            </div>
          </div>

          <!-- Fila 2: Taller y Acompañantes -->
          <div class="formulario__fila">
            <div class="formulario__grupo">
              <label for="campo-taller" class="formulario__etiqueta">Taller:</label>
              <select id="campo-taller" name="taller" class="formulario__campo" required>
                <option value="" disabled selected>-- Seleccioná un taller de la agenda --</option>
                <option value="cata-a-ciegas">Cata a ciegas (7 de marzo - Centro)</option>
                <option value="latte-art">Latte art para principiantes (14 de marzo - Norte)</option>
                <option value="filtrado-en-casa">Métodos de filtrado en casa (21 de marzo - Centro)</option>
                <option value="del-grano-a-la-taza">Del grano a la taza: tueste y origen (28 de marzo - Sur)</option>
                <option value="cafe-y-reposteria">Café y repostería: maridaje (4 de abril - Norte)</option>
              </select>
            </div>
            <div class="formulario__grupo">
              <label for="campo-acompanantes" class="formulario__etiqueta">Número de acompañantes (máx. 3):</label>
              <input type="number" id="campo-acompanantes" name="acompanantes" class="formulario__campo" min="0" max="3" value="0" placeholder="0" required>
            </div>
          </div>

          <!-- Fila 3: Nivel (radio) -->
          <div class="formulario__grupo">
            <span class="formulario__etiqueta">Nivel:</span>
            <div class="formulario__grupo-radio">
              <label class="formulario__opcion" for="nivel-basico">
                <input type="radio" id="nivel-basico" name="nivel" value="basico" required>
                Básico
              </label>
              <label class="formulario__opcion" for="nivel-intermedio">
                <input type="radio" id="nivel-intermedio" name="nivel" value="intermedio">
                Intermedio
              </label>
            </div>
          </div>

          <!-- Fila 4: Recordatorios (checkbox) -->
          <div class="formulario__grupo">
            <label class="formulario__opcion" for="campo-recordatorios">
              <input type="checkbox" id="campo-recordatorios" name="recordatorios">
              Quiero recibir recordatorios
            </label>
          </div>

          <!-- Fila 5: Comentarios (textarea) -->
          <div class="formulario__grupo">
            <label for="campo-comentarios" class="formulario__etiqueta">Comentarios:</label>
            <textarea id="campo-comentarios" name="comentarios" class="formulario__campo" rows="4" placeholder="Escribí aquí si tenés alguna intolerancia, duda previa o requerimiento..."></textarea>
          </div>

          <!-- Botón de envío -->
          <div class="formulario__grupo">
            <button type="submit" class="boton boton--primario boton--completo">Inscribirme</button>
          </div>

        </fieldset>
      </form>
    </section>
```

- **`<form action="#" method="get">`:** Contenedor de envío. Al utilizar `method="get"` y `action="#"`, permite probar el envío en servidores locales estáticos sin generar errores `501 POST`.
- **`<fieldset>` y `<legend>`:** Agrupan semánticamente los campos relacionados. `<legend>` actúa como el título del grupo.
- **`<label for="id-del-campo">`:** Cada etiqueta tiene su atributo `for` que coincide con el `id` del `<input>`, `<select>` o `<textarea>`. Esto permite que al hacer clic sobre el texto de la etiqueta, el cursor se posicione automáticamente dentro del campo.
- **Atributo `name`:** Imprescindible para que los datos del formulario se envíen asociados a su clave (`nombre=Camila&taller=latte-art`).
- **`required`:** Validación nativa de HTML5. Impide enviar el formulario si el campo está vacío.
- **`min="0"` y `max="3"`:** Restringen el control de tipo `number` al rango exacto solicitado.

---

### H. Pie de Página (`<footer>`)

```html
  <footer class="pie">
    <div class="contenedor pie__interior">
      <div class="pie__columna">
        <h3>Café Altiplano</h3>
        <p>Cafetería de especialidad comprometida con el café de origen andino, la sostenibilidad y el buen servicio.</p>
        <p><small>Horario general: Lunes a Domingo de 7:00 a 21:00</small></p>
      </div>

      <div class="pie__columna">
        <h3>Navegación</h3>
        <ul class="pie__lista">
          <li><a href="index.html">Inicio</a></li>
          <li><a href="carta.html">Nuestra Carta</a></li>
          <li><a href="sedes.html">Nuestras Sedes</a></li>
          <li><a href="reservas.html">Reservar Mesa</a></li>
          <li><a href="talleres.html">Talleres y Eventos</a></li>
        </ul>
      </div>

      <div class="pie__columna">
        <h3>Comunidad y Cultura</h3>
        <p>Aprende más sobre el café colombiano y la cultura cafetera mundial:</p>
        <ul class="pie__lista">
          <li>
            <a href="https://scaa.org" target="_blank" rel="noopener noreferrer">Specialty Coffee Association (SCA)</a>
          </li>
          <li>
            <a href="https://federaciondecafeteros.org" target="_blank" rel="noopener noreferrer">Federación de Cafeteros</a>
          </li>
        </ul>
      </div>

      <div class="pie__creditos">
        <p>&copy; 2026 Café Altiplano. Proyecto académico de desarrollo web.</p>
      </div>
    </div>
  </footer>
```

- **`<footer>`:** Pie semántico del sitio.
- **`target="_blank" rel="noopener noreferrer"`:** Abre enlaces externos en una nueva pestaña protegiendo la seguridad y el rendimiento de la ventana de origen.

---

## 3. CSS Explicado (Propiedades, Selectores y Unidades)

### A. Metodología BEM (*Block Element Modifier*)

BEM es una convención de nombres para clases CSS que evita colisiones de estilos y hace el código legible y reutilizable:

- **Bloque (`.bloque`):** Componente independiente (ej. `.menu`, `.tarjeta`, `.formulario`, `.tabla`).
- **Elemento (`.bloque__elemento`):** Parte interna que solo tiene sentido dentro del bloque (ej. `.menu__item`, `.menu__enlace`, `.tarjeta__cuerpo`, `.formulario__campo`).
- **Modificador (`.bloque--modificador` o `.bloque__elemento--modificador`):** Variante de apariencia o estado (ej. `.menu__enlace--activo`, `.tarjeta--destacada`, `.boton--primario`, `.tabla__celda--precio`, `.tabla__celda--cupos`).

### B. Tabla Didáctica de Propiedades Clave

| Propiedad CSS | ¿Qué significa y para qué sirve? | ¿Dónde se usó en el proyecto? | ¿Qué efecto visual produce? | Ejemplo de cómo modificarlo |
|---|---|---|---|---|
| `box-sizing: border-box` | Hace que `padding` y `border` se incluyan dentro del ancho total. | En el reset universal `*, *::before, *::after` en `base.css`. | Evita que los elementos se desborden cuando les agregamos relleno o bordes. | Si pones `content-box`, el ancho crecerá sumando el padding. |
| `display: grid` | Convierte un contenedor en una cuadrícula bidimensional de filas y columnas. | En `.maqueta`, `.cabecera__interior`, `.galeria-talleres`, `.formulario__fila`. | Permite posicionar cajas hijas en columnas y filas exactas. | Si lo quitas, los bloques se apilan verticalmente como bloques normales. |
| `grid-template-columns` | Define el número y tamaño de las columnas de la cuadrícula. | En `.maqueta` (`repeat(2, 1fr)` a 600px, `repeat(3, 1fr)` a 900px). | Divide la pantalla en 1, 2 o 3 columnas iguales. | `grid-template-columns: 2fr 1fr;` haría una columna el doble de ancha. |
| `gap` | Espacio de separación entre filas y columnas de una grilla. | En `.maqueta { gap: 2rem; }` y `.formulario__fila { gap: 1.25rem; }`. | Separa limpiamente los bloques sin necesidad de márgenes individuales. | `gap: 3rem;` aumentaría el espacio entre bloques. |
| `grid-column: 1 / -1` | Hace que un elemento abarque desde la primera línea vertical de la grilla hasta la última. | En `.bloque--completo`, `.hero`, `.cabecera`, `.pie`. | El elemento ocupa el 100% del ancho de todas las columnas. | `grid-column: 1 / 2;` lo limitaría a la primera columna. |
| `grid-column: span 2` | Hace que un elemento ocupe dos columnas consecutivas de la grilla. | En `.bloque--doble` (agenda de talleres) a 600px y 900px. | La agenda se muestra ancha ocupando 2 columnas. | `grid-column: span 3;` ocuparía 3 columnas. |
| `repeat(auto-fit, minmax(...))` | Genera tantas columnas como quepan automáticamente respetando un tamaño mínimo. | En `.galeria-talleres { grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); }`. | Las 6 tarjetas se acomodan solas en 1, 2 o 3 columnas según el ancho de la ventana. | Cambiar `16rem` a `12rem` permitiría 4 columnas en monitores anchos. |
| `overflow-x: auto` | Muestra una barra de desplazamiento horizontal únicamente si el contenido interno desborda. | En `.tabla-contenedor`. | En celulares la tabla se puede deslizar horizontalmente sin romper la página. | `overflow-x: hidden;` recortaría la tabla impidiendo leer los precios. |
| `max-width: 65ch` | Limita el ancho de lectura a 65 caracteres promedio. | En `p { max-width: 65ch; }` en `tipografia.css`. | Mejora la legibilidad impidiendo que las líneas de texto sean excesivamente largas. | `max-width: 45ch;` haría los párrafos más angostos. |
| `min-height: 50vh` | Altura mínima del 50% de la altura visible del navegador (*viewport height*). | En `.hero` en `layout.css`. | Asegura que la portada ocupe al menos la mitad de la pantalla al entrar. | `min-height: 70vh;` haría la portada más imponente. |
| `:nth-child(even)` | Pseudoclase que selecciona los elementos pares. | En `.tabla tbody tr:nth-child(even)`. | Crea el efecto "cebra" con fondo alterno para leer tablas fácilmente. | `:nth-child(odd)` seleccionaría las filas impares. |

### C. Selectores Avanzados del Examen

1. **Selector de Atributo:**
   - En `componentes.css`:
     ```css
     input[type="number"],
     input[type="text"],
     input[type="email"] {
       width: 100%;
       padding: 0.625rem 0.75rem;
     }
     ```
   - Aplica estilos exclusivamente a los campos `<input>` cuyo atributo `type` coincida exactamente.
2. **Combinador (`>` o `+`):**
   - En `componentes.css`: `.menu__lista > .menu__item` (combinador hijo directo `>`).
   - En `tipografia.css`: `h2 + p` (combinador hermano adyacente `+`, aplica estilo al primer párrafo inmediatamente después de un `<h2>`).
3. **Selector Lógico (`:is()`, `:not()`):**
   - En `tipografia.css`: `:is(h1, h2, h3)` (agrupa encabezados en una sola regla).
   - En `tipografia.css`: `a:not(.boton)` (aplica estilo a todos los enlaces de texto que **no** sean botones).

---

## 4. CSS Grid desde Cero

CSS Grid es un sistema de maquetación bidimensional nativo de CSS3 que permite organizar elementos en **filas** y **columnas** al mismo tiempo.

```text
┌─────────────────────────────────────────────────────────────┐
│ .cabecera (grid-column: 1 / -1)                             │
├─────────────────────────────────────────────────────────────┤
│ .hero (grid-column: 1 / -1)                                 │
├──────────────────────────────┬──────────────────────────────┤
│ .bloque--doble (Agenda)      │ .barra-lateral (Info)        │
│ Columna 1 y Columna 2        │ Columna 3                    │
│ (grid-column: span 2)        │ (grid-column: span 1)        │
├──────────────────────────────┴──────────────────────────────┤
│ .galeria-talleres (repeat(auto-fit, minmax(16rem, 1fr)))    │
│ Tarjeta 1  │ Tarjeta 2  │ Tarjeta 3  │ Tarjeta 4...         │
├─────────────────────────────────────────────────────────────┤
│ .formulario (grid-column: 1 / -1)                           │
├─────────────────────────────────────────────────────────────┤
│ .pie (grid-column: 1 / -1)                                  │
└─────────────────────────────────────────────────────────────┘
```

### ¿Cómo funciona la estrategia Mobile First?

1. **Base (Móvil < 600 px):**
   ```css
   .maqueta {
     display: grid;
     grid-template-columns: 1fr; /* 1 sola columna vertical */
     gap: 2rem;
   }
   ```
   Todos los elementos (`.bloque--completo`, `.bloque--doble`, `.barra-lateral`) se apilan uno debajo del otro de forma natural.
2. **Breakpoint Tableta (`@media (min-width: 600px)`):**
   ```css
   @media (min-width: 600px) {
     .maqueta {
       grid-template-columns: repeat(2, 1fr); /* 2 columnas iguales */
       gap: 2rem;
     }
     .bloque--doble {
       grid-column: span 2; /* Ocupa las 2 columnas */
     }
     .barra-lateral {
       grid-column: span 2; /* Ocupa las 2 columnas */
     }
   }
   ```
3. **Breakpoint Escritorio (`@media (min-width: 900px)`):**
   ```css
   @media (min-width: 900px) {
     .maqueta {
       grid-template-columns: repeat(3, 1fr); /* 3 columnas iguales */
       gap: 2.25rem;
     }
     .bloque--doble {
       grid-column: span 2; /* Agenda en 2 columnas */
     }
     .barra-lateral {
       grid-column: span 1; /* Barra lateral en 1 columna */
       align-self: start;   /* No se estira hacia abajo */
     }
   }
   ```

---

## 5. Tabla HTML: Construcción y Accesibilidad

Una tabla accesible no es solo un conjunto de filas y celdas; requiere una estructura que permita a los lectores de pantalla transmitir el significado de los datos:

```html
<table class="tabla">
  <!-- 1. Título accesible de la tabla -->
  <caption class="tabla__caption">Cronograma de talleres y experiencias cafeteras</caption>

  <!-- 2. Encabezado con nombres de columnas -->
  <thead>
    <tr>
      <th scope="col">Fecha</th>
      <th scope="col">Taller</th>
      <th scope="col">Sede</th>
      <th scope="col">Duración</th>
      <th scope="col" class="tabla__celda--cupos">Cupos</th>
      <th scope="col" class="tabla__celda--precio">Precio</th>
    </tr>
  </thead>

  <!-- 3. Cuerpo de datos -->
  <tbody>
    <tr>
      <th scope="row">7 de marzo</th>
      <td>Cata a ciegas</td>
      <td>Centro</td>
      <td>2 h</td>
      <td class="tabla__celda--cupos">12</td>
      <td class="tabla__celda--precio">$ 30.000</td>
    </tr>
  </tbody>
</table>
```

---

## 6. Formularios HTML: Explicación de Cada Control

Los formularios permiten recolectar información del usuario. Cada elemento cumple una función técnica precisa:

1. **`<fieldset>` y `<legend>`:** Agrupa controles relacionados y le da un título visible.
2. **`<label for="id">`:** Etiqueta de texto asociada al control cuyo `id` coincida. Si haces clic en la palabra "Nombre completo", el foco salta automáticamente al campo.
3. **`<input type="text">`:** Campo de texto libre para nombres, apellidos, etc.
4. **`<input type="email">`:** Campo especializado que valida que el texto contenga un formato de correo válido (`usuario@dominio.com`). En celulares despliega el teclado con `@` y `.com`.
5. **`<select>` y `<option>`:** Menú desplegable. La primera opción suele ser un indicador inactivo:
   ```html
   <option value="" disabled selected>-- Seleccioná un taller --</option>
   ```
6. **`<input type="radio">`:** Botón de opción mutuamente excluyente. Todos los radio buttons de un mismo grupo **deben compartir el mismo atributo `name`** (`name="nivel"`). Así, al marcar "Básico", "Intermedio" se desmarca automáticamente.
7. **`<input type="number">`:** Campo numérico. Los atributos `min="0"` y `max="3"` impiden ingresar valores negativos o mayores a 3.
8. **`<input type="checkbox">`:** Casilla de verificación booleana (sí/no).
9. **`<textarea>`:** Área de texto multilínea para comentarios largos.
10. **`required`:** Atributo booleano que impide el envío si el campo está vacío.
11. **`placeholder`:** Texto de ayuda en gris tenue que desaparece al empezar a escribir.

---

## 7. Diez Ejercicios Prácticos de Modificación

1. **Ejercicio 1:** Cambia el color de fondo de las tarjetas destacadas (`.tarjeta--destacada`).
2. **Ejercicio 2:** Cambia la cantidad mínima de acompañantes a 1 y la máxima a 5 en el formulario de `talleres.html`.
3. **Ejercicio 3:** Agrega un sexto taller a la tabla de agenda: "Barista en casa" en sede Norte por $ 30.000 con 10 cupos el 11 de abril.
4. **Ejercicio 4:** Modifica el breakpoint de escritorio de 900 px a 1000 px en `css/layout.css`.
5. **Ejercicio 5:** Agrega una séptima tarjeta a la galería de talleres: "Arte latte avanzado" (Nivel: Intermedio).
6. **Ejercicio 6:** Cambia el tamaño del título principal de la portada (`.hero__titulo`) de 2.5rem a 2.75rem.
7. **Ejercicio 7:** Modifica el color de fondo del enlace activo del menú (`.menu__enlace--activo`) a través de sus variables en `base.css`.
8. **Ejercicio 8:** Agrega una nueva opción al `<select>` del formulario de talleres.
9. **Ejercicio 9:** Haz que las tarjetas de la galería tengan un ancho mínimo de `18rem` en lugar de `16rem`.
10. **Ejercicio 10:** Añade un tercer nivel ("Avanzado: para baristas con experiencia previa") a la lista `<dl>` de niveles.

---

### Soluciones a los Diez Ejercicios

<details>
<summary><strong>Haz clic aquí para ver las soluciones paso a paso</strong></summary>

- **Solución 1:** En `css/base.css`, modifica la variable `--color-tarjeta-destacada-fondo: #f3ede2;` por otro tono como `#fdfbf7;`.
- **Solución 2:** En `talleres.html`, busca `<input type="number" id="campo-acompanantes"...>` y cambia `min="1"` y `max="5"`.
- **Solución 3:** En `talleres.html`, dentro de `<tbody>`, agrega:
  ```html
  <tr>
    <th scope="row">11 de abril</th>
    <td>Barista en casa</td>
    <td>Norte</td>
    <td>3 h</td>
    <td class="tabla__celda--cupos">10</td>
    <td class="tabla__celda--precio">$ 30.000</td>
  </tr>
  ```
- **Solución 4:** En `css/layout.css`, cambia `@media (min-width: 900px)` por `@media (min-width: 1000px)`.
- **Solución 5:** En `talleres.html`, dentro de `.galeria-talleres`, agrega un nuevo `<article class="tarjeta">`:
  ```html
  <article class="tarjeta">
    <div class="tarjeta__cuerpo">
      <h3>Arte latte avanzado</h3>
      <p>Dominio del cisne y rosetas complejas en taza de 8 oz.</p>
      <p><strong>Nivel:</strong> Intermedio</p>
    </div>
  </article>
  ```
- **Solución 6:** En `css/layout.css`, busca `.hero__titulo` y cambia `font-size: 2.5rem;` a `font-size: 2.75rem;`.
- **Solución 7:** En `css/base.css`, localiza `--color-menu-hover-fondo` y actualiza su valor hexadecimal.
- **Solución 8:** En `talleres.html`, dentro de `<select id="campo-taller">`, agrega `<option value="barista-en-casa">Barista en casa (11 de abril - Norte)</option>`.
- **Solución 9:** En `css/layout.css`, busca `.galeria-talleres` y cambia `minmax(16rem, 1fr)` por `minmax(18rem, 1fr)`.
- **Solución 10:** En `talleres.html`, dentro de `<dl class="glosario-lista">`, agrega:
  ```html
  <dt class="glosario-termino">Avanzado</dt>
  <dd class="glosario-definicion">Para baristas profesionales o personas con experiencia previa en extracción comercial.</dd>
  ```

</details>

---

## 8. Cómo Construirlo desde Cero (Paso a Paso Lógico)

1. **Paso 1: Crear el archivo y declarar la estructura base:**
   Escribe el esqueleto HTML5 (`<!DOCTYPE html>`, `html lang="es"`, `head`, `meta charset`, `meta viewport`, `title` y los 5 `<link>` a CSS).
2. **Paso 2: Cabecera y Menú:**
   Copia la estructura del `<header>` con su logotipo y los 5 enlaces `<a>`, asegurándote de colocar la clase `.menu__enlace--activo` en la página actual.
3. **Paso 3: Portada Hero:**
   Crea la sección `<section class="hero bloque--completo">` con el único `<h1>` de la página y el texto de introducción.
4. **Paso 4: Construir la Tabla de Datos:**
   Crea la `<section class="bloque--doble">`, envuélvela en `.tabla-contenedor` y escribe la tabla con `caption`, `thead`, `tbody`, `th scope="col/row"` y las clases para alinear números y cupos a la derecha.
5. **Paso 5: Barra Lateral con Figura y Listas:**
   Crea el `<aside class="barra-lateral">`, inserta el `<figure class="figura-taller">` con su imagen descriptiva y redacta las tres listas semánticas requeridas (`ol` para pasos, `ul` para inclusiones y `dl` para niveles).
6. **Paso 6: Galería de Tarjetas:**
   Escribe la sección con la clase `.galeria-talleres` y dentro coloca los 6 `<article class="tarjeta">`.
7. **Paso 7: Formulario de Inscripción:**
   Escribe el `<form>`, el `<fieldset>`, el `<legend>` y cada uno de los controles solicitados asegurándote de asociar cada `label for` con el `id` correspondiente.
8. **Paso 8: Pie de Página:**
   Escribe el `<footer>` con las 4 columnas informativas y enlaces completos.
9. **Paso 9: Ajustar CSS:**
   Asegúrate de que en `layout.css` el menú distribuya 5 columnas en `@media (min-width: 600px)` y que no existan propiedades prohibidas (flexbox, animaciones, !important).
10. **Paso 10: Pruebas Responsivas:**
    Abre las herramientas de desarrollador (`F12`), prueba en 500 px, 800 px y 1200 px, y valida que no exista desbordamiento horizontal.

---

## 9. Preguntas Típicas de Sustentación con Respuestas Sencillas

#### 1. ¿Por qué utilizaste CSS Grid en lugar de Flexbox?
> **Respuesta:** "Porque la restricción RNF-02 de la rúbrica prohibía estrictamente el uso de Flexbox en este examen para evaluar nuestro dominio sobre CSS Grid. Con Grid demostré que puedo construir tanto la estructura macro de 3 columnas de la página como componentes micro, tales como el menú y las filas del formulario, usando `display: grid`."

#### 2. ¿Cómo funciona la galería con `auto-fit` y por qué no necesitó media queries?
> **Respuesta:** "Utilicé `grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr))`. La función `minmax(16rem, 1fr)` le dice al navegador que cada tarjeta debe medir al menos 16 rem (256 px) pero puede expandirse. Y la palabra clave `auto-fit` calcula automáticamente cuántas columnas de ese tamaño caben en la pantalla: si cabe solo una, forma 1 columna; si caben dos, crea 2; y si caben tres, crea 3, adaptándose fluidamente sin requerir `@media`."

#### 3. ¿Para qué sirve el contenedor `.tabla-contenedor` con `overflow-x: auto`?
> **Respuesta:** "Las tablas con muchas columnas suelen desbordar las pantallas móviles angostas (como en 500 px). Al envolver la tabla en un contenedor con `overflow-x: auto; width: 100%;`, la tabla genera su propia barra de desplazamiento horizontal táctil interna, evitando que el cuerpo de la página web sufra scroll horizontal indeseado."

#### 4. ¿Cuál es la diferencia semántica entre `<ul>`, `<ol>` y `<dl>` y dónde las usaste?
> **Respuesta:** 
> - "`<ol>` es una lista ordenada donde el orden importa: la usé en *Cómo inscribirse* porque los pasos son cronológicos."
> - "`<ul>` es una lista no ordenada donde el orden no altera el significado: la usé en *Qué incluye cada taller*."
> - "`<dl>` es una lista de definiciones con pares de término (`<dt>`) y descripción (`<dd>`): la usé para explicar los *Niveles* Básico e Intermedio."

#### 5. ¿Por qué es obligatorio usar el atributo `scope` en las celdas `<th>`?
> **Respuesta:** "Por accesibilidad. El atributo `scope` le informa a los lectores de pantalla si esa celda de encabezado pertenece a toda la columna vertical (`scope="col"`) o a toda la fila horizontal (`scope="row"`), permitiendo a personas invidentes entender qué significa cada dato."

#### 6. ¿Cómo se relacionan un `<label>` y un `<input>` y por qué es importante?
> **Respuesta:** "Se vinculan mediante el atributo `for` del label y el atributo `id` del input, los cuales deben tener exactamente el mismo valor (ej. `for="campo-correo"` e `id="campo-correo"`). Es importante porque aumenta el área táctil de clic para el usuario y porque permite a los lectores de pantalla anunciar el nombre del campo al entrar en él."

#### 7. ¿Por qué los radio buttons de un mismo grupo deben tener el mismo `name`?
> **Respuesta:** "Porque en HTML el navegador agrupa los botones de radio según su atributo `name`. Al compartir `name="nivel"`, el navegador entiende que son opciones mutuamente excluyentes y desmarca una al seleccionar la otra."

#### 8. ¿Qué significa la estrategia *Mobile First* y cómo se refleja en tu CSS?
> **Respuesta:** "Significa escribir primero el código CSS para pantallas de teléfonos móviles fuera de cualquier media query (una sola columna apilada). Luego, se agregan progresivamente reglas para pantallas más grandes utilizando `@media (min-width: 600px)` y `@media (min-width: 900px)`. En mi código, las media queries están ordenadas estrictamente de menor a mayor."

#### 9. ¿Por qué todas las fuentes y espaciados están en `rem` y no en `px`?
> **Respuesta:** "Porque `rem` es una unidad relativa al tamaño de fuente raíz del navegador (`html { font-size: 100%; }`). Si un usuario con problemas visuales aumenta el tamaño de letra predeterminado en su sistema o navegador, toda nuestra interfaz escala proporcionalmente, garantizando la accesibilidad. Los `px` los reservamos únicamente para bordes finos de 1 a 4 píxeles."

#### 10. ¿Para qué sirve la unidad `ch` y dónde la utilizaste?
> **Respuesta:** "La unidad `1ch` equivale al ancho del carácter '0' de la tipografía actual. La utilicé en `p { max-width: 65ch; }` para limitar el ancho de las líneas de texto a un promedio de 65 caracteres, lo cual constituye el estándar tipográfico ergonómico recomendado para evitar el cansancio visual."

#### 11. ¿Qué es la metodología BEM y qué ventaja ofrece?
> **Respuesta:** "Significa Bloque-Elemento-Modificador. Por ejemplo en `.menu__enlace--activo`, `.menu` es el bloque, `__enlace` es el elemento interno y `--activo` es el modificador de estado. Su ventaja es que otorga una especificidad baja y uniforme en CSS, evitando colisiones de nombres y eliminando la necesidad de usar `!important` o selectores de ID."

#### 12. ¿Por qué está prohibido usar selectores de ID (`#id`) en las hojas de estilo?
> **Respuesta:** "Porque los selectores de ID tienen una especificidad extremadamente alta que rompe la cascada natural de CSS y dificulta sobrescribir estilos limpiamente. Los IDs deben usarse exclusivamente para anclas de navegación interna (`href="#agenda"`) y para asociar etiquetas de formulario (`label for`). En CSS siempre damos estilo mediante clases."

#### 13. ¿Qué hace `grid-column: 1 / -1`?
> **Respuesta:** "Le indica al navegador que el elemento debe comenzar en la primera línea de la grilla (línea 1) y expandirse hasta la última línea disponible (línea -1). Lo utilicé en la cabecera, la portada hero, la galería, el formulario y el pie para asegurar que abarquen el ancho completo sin importar cuántas columnas tenga la cuadrícula."

#### 14. ¿Qué función cumple `align-self: start` en la barra lateral?
> **Respuesta:** "En CSS Grid, el comportamiento predeterminado de los elementos es `stretch` (estirarse verticalmente para igualar la altura del bloque vecino más alto). Como la agenda tiene muchas filas, la barra lateral se estiraba dejando un espacio en blanco feo abajo. Con `align-self: start;` en el breakpoint de 900 px, la barra lateral mide solo lo que ocupa su contenido y no se estira forzadamente."

#### 15. ¿Cómo garantizaste que no hubiera colores sueltos fuera de `:root`?
> **Respuesta:** "Definiendo toda la paleta de colores corporativos como variables CSS dentro del selector `:root` en `base.css` (ej. `--color-tarjeta-fondo`, `--color-menu-texto`). En las reglas CSS únicamente invocamos `var(--nombre-variable)`. Esto facilita el mantenimiento: si el cliente quiere cambiar el color del menú, solo se modifica una línea en `:root`."

---

## 10. Resumen Rápido para Estudiar (Hoja de Repaso)

### Conceptos Innegociables del Examen
- **1 solo `<h1>` por página.**
- **Cero JavaScript, cero Flexbox, cero animaciones, cero `!important`, cero estilos inline.**
- **Mobile First:** Reglas base sin media query $\rightarrow$ `@media (min-width: 600px)` $\rightarrow$ `@media (min-width: 900px)`.
- **Accesibilidad en tablas:** `caption` + `thead` + `tbody` + `th scope="col/row"`.
- **Accesibilidad en formularios:** `fieldset` + `legend` + `label for="id"` idéntico al `id` del control.

### Fórmulas CSS Clave
- **Centrar la web:** `.contenedor { max-width: 75rem; margin: 0 auto; padding: 0 1rem; width: 100%; }`
- **Reset de caja:** `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`
- **Galería automática:** `grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));`
- **Abarcar todo el ancho:** `grid-column: 1 / -1;`
- **Abarcar dos columnas:** `grid-column: span 2;`
- **Scroll seguro en tablas:** `.tabla-contenedor { width: 100%; overflow-x: auto; }`
- **Límite ergonómico de texto:** `p { max-width: 65ch; }`
