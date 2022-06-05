#  import data.json
#  convert into jsonle format

import json
import os


def convert(file_name):
    with open(file_name, 'r') as JSON_file:
        data = json.load(JSON_file)
        with open('data' + '.txt', 'w') as output:
            for item in data:
                item['completion'] = str(item['completion']) + '###'
                # dump 
                output.write(json.dumps
                (item))
                output.write('\n')
                # output.write(item['prompt'] + ':' + item['completion'] + '\n')
    # os.remove(file_name)
    print("Converted {} to {}.json".format(file_name, file_name))
# get current directory
currentDirection = os.getcwd()
jsonfile = currentDirection + '\\data.json'
convert(jsonfile)