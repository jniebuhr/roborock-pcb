#!/usr/bin/env bash
cd ./kicad
pcbdraw plot --side front -l custom --components -m remap.json -s set-black-hasl Roborock-CPAP.kicad_pcb ../assets/Roborock-CPAP_top.png
pcbdraw plot --side back -l custom --components -m remap.json -s set-black-hasl Roborock-CPAP.kicad_pcb ../assets/Roborock-CPAP_bottom.png
sips -r 180 ../assets/Roborock-CPAP_bottom.png