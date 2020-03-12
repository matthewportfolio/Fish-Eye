from fisheye.client import Client

FishEye = Client(cache=True)
FishEye.start()

fish = FishEye.get_species(limit=1)
print(fish)