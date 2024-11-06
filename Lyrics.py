from time import sleep 
import time 
import sys

def lyrics():
    lines = [
        ("Sarangeuro", 0.2),
        ("Sarangeuro", 0.2),
        ("Naui jageun maeumdo", 0.23),
        ("Geu ane jageun padocheoreom", 0.2),
        ("Buseojigo millyeowaseon", 0.3),
        ("Nege noganaerigo", 0.3),
        ("Geujeseoya boineun naui yeongwon", 0.2),
    ]
    delays =[2, 2, 2, 2, 2, 2, 1]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end = '')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

lyrics()