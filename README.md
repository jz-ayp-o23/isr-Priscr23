# Estructuras de decisión

## Ejercicio: ISR

## Instrucciones
- Elabora el análisis y el algoritmo ***antes de escribir el código***. Utiliza un diagrama de flujo para representar tu algoritmo e ilustrar su lógica.

- **Diseña un programa para calcular el impuesto sobre la renta (ISR) correspondiente a un sueldo mensual dado**. El ISR se calcula usando la tarifa de la siguiente tabla. 

Límite inferior ($) | Límite superior ($) | Cuota fija ($) | Porciento a aplicarse sobre el excedente del límite inferior
----------|-------------|----------|----
0.01      | 3,644.94    |    12.88 | 10
3,644.95  | 7,446.19    |   303.76 | 20
7,466.20  | 10,298.35   | 1,063.92 | 30
10,298.36 | en adelante | 3,327.42 | 35

*Uso de la tabla*: se localiza en qué renglón queda el sueldo, se le resta el límite inferior (columna 1) correspondiente, este resultado (se le llama excedente) se multiplica por el porcentaje de la última columna para obtener el impuesto marginal. El ISR total se calcula sumando este impuesto marginal a la cuota fija del renglón

- Codifica tu solución en el archivo [`isr.py`](/isr.py).
   
- Utiliza los siguientes ejemplos para dar formato a tus entradas y salidas:
  ```
  Sueldo: 5000
  ISR: 574.77
  
  Sueldo: 20000
  ISR: 6722.994
  ```
  
- Prueba tu programa corriéndolo varias veces con diferentes entradas. Verifica que tu algoritmo produzca las salidas correctas. Pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade la correspondiente cadena de documentación (*docstring*) al inicio de tu programa.
  
## Entrega
Completa este y el resto de los ejercicios y compila, para cada ejercicio, el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución, en un informe tal como se describe en los requisitos para entrega de tareas en Canvas. No olvides incluir portada y conclusiones.

## Casos de prueba de ejemplo
| Entradas | Salidas |
|:---------|:--------|
| `5000` | `574.77` |
| `20000` | `6722.994` |

## Rúbrica
Verifica tu entrega contra la rúbrica disponible en Canvas para maximizar tu calificación.
