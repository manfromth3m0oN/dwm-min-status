import subprocess


while True:
    acpi = subprocess.Popen('acpi', stdout=subprocess.PIPE)
    bat = acpi.stdout.read()
    timestd = subprocess.Popen(['date', '+"%T"'], stdout=subprocess.PIPE)
    time = timestd.stdout.read()

    root = ' ' + bat.split()[3].decode('utf-8').strip(',') + " | " + time.decode('utf-8')[1:6] + ' '
    subprocess.run(['xsetroot', '-name', root])
