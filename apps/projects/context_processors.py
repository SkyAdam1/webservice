from apps.projects.models import Project


def projects_count(request):
    return {'projects_count': Project.objects.count()}


def user_projects_count(request):
    return {'user_projects_count': Project.objects.filter(user__username=request.user).count()}
