# Extracción de ejercicios desde videos de YouTube

Documento de referencia para extraer ejercicios resueltos publicados en YouTube. Cargar bajo demanda cuando el usuario pida transcribir/capturar un video (ver triggers en `CLAUDE.md`).

---

## Flujo

1. **Extraer transcripción** con `yt-dlp` (instalado): `yt-dlp --write-auto-sub --sub-lang es --skip-download --sub-format vtt -o "ruta/output" "URL"`
2. **Parsear la transcripción** VTT a texto limpio con timestamps usando el script `utils/parse_vtt.py`
3. **Analizar la transcripción** para identificar momentos clave: enunciado, datos, fórmulas, cálculos, resultado
4. **Navegar al video** con Playwright (`browser_navigate`)
5. **Cerrar diálogos** si aparecen (YouTube Premium "No thanks", cookies consent)
6. **Pausar el video** y verificar duración real (si la propaganda desplazó los tiempos, el video puede mostrar duración incorrecta hasta que se recargue)
7. **Tomar screenshots** en timestamps clave usando `browser_run_code`:
   - Pausar: `document.querySelector('video').pause()`
   - Seek: `document.querySelector('video').currentTime = seconds`
   - Esperar: `page.waitForTimeout(2000)` (dar tiempo al frame de renderizar)
   - Capturar área del video: `page.screenshot({ clip: { x: 0, y: 60, width: 914, height: 514 } })`
   - **Importante**: las coordenadas del video son fijas (`y: 60` por la barra de YouTube); verificar con `boundingBox()` si hay problemas
8. **Verificar capturas** leyéndolas — si solo muestran la barra de YouTube, el video no estaba visible (pudo haber terminado y colapsado); re-seek a `currentTime = 0` y reintentar
9. **Crear la nota** combinando transcripción + capturas, con resolución paso a paso en LaTeX

---

## Notas importantes

- `yt-dlp` está instalado globalmente via pip
- El script [`utils/parse_vtt.py`](../utils/parse_vtt.py) limpia el formato VTT (elimina tags `<c>`, deduplica líneas repetidas, extrae timestamps `m:ss`)
- Los subtítulos auto-generados tienen errores de transcripción en términos técnicos (e.g. "weever" = Weber, "ampi" = Ampere) — interpretar con contexto
- Si el video tiene propaganda al inicio, la duración reportada por `document.querySelector('video').duration` puede ser solo la del ad; esperar a que termine o saltar
- Guardar las capturas del video en `attachments/` con prefijo descriptivo (e.g. `video-ej-enunciado.png`, `video2-tabla.png`)
- Al insertar un ejercicio de video entre notas existentes: renumerar las notas posteriores (archivos + frontmatter `orden` + wikilinks en Formulario y otras notas)
