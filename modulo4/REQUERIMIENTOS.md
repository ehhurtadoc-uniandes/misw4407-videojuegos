# Ejercicio Semana 1: Rectángulos que rebotan

## Resumen

Crear un programa que genere una serie de rectángulos de diferentes colores que rebotan en la pantalla. Cada rectángulo tiene un tiempo de aparición (en segundos), un tamaño (x, y), una posición (esquina superior izquierda), un color, una velocidad y una dirección al azar. Toda esta información se obtiene de archivos de configuración.

## Requerimientos generales

- [x] El programa funciona y cumple los requerimientos con los archivos de configuración dados.
- [x] El programa funciona con archivos de configuración modificados. Debe soportar:
  - [x] Cambios en las características de la ventana.
  - [x] Cambios en los rectángulos generados.
  - [x] Agregar o eliminar rectángulos en el sistema de eventos (puede haber más de seis o ninguno).
- [x] Todo se implementa bajo el marco **ECS**.
- [x] Los componentes y sistemas son fácilmente identificables y tienen un comportamiento único:
  - Los componentes no tienen lógica.
  - Los sistemas solo manipulan los datos de los componentes que solicitan.
- [x] El patrón **gameloop** es claramente identificable, con secciones de iniciar, calcular tiempo, actualizar, dibujar y terminar.

## Archivos de configuración

### `window.json`: ventana

| Propiedad | Llave |
|---|---|
| Título | `title` |
| Tamaño en píxeles | `size.w`, `size.h` |
| Color de fondo | `bg_color.r`, `bg_color.g`, `bg_color.b` |
| Framerate | `framerate` |

### `enemies.json`: tipos de rectángulo

Cada tipo se identifica por su nombre (la llave del objeto) y tiene:

| Propiedad | Llave |
|---|---|
| Tamaño | `size.x`, `size.y` |
| Color | `color.r`, `color.g`, `color.b` |
| Velocidad mínima | `velocity_min` |
| Velocidad máxima | `velocity_max` |

### `level_01.json`: eventos de aparición

Lista `enemy_spawn_events`. Cada evento especifica:

| Propiedad | Llave |
|---|---|
| Tipo de rectángulo (nombre en `enemies.json`) | `enemy_type` |
| Tiempo de aparición en segundos | `time` |
| Posición (esquina superior izquierda) | `position.x`, `position.y` |

- La velocidad se asigna al azar entre `velocity_min` y `velocity_max`.
- El ángulo de dirección inicial se asigna al azar.

## Detalles de implementación

### Spawner

- [x] Crear el componente `CEnemySpawner` y el sistema `system_enemy_spawner`.
- [x] Debe existir **una única** entidad con **un** componente `CEnemySpawner`.
- [x] El componente guarda la información del nivel cargado. No se trabaja directamente con el JSON del nivel.
- [x] El sistema crea los rectángulos uno por uno cuando el tiempo transcurrido es igual o mayor al tiempo de cada evento.
- [x] El paso del tiempo se registra con `delta_time`. **No** se permiten Timers ni Schedulers nativos de Python.
- [x] Recomendado: cada evento tiene una marca que indica si ya fue disparado, para ignorarlo después.

### Restricciones

- [x] **No** se cargan archivos JSON dentro de un sistema. Se cargan desde el motor (u otra clase) y quedan listos para usarse.
- [x] Los otros JSON (`window.json`, `enemies.json`) pueden estar precargados en el motor.
- [x] Los sistemas solo usan datos obtenidos a través de ECS y no tienen lógica adicional a su propósito.

### Elementos que deben estar en ECS

- [x] Dibujado de rectángulos
- [x] Movimiento
- [x] Rebote
- [x] Spawner

## Dónde está implementado

| Requerimiento | Archivo |
|---|---|
| Gameloop y carga de JSON | `src/engine/game_engine.py` |
| Componentes | `src/ecs/components/` (`c_transform`, `c_velocity`, `c_surface`, `c_enemy_spawner`) |
| Movimiento | `src/ecs/systems/s_movement.py` |
| Rebote | `src/ecs/systems/s_screen_bounce.py` |
| Dibujado | `src/ecs/systems/s_rendering.py` |
| Spawner | `src/ecs/systems/s_enemy_spawner.py` |
| Creación de entidades | `src/create/prefab_creator.py` |

## Rúbrica (100 puntos)

| Dimensión | Puntos | Criterio para "Excelente" |
|---|---|---|
| Funcionamiento básico | 12 | El programa ejecuta correctamente. |
| Sistema de Spawner | 12 | Crea rectángulos respetando el tiempo de creación y en el orden correcto. |
| Uso de ECS | 20 | Usa ECS completamente con sistemas y componentes. |
| Colores y tamaños | 8 | El sistema de dibujo usa el color y tamaño correctos. |
| Sistema de movimiento | 12 | Toma en cuenta correctamente las velocidades y los rebotes. |
| Uso del patrón gameloop | 20 | El gameloop es claro y bien estructurado (nada de actualizar o calcular tiempo en la sección de dibujar). |
| Uso de archivos de configuración | 8 | Carga y usa todos los elementos de configuración y acepta cambios. |
| Archivos extra de configuración | 8 | Funciona con todos los archivos de configuración de ejemplo. |

## Entrega

- Subir el ZIP del proyecto entero con el programa funcionando.
- Probar antes con los archivos de verificación del sitio del curso (SEMANA UNO - EJERCICIO - RECURSOS PARA VERIFICACIÓN).
