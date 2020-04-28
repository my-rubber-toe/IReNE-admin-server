from mongoengine import *
from database.schema_DB import *
from datetime import datetime



collab1 = Collaborator(first_name="Jainel", last_name="Torres", email="jainel.torres1@upr.edu", approved=True)
collab1.save()
collab2 = Collaborator(first_name="Roberto", last_name="Guzman", email="roberto.guzman3@upr.edu", approved=True)
collab2.save()
collab3 = Collaborator(first_name="Alberto", last_name="Canela", email="alberto.canela@upr.edu")
collab3.save()
collab4 = Collaborator(first_name="Alejandro", last_name="Vasquez", email="alejandro.vasquez@upr.edu",approved=True, banned=True )
collab4.save()
collab5 = Collaborator(first_name="Yomar", last_name="Ruiz", email="yomar.ruiz@upr.edu")
collab5.save()

get_collab1 = Collaborator.objects.get(first_name= "Jainel")
authorDoc1 = Author(author_FN = get_collab1.first_name, author_LN = get_collab1.last_name, 
author_email = get_collab1.email, author_faculty="ICOM")
actorDoc1 = Actor(actor_FN = "Victoria", actor_LN = "Black", role = "Mayor")
timelineDoc1 = Timeline(event = "The rain has started", 
eventStartDate = "2017-09-17", eventEndDate = "2017-09-19")
sectionDoc1 = Section(secTitle = "Introduction", content = "It was raining a lot")
doc1 = DocumentCase(creatoriD = str(get_collab1.id), title = ("The Great Rain"), location=["Coamo, PR"], 
description = "It was a cold and stormy night...", published= True,
incidentDate = "2017-09-17", 
creationDate= "2018-03-20",
lastModificationDate= "2019-04-08",
tagsDoc=['Hurricane', 'Rain'], 
infrasDocList= ["Structure", "Water"],
damageDocList= ['Flooding'],
author = [authorDoc1], actor = [actorDoc1],section = [sectionDoc1],timeline = [timelineDoc1], language="English")
doc1.save()


# doc = DocumentCaseRevision(creatorId = str(collab1.id), docId = str(doc1.id))
# rev = Revision()
# rev.revType = 'Tags'
# rev.revDate = datetime.today().strftime('%Y-%m-%d')
# doc.revisions.append(rev)
# rev = Revision()
# rev.revType = 'Author'
# rev.revDate = datetime.today().strftime('%Y-%m-%d')
# doc.revisions.append(rev)
# rev = Revision()
# rev.revType = 'Incident Date'
# rev.revDate = datetime.today().strftime('%Y-%m-%d')
# doc.revisions.append(rev)
# rev = Revision()
# rev.revType = 'Actors'
# rev.revDate = datetime.today().strftime('%Y-%m-%d')
# doc.revisions.append(rev)
# doc.save()
# doc = DocumentCaseRevision(creatorId = str(collab2.id), docId = str(doc1.id))
# doc.save()
# doc = DocumentCaseRevision(creatorId = str(collab3.id), docId = str(doc1.id))
# doc.save()
# doc = DocumentCaseRevision(creatorId = str(collab4.id), docId = str(doc1.id))
# doc.save()

admin1 = Admin(username="yomar.ruiz", password='$2y$12$F8JpE/vVYHW5CGHerUfy3er15s7ApqT7ziRkc9lTGpnVuw9X8jZ4W') #Password0
admin1.save()
admin2 = Admin(username="Roberto.guzman", password= '$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin2.save()
admin3 = Admin(username="alejandro.vasquez", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin3.save()
admin4 = Admin(username="jainel.torres", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin4.save()
admin5 = Admin(username="alberto.canela", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin5.save()




tags = ['Hurricane', 'Rain', 'Earthquake', 'Fire', 'Burning', 'Flood', 'Power Outage']
for tag in tags:
    x = Tag(tagItem= tag)
    x.save()


damage = ['Flooding', 'Earthquake', 'Fire', 'Tsunamis', 'Hurricane']
for dam in damage:
    x = Damage(damageType= dam)
    x.save()


infrastructure = ['Transportation', 'Energy', 'Water', 'Security', 'Ports', 'Structure', 'Construction']
for infras in infrastructure:
    x = Infrastructure(infrastructureType= infras)
    x.save()
                                                                                                                                                                                                                                            
