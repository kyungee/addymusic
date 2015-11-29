import json

from apiclient.discovery import build

from astrid import Astrid
from astrid.http import response


YOUTUBE = build('youtube', 'v3', developerKey="AIzaSyCWumvIWyysRd5VsKCrcdF2Z5Fak3oV9fU")

app = Astrid()


@app.route('/api/search/{name}')
def api_search(request):
    result = {'status': 'success', 'data': None}
    query = request.match_info['name']

    result['data'] = YOUTUBE.search().list(
        q=query, part="id,snippet", maxResults=9
    ).execute()['items']

    return response(json.dumps(result))


app.run()
