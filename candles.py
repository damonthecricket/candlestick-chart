
import matplotlib.dates as mdates
import numpy as np
import urllib
import datetime as dt



def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter



# Load

def load(url):
	source_code = urllib.request.urlopen(url).read().decode()
	stock_data = []
	split_source = source_code.split('\n')
	for line in split_source[1:]:
		split_line = line.split(',')
		if len(split_line) == 7:
			if 'values' not in line and 'labels' not in line:
				stock_data.append(line)

    
	date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
															delimiter=',',
															unpack=True,
															converters={0: bytespdate2num('%Y-%m-%d')})

	x = 0
	y = len(date)
	ohlc = []

	while x < y:
		append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
		ohlc.append(append_me)
		x+=1

	return ohlc