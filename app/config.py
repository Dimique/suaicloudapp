import toml    

def init_config():
    global cfg
    cfg = toml.load('config.toml')
