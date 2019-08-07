
import utils.array as array



def name_from_path(path):
	path_array = path.split("/")
	return array.last(path_array)


def extension_from_path(path):
	file_name = name_from_path(path)
	name = file_name.split(".")
	return array.last(name)