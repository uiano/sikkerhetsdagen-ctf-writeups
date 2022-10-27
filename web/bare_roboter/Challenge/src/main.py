from flask import Flask, request
app = Flask(__name__)

# https://developers.whatismybrowser.com/useragents/explore/software_type_specific/crawler/
allowed_agents = ['GoogleImageProxy', 'Googlebot', 'bingbot', 'Yahoo!', 'Baiduspider', 'MJ12bot', 'MegaIndex',
'Ahrefsbot', 'DotBot', 'Jobboersebot' ,'SemrushBot', 'deverlopers.google', 'YandexImages', 'msnbot', 'seoscanners',
'BingPreview', 'SEOkicks', 'BLEXBot', 'bingbot', 'CheckMarkNetwork', 'SeznamBot' ,'Mediapartners' ,'BUbiNG',
'BingPreview', 'Sogou', 'MSNbot', 'AdsBot', 'VoilaBot', 'adscanner', 'Google Favicon']

FLAG = b'UIACTF{following the path to robot glory}'.hex()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    for agent in allowed_agents:
        if agent in request.headers.get('User-Agent'):
            break
    else:
        return 'Bare &#129302; tillatt!'
    path = path.replace('/', '')
    if path == FLAG:
        return 'You found the promised land! HEX-soup for everyone!'
    if path == '':
        return f'Start your journy at {FLAG[0]}, remember to follow the path in sequence or the next robot greeting you won\' know where to send you next'
    # Find the next step in the path
    nidx = 0
    for a,b in zip(path, FLAG):
        if a != b:
            return 'Seems you took a wrong turn, you should go back to the previos place'
        nidx += 1
    return f'Keep following the path, next you should head to {FLAG[nidx]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


