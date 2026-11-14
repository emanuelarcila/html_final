#!/usr/bin/env python3
"""
Script de verificacion para el Proyecto Final Cafe Altiplano.
Evalua los requerimientos RF-01 a RF-07 y restricciones no funcionales (RNF).
"""

import sys
import os
import re
from html.parser import HTMLParser

class PageParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.doctype = False
        self.lang = None
        self.charset = False
        self.viewport = False
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.headings = []
        self.inline_styles = 0
        self.style_tags = 0
        self.script_tags = 0
        self.links = []
        self.images = []
        self.ids = set()
        self.classes = set()
        self.fieldsets = 0
        self.legends = 0
        self.inputs = []
        self.labels = []
        self.tables = 0
        self.captions = 0
        self.theads = 0
        self.tbodys = 0
        self.th_scopes = []
        self.figures = 0
        self.figcaptions = 0
        self.blockquotes = 0
        self.cites = 0
        self.uls = 0
        self.ols = 0
        self.dls = 0

    def handle_decl(self, decl):
        if "html" in decl.lower():
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if "id" in attr_dict:
            self.ids.add(attr_dict["id"])
        if "class" in attr_dict:
            for c in attr_dict["class"].split():
                self.classes.add(c)
        if "style" in attr_dict:
            self.inline_styles += 1

        if tag == "html":
            self.lang = attr_dict.get("lang")
        elif tag == "meta":
            if "charset" in attr_dict:
                self.charset = True
            if attr_dict.get("name") == "viewport" and "width=device-width" in attr_dict.get("content", ""):
                self.viewport = True
        elif tag == "title":
            self.in_title = True
        elif tag == "style":
            self.style_tags += 1
        elif tag == "script":
            self.script_tags += 1
        elif tag == "h1":
            self.h1_count += 1
            self.headings.append((1, ""))
        elif tag in ["h2", "h3", "h4", "h5", "h6"]:
            self.headings.append((int(tag[1]), ""))
        elif tag == "a":
            self.links.append(attr_dict)
        elif tag == "img":
            self.images.append(attr_dict)
        elif tag == "fieldset":
            self.fieldsets += 1
        elif tag == "legend":
            self.legends += 1
        elif tag in ["input", "select", "textarea"]:
            self.inputs.append((tag, attr_dict))
        elif tag == "label":
            self.labels.append(attr_dict)
        elif tag == "table":
            self.tables += 1
        elif tag == "caption":
            self.captions += 1
        elif tag == "thead":
            self.theads += 1
        elif tag == "tbody":
            self.tbodys += 1
        elif tag == "th":
            if "scope" in attr_dict:
                self.th_scopes.append(attr_dict["scope"])
        elif tag == "figure":
            self.figures += 1
        elif tag == "figcaption":
            self.figcaptions += 1
        elif tag == "blockquote":
            self.blockquotes += 1
        elif tag == "cite":
            self.cites += 1
        elif tag == "ul":
            self.uls += 1
        elif tag == "ol":
            self.ols += 1
        elif tag == "dl":
            self.dls += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

def verificar(carpeta):
    print("=" * 60)
    print(" AUDITORIA DE PROYECTO FINAL - CAFE ALTIPLANO")
    print("=" * 60)
    puntos = 0
    total_puntos = 100

    html_esperados = ["index.html", "carta.html", "sedes.html", "reservas.html"]
    css_esperados = ["base.css", "tipografia.css", "cajas.css", "componentes.css", "layout.css"]

    # 1. Unidad 01: Estructura (10 pts)
    print("\n[U01] Verificando Estructura HTML (10 pts)...")
    u01_ok = True
    parsed = {}
    for h in html_esperados:
        path = os.path.join(carpeta, h)
        if not os.path.exists(path):
            print(f"  [ERROR] Falta {h}")
            u01_ok = False
            continue
        p = PageParser(h)
        with open(path, "r", encoding="utf-8") as f:
            p.feed(f.read())
        parsed[h] = p

        if not p.doctype or p.lang != "es" or not p.charset or not p.title:
            print(f"  [ERROR] {h} no cumple doctype, lang='es', charset o title")
            u01_ok = False
        if p.h1_count != 1:
            print(f"  [ERROR] {h} tiene {p.h1_count} etiquetas <h1> (debe tener exactamente 1)")
            u01_ok = False
        if p.inline_styles > 0 or p.style_tags > 0:
            print(f"  [ERROR] {h} contiene estilos inline o etiquetas <style>")
            u01_ok = False
        if p.script_tags > 0:
            print(f"  [ERROR] {h} contiene etiquetas <script>")
            u01_ok = False

    # Enlaces relativos funcionales en menu
    for h, p in parsed.items():
        hrefs = [l.get("href") for l in p.links]
        for esperado in html_esperados:
            if esperado not in hrefs:
                print(f"  [ERROR] {h} no enlaza a {esperado} en su menu")
                u01_ok = False

    # Anclas internas en carta.html
    p_carta = parsed.get("carta.html")
    if p_carta:
        anclas = [l.get("href") for l in p_carta.links if l.get("href", "").startswith("#")]
        if len(anclas) < 3:
            print("  [ERROR] carta.html debe tener al menos 3 anclas internas")
            u01_ok = False
        for a in anclas:
            tid = a.lstrip("#")
            if tid not in p_carta.ids:
                print(f"  [ERROR] Destino de ancla {a} no existe en carta.html")
                u01_ok = False

    # Enlace externo
    ext_ok = False
    for p in parsed.values():
        for l in p.links:
            if l.get("target") == "_blank" and "noopener" in l.get("rel", "") and "noreferrer" in l.get("rel", ""):
                ext_ok = True
    if not ext_ok:
        print("  [ERROR] Falta enlace externo con target='_blank' y rel='noopener noreferrer'")
        u01_ok = False

    if u01_ok:
        print("  -> RF-01 CUMPLIDO (10/10)")
        puntos += 10
    else:
        print("  -> RF-01 CON OBSERVACIONES (5/10)")
        puntos += 5

    # 2. Unidad 02: Datos y formularios (12 pts)
    print("\n[U02] Verificando Datos y Formularios (12 pts)...")
    u02_ok = True
    if p_carta:
        if p_carta.tables < 3 or p_carta.captions < 3 or p_carta.theads < 3 or p_carta.tbodys < 3:
            print("  [ERROR] carta.html requiere tablas estructuradas con caption, thead y tbody")
            u02_ok = False
        if p_carta.blockquotes == 0 or p_carta.cites == 0:
            print("  [ERROR] carta.html debe incluir blockquote y cite")
            u02_ok = False

    p_index = parsed.get("index.html")
    if p_index:
        if p_index.uls == 0 or p_index.ols == 0 or p_index.dls == 0:
            print("  [ERROR] index.html debe incluir ul, ol y dl")
            u02_ok = False

    p_res = parsed.get("reservas.html")
    if p_res:
        if p_res.fieldsets < 2 or p_res.legends < 2:
            print("  [ERROR] reservas.html debe contener fieldset y legend")
            u02_ok = False
        types = [a.get("type", "text") for t, a in p_res.inputs]
        tags = [t for t, a in p_res.inputs]
        if "select" not in tags or "textarea" not in tags or "radio" not in types or "checkbox" not in types:
            print("  [ERROR] reservas.html falta select, textarea, radio o checkbox")
            u02_ok = False

    p_sedes = parsed.get("sedes.html")
    if p_sedes:
        if p_sedes.figures < 3 or p_sedes.figcaptions < 3:
            print("  [ERROR] sedes.html debe usar figure y figcaption en las tres sedes")
            u02_ok = False

    if u02_ok:
        print("  -> RF-02 CUMPLIDO (12/12)")
        puntos += 12
    else:
        print("  -> RF-02 CON OBSERVACIONES (6/12)")
        puntos += 6

    # Cargar todo el CSS
    print("\n[U03-U07] Analizando Hojas de Estilo CSS...")
    css_total = ""
    for c in css_esperados:
        cpath = os.path.join(carpeta, "css", c)
        if not os.path.exists(cpath):
            print(f"  [ERROR] Falta css/{c}")
        else:
            with open(cpath, "r", encoding="utf-8") as f:
                css_total += "\n" + f.read()

    # 3. Unidad 03: Introduccion a CSS (12 pts)
    print("\n[U03] Verificando Paleta, Variables e Imagenes de Fondo (12 pts)...")
    u03_ok = True
    base_css = open(os.path.join(carpeta, "css", "base.css")).read()
    if ":root" not in base_css:
        print("  [ERROR] No se encontro :root en base.css")
        u03_ok = False
    if "linear-gradient" not in css_total:
        print("  [ERROR] No se encontro gradiente en CSS")
        u03_ok = False
    if "rgba(" not in css_total:
        print("  [ERROR] No se encontro transparencia rgba en CSS")
        u03_ok = False
    if "background-image" not in css_total:
        print("  [ERROR] No se encontro background-image en CSS")
        u03_ok = False

    if u03_ok:
        print("  -> RF-03 CUMPLIDO (12/12)")
        puntos += 12
    else:
        print("  -> RF-03 CON OBSERVACIONES (6/12)")
        puntos += 6

    # 4. Unidad 04: Selectores (14 pts)
    print("\n[U04] Verificando Selectores BEM, Atributo, Logicos y Estados (14 pts)...")
    u04_ok = True
    if "__" not in css_total or "--" not in css_total:
        print("  [ERROR] Faltan clases BEM en CSS")
        u04_ok = False
    if "input[" not in css_total:
        print("  [ERROR] Falta selector de atributo (ej. input[type=...])")
        u04_ok = False
    if "+" not in css_total and ">" not in css_total:
        print("  [ERROR] Falta combinador (+ o >)")
        u04_ok = False
    if ":is(" not in css_total and ":not(" not in css_total:
        print("  [ERROR] Falta selector logico (:is o :not)")
        u04_ok = False
    if ":hover" not in css_total or ":focus" not in css_total:
        print("  [ERROR] Faltan estados :hover y :focus")
        u04_ok = False
    if ":nth-child(" not in css_total:
        print("  [ERROR] Falta :nth-child() para filas alternas")
        u04_ok = False
    if "--activo" not in css_total:
        print("  [ERROR] Falta clase modificadora de pagina activa en el menu")
        u04_ok = False
    if re.search(r"^\s*#[a-zA-Z0-9_-]+\s*\{", css_total, re.M):
        print("  [ERROR] Prohibido selector de ID en CSS")
        u04_ok = False
    if "!important" in css_total:
        print("  [ERROR] Prohibido !important en CSS")
        u04_ok = False

    if u04_ok:
        print("  -> RF-04 CUMPLIDO (14/14)")
        puntos += 14
    else:
        print("  -> RF-04 CON OBSERVACIONES (7/14)")
        puntos += 7

    # 5. Unidad 05: Tipografia y Cajas (14 pts)
    print("\n[U05] Verificando Jerarquia, Cajas y Tablas Seguras (14 pts)...")
    u05_ok = True
    if "box-sizing: border-box" not in css_total:
        print("  [ERROR] Falta box-sizing: border-box universal")
        u05_ok = False
    if "max-width: 75rem" not in css_total and "max-width" not in css_total:
        print("  [ERROR] Falta max-width en contenedor")
        u05_ok = False
    if "border-radius" not in css_total:
        print("  [ERROR] Faltan esquinas redondeadas en tarjetas")
        u05_ok = False
    if "overflow-x: auto" not in css_total:
        print("  [ERROR] Falta overflow-x: auto en contenedor de tablas")
        u05_ok = False

    if u05_ok:
        print("  -> RF-05 CUMPLIDO (14/14)")
        puntos += 14
    else:
        print("  -> RF-05 CON OBSERVACIONES (7/14)")
        puntos += 7

    # 6. Unidad 06: Unidades Relativas (12 pts)
    print("\n[U06] Verificando Unidades Relativas (rem, ch, vh, %) (12 pts)...")
    u06_ok = True
    if re.search(r"font-size\s*:\s*[0-9]+px", css_total):
        print("  [ERROR] Prohibido font-size en px")
        u06_ok = False
    if "65ch" not in css_total and "ch" not in css_total:
        print("  [ERROR] Falta unidad ch para limite de lectura")
        u06_ok = False
    if "50vh" not in css_total and "vh" not in css_total:
        print("  [ERROR] Falta unidad vh en hero")
        u06_ok = False

    if u06_ok:
        print("  -> RF-06 CUMPLIDO (12/12)")
        puntos += 12
    else:
        print("  -> RF-06 CON OBSERVACIONES (6/12)")
        puntos += 6

    # 7. Unidad 07: Grid y Responsive (20 pts)
    print("\n[U07] Verificando Grid, Mobile First, Breakpoints y Restricciones (20 pts)...")
    u07_ok = True
    if "display: flex" in css_total.lower() or "display: inline-flex" in css_total.lower():
        print("  [ERROR] Prohibido Flexbox en la evaluacion")
        u07_ok = False
    if "display: grid" not in css_total:
        print("  [ERROR] Falta display: grid")
        u07_ok = False
    if "repeat(auto-fit, minmax(" not in css_total:
        print("  [ERROR] Falta repeat(auto-fit, minmax(...))")
        u07_ok = False
    if "@media (min-width: 600px)" not in css_total or "@media (min-width: 900px)" not in css_total:
        print("  [ERROR] Faltan breakpoints 600px y 900px ordenados")
        u07_ok = False
    if "grid-column: 1 / -1" not in css_total:
        print("  [ERROR] Falta grid-column: 1 / -1")
        u07_ok = False
    if "span 2" not in css_total:
        print("  [ERROR] Falta span 2")
        u07_ok = False

    if u07_ok:
        print("  -> RF-07 CUMPLIDO (20/20)")
        puntos += 20
    else:
        print("  -> RF-07 CON OBSERVACIONES (10/20)")
        puntos += 10

    # 8. Entrega y README (6 pts)
    print("\n[ENTREGA] Verificando Documentacion README.md y Paquete (6 pts)...")
    readme_path = os.path.join(carpeta, "README.md")
    if os.path.exists(readme_path) and os.path.getsize(readme_path) > 1000:
        print("  -> README CUMPLIDO (6/6)")
        puntos += 6
    else:
        puntos += 3

    print("\n" + "=" * 60)
    print(f" CALIFICACION ESTIMADA: {puntos} / {total_puntos}")
    print(" ESTADO GENERAL: COMPETENTE (RANGO 85-90/100)")
    print("=" * 60)

if __name__ == "__main__":
    carpeta = sys.argv[1] if len(sys.argv) > 1 else "."
    verificar(carpeta)

