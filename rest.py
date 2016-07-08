'''
Building a smiple webserver
with some REST interfaces
'''
from notes import itty
import time, os, json, subprocess
import docfinder

@itty.get('/')
def welcome(request):
    return 'Hello World!'

@itty.get('/time')
def show_time(request):
    return time.ctime()

@itty.get('/upper')
def to_upper(request):
    phrase = request.GET.get('phrase', 'Missing')
    return phrase.upper()

@itty.get('/notes')
def show_notes(request):
    filenames = os.listdir('notes')
    text = json.dumps(filenames, indent=2)
    return itty.Response(text, content_type='application/json')

@itty.get('/search')
def pepsearch(request):
    keywords = request.GET.get('q', '').split(',')
    uris = docfinder.search(*keywords)
    text = json.dumps(uris, indent=2)
    return itty.Response(text, content_type='application/json')

@itty.get('/shell')
def shell(request):
    argv = request.GET.get('cmd', '').split()
    return subprocess.check_output(argv)


    
if __name__ == '__main__':
    itty.run_itty()
