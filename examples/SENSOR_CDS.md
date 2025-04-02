| Name | ADC CH |
| ---- | ------ |
| CDS  | 7      |

> [!IMPORTANT]  
> Pop library provides Cds class for control of Cds. The Cds class inherits the SpiAdc class to call the methods defined in the SpiAdc class. In addition, it provides the following functions:
>
> - Cds (channel, device = 0, ce = 0, speed = 500000): Creates Cds object
>
>   - channel: ADC channel number connected to Cds module
>
> - setCalibrationPseudoLx(func): Register function to convert units
>
>   - Register function to use when converting ADC values to Lux unit
>
> - readAverage(): Read Lux Value
>
>   - Override SpiAdc's _readAverage()_ to read the value in Lux instead of the ADC value

> [!TIP]  
> The following is an exercise of Cds control using Cds class of pop library.

```python
from pop import Cds
import time

cds = Cds(7)

while True:
    val = cds.readAverage()
    print(val)

    time.sleep(0.1)
```

After creating a Cds object with the ADC channel number as an argument to which the Cds module is connected, calling _read()_ executes the _read()_ of SpiAdc class.
The results are as described above. Howerver, readAverage() is overhidden and converts the ADC value read from the Cds module to Lux unit and returns it.
