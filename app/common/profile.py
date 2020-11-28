from app.models import Profile


def get_profile():
    return Profile.objects.all()[0]
