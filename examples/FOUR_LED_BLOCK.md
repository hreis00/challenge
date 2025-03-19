| Name  |
| ----- |
| LED 1 |

> [!CAUTION]
> TERMINAR TABELA DOS LEDS

> [!TIP]
> The following is an exercise of controlling all 4 LED blocks.

```python
from pop import Led
import time

leds = [Led (23), Led(24), Led(25), Led (27)]

while True:
    for led in leds:
        led.on()
        time.sleep(0.1)

    for led in leds[-1::-1]:
        led.off()
        time.sleep(0.1)
```

As a result, the 4 LED blocks are turned on and off sequentially.
