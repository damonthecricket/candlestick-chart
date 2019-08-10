
import csv



def load(path):
	c = []
	with open(path, 'r') as csvfile:
		spamreader = csv.DictReader(csvfile)
		for dictionary in spamreader:
			c.append(dictionary)
	return c