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

dcfan = Fan(17)

dcfan.on()
time.sleep(3)
dcfan.off()
```

As a result, you can see that the DC Fan is running for 3 seconds and stopped.
