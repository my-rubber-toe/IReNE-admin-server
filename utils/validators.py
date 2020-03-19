from bson import ObjectId

class ObjectID:

    def is_valid(self, object_id):
        return ObjectId.is_valid(object_id)
