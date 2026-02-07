---
name: Image Banko Master
description: Enseña a Antigravity a utilizar el MCP image-banko para buscar y utilizar imágenes reales de alta calidad, aplicar efectos de diseño premium como parallax y evitar el uso de placeholders.
---

# Image Banko Master Skill

Esta skill capacita a Antigravity para ser un experto en la búsqueda e integración de recursos visuales utilizando el MCP `image-banko`. Las imágenes son el corazón de un diseño premium; esta skill asegura que nunca se utilicen placeholders y que cada diseño se sienta vivo y profesional.

## 🛠 Herramientas del MCP
El servidor `image-banko` proporciona las siguientes herramientas:
- `search_free_images(query, limit)`: Busca en Wikimedia Commons (CC0, sin API Key). Ideal para contenido libre.
- `search_pexels(query, limit)`: Imágenes de alta calidad de Pexels.
- `search_unsplash(query, limit)`: Imágenes artísticas de Unsplash.
- `search_sourcesplash(query, limit)`: Imágenes aleatorias rápidas desde SourceSplash.

## 🎨 Principios de Diseño con Imágenes
1. **No Placeholders**: NUNCA utilices `placehold.it` o rectángulos grises. Si necesitas una imagen, búscala inmediatamente con el MCP.
2. **Calidad Premium**: Prioriza Pexels y Unsplash para fotografía de stock moderna. Usa Wikimedia para temas específicos o históricos.
3. **Formatos**: Cuando necesites superponer elementos (como en parallax), busca específicamente términos como "isolated", "transparent background" o "PNG" en la query, aunque el MCP devuelva JPG, puedes filtrar por visuales que parezcan fáciles de recortar o usar.
4. **Coherencia**: Mantén una paleta de colores coherente entre todas las imágenes de un sitio.

## 🚀 Efectos Avanzados: Parallax
Para crear un efecto parallax impresionante que deje al usuario "wowed":

### 1. Parallax de Fondo Simple (CSS)
Utiliza `background-attachment: fixed` para un efecto de ventana:
```css
.hero-section {
    background-image: url('URL_DE_PEXELS');
    background-attachment: fixed;
    background-size: cover;
    background-position: center;
    height: 100vh;
}
```

### 2. Multi-capas (Layered Parallax)
Busca varias imágenes (ej: un bosque al fondo y un árbol aislado al frente).
```html
<div class="parallax-container">
    <img src="background.jpg" class="layer bg" data-speed="0.2">
    <img src="middle.png" class="layer mid" data-speed="0.5">
    <img src="foreground.png" class="layer fg" data-speed="0.8">
</div>
```
*Tip: Usa JavaScript para mover las capas a diferentes velocidades basadas en el scroll.*

## 💡 Tips de Búsqueda
- **Queries en Inglés**: Los motores de Pexels y Unsplash funcionan mejor con términos en inglés (ej: "dark aesthetic mountain" en lugar de "montaña oscura").
- **Especificidad**: En lugar de "comida", usa "minimalist organic salad top view".
- **Atribución**: Siempre que sea posible, incluye un comentario o un pequeño crédito al autor si la licencia lo requiere.

## 🔄 Flujo de Trabajo
Cada vez que crees un componente (Hero, Card, Gallery):
1. Identifica el tema.
2. Llama a `search_pexels` o `search_unsplash`.
3. Selecciona la mejor URL.
4. Implementa el CSS/HTML directamente con esa URL.
5. Si el diseño es complejo, aplica técnicas de parallax o filtros CSS (`backdrop-filter: blur()`, `gradient overlays`) para elevar la estética.
