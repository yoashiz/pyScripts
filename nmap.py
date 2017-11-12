import os, json


def get_host_recon(options, ip):
    command = "nmap " + options + " " + ip + " -oX - scanme.nmap.org"
    process = os.popen(command)
    results = process.read()
    return results


print(get_host_recon('-o', 'ip'))
