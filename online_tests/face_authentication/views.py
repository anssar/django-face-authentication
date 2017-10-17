from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import base64

from .core import recognize
from .models import FAUser

def check(request):
    return render(request, 'check.html')

@csrf_exempt
def checkPhoto(request):
    photo = base64.b64decode(json.loads(request.POST.get('data'))['image'].split(',')[1].strip())
    file = open('/tmp/faphoto.png', 'wb')
    file.write(photo)
    file.close()
    users = []
    if recognize('/tmp/faphoto.png', []):
        request.session['fatoken'] = 'YES'
        return JsonResponse({'result': 'OK'}, status=200)
    return JsonResponse({'result': 'FAIL'}, status=200)
