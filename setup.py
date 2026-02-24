import os
import json
import platform
import shutil
import sys
import subprocess
from pathlib import Path
from typing import Any

SKILL_CONTENT = """---
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
"""

def find_modern_python():
    """Busca una versión de Python compatible (>= 3.10)"""
    if sys.version_info >= (3, 10):
        return sys.executable
    
    # Intentar buscar versiones específicas
    for cmd in ["python3.12", "python3.11", "python3.10", "python3", "python"]:
        path = shutil.which(cmd)
        if path:
            try:
                res = subprocess.check_output([path, "-c", "import sys; print(sys.version_info >= (3,10))"], text=True, stderr=subprocess.DEVNULL).strip()
                if res == "True":
                    return path
            except:
                continue
    
    # Rutas comunes en macOS (Homebrew)
    common_mac_paths = [
        "/opt/homebrew/bin/python3.12",
        "/opt/homebrew/bin/python3.11",
        "/opt/homebrew/bin/python3.10",
        "/usr/local/bin/python3.12",
        "/usr/local/bin/python3.11",
        "/usr/local/bin/python3.10"
    ]
    for path in common_mac_paths:
        if os.path.exists(path):
            return path
            
    return None

def setup():
    print("🚀 Iniciando instalación de MCP Image Banko...")
    
    curr_dir = Path(os.getcwd()).absolute()
    is_windows = platform.system() == "Windows"
    
    # 1. Verificar/Buscar Python moderno
    modern_python = find_modern_python()
    if not modern_python:
        print("❌ ERROR: Este proyecto requiere Python 3.10 o superior.")
        print("Por favor, instala una versión reciente de Python (ej. 'brew install python@3.12') y vuelve a intentarlo.")
        sys.exit(1)
    
    print(f"✅ Usando Python para configuración: {modern_python}")

    # 2. Gestionar Entorno Virtual
    venv_dir = curr_dir / ".venv"
    if is_windows:
        venv_python = venv_dir / "Scripts" / "python.exe"
        venv_pip = venv_dir / "Scripts" / "pip.exe"
    else:
        venv_python = venv_dir / "bin" / "python"
        venv_pip = venv_dir / "bin" / "pip"

    if not venv_dir.exists():
        print(f"📦 Creando entorno virtual en {venv_dir}...")
        subprocess.run([str(modern_python), "-m", "venv", ".venv"], check=True)
    else:
        # Verificar si el venv existente es válido (>3.10)
        try:
            res = subprocess.check_output([str(venv_python), "-c", "import sys; print(sys.version_info >= (3,10))"], text=True, stderr=subprocess.DEVNULL).strip()
            if res != "True":
                print("⚠️ El entorno virtual actual no es compatible. Recreando...")
                shutil.rmtree(venv_dir)
                subprocess.run([str(modern_python), "-m", "venv", ".venv"], check=True)
            else:
                print("✅ Entorno virtual existente es compatible.")
        except:
            print("⚠️ Entorno virtual dañado o incompatible. Recreando...")
            if venv_dir.exists():
                shutil.rmtree(venv_dir)
            subprocess.run([str(modern_python), "-m", "venv", ".venv"], check=True)

    # 3. Instalar dependencias automáticamente
    print("📥 Instalando dependencias...")
    try:
        subprocess.run([str(venv_pip), "install", "--upgrade", "pip"], check=True)
        req_file = curr_dir / "requirements.txt"
        if req_file.exists():
            subprocess.run([str(venv_pip), "install", "-r", str(req_file)], check=True)
        else:
            subprocess.run([str(venv_pip), "install", "mcp", "httpx", "python-dotenv"], check=True)
        print("✅ Dependencias instaladas.")
    except Exception as e:
        print(f"❌ Error instalando dependencias: {e}")

    # 4. Solicitar/Cargar Keys
    def load_env_manual(path):
        env_vars = {}
        if os.path.exists(path):
            with open(path, "r") as f:
                for line in f:
                    if "=" in line and not line.startswith("#"):
                        k, v = line.strip().split("=", 1)
                        env_vars[k] = v
        return env_vars

    env_data = load_env_manual(".env")
    
    pexels_key = env_data.get("PEXELS_API_KEY") or os.getenv("PEXELS_API_KEY")
    unsplash_key = env_data.get("UNSPLASH_ACCESS_KEY") or os.getenv("UNSPLASH_ACCESS_KEY")
    
    if not pexels_key or not unsplash_key:
        print("\n🔑 Configuración de API Keys:")
        if not pexels_key:
            pexels_key = input("Introduce tu PEXELS_API_KEY: ").strip()
        if not unsplash_key:
            unsplash_key = input("Introduce tu UNSPLASH_ACCESS_KEY: ").strip()
        
        # Guardar en .env
        with open(".env", "w") as f:
            f.write(f"PEXELS_API_KEY={pexels_key}\n")
            f.write(f"UNSPLASH_ACCESS_KEY={unsplash_key}\n")
        print("✅ Archivo .env actualizado.")

    # 5. Configurar mcp_config.json
    if is_windows:
        antigravity_path = Path(os.environ.get("USERPROFILE", "")) / ".gemini" / "antigravity"
    else:
        antigravity_path = Path.home() / ".gemini" / "antigravity"
    
    server_path = curr_dir / "src" / "server.py"
    config_file = antigravity_path / "mcp_config.json"
    antigravity_path.mkdir(parents=True, exist_ok=True)
    
    config_data: Any = {"mcpServers": {}}
    if config_file.exists():
        try:
            with open(config_file, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    config_data.clear()
                    config_data.update(data)
        except:
            pass
            
    if "mcpServers" not in config_data or not isinstance(config_data["mcpServers"], dict):
        config_data["mcpServers"] = {}
        
    mcp_servers: Any = config_data["mcpServers"]
    mcp_servers["image-banko"] = {
        "command": str(venv_python).replace("\\", "/"),
        "args": [str(server_path).replace("\\", "/")],
        "env": {
            "PEXELS_API_KEY": pexels_key,
            "UNSPLASH_ACCESS_KEY": unsplash_key
        }
    }
    
    # Asegurarse de que el directorio existe
    config_file.parent.mkdir(parents=True, exist_ok=True)
    with open(config_file, "w") as f:
        json.dump(config_data, f, indent=4)
    print(f"✅ mcp_config.json actualizado en {config_file}")

    # 6. Instalar Skill
    skill_dir = antigravity_path / "skills" / "image-banko-master"
    skill_dir.mkdir(parents=True, exist_ok=True)
    with open(skill_dir / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(SKILL_CONTENT)
    print(f"✅ Skill instalada en {skill_dir}")

    print("\n✨ ¡Instalación completada con éxito!")
    print("Reinicia tu cliente de Antigravity para activar el nuevo MCP y la Skill.")

if __name__ == "__main__":
    setup()
