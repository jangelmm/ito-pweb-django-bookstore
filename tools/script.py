import os
import argparse

# --- CONFIGURACIÓN PARA DJANGO ---

# Directorios que NO nos interesan (Basura, compilados, librerías externas)
IGNORE_DIRS = {
    '__pycache__',       # Compilados de Python
    'venv', 'env', '.env', '.venv', # Entornos virtuales (CRÍTICO ignorar esto)
    '.git', '.vscode', '.idea',     # Configuración de editor/git
    'node_modules',                 # Si usas npm/frontend
    'media',             # Archivos subidos por usuarios (imágenes, etc)
    'staticfiles',       # Archivos estáticos recolectados (duplicados)
    'site-packages',     # Librerías instaladas
    'htmlcov',           # Reportes de cobertura de tests
    'tmp',
    'tools'
}

# Archivos específicos a ignorar
IGNORE_FILES = {
    'db.sqlite3',        # Base de datos binaria (ilegibible)
    'db.sqlite3-journal',
    '.DS_Store',
    'poetry.lock',       # Suele ser muy largo
    'Pipfile.lock',      # Suele ser muy largo
    'package-lock.json',
}

# Extensiones que SÍ nos importan para entender el código
ALLOWED_EXTS = {
    '.py',               # Lógica de Django (views, models, urls...)
    '.html',             # Templates
    '.css',              # Estilos
    '.js',               # Interactividad
    '.json',             # Configuración / Fixtures
    '.md',               # Documentación
    '.txt',              # requirements.txt
    '.yml', '.yaml'      # Docker / Configuración CI
}

# Archivos prioritarios que SIEMPRE queremos ver (si existen)
INCLUDED_FILES = {
    'manage.py',         # Entry point de Django
    'requirements.txt',  # Dependencias
    'Pipfile',           # Dependencias
    'pyproject.toml',    # Configuración moderna
    'Dockerfile',
    'docker-compose.yml',
    'README.md',
    '.env.example'       # Útil para saber qué variables de entorno se necesitan
}

# Prefijos para dibujar el árbol
TREE_PREFIXES = {
    'branch': '├── ',
    'last':   '└── ',
    'indent': '    ',
    'pipe':   '│   '
}

def build_tree(root_path):
    """Genera el árbol de directorios visual."""
    tree_lines = []

    def _tree(dir_path, prefix=''):
        try:
            entries = sorted(os.listdir(dir_path))
        except PermissionError:
            return # Saltar carpetas sin permiso

        # Filtrado para el árbol
        entries = [
            e for e in entries
            if e not in IGNORE_DIRS
               and (not e.startswith('.') or e in INCLUDED_FILES)
        ]

        dirs = [e for e in entries if os.path.isdir(os.path.join(dir_path, e))]
        files = [e for e in entries if os.path.isfile(os.path.join(dir_path, e))]
        total = len(dirs) + len(files)

        for idx, name in enumerate(dirs + files):
            path = os.path.join(dir_path, name)
            connector = TREE_PREFIXES['last'] if idx == total - 1 else TREE_PREFIXES['branch']
            tree_lines.append(f"{prefix}{connector}{name}")
            
            if os.path.isdir(path):
                extension = TREE_PREFIXES['indent'] if idx == total - 1 else TREE_PREFIXES['pipe']
                _tree(path, prefix + extension)

    tree_lines.append(os.path.basename(root_path) or root_path)
    _tree(root_path)
    return tree_lines

def should_include_file(path, root):
    """Decide si leemos el contenido del archivo o no."""
    rel = os.path.relpath(path, root)
    fname = os.path.basename(path)
    ext = os.path.splitext(path)[1]
    
    # 1. REGLAS DE EXCLUSIÓN
    if fname in IGNORE_FILES:
        return False
    
    # Ignorar contenido de migraciones (mucho ruido, poca utilidad si vemos models.py)
    # Excepción: Si quieres ver la migración inicial, comenta esto.
    if 'migrations' in rel and fname != '__init__.py':
        return False
        
    # 2. REGLAS DE INCLUSIÓN
    if fname in INCLUDED_FILES:
        return True
        
    # Archivos con extensión permitida
    if ext in ALLOWED_EXTS:
        # Filtro extra: evitar scripts sueltos en carpetas raras
        # En Django casi todo el código útil está dentro de carpetas de apps o configuración
        return True

    return False

def collect_relevant_files(root):
    """Busca los archivos a leer."""
    paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Modificar dirnames in-place para que os.walk no entre en carpetas ignoradas
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            if should_include_file(fpath, root):
                paths.append(fpath)
    return paths

def ext_to_lang(ext):
    """Detecta lenguaje para el bloque de código Markdown."""
    return {
        '.py': 'python',
        '.html': 'html',
        '.css': 'css',
        '.js': 'javascript',
        '.json': 'json',
        '.yml': 'yaml',
        '.md': 'markdown'
    }.get(ext, 'text')

def main():
    parser = argparse.ArgumentParser(description="Resumen de proyecto Django.")
    parser.add_argument(
        'output', nargs='?', default='tools/django_project_overview.md',
        help='Archivo de salida (default: django_project_overview.md)'
    )
    args = parser.parse_args()
    root = os.getcwd()
    
    print(f"Escaneando proyecto Django en: {root}")
    print("Generando estructura...")
    tree_lines = build_tree(root)
    
    print("Recolectando archivos...")
    files = collect_relevant_files(root)

    with open(args.output, 'w', encoding='utf-8') as md:
        md.write(f"# Resumen del Proyecto Django: {os.path.basename(root)}\n\n")
        md.write(f"Ruta base: `{root}`\n\n")

        md.write("## Estructura del proyecto\n")
        md.write("```text\n")
        md.write("\n".join(tree_lines))
        md.write("\n```\n\n")

        md.write("## Contenido de Archivos\n\n")
        for path in files:
            rel = os.path.relpath(path, root)
            ext = os.path.splitext(path)[1]
            lang = ext_to_lang(ext)

            md.write(f"### `{rel}`\n")
            md.write(f"```{lang}\n")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Opcional: Si el archivo está vacío (ej. __init__.py), poner aviso
                    if not content.strip():
                        md.write("# (Archivo vacío)\n")
                    else:
                        md.write(content)
            except Exception as e:
                md.write(f"# Error al leer: {e}\n")
            md.write("```\n\n")

    print(f"¡Listo! Resumen guardado en: {args.output}")
    print(f"Archivos incluidos: {len(files)}")

if __name__ == '__main__':
    main()