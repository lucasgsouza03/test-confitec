from flask import Flask, jsonify, request
import redis
import aws_controller
import ginius_controller

app = Flask(__name__)

r = redis.Redis.from_url('redis://confitec.y6tzgf.ng.0001.use1.cache.amazonaws.com:6379')

@app.route('/')
def index():
    return "Página principal."
    

@app.route('/top_musicas')
def get_items():
    args = request.args
    artist = args['artist']
    cache = args['cache']
    try:
        r.exists(artist)
    except:
        top_musics = ginius_controller.get_by_artist(artist)
        r.hset(artist, top_musics)

        return jsonify(top_musics)


if __name__ == '__main__':
    app.run()
