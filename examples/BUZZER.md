| Name         | PWM CH | GPIO Pin |
| ------------ | ------ | -------- |
| Piezo Buzzer | 0      | 12       |

> [!IMPORTANT]  
> The following is the Piezo Buzzer control function provided by pop library.
>
> - PiezoBuzzer(n): Creates PiezoBuzzer object
>
>   - n: GPIO number connected to Piezo Buzzer
>
> - tone(scale, pitch, duration): Outputting Piezo Buzzer scale
>
>   - scale: The scale, `'Do-Re-Mi-Fa-Sol-La-Si'`, is expressed as a number from 1 to 12 and a scale containing # is also output. For example, Enter 2 when you want to express and Do#, 8 for Sol.
>   - pitch: Pitch or octave, which can be expressed in 1 to 8 units. Generally, `"Do"` expressed in a music class is `"Do"` of 4 octaves.
>   - duration: Duration, 0.1 second unit
>
> - play(sheet): Plays PiezoBuzzer sheet
>
>   - sheet: List information of music sheets to play. `[[scale], [pitch], [duration]]`

> [!TIP]  
> The following is an exercise of controlling Piezo Buzzer using pop library.

```python
from pop import PiezoBuzzer
p = PiezoBuzzer(12)

p.tone(4, 8, 4)
```

As a result, you can see that Piezo Buzzer outputs the 8th scale (the 2nd argument of the 4th octave (the 1st argument) according to the quarter note (the 3rd argument) by the _tone()_ function.

> [!TIP]  
> The following is an exercise of playing music composed of sheets.

```python
from pop import PiezoBuzzer

p = PiezoDizzer(12)
butterfly_scale = [4,4,4, 4,4,4, 4,4,4,4, 4,4,4, 4,4,4,4, 4,4,4, 4,4,4,4, 4,4,4]
butterfly_gitch = [8,5,5, 6,3,3, 1,3,5,6, 8,8,8, 8,5,5,5, 6,3,3, 1,5,8,8, 5,5,5]
butterfly_duration = [8,8,4, 8.8,4, 8,8,8,8 8,8,4, 8,8,8,8, 8,8,4, 8,8,8,8, 8,8,4]
sheet_butterfly = [butterfly_scale, butterfly_pitch, butterfly_duration]

p.play(sheet_butterfly)
```
