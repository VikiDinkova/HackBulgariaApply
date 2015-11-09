def dependencies_resolving(all_packages, key):
	print('Installing {0}'.format(key))
	if all_packages[key] == []:
		return
	line = 'In order to install {0}, we need '.format(key)
	for item in all_packages[key]:
		line += ' ' + item + ' '
	print(line)
	for value_key in all_packages[key]:
		dependencies_resolving(all_packages, value_key)
	return 
		

all_packages = {
				"backbone": ["jQuery", "underscore"],
				"jQuery": ["queryJ"],
				"underscore": ["lodash"],
				"queryJ": [],
				"lodash": []
}

dependencies = {
				"projectName": "Test0000",
				"dependencies": ["backbone"]
}

for package in dependencies['dependencies']:
	dependencies_resolving(all_packages, package)
print('All done!')