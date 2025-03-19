| Name                      | PWN CH |
| ------------------------- | ------ |
| Servo Motor (Door)        | 4      |
| Servo Motor (Gas Breaker) | 4      |

> [!TIP]  
> Let's control the servo motor connected to the PWN control module. Servo Motor is connected to 3 and 4 channels of PWN control module. In order to control the servo motor, a frequency of 50 Hz (20ms) must be used. It is controlled with a high signal of 0.5 ms at 0º, 1.5 ms at 90º, and 2.5 ms at 180º.

```python
from pop import PwnController
import time

pwn = pwnController()
pwn.init()
pwn.setChannel(3)
pwn.setFreq(50)
While True:
    pwn.setDuty((0.5/20)*100)
    time.sleep(3)
    pwn.setDuty((1.5/20)*100)
    time.sleep(3)
    pwn.setDuty((2.5/20)*100)
    time.sleep(3)
```

If you run the code, Gas Break repeats 3 angle rotations of 0º, 90º, and 180º.
