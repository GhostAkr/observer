import os

objects_extensions = ['jpg', 'jpeg', 'png']

def getClasses(pair):
	result = []
	for annotation in pair['annotations']:
		if annotation['mask'] != None:
			result.append(annotation['mask'])
	return result

def getAnnotationsData(files_metadata):
	return None

def getAnnotations(object, all_annotations_files):
	object_label = object['name'].split('__label__')[1].replace('.jpg', '')
	return [{'mask': object_label}]