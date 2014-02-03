import fileinput
import glob
import pylab as pl

years = []
speeds = []

for f in glob.glob('data/*.dat'):
    for line in fileinput.input(f):
        s = line.split(' ')
        if len(s) == 2 and s[0] != '#':
            years.append(float(s[0]))
            speeds.append(float(s[1]))

pl.semilogy(years, speeds, marker='o', color='blue', 
        linewidth=0, alpha=.8, label='Intel CPUs')
pl.ylabel('Clock Speed [Hz]')
pl.xlabel('Year')
pl.axis([1970, 2015, -50, None])
pl.title('Intel CPU Clock Speeds')
pl.show()
pl.savefig('intel_clock_speeds.pdf')

def parse_xistor_year_speed(path):
    years = []
    counts = []
    for line in fileinput.input(path):
        s = line.split('\t')
        if len(s) >= 3:
            count = ''.join(s[1].split(','))
            year = s[2]
            years.append(float(year))
            counts.append(float(count))
            if count <= 0:
                print s
    return years, counts

cpu_xistor = parse_xistor_year_speed('data/cpu_transistor.txt')
gpu_xistor = parse_xistor_year_speed('data/gpu_transistor.txt')

pl.figure()
pl.semilogy(*cpu_xistor, label='CPU', marker='o', alpha=.8, 
        color='blue', linewidth=0)
pl.semilogy(*gpu_xistor, label='GPU', marker='o', alpha=.8, 
        color='green', linewidth=0)
pl.axis([1970, 2015, -.1e9, None])
pl.xlabel('Year')
pl.ylabel('Transistor count')
pl.legend(loc='upper left')
pl.title('CPU and GPU Transistor Counts')
pl.show()
pl.savefig('transistor_count.pdf')

