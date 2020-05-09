from mongoengine import *
from database.schema_DB import *
import json
import names
import random
import namegenerator
import datetime
from faker  import Faker 

"""
    The purpose of this file is to auto generate mock data for the database
"""
fake = Faker() 

infrastructure = ["Streets or Highway", "Bridges", "Airports", "Water Supply", "Waste Water Management",
    "Power Generation & Transmission", "Telecommunications" , "Housing", "Building", "Ports",
    "Public Transportation"]
damage = [ "Earthquake", "Hurricane", "Tsunami", "Flooding", "Landslide", "Fire/smoke", 
    "Extreme Precipitation", "Water Damage", "Wind Damage", "Tornado"]
tags = infrastructure + damage

for i in infrastructure:
    Infrastructure(infrastructureType = i).save()

for i in damage:
    Damage(damageType = i).save()

for i in tags:
    Tag(tagItem = i).save()

with open('./database/cityPR.json') as f:
    data = json.loads(f.read())
    for cities in data['city_PR']:
        city = CityPR(city= cities['city'], latitude=cities['latitude'], longitude=cities['longitude'])
        city.save()

index = 0
for index in range(0,100):
    #mock data for creating collaborators
    fn = names.get_first_name()
    ln = names.get_last_name()
    emailc = fn.lower() + '.' + ln.lower() + "@upr.edu"
    print(emailc)
    collab1 = Collaborator(first_name = fn, 
    last_name = ln, 
    approved = random.choice([True, False]),
    banned = random.choice([True, False]),
    email = emailc)
    collab1.save()
   

    #make fake text
    my_word_list = [
    'Fire','The','Date',
    'City','Building','Water',
    'Rain','Shake','Earthquake',
    'Energy','Power','Pipes','Closed','Hurricane', 'Flood', 'wow'
    'Damage','Infrastructure', 'PR', 'Island', 'What', 'is', 'comes' ]

    #random date
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2020, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    dates = []
    for x in range(100):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        dates.append(str(random_date))

    #creates doc
    facultyITEM = ['ICOM', 'CIIC', 'INCI', 'INSO', 'INQU', 'INEL', 'MATE', 'QUIM', 'ADEM', 'PSIC']
    roles = ['Mayor', 'President', 'CEO','Owner','Resident','Engineer','Doctor']
    get_collab = Collaborator.objects.get(email= emailc)
    authorDoc = Author(author_FN = get_collab.first_name, author_LN = get_collab.last_name, 
    author_email = get_collab.email, author_faculty = random.choice(facultyITEM))

    actorDoc = Actor(actor_FN = names.get_first_name(), actor_LN = names.get_last_name(), 
    role = random.choice(roles))

    start = random.choice(dates)
    end = random.choice(dates)
    while(start > end):
        end = random.choice(dates)
    
    timelineDoc = Timeline(event = fake.sentence(ext_word_list=my_word_list), 
    eventStartDate = start, eventEndDate = end)

    titles=['Introduction', 'Body', 'Analysis', 'Conclusion', 'Executive Summary', 'Discussion']
    sectionDoc = Section(secTitle = random.choice(titles), 
    content = fake.sentence(ext_word_list=my_word_list))
    languageDoc = ['English', 'Spanish']

    ad = ["Coamo, PR", "Arecibo, PR", "Santa Isabel, PR", "Camuy, PR", "Salinas, PR", "San Juan, PR", "Mayagüez, PR", "Carolina, PR", "Aguas Buenas, PR", "Isabela, PR", "Quebradillas, PR", "Moca, PR", "Añasco, PR", "Yabucoa, PR", "Caguas, PR", "Lares, PR", "Humacao, PR", "Gurabo, PR", "Vieques, PR", "Maricao, PR", "Patillas, PR", "Arroyo, PR", "Las Piedras, PR", "Cidra, PR", "Maunabo, PR", "Fajardo, PR", "Ceiba, PR", "Juncos, PR", "Orocovis, PR", "Utuado, PR", "Jayuya, PR", "Ciales, PR", "Corozal, PR", "Aibonito, PR", "Sabana Grande, PR", "Guánica, PR", "Cayey, PR", "Vega Baja, PR"]
    j = random.choice(ad)
    l = random.choice(ad)
    print('j: ', j, " l: ", l)
    citypr = CityPR.objects.get(city = j)
    citypr1 = CityPR.objects.get(city = l)
    loc = Location(address= citypr.city, latitude= citypr.latitude, longitude=citypr.longitude)
    loc1 = Location(address= citypr1.city, latitude= citypr1.latitude, longitude=citypr1.longitude)
    inc = random.choice(dates)
    created = random.choice(dates)
    mod = random.choice(dates)
    while(inc > created):
        created = random.choice(dates)
    
    while(created > mod):
        mod = random.choice(dates)
    
    doc = DocumentCase(creatoriD = str(get_collab.id), title = ("The Great " + namegenerator.gen()), location=[loc,loc1], 
    description = fake.sentence(ext_word_list=my_word_list), published=random.choice([True, False]),
    incidentDate = inc, 
    creationDate= created,
    lastModificationDate= mod,
    tagsDoc=[random.choice(tags),random.choice(tags)], 
    infrasDocList= [random.choice(infrastructure), random.choice(infrastructure)],
    damageDocList= [random.choice(damage), random.choice(damage)],
    author = [authorDoc], actor = [actorDoc],section = [sectionDoc],timeline = [timelineDoc], language=random.choice(languageDoc))
    doc.save()
    doc = DocumentCase.objects.get(creatoriD=str(get_collab.id))


admin1 = Admin(username="yomar.ruiz", password='$2y$12$F8JpE/vVYHW5CGHerUfy3er15s7ApqT7ziRkc9lTGpnVuw9X8jZ4W') #Password0
admin1.save()
admin2 = Admin(username="roberto.guzman", password= '$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin2.save()
admin3 = Admin(username="alejandro.vasquez", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin3.save()
admin4 = Admin(username="jainel.torres", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin4.save()
admin5 = Admin(username="alberto.canela", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
admin5.save()
