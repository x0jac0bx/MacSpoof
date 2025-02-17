import logging
import subprocess
import pwnagotchi.plugins as plugins
#YOU MUST DOWNLOAD macchanger!!!!!!
#sudo apt install macchanger


class MacSpoofStatic(plugins.Plugin):
    __author__ = 'x0jac0b0x'
    __version__ = '1.0.0'
    __license__ = 'GPL3'

    def __init__(self):
        self.running = False

    def static_mac(self):
        new_mac = 'ca:fe:c0:ff:ee:00' #change for new mac address
        interface = "wlan0" #network interface
        try:
            subprocess.run(['sudo', 'macchanger', '-m', new_mac, interface])
            logging.info(f"MAC Address changed to: {new_mac}")
        except Exception as e:
            logging.warning(f"Failed to change MAC address:{e}")

    def on_loaded(self):
        self.static_mac()
        logging.info("MACspoofStatic Plugin loaded")

    def on_unload(self):
        logging.info("MACspoofStatic Plugin unloaded")