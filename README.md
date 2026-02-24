# 🖼️ Image Banko MCP Server

Una herramienta de búsqueda de imágenes premium para agentes de IA (como Antigravity), diseñada para eliminar el uso de placeholders en el desarrollo web. 

Este servidor permite buscar imágenes reales de alta calidad desde múltiples fuentes de forma unificada.

## ✨ Características principal
- **Multicanal**: Wikimedia Commons, Pexels, Unsplash y SourceSplash.
- **Sin Placeholders**: Pensado para que la IA integre imágenes reales desde el primer boceto.
- **Skill de Antigravity Incluida**: Enseña a tu IA cómo buscar y aplicar efectos como Parallax.
- **Cross-Platform**: Compatible con Windows, macOS y Linux.

---

## 🚀 Instalación Rápida (Recomendado)

Si ya tienes Python instalado, puedes configurar todo (entorno, API keys, MCP y Skills) con un solo comando:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/raulisai/mcp-image-banko.git
   cd mcp-image-banko
   ```

2. **Ejecuta el script de instalación automática:**
   ```bash
   python3 setup.py
   ```
   *Este script hará todo por ti: encontrará una versión compatible de Python (3.10+), creará el entorno virtual, instalará las dependencias y configurará Antigravity con tus API Keys.*

---

## 🛠 Instalación Manual

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuración de variables:**
   Crea un archivo `.env` o pásalas directamente en la configuración del servidor:
   - `PEXELS_API_KEY`: Consíguela en [Pexels API](https://www.pexels.com/api/).
   - `UNSPLASH_ACCESS_KEY`: Consíguela en [Unsplash Developers](https://unsplash.com/developers).

---

## 🔧 Configuración MCP (Manual)

Si no usas el `setup.py`, añade esto a tu `mcp_config.json`:

```json
{
  "mcpServers": {
    "image-banko": {
      "command": "C:/Ruta/A/Tu/.venv/Scripts/python.exe",
      "args": ["C:/Ruta/A/Tu/src/server.py"],
      "env": {
        "PEXELS_API_KEY": "tu_llave",
        "UNSPLASH_ACCESS_KEY": "tu_llave"
      }
    }
  }
}
```

---

## 🎯 Herramientas disponibles

| Herramienta | Fuente | Descripción |
| :--- | :--- | :--- |
| `search_free_images` | Wikimedia | Imágenes CC0 de dominio público. No requiere API Key. |
| `search_pexels` | Pexels | Fotografía de stock premium de alta calidad. |
| `search_unsplash` | Unsplash | Imágenes artísticas y contemporáneas. |
| `search_sourcesplash` | SourceSplash | Búsqueda flash aleatoria (ideal para demos rápidas). |

---

## 🧠 Skill Maestro (Antigravity)

Este repositorio incluye una **Skill** que le da "superpoderes" de diseño a Antigravity. Para instalarla manualmente, copia el archivo de `.agent/skills/image-banko-master/SKILL.md` a tu carpeta local de skills o usa `setup.py`.

**¿Qué aprende Antigravity con esta skill?**
- A buscar imágenes con términos visuales óptimos.
- A implementar efectos CSS avanzados como **Parallax** y filtros dinámicos.
- A mantener una coherencia visual sin depender de imágenes genéricas.

---

⭐ **Tip**: Usa términos en inglés para obtener mejores resultados en las búsquedas (ej. "modern office aesthetic" en lugar de "oficina").
