from django.shortcuts import redirect, render

from landings.models import CommonCV


def index(request):
    context = None

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return render(request, 'landings/index.html', status=200, context=context)


def cv(request):
    cv = CommonCV.objects.all().order_by('-uploaded').first()
    return redirect(cv.doc.url)
