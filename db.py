
import csv
from os import listdir



# Constants

DATA_FOLDER_PATH = "data/"

CSV_EXTENSION = "txt"

DATE_KEY  	 = "Date"

OPEN_KEY  	 = "Open"

HIGH_KEY     = "High"

LOW_KEY   	 = "Low"

CLOSE_KEY    = "Close"

VOLUME_KEY   = "Volume"

OPEN_INT_KEY = "OpenInt"



# CSV

def load_csv(path):
	array = []
	with open(path, 'r') as csvfile:
		spamreader = csv.DictReader(csvfile)
		for dictionary in spamreader:
			array.append(dictionary)
	return array


def file_name_from_path(path):
	path_array = path.split("/")
	return last(path_array)


def file_extension_from_path(path):
	file_name = file_name_from_path(path)
	name = file_name.split(".")
	return last(name)


def folder_content(path, extensions = []):
	content = []
	for file in listdir(path):
		extension = file_extension_from_path(file)
		if is_empty(extensions) or extension in extensions:
			content.append(file)
	content.sort()
	return content


def last(array):
	return array[len(array) - 1]


def is_empty(array):
	return len(array) == 0


def is_elements(array):
	return is_empty(array) is False



# Load

def load(folder = DATA_FOLDER_PATH):
	csv_array = []
	for file_name in folder_content(folder, [CSV_EXTENSION]):
		path = folder + "/" + file_name
		csv = load_csv(path)
		csv_array.append(csv)
	return csv_array