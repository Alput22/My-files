#%%
import json

with open(r'C:\Users\hp\Desktop\Mada\Homework\tweety.json') as f:
    twitty = json.loads(f.read())
for i in twitty['tweets']:
    print(i)
adder = input('What do you want to tweet? ')
username = input('Your username? ')
twitty['tweets'].append({'text':adder, 'name':username})
with open(r'C:\Users\hp\Desktop\Mada\Homework\tweety.json','w') as f:
    f.write(json.dumps(twitty, indent = 4))