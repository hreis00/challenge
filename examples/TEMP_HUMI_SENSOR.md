| Name                        | I2C Address |
| --------------------------- | ----------- |
| Temperature/Humidity Module | 0x77        |

> [!IMPORTANT]
> The TempHumi class provided by the pop library has the following features:
>
> - TempHumi(addr=0x77): Creates TempHumi object
>   - addr: I2C address of Textlcd Module
> - init(): Initializes Temperature/Humidity module, called when creating the class
> - softReset(): Resets Temperature/Humidity module software
> - getSensorData(): Collects sensor data of Temperature/Humidity module, return it in a list form
>   - (temperature, pressure, humidity, gas_resistance)
> - getTemperature(): Collects Temperature data
> - getHumidity(): Collects Humidity data

• getTemperature(): Collects Temperature data
• getHumidity(): Collects Humidity data

> [!TIP]
> The code that reads and prints the ambient temperature and humidity values from the temperature/humidity module using the TempHumi class is written as follows.

```python
from pop import TempHumi
import time

th = TempHumi()
for i in range(20):
    temp = th.getTemperature()
    humi = th.getHumidity()
    print(temp, humi)
    time.sleep(0.5)
```

If you run the example, the temperature/humidity values are printed every 0.5 seconds.
