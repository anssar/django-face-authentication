from .views import check
from .models import FAUser

def FARequired(view):
    def checkedView(request):
        fatokens = [x.token for x in FAUser.objects.all()]
        if request.session.get('fatoken', '') in fatokens or request.session.get('fatoken', '') == 'YES':
            return view(request)
        return check(request)
    return checkedView
