| Name       | ADC CH |
| ---------- | ------ |
| Gas Sensor | 6      |

> [!IMPORTANT]
> The pop library provides a gas class for gas module control. Gas class inherits the class and calls methods defined in the SpiAdc class, and additionally provides the following functions:
>
> - calcPropan(val): Calculate the propane gas value
>
>   - val: ADC Data
>
> - calcMethan(val): Calculate methane gas value
>
>   - val: ADC Data
>
> - calcEthanol(val): Calculates ethanol gas value
>
>   - val: ADC Data

> [!TIP]
> The following is an example of gas module control using Gas class of pop library.

After creating a Gas object with ADC channel 6 as argument, read the ADC data of the current gas sensor with readAverage().

```python
from pop import Gas
import time

gas = Gas(6)

while True:
    val = gas.readAverage()
    print(val)
    time.sleep(0.1)
```

> [!TIP]
> The following is an example of outputting methane gas data.

```python
from pop import Gas
import time

gas = Gas(6)

while True:
    val = gas.readAverage()
    print("val = %d, methan = %d"%(val, gas.calcMethan(val)))
    time.sleep(0.1)
```
