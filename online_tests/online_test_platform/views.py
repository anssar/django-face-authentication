from django.shortcuts import render
from face_authentication.decorators import FARequired

@FARequired
def main(request):
    return render(request, 'main.html')
