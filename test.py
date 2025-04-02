from pop import ShiftRegister
from threading import Thread
import time 

run_flag = 1 # True
detect_flag = 0 # False
# lcd = Textlcd()
# pca = PwmController()
# pca.init()

def sr_loop():
    global detect_flag 
    sw = True
    gpio = [16, 6, 5]
    sr = ShiftRegister(gpio)
    c = 1
    while run_flag == 1:
        if detect_flag == 0:
            sr.shiftout(0xff)
        else:
            sr.shiftout(c)
            if sw:
                c = c << 1 | 1
            else:
                c = c >> 1 | 1
            if c > 0xff:
                sw = False
            elif c <= 0x01:
                sw = True
            time.sleep(0.1)

th=[Thread(target=sr_loop),
    # Thread(target=pir_loop),
    # Thread(target=cds_loop),
    # Thread(targee=th_loop),
    # Thread(target=gas_loop),
    ]

for i in range(len(th)):
    th[i].start()

# m = Touch()
# pw = [0,1,2,3]
# temp = []
# pca.setChannel(4)
# pca.setDuty(30)
# ptime = time.time()

run_flag = 0
for i in range(len(th)):
    th[i].join()
