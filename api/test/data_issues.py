from django.contrib.auth.models import Group
from issue.models import Reason, SubCategory, Status, MyGroup

# REASONS
working_on_it = Reason.objects.get(name="We're working on it")

# SUBCATEGORIES
sub_student_portal_issues = SubCategory.objects.get(name='Student portal issues')
sub_coursera_issues = SubCategory.objects.get(name='Coursera issues')

ISSUES = {
    'ISSUE1': {
        'brief': 'I cannot login to the student portal',
        'description': 'when I enter my password it takes me to an error page',
        'subcategory': 5
    },
    'ISSUE2': {
        'brief': 'I cannot find my course in Coursera',
        'description': 'My In Progress doesnt show CM2020',
        'subcategory': 4
    },
}

PROGRESS = {
    'PROGRESS1': {
        'assignee': None,
        'team': MyGroup.Level1Id,
        'issue': None,
        'reason': working_on_it.id,
        'description': "Your issue has been assigned to an agent, we will give you an update soon!"
    }
}