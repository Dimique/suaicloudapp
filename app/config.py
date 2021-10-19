import toml    

def init_config():
    try:
        global cfg
        cfg = toml.load('config.toml')
    except:
        print("Error: Could not find config file.")
        exit(1)
