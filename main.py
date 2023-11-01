from ota import OTAUpdater
import time
# new
firmware_url = "https://raw.githubusercontent.com/ShulcN/test_pi_ota/"
ota_updater = OTAUpdater("POCO M4 Pro", "123456789f", firmware_url, "main.py")
#def update_2(timer):
   # global ota_updater
   # ota_updater.download_and_install_update_if_available()
   # ota_updater.download_and_install_update_if_available()
#ota_updater.download_and_install_update_if_available()
while True:
    ota_updater.download_and_install_update_if_available()
    time.sleep(1)
#timer.init(freq=0.2, mode=Timer.PERIODIC, callback=update_2)
