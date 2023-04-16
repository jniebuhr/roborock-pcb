# Roborock CPAP PCB

This repository contains a custom PCB for use with the awesome work at [Roborock CPAP](https://github.com/condottab/Roborock-CPAP). The PCB shields the controller board from any back flow that might occur from the brushless controller.

The logic is the same as in the work of [stas2z](https://github.com/stas2z) but reshaped to better fit on the back of the blower while also allowing
for a cooling fan to be added.

![](assets/cpap_render.png)

## BOM

| Quantity | Description          |
|----------|----------------------|
| 1        | 4010 cooling fan 24V |
| 1        | DSK24 Diode          |
| 2        | BZT52C5V1S Diode     |
| 1        | SS56 Diode           |
| 1        | 0805 10kΩ resistor   |
| 1        | 0805 1kΩ resistor    |
| 2        | JST PH 3P 2.54mm     |
| 1        | JST PH 2P 2.54mm     |

## Pinout

![](assets/pinout.png)

## Ordering

The files to order this PCB are in the `jlcpcb` sub-folder. These work with the JLCPCB assembly service as well, there will be extended component fees though.
