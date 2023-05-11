from dash.models import Cohorts
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import get_user_model

user = get_user_model()

def get_cohorts(request):
    try:
       persoancohorts = Cohorts.objects.get(users=request.user)
       return {'persoancohorts': persoancohorts}
    except:
        return {}
   
   


# class Cohorts(View):
#     def get_cohorts(self, request):
#        allcojrts = Cohorts.objects.get(users=request.user)
#        context = {'allcojrts':allcojrts}
#        return context
        