from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Reason, Status, SubCategory, Category

from api.test.data_user import *

def add_issue_related_data():
    #### RELATED DATA ####
    for team in ["Student","Level1","Level2","Level3","General","Registrations","Class Support","Finance", "Admin"]:
        Group.objects.get_or_create(name=team)
        
    for reason in ["Assigned to team","We're working on it","Student commented","Agent acknowledged","Resolved","No Response","Happened Again"]:
        Reason.objects.get_or_create(name=reason)

    for status in ["New","Assigned","In Progress","Blocked","Referred","Escalated","Resolved","Closed"]:
        Status.objects.get_or_create(name=status)

    for category in [
        "General",
        "Enrollment",
        "Registration",
        "Technology",
        ]:
        Category.objects.get_or_create(name=category)

    subcategories = [
        # GENERAL
        
        # ENROLLMENT
        
        # REGISTRATION
        {'name':'Help with a new registration',
        'category': Category.objects.get(name='Registration'),
        'supportedBy':Group.objects.get(name='Registrations')},
        {'name':'Change a registration',
        'category': Category.objects.get(name='Registration'),
        'supportedBy':Group.objects.get(name='Registrations')},
        
        # TECHNOLOGY
        {'name':'Coursera issues',
        'category': Category.objects.get(name='Technology'),
        'supportedBy':Group.objects.get(name='Level1')},
        {'name':'Student portal issues',
        'category': Category.objects.get(name='Technology'),
        'supportedBy':Group.objects.get(name='Level1')},
    ]

    for subcategory in subcategories:
        SubCategory.objects.get_or_create(**subcategory)

def add_user_data():
    #### USERS AND GROUPS ####
    User = get_user_model()
    user1, created = User.objects.get_or_create(email=TEST_USER_1)
    if created: 
        user1.set_password(TEST_PASS_1)
        user1.save()

    user2, created = User.objects.get_or_create(email=TEST_USER_2)
    if created:
        user2.set_password(TEST_PASS_2)
        user2.save()

    user3, created = User.objects.get_or_create(email=TEST_USER_3)
    if created:
        user3.set_password(TEST_PASS_3)
        user3.save()

    student_grp = Group.objects.get(name="Student")
    student_grp.user_set.add(user1, user2, user3)

    admin1, created = User.objects.get_or_create(email=TEST_ADM_USER)
    if created:
        admin1.set_password(TEST_ADM_PASS)
        admin1.save()
    admin_grp = Group.objects.get(name="Admin")
    admin_grp.user_set.add(admin1)

    level1, created = User.objects.get_or_create(email=TEST_L1_USER)
    if created:
        level1.set_password(TEST_L1_PASS)
        level1.save()
    l1_grp = Group.objects.get(name="Level1")
    l1_grp.user_set.add(level1)

    level2, created = User.objects.get_or_create(email=TEST_L2_USER)
    if created:
        level2.set_password(TEST_L2_PASS)
        level2.save()
    l2_grp = Group.objects.get(name="Level2")
    l2_grp.user_set.add(level2)

def run():
    add_issue_related_data()
    add_user_data()