gunicorn osmosis_music_api.wsgi:application -b :8000 --timeout 300 -w 1 -k gevent
