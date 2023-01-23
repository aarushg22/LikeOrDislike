import mongoengine as me


class LocationData(me.Document):
    continent = me.StringField()
    country = me.StringField()
    state = me.StringField()
    city = me.StringField()

    likes = me.LongField()
    dislikes = me.LongField()
    last_updated = me.DateTimeField()

    def to_json(self):
        return {
            "continent": self.continent,
            "country": self.country,
            "state": self.state,
            "city": self.city,
            "likes": self.likes,
            "dislikes": self.dislikes,
            "last_updated": self.last_updated
        }
# @TODO: Think about separating out Location and it's relevant data

#
# class LocationData(me.Document):
#     like = me.LongField()
#     dislike = me.LongField()
#     location = me.EmbeddedDocumentField(Location)
#
#     def to_json(self):
#         return {
#             "likes": self.likes,
#             "dislikes": self.dislikes,
#             "location": self.location.to_json()
#         }
