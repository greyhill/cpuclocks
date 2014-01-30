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

pl.plot(years, speeds, 'o', alpha=.8, markeredgewidth=0, label='Intel CPUs')
pl.ylabel('Clock Speed [Hz]')
pl.xlabel('Year')
pl.axis([None, None, -50, None])
pl.title('Intel CPU Clock Speeds')
pl.show()
pl.savefig('intel_clock_speeds.pdf')

