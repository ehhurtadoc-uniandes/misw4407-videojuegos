# Ejercicio Semana 4: Sonidos, textos, pausa, Service Locator y característica única

## Resumen

Complementar el programa del ejercicio 3 con la siguiente funcionalidad:

- [x] Texto con el título en la pantalla principal del juego.
- [x] Evento para pausar y reanudar con la tecla `P`, mostrando un texto que indica que el juego está pausado.
- [x] Efectos de sonido para las colisiones.
- [x] Efecto de sonido para el movimiento del personaje.
- [x] Los efectos suenan en los momentos adecuados.
- [x] Patrón **Service Locator** para **todos** los recursos externos (imagen, sonido, fuentes y archivos de configuración).
- [ ] Característica única del juego, implementada con ECS.
- [ ] Juego publicado en itch.io y enlace en `README.txt`.

Un ejemplo del resultado está en el sitio del curso: **SEMANA CUATRO - EJERCICIO - RESULTADO WEB**. No es obligatorio usarlo como plantilla.

## Service Locator

- [x] Clase `ServiceLocator` que guarda los servicios de carga.
- [x] Servicio de imágenes (`images_service`).
- [x] Servicio de sonidos (`sounds_service`).
- [x] Servicio de fuentes.
- [x] Servicio de configuraciones (`ConfigsService`) que administra los recursos JSON del juego.
- [x] Modificar la carga actual de JSON: `game_engine.py` no debe usar `open()` ni `json.load()` directamente.
- [x] Cada servicio tiene métodos específicos para su tipo de recurso.

## Sonidos

Se asocian a cada entidad con el parámetro `sound`:

- [x] Asteroides: suenan al aparecer (`enemies.json`, `sound`).
- [x] Balas: suenan al aparecer (`bullet.json`, `sound`).
- [x] Explosiones: suenan al aparecer (`explosion.json`, `sound`).
- [x] Hunter: suena solo al comenzar a perseguir al jugador (`enemies.json`, `sound_chase`).
- [x] Movimiento del personaje: suena en bucle mientras se mueve (`sounds.json`, `player_move`). Se define aparte porque `player.json` no trae un sonido para esto.

## Interfaz: `interface.json`

Archivo de creación propia. Su estructura es libre, pero debe existir y usarse para las propiedades básicas de los textos:

- [x] Ruta de la fuente `.ttf`, cargada con el Service Locator.
- [x] Contenido del texto.
- [x] Color del texto.
- [x] Tamaño del texto.

## Textos

- [x] Modificar `CSurface` con un método de clase `from_text` para crear texto estático.
- [ ] El texto dinámico se actualiza dentro de un sistema: ejecuta `font.render` con el texto adecuado y reemplaza la superficie y el área del componente.

## Pausa

- [x] Pausar y reanudar consiste en ejecutar o no los sistemas pertinentes.
- [x] El texto de pausa aparece al pausar y desaparece al reanudar.
- [x] Soltar o presionar teclas de movimiento durante la pausa no deja a la nave moviéndose sola al reanudar.
- [x] No se puede disparar durante la pausa.
- [ ] No se puede activar la característica única durante la pausa.

## Característica única

Condiciones del enunciado:

- [ ] Usa un elemento de input del teclado o el ratón.
- [ ] Es temporal y requiere recargar.
- [ ] Tiene un elemento visible diferente de los actuales.
- [ ] La recarga se ve en una barra de carga o en un número en pantalla.
- [ ] Aplica elementos de gamefeel.
- [ ] Hay instrucciones de input muy simples en pantalla.
- [ ] Respeta el patrón ECS de principio a fin.

### Diseño elegido: escudo de pulso

- [ ] Se activa con clic derecho o Espacio.
- [ ] Dura 2 segundos, con la animación `shield.png` alrededor de la nave y el sonido `laser_special.ogg`.
- [ ] Destruye a los enemigos dentro de un radio.
- [ ] Se recarga en 5 segundos, con barra en pantalla y texto `LISTO`.
- [ ] Gamefeel: vibración de pantalla al destruir enemigos y pulso visual al activarse.
- [ ] Configuración en un archivo propio (`special.json`).
- [ ] Componente `CSpecialAbility`, entidad del escudo, `system_special_ability` y `system_hud`.

## Recursos

- [x] Fuente `PressStart2P.ttf` y sonidos base copiados a `assets/`.
- [ ] Reemplazar `assets/snd/ufo.ogg` por la versión de verificación, que es distinta.
- [ ] Copiar `shield.png`, `bullet_especial.png` y `laser_special.ogg`.
- [x] Actualizar el título de `window.json` a `MISO - Ejercicio 04`.
- [ ] Revisar la licencia de cualquier recurso externo que se agregue.

Sitios recomendados: <https://opengameart.org/>, <https://kenney.nl/>, <https://freesound.org/>, <https://indiegamemusic.com/>.

## Distribución

- [ ] Subir el juego a itch.io, en despliegue web o ejecutable descargable.
- [ ] Si es ejecutable, que sea para Windows o Linux. Mac se acepta, pero se prefiere evitarlo.
- [ ] Incluir `README.txt` con el enlace a itch.io.

## Restricciones

- [ ] Los archivos de verificación pueden reemplazar a los del proyecto sin romper el juego.
- [x] Los sistemas no cargan archivos directamente.
- [ ] Los temporizadores usan `delta_time`, para que se detengan durante la pausa.

## Rúbrica (100%)

| Dimensión | Peso | Criterio para "Excelente" |
|---|---|---|
| Funcionamiento básico | 10% | El programa ejecuta correctamente. |
| Carga y despliegue de sprites, sonidos y configuración | 10% | El programa carga correctamente los recursos. |
| Carga y despliegue de texto y fuentes | 10% | El programa carga correctamente textos. |
| Pausar y reanudar el juego | 10% | Pausa y reanuda correctamente y muestra un texto de pausa. |
| Patrón Service Locator para todos los recursos externos | 20% | Usa completamente el patrón Service Locator. |
| Característica única del juego | 20% | Se despliega correctamente junto con el uso del patrón ECS. |
| Publicación en itch.io | 20% | Está publicado en itch.io listo para jugar o descargar. |

## Entrega

- Subir el ZIP del proyecto entero con el programa funcionando.
- El ZIP debe contener `README.txt` con el enlace a itch.io del juego compilado.
- Probar antes con los archivos del sitio del curso (SEMANA CUATRO - EJERCICIO - RECURSOS PARA VERIFICACIÓN).
