| Name          | GPIO Pin |
| ------------- | -------- |
| Data (SRDATA) | 16       |
| Clock (SRCLK) | 5        |
| Latch (RCLK)  | 6        |

> [!IMPORTANT]
> The pop library provides the following functions to easily control the Shift Register.
> Therefore, the LED bar can be easily controlled without complicated process.
>
> - ShiftRegister(n): Creates Shift Register object
>   - n: List of GPIO numbers connected to Shift Register
>     - GPIO list is in order of Data, Clock, and Latch
>   - shiftout(value): Data writing to Shift Register
>     - value: 8-Bit Data to transfer to Shift Register

> [!TIP]
> The following is an exercise of LED Bar control using pop library.

```python
from pop import ShiftRegister
import time

gpio = [16,5,6]
s = ShiftRegister(gpio)

s.shiftout(0xff)
time.sleep(1)
s.shiftout(0x00)
time.sleep(2)
s.shiftout(0x00)
```

Since method _shiftout()_ inputs 8-bit data, it is necessary to call _shiftout()_ twice to control two LED BARs simultaneously. Therefore, 0xff is output to the first LED Bar with the command `s.shiftout(0xff)`, and 0x00 is output to the first LED Bar with the command `s.shiftout(0x00)` after 1 second. And the 0xff data that was output to the first LED Bar is shifted and output to the second LED Bar.
