from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

def main(global_config, **settings):

    # create sesson factory
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    config = Configurator(settings=settings, session_factory=session_factory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('playing','/playing')
    config.scan()
    return config.make_wsgi_app()
