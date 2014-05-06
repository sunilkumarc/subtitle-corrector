#!/bin/bash

sudo chmod +x subtitle_corrector.py remove.sh
sudo mkdir /opt/subtitle-corrector
sudo cp remove.sh subtitle_corrector.py /opt/subtitle-corrector
sudo ln -s /opt/subtitle-corrector/subtitle_corrector.py /usr/bin/corrector
sudo ln -s /opt/subtitle-corrector/remove.sh /usr/bin/corrector-uninstall
