import logging
import subprocess
import pwnagotchi.plugins as plugins
#YOU MUST DOWNLOAD macchanger!!!!!!
#sudo apt install macchanger


class MacSpoofRandom(plugins.Plugin):
    __author__ = 'x0jac0b0x'
    __version__ = '1.0.0'
    __license__ = 'GPL3'

    def __init__(self):
        self.running = False

    def Random_mac(self):
        interface = "wlan0" #network interface
        try:
            subprocess.run(['sudo', 'macchanger', '-r', interface])
            logging.info(f"MAC Address changed")
        except Exception as e:
            logging.warning(f"Failed to change MAC address:{e}")

    def on_loaded(self):
        self.static_mac()
        logging.info("MACspoofRandom Plugin loaded")

    def on_unload(self):
        logging.info("MACspoofRandom Plugin unloaded")