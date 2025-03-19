| Name    | I2C Address |
| ------- | ----------- |
| TextLCD | 0x27        |

> [!IMPORTANT]
> The functions of the Textlcd class provided by the pop library are as follows:
>
> - Textlcd(addr = 0x27): Creates Textlcd object
>   - addr: I2C address of Textlcd module
> - command(command): Sends a command to TextLCD
>   - command: Command to send
> - clear(): Initializes TextLCD screen
> - returnHome(): Moves the cursor to Home
> - displayOn(): Turns on TextLCD
> - displayOff(): Turns off TextLCD
> - displayShiftR(): Moves the TextLCD screen 1 space to the right
> - displayShiftL(): Moves the TextLCD screen 1 space to the left
> - cursorOn(blinking): Cursor on
>   - blinking: Specifies to use the blinking cursor
> - cursorOff(): Cursor off
> - cursorShiftR(): Moves the cursor position 1 space to the right
> - cursorShiftL(): Moves the cursor position 1 space to the left
> - entryModeSet(): When reading and writing data, the screen does not move but the cursor
>   position increases by 1 space
> - setCursor(x,y): Cursor positioning
>   - x,y: Specified within the cursor's coordinates 16x2
> - data(data): Writes text to the TextLCD
>   - data: Character to be displayed on Text LCD
> - print(str): Writes a string to TextLCD
>   - str: String to be displayed on the Text LCD

> [!TIP]
> Now let's use the Texticd class to initialize the Text LCD, turn on the cursor and write code to move.

```python
from pop import Textlcd
import time

lcd = Textlcd()

lcd.clear()
lcd.cursorOn(1)
time.sleep(1)
lcd.cursorShiftR()
tine.sleep(1)
lcd.cursorShiftL()
time.sleep (1)
lcd.setCursor (10, 2)
time.sleep(1)
lcd.cursorOff()
```

When vou create a Texlcd instance, initialization proceeds and the cursor turns on.
After 1 second, the cursor moves one space to the right. After 1 second again, cursor moves one space to the left. After 1 second again, the cursor moves to the coordinate (2,10). And after 1 second, the cursor turns off.

> [!TIP]
> The following is an exercise of printing and moving the text in Texticd.

```python
from pop import Textlcd
import time

lcd = Textlcd()
str = "Hello AlOT Home"
time.sleep (1)
lcd.clear()
lcd.print(str)
time.sleep(1)
lcd.displayShiftRO
time.sleep (1)
lcd.displayShiftLQ
time.sleep(1)

lcd.displayOff()
time.sleep(1)
lcd.displayOn()
time.sleep(1)
```

When you run the example, the phrase "Hello AIoT Home" is displayed, and after 1 second, the entire character moves one space to the right. After 1 second, the entire text moves to the left one space. And after 1 second again, the TextLCD screen turns off and after 1 second, the screens turns on again.
