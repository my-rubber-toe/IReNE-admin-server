from daos.dummy_data.tag import tags

class TagsDAO:
    tagList = []
    
    def __init__(self):
        self.tagList = tags

    def get_tags(self):
        return self.tagList
    
    def remove_tag(self, tagID):
        tag_temp = None
        for tag in self.tagList:
            if(tag.get('_id')==tagID):             
                tag_temp =  tag
        if(tag_temp is not None):
            self.tagList[:] = [tag for tag in self.tagList if tag.get('_id') != tagID ]
        return tag_temp