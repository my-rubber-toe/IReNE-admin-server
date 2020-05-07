from database.schema_DB import *

creation = [
    {
    'creatoriD': "5ea65196542fd4f6895b8224", 
    'title': "Damage to roads cause by earthquake in Yauco", 
    'language': "English", 
    'location': [], 
    'description': "this is a test", 
    'published': True, 
    'incidentDate': "2020-02-15", 
    'creationDate': "2000-04-26", 
    'lastModificationDate': "2020-04-26", 
    'tagsDoc': [], 
    'infrasDocList': ["infrastructure1", "infrastructure2", "infrastructure3"], 
    'damageDocList': [], 
    'author': [], 
    'actor': [], 
    'section': [], 
    'timeline': []
    },
    {
    'creatoriD': "5ea651bd3cdecc0f0b1e77ec", 
    'title': "Damage to Housing cause by earthquake in Yauco", 
    'language': "English", 
    'location': [], 
    'description': "this is a test", 
    'published': True, 
    'incidentDate': "2020-01-15", 
    'creationDate': "2000-04-03", 
    'lastModificationDate': "2020-02-26", 
    'tagsDoc': [], 
    'infrasDocList': ["infrastrucutre1", "infrastructure2", "infrastructure3"], 
    'damageDocList': [], 
    'author': [], 
    'actor': [], 
    'section': [], 
    'timeline': []
    },

    {
    'creatoriD': "5ea651da6a1115b76cd8d6a8", 
    'title': "Public Infrastructure Damage Caused by Hurricane Maria", 
    'language': "English", 
    'location': [], 
    'description': "Test data for Public Infrastructure Damage Caused by Hurricane Maria ", 
    'published': True, 
    'incidentDate': "2017-09-21", 
    'creationDate': "2000-04-26", 
    'lastModificationDate': "2020-04-26", 
    'tagsDoc': [], 
    'infrasDocList': ["infrastrucutre1", "infrastructure2", "infrastructure3"], 
    'damageDocList': [], 
    'author': [], 
    'actor': [], 
    'section': [], 
    'timeline': []
    }

]

actor = [
    {
        "new":ActorEmbedded(actor=
            [
                Actor(**{
                "actor_FN": "Dulcinea",
                "actor_LN": "Del Toboso",
                "role": "Advisor"
            }),
        Actor(**{
            "actor_FN": "Sancho",
            "actor_LN": "Panza",
            "role": "Advisor"
        })]),
        "old":ActorEmbedded(actor = [
        Actor(**{
            "actor_FN": "Don",
            "actor_LN": "Quijote",
            "role": "Advisor"
        })])
    },
    {
        "new":ActorEmbedded(actor = [
        Actor(**{
            "actor_FN": "Sancho",
            "actor_LN": "Panza",
            "role": "Advisor"
        })]),
        "old":[
        ]
    },
    {
        "new":ActorEmbedded(actor = [
         Actor(**{
            "actor_FN": "Dulcinea",
            "actor_LN": "Del Toboso",
            "role": "Advisor"
        })],
        "old":[
            {
                "actor_FN": "Sancho",
                "actor_LN": "Panza",
                "role": "Advisor"
            },
        {
            "actor_FN": "Don",
            "actor_LN": "Quijote",
            "role": "Advisor"
        }]
    }
]

check = FieldsEmbbeded(**actor[0])
author =[
    {
        "new":
        [{
            "author_FN": "Sancho",
            "author_LN": "Panza",
            "author_email": "Sancho@Panza.com",
            "author_faculty": "INEL"
        },
        {
            "author_FN": "Don",
            "author_LN": "Quijote",
            "author_email": "Don@Quijote.com",
            "author_faculty": "INEL"
        }
    ],
        "old":
        []
    },
    {
        "new":
        [{
            "author_FN": "Sancho",
            "author_LN": "Panza",
            "author_email": "Sancho@Panza.com",
            "author_faculty": "INEL"
        }],
        "old":
        [{
            "author_FN": "Dulcinea",
            "author_LN": "Del Toboso",
            "author_email": "Dulcinea@email.com",
            "author_faculty": "CIIC"
        }]
    },
    {
        "new":
        [],
        "old":
        [{
            "author_FN": "Don",
            "author_LN": "Quijote",
            "author_email": "Don@Quijote.com",
            "author_faculty": "INEL"
        },
        {
            "author_FN": "Dulcinea",
            "author_LN": "Del Toboso",
            "author_email": "Dulcinea@email.com",
            "author_faculty": "CIIC"
        }]
    }
]

incident = [
    {
        "new": "2013-07-21",
        "old": "2012-02-01"
    },

    {
        "new": "2013-04-09",
        "old": "2012-02-01"
    },

    {
        "new": "2011-12-01",
        "old": "2009-03-01"
    }
]

tag = [
    {
        "new": ["tag1", "tag2", "tag3", "tag4"],
        "old": []
    },

    {
        "new": ["tag5", "tag6", "tag7", "tag8"],
        "old": ["tag1", "tag2", "tag3", "tag4"]
    },

    {
        "new": [],
        "old": ["tag1", "tag2", "tag3", "tag4"]
    }
]

location = [
    {
        "new": ["location1", "location2", "location3", "location4"],
        "old": []
    },

    {
        "new": ["location5", "location7", "location8", "location9"],
        "old": ["location1", "location2", "location3", "location4"]
    },

    {
        "new": [],
        "old": ["location1", "location2", "location3", "location4"]
    }
]

damage = [
    {
        "new": ["damage1", "damage2", "damage3", "damage4"],
        "old": []
    },

    {
        "new": ["damage5", "damage6", "damage7", "damage8"],
        "old": ["damage1", "damage2", "damage3", "damage4"]
    },

    {
        "new": ["damage7"],
        "old": ["damage1", "damage2", "damage3", "damage4"]
    }
]

infrastructure = [
    {
        "new": ["type1", "type2", "type3", "type4"],
        "old": []
    },

    {
        "new": ["infra2", "infra3", "infra4", "infra5"],
        "old": ["type1", "type2", "type3", "type4"]
    },

    {
        "new": ["infra9"],
        "old": ["infra21", "infra31", "infra41", "infra51"]
    }
]


section = [
    {
        "new": {"secTitle": "Section 2", "content": "<p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore assumenda expedita ducimus nemo officiis cum nam recusandae, est omnis similique aliquam, quaerat aperiam tempore, eligendi nulla architecto hic minima labore?</p>"}, 
        "old": {}
    },

    {
        "new": {"secTitle": "Section 3", "content": "<p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore assumenda expedita ducimus nemo officiis cum nam recusandae, est omnis similique aliquam, quaerat aperiam tempore, eligendi nulla architecto hic minima labore?</p>"},
        "old": {"secTitle": "Section 2", "content": "<p> This is an old description of a senction content for test...</p>"}
    
    },

    {
        "new": {},
        "old": {"secTitle": "Section 3", "content": "<p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore assumenda expedita ducimus nemo officiis cum nam recusandae, est omnis similique aliquam, quaerat aperiam tempore, eligendi nulla architecto hic minima labore? </p>"}
    }
]

timeline = [
    {
        "new": [
            {"event": "New timeline event1", "eventEndDate": "2019-09-29", "eventStartDate": "2017-02-13"}, 
            {"event": "New timeline event2", "eventEndDate": "2019-09-29", "eventStartDate": "2017-02-13"}
        ], 
        "old": []
    },

    {
        "new": [
            {"event": "New timeline event3", "eventEndDate": "2017-09-29", "eventStartDate": "2015-02-13"}
        ], 
        "old": [
            {"event": "Old timeline event1", "eventEndDate": "2015-09-29", "eventStartDate": "2013-02-13"},
            {"event": "Old Timeline event2", "eventEndDate": "2015-09-29", "eventStartDate": "2013-02-13"}
        ]
    },

    {
        "new": [], 
        "old": [
            {"event": "I am the old event description1", "eventEndDate": "2017-09-29", "eventStartDate": "2015-02-13"}, 
            {"event": "I am the old event description2", "eventEndDate": "2017-09-29", "eventStartDate": "2015-02-13"}
        ]
    }
]

title = [
    {
        "new": 'Damage to roads cause by earthquake in Yauco',
        "old": 'Title of document: This is a test'
    },
    {
        "new": 'Damage to Housing cause by earthquake in Yauco',
        "old": 'This is a title: Hello World!'
    },
    {
        "new": 'Public Infrastructure Damage Caused by Hurricane Maria',
        "old": 'This is a document title'
    }
]

description = [
    {
        "new": 'New description of document',
        "old": 'Old description of document'
    },
    {
        "new": 'New description of document for test',
        "old": ''
    },
    {
        "new": 'Test New description of document',
        "old": 'Test Old description of document'
    }
]

revisionsTest = [
    {
        "revision_date": "2000-04-26",
        "revision_type": "Creation",
        "field_changed": creation[0]
    },
    {
        "revision_date": "2000-04-03",
        "revision_type": "Creation",
        "field_changed": creation[1]
    },
    {
        "revision_date": "2000-04-26",
        "revision_type": "Creation",
        "field_changed": creation[2]
    },

#descriptions
    {
        "revision_date": "2002-04-28",
        "revision_type": "Description",
        "field_changed": description[0]
    },
    {
        "revision_date": "2009-04-30",
        "revision_type": "Description",
        "field_changed": description[1]
    },
    {
        "revision_date": "2010-05-01",
        "revision_type": "Description",
        "field_changed": description[2]
    },

#titles
    {
        "revision_date": "2002-04-30",
        "revision_type": "Title",
        "field_changed": title[0]
    },
    {
        "revision_date": "2009-05-02",
        "revision_type": "Title",
        "field_changed": title[1]
    },
    {
        "revision_date": "2010-05-03",
        "revision_type": "Title",
        "field_changed": title[2]
    },

#timelines
    {
        "revision_date": "2002-04-30",
        "revision_type": "Timeline",
        "field_changed": timeline[0]
    },
    {
        "revision_date": "2009-05-02",
        "revision_type": "Timeline",
        "field_changed": timeline[1]
    },
    {
        "revision_date": "2010-05-03",
        "revision_type": "Timeline",
        "field_changed": timeline[2]
    },

#Sections
    {
        "revision_date": "2002-05-30",
        "revision_type": "Section",
        "field_changed": section[0]
    },
    {
        "revision_date": "2009-06-02",
        "revision_type": "Section",
        "field_changed": section[1]
    },
    {
        "revision_date": "2010-06-03",
        "revision_type": "Section",
        "field_changed": section[2]
    },

#Infrastructure
    {
        "revision_date": "2002-06-30",
        "revision_type": "Infrastructure",
        "field_changed": infrastructure[0]
    },
    {
        "revision_date": "2009-07-02",
        "revision_type": "Infrastructure",
        "field_changed": infrastructure[1]
    },
    {
        "revision_date": "2010-07-03",
        "revision_type": "Infrastructure",
        "field_changed": infrastructure[2]
    },

#Damage
    {
        "revision_date": "2002-06-30",
        "revision_type": "Damage",
        "field_changed": damage[0]
    },
    {
        "revision_date": "2009-07-02",
        "revision_type": "Damage",
        "field_changed": damage[1]
    },
    {
        "revision_date": "2010-07-03",
        "revision_type": "Damage",
        "field_changed": damage[2]
    },

#Location
    {
        "revision_date": "2002-07-30",
        "revision_type": "Location",
        "field_changed": location[0]
    },
    {
        "revision_date": "2009-08-02",
        "revision_type": "Location",
        "field_changed": location[1]
    },
    {
        "revision_date": "2010-09-03",
        "revision_type": "Location",
        "field_changed": location[2]
    },

#Tag
    {
        "revision_date": "2002-07-30",
        "revision_type": "Tag",
        "field_changed": tag[0]
    },
    {
        "revision_date": "2009-08-02",
        "revision_type": "Tag",
        "field_changed": tag[1]
    },
    {
        "revision_date": "2010-09-03",
        "revision_type": "Tag",
        "field_changed": tag[2]
    },

#Incident
    {
        "revision_date": "2002-07-30",
        "revision_type": "Incident Date",
        "field_changed": incident[0]
    },
    {
        "revision_date": "2009-08-02",
        "revision_type": "Incident Date",
        "field_changed": incident[1]
    },
    {
        "revision_date": "2010-09-03",
        "revision_type": "Incident Date",
        "field_changed": incident[2]
    },

#Author
    {
        "revision_date": "2002-08-20",
        "revision_type": "Author",
        "field_changed": author[0]
    },
    {
        "revision_date": "2009-09-12",
        "revision_type": "Author",
        "field_changed": author[1]
    },
    {
        "revision_date": "2010-10-23",
        "revision_type": "Author",
        "field_changed": author[2]
    },

#Actor
    {
        "revision_date": "2002-09-30",
        "revision_type": "Actor",
        "field_changed": actor[0]
    },
    {
        "revision_date": "2009-10-17",
        "revision_type": "Actor",
        "field_changed": actor[1]
    },
    {
        "revision_date": "2010-11-27",
        "revision_type": "Actor",
        "field_changed": actor[2]
    }
]


fakeHist = [
    {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2000-04-26",
        "revision_number": "0",
        "revision_type": "Creation",
        "field_changed": creation[0]
    },
    #     {
    #     "creatorId": "5ea65196542fd4f6895b8224",
    #     "docId": "5ea6518a9c9a794cd0243d39",
    #     "creator_name": "Yomar Ruiz",
    #     "creator_email": "yomar.ruiz@upr.edu",
    #     "document_title": "This is some random title",
    #     "revision_date": "2000-04-03",
    #     "revision_type": "Creation",
    #     "field_changed": creation[1]
    # },
    #     {
    #     "creatorId": "5ea65196542fd4f6895b8224",
    #     "docId": "5ea6518a9c9a794cd0243d39",
    #     "creator_name": "Yomar Ruiz",
    #     "creator_email": "yomar.ruiz@upr.edu",
    #     "document_title": "This is some random title",
    #     "revision_date": "2000-04-26",
    #     "revision_type": "Creation",
    #     "field_changed": creation[2]
    # },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-04-28",
        "revision_number": "1",
        "revision_type": "Description",
        "field_changed": description[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-04-30",
        "revision_number": "2",
        "revision_type": "Description",
        "field_changed": description[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-05-01",
        "revision_number": "3",
        "revision_type": "Description",
        "field_changed": description[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-04-30",
        "revision_number": "4",
        "revision_type": "Title",
        "field_changed": title[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-05-02",
        "revision_number": "5",
        "revision_type": "Title",
        "field_changed": title[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-05-03",
        "revision_number": "6",
        "revision_type": "Title",
        "field_changed": title[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-04-30",
        "revision_number": "7",
        "revision_type": "Timeline",
        "field_changed": timeline[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-05-02",
        "revision_number": "8",
        "revision_type": "Timeline",
        "field_changed": timeline[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-05-03",
        "revision_number": "9",
        "revision_type": "Timeline",
        "field_changed": timeline[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-05-30",
        "revision_number": "10",
        "revision_type": "Section",
        "field_changed": section[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-06-02",
        "revision_number": "11",
        "revision_type": "Section",
        "field_changed": section[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-06-03",
        "revision_number": "12",
        "revision_type": "Section",
        "field_changed": section[2]
    },
    {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-06-30",
        "revision_number": "13",
        "revision_type": "Infrastructure",
        "field_changed": infrastructure[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-07-02",
        "revision_number": "14",
        "revision_type": "Infrastructure",
        "field_changed": infrastructure[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-07-03",
        "revision_number": "15",
        "revision_type": "Infrastructure",
        "field_changed": infrastructure[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-06-30",
        "revision_number": "16",
        "revision_type": "Damage",
        "field_changed": damage[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-07-02",
        "revision_number": "17",
        "revision_type": "Damage",
        "field_changed": damage[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-07-03",
        "revision_number": "18",
        "revision_type": "Damage",
        "field_changed": damage[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-07-30",
        "revision_number": "19",
        "revision_type": "Location",
        "field_changed": location[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-08-02",
        "revision_number": "20",
        "revision_type": "Location",
        "field_changed": location[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-09-03",
        "revision_number": "21",
        "revision_type": "Location",
        "field_changed": location[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-07-30",
        "revision_number": "22",
        "revision_type": "Tag",
        "field_changed": tag[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-08-02",
        "revision_number": "23",
        "revision_type": "Tag",
        "field_changed": tag[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-09-03",
        "revision_number": "24",
        "revision_type": "Tag",
        "field_changed": tag[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-07-30",
        "revision_number": "23",
        "revision_type": "Incident Date",
        "field_changed": incident[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-08-02",
        "revision_number": "26",
        "revision_type": "Incident Date",
        "field_changed": incident[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-09-03",
        "revision_number": "27",
        "revision_type": "Incident Date",
        "field_changed": incident[2]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-08-20",
        "revision_number": "28",
        "revision_type": "Author",
        "field_changed": author[0]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-09-12",
        "revision_number": "29",
        "revision_type": "Author",
        "field_changed": author[1]
    },
        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-10-23",
        "revision_number": "30",
        "revision_type": "Author",
        "field_changed": author[2]
    },

        {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2002-09-30",
        "revision_number": "31",
        "revision_type": "Actor",
        "field_changed": actor[0]
    },
            {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2009-10-17",
        "revision_number": "32",
        "revision_type": "Actor",
        "field_changed": actor[1]
    },
            {
        "creatorId": "5ea65196542fd4f6895b8224",
        "docId": "5ea6518a9c9a794cd0243d39",
        "creator_name": "Yomar Ruiz",
        "creator_email": "yomar.ruiz@upr.edu",
        "document_title": "This is some random title",
        "revision_date": "2010-11-27",
        "revision_number": "33",
        "revision_type": "Actor",
        "field_changed": actor[2]
    },
]
# fakeHist = [
#     {
#         "creatorId": "5ea65196542fd4f6895b8224",
#         "docId": "5ea6518a9c9a794cd0243d39",
#         "revisions": [revisionsTest[0], revisionsTest[3], revisionsTest[6], revisionsTest[9], revisionsTest[12], revisionsTest[15], revisionsTest[18], revisionsTest[21], revisionsTest[24], revisionsTest[27], revisionsTest[30], revisionsTest[33]]
#     },
#     {
#         "creatorId": "5ea651bd3cdecc0f0b1e77ec",
#         "docId": "5ea651b31b1201f6a6c1b254",
#         "revisions": [revisionsTest[1], revisionsTest[4], revisionsTest[7], revisionsTest[10], revisionsTest[13], revisionsTest[16], revisionsTest[19], revisionsTest[22], revisionsTest[25], revisionsTest[28], revisionsTest[31], revisionsTest[34]]
#     },
#     {
#         "creatorId": "5ea651da6a1115b76cd8d6a8",
#         "docId": "5ea651d290dde5224efba7a9",
#         "revisions": [revisionsTest[2], revisionsTest[5], revisionsTest[8], revisionsTest[11], revisionsTest[14], revisionsTest[17], revisionsTest[20], revisionsTest[23], revisionsTest[26], revisionsTest[29], revisionsTest[32], revisionsTest[35]]
#     }
# ]



# fakeHist2 = [
#     {
#         "creatorId": "5ea65196542fd4f6895b8224",
#         "docId": "5ea6518a9c9a794cd0243d39",
#         "title": "this is some random title that i just invented for this test",
#         "name": "i am the slim shady",
#         "email": "this ismy@upr.edu email",
#         "revision_date": "2009-10-17",
#         "revision_type": "Actor",
#         "field_changed": actor[0]
#     },
#     {
#         "creatorId": "5ea651bd3cdecc0f0b1e77ec",
#         "docId": "5ea651b31b1201f6a6c1b254",
#         "revisions": [revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33], revisionsTest[33]]
#     },
#     {
#         "creatorId": "5ea651da6a1115b76cd8d6a8",
#         "docId": "5ea651d290dde5224efba7a9",
#         "revisions": [revisionsTest[2], revisionsTest[5], revisionsTest[8], revisionsTest[11], revisionsTest[14], revisionsTest[17], revisionsTest[20], revisionsTest[23], revisionsTest[26], revisionsTest[29], revisionsTest[32], revisionsTest[35]]
#     }
# ]
