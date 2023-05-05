from dash.models import Cohorts

def get_cohorts(request):
    allcojrts = Cohorts.objects.get(users=request.user)
    return {'allcojrts':allcojrts}