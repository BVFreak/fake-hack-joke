from faker import Faker
import time
import random
from time import sleep


def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left

    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)


hacking = True
while hacking:
    ex = Faker()
    ip = ex.ipv4()
    ip2 = ex.ipv6()
    print('Scanning potential weak security systems...')
    for i in range(101):
        progress(i)
        sleep(0.05)
    print('\nScan complete, neutral systems found')
    time.sleep(random.randint(0, 2))
    print('Gaining values...')
    for i in range(101):
        progress(i)
        sleep(0.05)
    print('Successfully implanted virus')
    time.sleep(random.randint(0, 2))
    print('Destroying files...')
    for i in range(101):
        progress(i)
        sleep(0.05)
    print('Running nuke.exe...')
    for i in range(101):
        progress(i)
        sleep(0.05)
    print('Successfully gained root access')
    time.sleep(random.randint(0, 2))
    print('Compiling data...')
    for i in range(101):
        progress(i)
        sleep(0.05)
    print('')
    print('IP hacked')
    print('  ipv4 address:- ', ip)
    print('  ipv6 address:- ', ip2)
    print('')
