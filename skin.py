class Skin:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.app_id = kwargs['app_id']

    def __str__(self):
        return f'{self.name} {self.app_id}'
