# Exportar notas a Word (.docx)

Procedimiento para convertir notas del vault a documentos Word con estilos APA v7 y ecuaciones LaTeX nativas.

## Stack

1. **Pandoc 3.9** (instalado): motor de conversion Markdown -> DOCX. Traduce `$...$` y `$$...$$` a OMML (ecuaciones nativas de Word).
2. **`plantillas/reference-apa7.docx`**: template de estilos. Editable en Word para personalizar fuente, margenes, encabezados, etc.
3. **`plantillas/apa-7th.csl`**: estilo de citas APA 7ma edicion (oficial, repo Citation Style Language).
4. **`utils/md_to_docx.py`**: wrapper que aplica el template + CSL.
5. **Skill `docx` de Anthropic** (plugin): para edicion fina post-export (track changes, comentarios, edicion XML).

## Uso basico

```powershell
python utils/md_to_docx.py "cursos/2026-1/Amplificadores/clases/s07/S07-1 Tema 12 - Filtros.md"
```

Genera `S07-1 Tema 12 - Filtros.docx` junto al `.md`.

### Con citas APA

```powershell
python utils/md_to_docx.py nota.md --bib refs.bib
```

En el markdown, citar con `[@key2024]`. Pandoc inserta la referencia y agrega la bibliografia al final en APA v7.

### Sin tabla de contenidos

```powershell
python utils/md_to_docx.py nota.md --no-toc
```

### Salida personalizada

```powershell
python utils/md_to_docx.py nota.md -o "C:\entregas\Tarea1.docx"
```

## Personalizar estilos

Para cambiar fuente, margenes, color de encabezados, etc.:

1. Abrir `plantillas/reference-apa7.docx` en Word.
2. Modificar los estilos via el panel de estilos (no editar texto, solo estilos).
3. Guardar. La proxima conversion usa los estilos actualizados.

Estilos clave que Pandoc respeta: `Heading 1..6`, `Body Text`, `Caption`, `Quote`, `Author`, `Title`, `Date`, `Hyperlink`, `Code`.

## Triggers para Claude

Cuando el usuario diga:

- **"exporta [nota] a docx"** o **"convierte a Word"** -> usar `utils/md_to_docx.py` con la nota dada.
- **"agrega bibliografia APA"** -> pedir o detectar el `.bib`, luego correr con `--bib`.
- **"edita el docx"** o tareas de track changes / comentarios / edicion XML del `.docx` -> invocar el skill `docx` de Anthropic (ver instalacion abajo).

## Skill `docx` de Anthropic (instalacion)

El skill no se puede instalar via Bash; el usuario debe correr en Claude Code:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Despues, invocar con: *"usa el skill docx para ..."*. El skill maneja:

- Edicion via unpack/repack del XML interno
- Track changes y comentarios
- Headers/footers, tablas con anchos en DXA
- Conversion .doc legacy -> .docx
- Generacion programatica con `docx-js` (Node)

No maneja: ecuaciones LaTeX (delegar a Pandoc), bibliografia APA (delegar a Pandoc + CSL).

## Limitaciones conocidas

- Macros LaTeX no estandar o entornos exoticos (`\newcommand`, `align*` con multiples columnas) pueden no traducirse a OMML.
- Cross-references numeradas (figuras, ecuaciones) requieren el filtro `pandoc-crossref` (no instalado por defecto).
- Imagenes referenciadas con `![[...]]` (wikilinks) no las resuelve Pandoc; convertir a `![](ruta)` antes si hace falta.
