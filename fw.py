cat .config/hexchat/addons/fw.py
import subprocess
#subprocess.run('/usr/bin/ssh -T -i ~/.ssh/apu_fwknop_id_rsa root@apu &', shell = True)
subprocess.run('/usr/bin/fwknop -n bom', shell = True)
