from django.contrib.auth.models import Group
from issue.models import Reason, SubCategory, Status

# REASONS
working_on_it = Reason.objects.get(name="We're working on it")

# SUBCATEGORIES
sub_student_portal_issues = SubCategory.objects.get(name='Student portal issues')
sub_coursera_issues = SubCategory.objects.get(name='Coursera issues')

# STATUSES
stat_new = Status.objects.get(name="New")

# TEAMS
level1 = Group.objects.get(name="Level1")

ISSUES = {
    'ISSUE1': {
        'brief': 'I can\'t login to the student portal',
        'description': 'when I enter my password it takes me to an error page',
        'subcategory': sub_student_portal_issues.id,
        'status': stat_new.id
    },
    'ISSUE2': {
        'brief': 'I can\'t find my course in Coursera',
        'description': 'My In Progress doesn\'t show CM2020',
        'subcategory': sub_coursera_issues.id,
        'status': stat_new.id
    },
}

PROGRESS = {
    'PROGRESS1': {
        'assignee': None,
        'team': level1.id,
        'issue': None,
        'reason': working_on_it.id,
        'description': "Your issue has been assigned to an agent, we will give you an update soon!"
    }
}