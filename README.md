# Roborock CPAP PCB

[![](https://dcbadge.vercel.app/api/server/APw7rgPGPf)](https://discord.gg/APw7rgPGPf)

This repository contains a custom PCB for use with the awesome work at [Roborock CPAP](https://github.com/condottab/Roborock-CPAP). The PCB shields the controller board from any back flow that might occur from the brushless controller.

The logic is the same as in the work of [stas2z](https://github.com/stas2z) but reshaped to better fit on the back of the blower while also allowing
for a cooling fan to be added.

![](assets/cpap_render.png)

## BOM

| Quantity | Designation    | Description          |
|----------|----------------|----------------------|
| 1        | SHOTTKY2       | DSK24 Diode          |
| 2        | SHOTTKY1       | BZT52C5V1S Diode     |
| 1        | ZENER1, ZENER2 | SS56 Diode           |
| 1        | R2             | 0805 10kΩ resistor   |
| 1        | R1             | 0805 1kΩ resistor    |
| 2        | J1, J2         | JST PH 3P 2.54mm     |
| 1        | J3             | JST PH 2P 2.54mm     |
| 1        | -              | 4010 cooling fan 24V |
| 2        | -              | M3x6                 |
| 4        | -              | M3x12                |
| 4        | -              | M3 hex nut           |
| 4        | -              | M3 heat set insert   |

## Pinout

![](assets/pinout.png)

## Ordering

The files to order this PCB are in the `jlcpcb` sub-folder. These work with the JLCPCB assembly service as well, there will be extended component fees though.

## License

This project is licensed as
![image](https://user-images.githubusercontent.com/37383368/139769027-7267da5b-7f58-499d-96bc-e41d164a3aac.png)

https://creativecommons.org/licenses/by-nc/4.0/
