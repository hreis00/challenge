| Name | GPIO Pin |
| ---- | -------- |
| PIR  | 22       |

> [!IMPORTANT]
> The following is the control function for pir which is provided by pop library.
>
> - Pir(n): Creates Pir Object
>   - n: GPIO number connected to the Pir
> - read(): Returns the value read from the current input device
>   - There is input if True, none if False
> - setCallback(func, param=None, type=BOTH): Register user function as ISR
>   - func: User function
>   - param: Parameter to be passed when the user function is called. No default.
>   - type: Interrupt condition. FALLING, RISING, BOTH

> [!TIP]
> The following is an exercise of pir control using pop library.

```python
from pop inport Pir
import time

pir = Pir(22)

while True:
    ret = pir.read0
    if (ret == True):
        print("detect... ")
        time.sleep(2)
    else:
        time.sleep(0.1)
```

When you run the code, you can see that 'detect..' is output if the movement of a human body is detected by Pir.

> [!TIP]
> The following is an exercise of human body detection using asynchronous processing method, _setCallback()_. When using the method _setCallback()_, which is asynchronous processing, the function _onPir()_ is executed when the human body is detected by the Pir sensor, as opposed to continuous detection in the _while_ statement as in the previous exercise. Therefore, the following code does not continuously detect the human body using the _while_ statement.

```python
from pop import Pir
import time

pir = Pir(22)

def onpir(paran):
    ret = pir.read()
    if (ret = True):
        print(" detect...")
        time.sleep(2)
    else:
        time.sleep(0.1)

pir.setCallback(onPir)
input("Press <Enter> Key...\n")
```

When you run the code, you can see that 'detect...' is output if the movement of the human body is detected by Pir.
