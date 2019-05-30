from flask import request,jsonify
from flask_restplus import Resource



from ..util.dto import ServeFile

api = ServeFile.api
jsonbizarre=[
  {
    "id": 1,
    "name": "Honda",
    "price": 4500000,
    "image": "https://scontent.fabj4-1.fna.fbcdn.net/v/t1.0-9/46739343_2066468250098620_881393221182160896_o.jpg?_nc_cat=102&_nc_ht=scontent.fabj4-1.fna&oh=d85354dc4f991f7ee7a535ffdf3dfff4&oe=5D5FCF8F",
    "category": "voitures"
  },
  {
    "id": 2,
    "name": "BMW S1",
    "price": 60,
    "image": "https://scontent.fabj4-1.fna.fbcdn.net/v/t1.0-9/46694242_2066460326766079_7713705759753633792_o.jpg?_nc_cat=100&_nc_ht=scontent.fabj4-1.fna&oh=49402ba3f201af3281c49cc550b07e69&oe=5D9EC591",
    "category": "voitures"
  },
  {
    "id": 3,
    "name": "Ford EDGE",
    "price": 4000000,
    "image": "https://scontent.fabj4-1.fna.fbcdn.net/v/t1.0-9/46409849_2056278944450884_9194358205625401344_o.jpg?_nc_cat=103&_nc_ht=scontent.fabj4-1.fna&oh=aea2393433422f8ce6448515847fd425&oe=5D9EE86E",
    "category": "voitures"
  },
  {
    "id": 4,
    "name": "Docksides SEBAGO",
    "price": 45000,
    "image": "https://scontent.fabj4-1.fna.fbcdn.net/v/t1.0-9/10806411_736501506428641_8516444809081266765_n.jpg?_nc_cat=103&_nc_ht=scontent.fabj4-1.fna&oh=1e9f03a3bedbc0cdf82686d1ee32231e&oe=5D9CF610",
    "category": "chaussures"
  },
  {
    "id": 5,
    "name": "Absolut Mandrin",
    "price": 56000,
    "image": "https://scontent.fabj4-1.fna.fbcdn.net/v/t1.0-9/1958223_622102251201901_1975893865_n.jpg?_nc_cat=104&_nc_ht=scontent.fabj4-1.fna&oh=cdf0b6cfe18b6ed5a2e71096cfad092e&oe=5D60BC0F",
    "category": "Alcool"
  },
  {
    "id": 6,
    "name": "Wolswagen passat cc",
    "price": 3500000,
    "image": "https://scontent.fabj4-1.fna.fbcdn.net/v/t1.0-9/1966839_617600174985442_504530916_n.jpg?_nc_cat=102&_nc_ht=scontent.fabj4-1.fna&oh=bfc631ed7d9a90737c9953e056121233&oe=5D5FBF2C",
    "category": "voitures"
  },
  {
    "id": 7,
    "name": "Galaxy S10",
    "price": 310000,
    "image": "https://images.frandroid.com/wp-content/uploads/2019/04/samsung-galaxy-s10-2019-frandroid.png",
    "category": "telephones"
  },
  {
    "id": 8,
    "name": "Samsung A5",
    "price": 150000,
    "image": "https://images.frandroid.com/wp-content/uploads/2019/04/samsung-galaxy-a50-2019-frandroid-france-packshot-png.png",
    "category": "telephones"
  },
  {
    "id": 9,
    "name": "Iphone x",
    "price": 540000,
    "image": "https://s7.s-sfr.fr/mobile/uc/device/j901hrnu/iphonex-spgry-front-400x540.png?ts=1508512673807",
    "category": "telephones"
  }
]

@api.route('/')
class SendFiles(Resource):
    def get(self):
        return jsonify(jsonbizarre)
