| Name         | I2C Address |
| ------------ | ----------- |
| Touch Module | 0x5A        |

> [!IMPORTANT]
> The pop library supports reading the state of the Touch module through the Touch class. It read each channel separately and expresses the status as 1 when pressing is detected, or as 0 when it is not detected. Or, it reads all channels at once and returns the status of each channel in the form of a list. The following are the functions provided by the Touch class:
>
> - Touch(addr=0x5a): Creates Touch object
>   - addr: I2C address of the Touch module, which is pre-assigned and can be used without specifying it
> - reset(): Software Reset for Touch module. Automatically called during creating an object, or can be called and used when separate initialization is needed
> - readChannel(ch): Reads the status 1 channel of Touch module
>   - ch: Channel to be checked in terms of status, Selected from 0 to 11
> - readAll(): Reads all the channels of Touch module and returning them in a list form

> [!TIP]
> As follows, you can write an example which prints if a channel is detected by reading the current status of Touch module with Touch class provided by Pop library

```python
from pop import Touch
import time

touch = Touch()

while True:
    for i in range(12):
        val = touch.readChannel(i)
        if val == 1:
            print('ch %d pushed! \n%i)
        time.sleep(0.05)
```

> [!TIP]
> You can use _readAll()_ method to get the same result as above example

```python
from pop import Touch
import time

touch = Touch()

while True:
    for i in range(100):
        ret = touch.readAll()
        for i in range(12):
            if ret[i] == True:
                print('ch %d pushed! \n%i)

            time.sleep(0.05)
```

Unlike monitoring each channel using the _readChannel()_ method as in the previous example, the example uses the _readAll()_ method to return and process all the 12 channels at once.
