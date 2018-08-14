from configparser import ConfigParser


def config_reader():
    cfg = ConfigParser()
    cfg.read('app.ini')
    return cfg


class Config:
    pass


'''#Config Usage
    
    config = config_reader()
    print(server_addr)
    server_addr = config.get('PORT', 'server_addr')
    print(server_addr)
'''
