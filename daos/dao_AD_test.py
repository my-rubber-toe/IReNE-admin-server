from mongoengine import *
from schema_DB import *
from dao_AD import *
import datetime

#test get_login()
# ad = Admin(username="jaits13", password="djoendjoewn")
# ad.save()
# admin = Admin.objects.get(username="jaits13")
# print(get_login(admin.id))

#testing unbanned DAO
# unbanned_collab("5e79491e94ef4436d5875200")
# get=Collaborator.objects.get(id = "5e79491e94ef4436d5875200")
# print(json.loads(get.to_json()))

#testing banned DAO
# banned_collab("5e79491e94ef4436d5875200")
# get=Collaborator.objects.get(id = "5e79491e94ef4436d5875200")
# print(json.loads(get.to_json()))

#testing setting publish doc DAO
# published_doc("5e77dd971007bada89c1f0f0")
# get=DocumentCase.objects.get(id = "5e77dd971007bada89c1f0f0")
# print(json.loads(get.to_json()))

#testing setting unpublish doc DAO
unpublished_doc("5e77dd971007bada89c1f0f0")
get=DocumentCase.objects.get(id = "5e77dd971007bada89c1f0f0")
print(json.loads(get.to_json()))
