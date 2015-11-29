import json
import os.path

from apiclient.discovery import build

from astrid import Astrid
from astrid.http import response, render


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES = os.path.join(BASE_DIR, 'templates')

YOUTUBE = build('youtube', 'v3', developerKey="AIzaSyCWumvIWyysRd5VsKCrcdF2Z5Fak3oV9fU")

app = Astrid(template_path=TEMPLATES)

app.app.router.add_static('/css/', os.path.join(STATIC_DIR, 'css'))
app.app.router.add_static('/js/', os.path.join(STATIC_DIR, 'js'))
#app.app.router.add_static('/img/', os.path.join(STATIC_DIR, 'img'))


@app.route('/')
def index(request):
    return render('index.html')


@app.route('/api/search/{name}')
def api_search(request):
    result = {'status': 'success', 'data': None}
    query = request.match_info['name']

    result['data'] = YOUTUBE.search().list(
        q=query, part="id,snippet", maxResults=9
    ).execute()['items']

    return response(json.dumps(result), content_type='application/json; charset=utf-8')


app.run()
