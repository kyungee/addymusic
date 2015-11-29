import json

from apiclient.discovery import build

from astrid import Astrid
from astrid.http import response


YOUTUBE = build('youtube', 'v3', developerKey="")

app = Astrid()


@app.route('/api/search/{name}')
def api_search(request):
    query = request.match_info['name']

    result = YOUTUBE.search().list(
        q=query,
        part="id,snippet",
        maxResults=9
    ).execute()['items']

    return response(json.dumps(result))


app.run()
