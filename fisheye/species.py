class Species:
    def __init__(self, client, data):
        self.client = client
        self.id = data['SpecCode']
        self.genus = data['Genus']
        self.species = data['Species']
        self.danger = data['Dangerous']
        self.comments = data['Comments']
        self.fb_name = data['FBname']
        self.length = data['Length']
        self.image = data['image']
