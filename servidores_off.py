#!/usr/bin/env python3

import os
import subprocess

# Define el directorio Vagrant y las máquinas virtuales
VagrantDir = "/home/frodo/clustermysql/"
vms = [
    'vm00-archaon',
    'vm01-valten',
    'vm02-tyrion',
    'vm03-malekith',
    'vm04-grimgor',
    'vm05-thorgrim',
    'vm06-orion',
    'vm07-kroqgar'
]

def stop_vms():
    for vm in vms:
        vm_dir = os.path.join(VagrantDir, vm)
        os.chdir(vm_dir)
        
        try:
            subprocess.run(["vagrant", "halt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"{vm} apagada ... OK")
        except subprocess.CalledProcessError as e:
            print(f"Error al apagar {vm}: {e.stderr.strip()}")

if __name__ == "__main__":
    stop_vms()
