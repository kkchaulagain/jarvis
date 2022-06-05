# string = [{'action': 'change_directory', 'project': 'bookmundi'}] 
import json
string = [{'action': 'change_directory', 'project': 'bookmundi'}, {'action': 'change_branch', 'branch': 'uat'}, {'action': 'pull_latest_changes'}, {'action': 'deploy'}]
# //convert to json string

json_data =  json.dumps(string)

#  convert to list
print (json_data)
li = json.loads(json_data)
for doc in li:
    print(doc['action'] )