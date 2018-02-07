from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('send_node','/send/node')
    config.add_route('send_reply','/send/reply')
    config.add_route('show_history','/show/history')
    config.add_route('rcv_send','/rcv/send')
   # config.add_route('type2','/see')
    config.scan('.views')
    return config.make_wsgi_app()