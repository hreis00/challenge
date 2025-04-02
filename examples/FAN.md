| Name   | GPIO Pin |
| ------ | -------- |
| DC Fan | 17       |

> [!IMPORTANT]
> The following is the DC Fan control function provided by pop library.
>
> - Fan(n): Creates DC Fan object
>
>   - n: Forwards the GPIO number connected to DC Fan
>
> - on(): Turns on DC Fan
>
> - off(): Turns off DC Fan

> [!TIP]
> The following is an exercise of DC Fan control using pop library.

```python
from pop import Fan
import time

fan = Fan(17)

fan.on()
time.sleep(3)
fan.off()
```

As a result, you can see that the Fan is running for 3 seconds and stopped.
