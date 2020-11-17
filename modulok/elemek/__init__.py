import os

files = os.listdir('./modulok/elemek')
for file in files:
    if(file != '__init__.py' and file.endswith('.py')):
        exec('import modulok.elemek.{0} as {0}'.format(file[:-3])) 
