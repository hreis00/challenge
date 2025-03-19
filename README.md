## Challenge

Inside the examples folder you have a couple files demonstrating how to use each sensor, pin and controller.
The objective of this challenge is to complete two phases:

1. First, analyze all the examples to gain a comprehensive understanding of how each component works, giving you a global perspective of the system.

2. Second, after this analysis, select and integrate two components to work together in parallel. For example, use the `GAS_SENSOR` to monitor values like ethanol, methane and propane and, if those readings fall outside the "normal" range, trigger the corresponding `SERVO_MOTOR` to automatically close the relevant valve, and then reopen it once the values return to safe levels.

This hands-on approach will help you understand both the individual components and how they can interact in a complete AIoT system.

## How to start to code

First, ensure that both the AIoT device and your computer are connected to the same network. Once connected, identify the IP address assigned to the AIoT device.

After completing these initial steps, you have two options to connect to the device

### Web Browser

- Navigate to `192.168.40.185:8888` in your browser
- Login with following password: `soda`

This will open a JupyterLab, where you can do your experiments. The first thing to do is to create a Jupyter Notebook with the names of the components you are integrating, following the pattern: `gas_sensor_servo_motor.ipynb`.

### Terminal

- Open a terminal window in your machine
- Run: `ssh soda@192.168.40.185`
- Login with following password: `soda`

After this, you'll need to navigate to where the code lives inside the AIoT device.

```shell
cd Projects/python/notebook
```

Following the Web Browser setup, you'll now need to create a new file for the components you are integrating, following the pattern: `gas_sensor_servo_motor.py`.

## How to test your code

### Web Browser

![Run](docs/images/run.png)

![Shutdown](docs/images/shutdown.png)

### Terminal

If you have connected via the terminal, you'll need to make sure you're inside the folder where the code lives, and run the following command:

```shell
python gas_sensor_servo_motor.py
```
