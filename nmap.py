import os, json


def get_host_recon(options, ip):
    command = "nmap " + options + " " + ip + " -oX - scanme.nmap.org"
    process = os.popen(command)
    results = process.read()
    return results


# change ip to real ip address '127.0.0.1'
print(get_host_recon('-o', 'ip'))
