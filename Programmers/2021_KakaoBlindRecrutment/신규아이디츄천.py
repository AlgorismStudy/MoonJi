import re

def solution(new_id):
    new_id = new_id.lower() 
    new_id = re.sub(r'[^a-zA-Z0-9-_.]', "", new_id)
    new_id = re.sub('\.+', '.', new_id)
    if new_id[0] == '.': new_id = new_id[1:]
    if new_id.endswith('.'): new_id = new_id[:-1]
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    if new_id.endswith('.'): new_id = new_id[:-1]
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id