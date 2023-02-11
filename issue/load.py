from django.contrib.auth.models import Group
from .models import Reason, Status


for team in ["Student","Level1","Level2","Level3","General","Registrations","Class Support","Finance"]:
    Group.objects.get_or_create(name=team)
    
for reason in ["Student commented","Agent acknowledged","Resolved","No Response","Happened Again"]:
    Reason.objects.get_or_create(name=reason)

for status in ["New","Assigned","In Progress","Blocked","Referred","Escalated","Resolved","Closed"]:
    Status.objects.get_or_create(name=status)

