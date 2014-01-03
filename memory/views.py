from pyramid.view import view_config
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pprint import pprint
import logging
import random

@view_config(route_name='home', renderer='templates/memory_home.pt')
def home_view(request):
    session = request.session
    if 'grid' in session:
       del session['grid']

    return playing_view(request)     


@view_config(route_name='playing', renderer='templates/memory_home.pt')
def playing_view(request):
       
    session = request.session
    if 'grid' in session:
            grid = session['grid']
            random.shuffle(grid)
            session['grid'] = grid
    else:
            originals = random.sample(range(111), 16)
            session['grid'] = originals

    grid = session['grid']
    return {'project': 'memory','grid': grid}
