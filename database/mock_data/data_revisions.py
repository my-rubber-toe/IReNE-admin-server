from mongoengine import *
from database.schema_DB import *
import json
import names
import random
import namegenerator
import datetime
from faker  import Faker 

fake = Faker()

# def get_random_date():
#     date = random.choice(random_dates)
#     time = datetime.datetime.today().strftime('%H:%M')
#     # hour24 = time.split(":")
#     # hour12 = []
#     # sufix = ""
#     # if(int(hour24[0]) >= 12):
#     #     sufix = "pm"
#     #     if (int(hour24[0]) !=12):
#     #         hour12.append(int(hour24[0])-12)
#     #     else:
#     #         hour12.append(12)
#     # else:
#     #     sufix = "am"
#     #     if(int(hour24[0]) !=0):
#     #         hour12.append(int(hour24[0]))
#     #     else:
#     #         hour12.append(12)
#     # hour12.append(int(hour24[1]))
#     return date + " "+ time

def build_doc_rev(revision_type):
    doc = DocumentCase.objects[random.randint(0, docSize-1)]
    collab = doc.creatoriD
    return DocumentCaseRevision(
        creatorId = collab.id,
        docId = doc.id,
        creator_name = collab.first_name +" "+collab.last_name,
        creator_email = collab.email,
        document_title = doc.title,
        revision_date = random.choice(random_dates),
        revision_number = DocumentCaseRevision.objects(creatorId = collab.id, docId =doc.id).count(),
        revision_type = revision_type)

random_dates = []
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 2, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
for x in range(5000):
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_dates.append(str(random_date))

docSize = DocumentCase.objects.count()

#___________________ACTORS_____________________________________________
roles = ['Advisor', 'Contributor', 'Data Manager', 'Investigator', 'Researcher', 'Principal Investigator']
actors = []
for i in range(0,100):
    actors.append(Actor(**{
                "actor_FN": names.get_first_name(),
                "actor_LN": names.get_last_name(),
                "role": random.choice(roles)
            }))


for i in range(0,100):
    rev = build_doc_rev('Actor')
    rev.field_changed = FieldsEmbedded(new = ActorEmbedded(actor = random.choices(actors, k = random.randint(0,5))),
                                        old = ActorEmbedded(actor = random.choices(actors, k = random.randint(0,5))))
    rev.save()


#___________________AUTHORS_____________________________________________
faculties = ['ICOM', 'CIIC', 'INCI', 'INSO', 'INQU', 'INEL', 'MATE', 'QUIM', 'ADEM', 'PSIC']
authors = []
for i in range(0,100):
    first_name =  names.get_first_name()
    last_name = names.get_last_name()
    authors.append(Author(**{'author_FN': first_name,
    'author_LN': last_name,
    'author_email': first_name + "." + last_name + "@upr.edu",
    'author_faculty': random.choice(faculties)}))

for i in range(0,100):
    rev = build_doc_rev('Author')
    rev.field_changed = FieldsEmbedded(new = AuthorEmbedded(author = random.choices(authors, k = random.randint(0,10))),
                                        old = AuthorEmbedded(author = random.choices(authors, k = random.randint(0,10))))
    rev.save()


#___________________TIMELINE_____________________________________________
events = ['Milestone 2', 'Milestone 1', 'Milestone 3', 'Milestone 4', 'Milestone 5', 'Milestone 6', 'Milestone 7', 'Milestone 8', 'Milestone 9', 'Milestone 10']

timelines = []
for i in range(0,100):
    date1 = random.choice(random_dates)
    date2 = random.choice(random_dates)
    if(date1 > date2):
        startDate = date2
        endDate = date1
    else:
        startDate = date1
        endDate = date2
    timelines.append(Timeline(event = random.choice(events), eventStartDate = startDate, eventEndDate = endDate))

tSize = len(timelines)
for i in range(0,100):
    rev = build_doc_rev('Timeline')
    time1 = []
    time2 = []
    for i in range(0,random.randint(0,5)):
        time1.append(timelines[random.randint(0, tSize-1)])
    for i in range(0,random.randint(0,5)):
         time2.append(timelines[random.randint(0, tSize-1)])

    rev.field_changed = FieldsEmbedded(new = TimelineEmbedded(timeline = time1),
                                        old = TimelineEmbedded(timeline = time2))
    rev.save()

#___________________LOCATIONS_____________________________________________
citySize = CityPR.objects.count()
for i in range(0,100):
    rev = build_doc_rev('Location')
    cities1 = []
    cities2 = []
    for i in range(0,random.randint(0,5)):
        city = CityPR.objects[random.randint(0, citySize-1)]
        cities1.append(Location(**{'address':city['city'], 'latitude': city['latitude'], 'longitude': city['longitude']}))
    for i in range(0,random.randint(0,5)):
        city = CityPR.objects[random.randint(0, citySize-1)]
        cities2.append(Location(**{'address':city['city'], 'latitude': city['latitude'], 'longitude': city['longitude']}))

    rev.field_changed = FieldsEmbedded(new = LocationEmbedded(location = cities1),
                                        old = LocationEmbedded(location = cities2))
    rev.save()

#___________________SECTIONS_____________________________________________
sectionsTitles = ['Section 1', 'Section 2', 'Section 3', 'Section 4', 'Section 5', 'Section 6', 'Section 7', 'Section 8', 'Section 9', 'Section 10']
sections = []
for i in range(0,100):
    content = "<p>"+fake.paragraph(10)+"</p>"
    secTitle = sectionsTitles[i%len(sectionsTitles)]
    sections.append(Section(**{'secTitle': secTitle,
    'content': content}))

for i in range(0,100):
    rev = build_doc_rev('Section')
    rev.field_changed = FieldsEmbedded(new = SectionEmbedded(section = random.choice(sections)),
                                        old = SectionEmbedded(section = random.choice(sections)))
    rev.save()


#___________________INCIDENT DATE_____________________________________________
incident_dates = []

start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 2, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
for x in range(100):
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    incident_dates.append(str(random_date))

for i in range(0,100):
    rev = build_doc_rev('Incident Date')
    rev.field_changed = FieldsEmbedded(new = IncidentEmbedded(incidentDate = random.choice(incident_dates)),
                                        old = IncidentEmbedded(incidentDate = random.choice(incident_dates)))
    rev.save()

#___________________INFRASTRUCTURE_____________________________________________
infrastructure = ["Streets or Highway", "Bridges", "Airports", "Water Supply", "Waste Water Management",
    "Power Generation & Transmission", "Telecommunications" , "Housing", "Building", "Ports",
    "Public Transportation"]

for i in range(0,100):
    rev = build_doc_rev('Infrastructure')
    rev.field_changed = FieldsEmbedded(new = InfrastructureEmbedded(infrasDocList = random.choices(infrastructure, k=random.randint(0,4))),
                                        old = InfrastructureEmbedded(infrasDocList = random.choices(infrastructure, k=random.randint(0,4))))
    rev.save()


#___________________DAMAGES_____________________________________________
damage = [ "Earthquake", "Hurricane", "Tsunami", "Flooding", "Landslide", "Fire/smoke", 
    "Extreme Precipitation", "Water Damage", "Wind Damage", "Tornado"]

for i in range(0,100):
    rev = build_doc_rev('Damage')
    rev.field_changed = FieldsEmbedded(new = DamageEmbedded(damageDocList = random.choices(damage, k=random.randint(0,4))),
                                        old = DamageEmbedded(damageDocList = random.choices(damage, k=random.randint(0,4))))
    rev.save()


#___________________TAGS_____________________________________________
tags = infrastructure + damage
for i in range(0,100):
    rev = build_doc_rev('Tag')
    rev.field_changed = FieldsEmbedded(new = TagEmbedded(tagsDoc = random.choices(tags, k=random.randint(0,4))),
                                        old = TagEmbedded(tagsDoc = random.choices(tags, k=random.randint(0,4))))
    rev.save()


#___________________DESCRIPTION_____________________________________________
for i in range(0,100):
    rev = build_doc_rev('Description')
    rev.field_changed = FieldsEmbedded(new = DescriptionEmbedded(description = fake.paragraph(5)),
                                        old = DescriptionEmbedded(description = fake.paragraph(5)))
    rev.save()


#___________________Title_____________________________________________
tags = infrastructure + damage
for i in range(0,100):
    rev = build_doc_rev('Title')
    rev.field_changed = FieldsEmbedded(new = TitleEmbedded(title = fake.sentence().replace(".","")),
                                        old = TitleEmbedded(title = fake.sentence().replace(".","")))
    rev.save()