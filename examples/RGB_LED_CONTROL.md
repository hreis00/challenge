| Name        | PWN CH |
| ----------- | ------ |
| RGB LED (R) | 0      |
| RGB LED (G) | 1      |
| RGB LED (B) | 2      |

> [!TIP]
> The following is and example of RGB LED control using PwnController class of pop library.

```python
from pop import PwnController
import time

pwn = PwnController()
pwn.init()
pwn.setChannel(0)
pwn.setFreq(50)
for i in range(10):
    pwn.setDuty(i*10)
    time.sleep(0.5)
```

If you run the example, the RGB LED gets brighter as red color.

> [!TIP]  
> The following is an example of sequentially controlling red, green and blue LEDs. To set all three channels of PWN to the same frequency, the argument of the method _setChannel()_ is given as -1. After setting the toal frequency to 50, set and control for each channel again.

```python
from pop import PwnController
import time

pwn = pwnController()
pwn.init()
pwn.setChannel(-1)
pwn.setFreq(50)

pwn.setChannel(0)
for i in range(10):
    pwn.setDuty(i*10)
    time.sleep(0.5)
pwn.setDuty(0)

pwn.setChannel(1)
for i in range(10):
    pwn.setDuty(i*10)
    time.sleep(0.5)
pwn.setDuty(0)

pwn.setChannel(2)
for i in range(10):
    pwn.setDuty(i*10)
    time.sleep(0.5)
pwn.setDuty(0)
```
