from django.shortcuts import render, redirect
from face_authentication.decorators import FARequired

@FARequired
def main(request):
    return render(request, 'main.html')

    
def logout(request):
    try:
        del request.session['fatoken']
    except:
        pass
    return redirect('/')