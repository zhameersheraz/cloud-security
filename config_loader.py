import yaml

class Config:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
    
    def get(self, *keys):
        value = self.config
        for key in keys:
            value = value.get(key)
            if value is None:
                return None
        return value