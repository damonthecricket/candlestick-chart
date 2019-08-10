
import libs.pyutils.file as file
import libs.pyutils.array as array
import libs.pyutils.csv_util as csv
import libs.pyutils.folder as folder



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





# Load

def load(folder_path = DATA_FOLDER_PATH):
	csv_array = []
	for file_name in folder.content(folder_path, [CSV_EXTENSION]):
		path = folder_path + "/" + file_name
		c = csv.load(path)
		csv_array.append(c)
	return csv_array


