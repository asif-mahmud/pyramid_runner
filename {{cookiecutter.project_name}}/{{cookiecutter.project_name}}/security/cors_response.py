def add_cors_headers(event):
    event.response.headerlist.extend((
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    ))