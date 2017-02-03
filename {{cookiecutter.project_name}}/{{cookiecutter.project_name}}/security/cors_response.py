def add_cors_headers(event):
    """Function to add CORS headers to work with JS libraries."""
    event.response.headerlist.extend((
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'),
        ('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, '
                                         'Origin, Authorization, Accept, '
                                         'Client-Security-Token, Accept-Encoding'),
        ('Access-Control-Max-Age', '3600'),
        ('Access-Control-Allow-Credentials', 'true')
    ))
