from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,\
HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseRedirect
from models import acortar_Url
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def process(request):

    urls = ""

    if request.method == "GET":

        lista_Urls = acortar_Url.objects.all()
        urls+="<a>URLS GUARDADAS:</a>"
        for url in lista_Urls:
            urls += "<pre>" + str(url.id) +\
                    " Url acortada de: " +url.Url + "<b/>"
        urls += "<br/>"
        form = "<form action='' method='POST'>Introduzca su Url: <input type=\
                'text' name='url'><input type='submit' value='Enviar'></form>"
        return HttpResponse(urls + form)

    elif request.method == "POST":

        url = request.POST.get("url")

        if url == "":
            return HttpResponseBadRequest("PAGINA VACIA")
        elif not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        try:
            newUrl = acortar_Url.objects.get(Url=url)
        except acortar_Url.DoesNotExist:
            newUrl = acortar_Url(Url=url)
            newUrl.save()
        response = "<p>url acortada: <a href=" + str(newUrl.id) + ">" +\
                    str(newUrl.id) + "</a></p>"
        response += "<a href=''>Pulse aqui para volver al acortador</a>"

        return HttpResponse(response)
    else:
        return HttpResponse("Something goes wrong :S")


def redirect(request, id):
    try:
        url = acortar_Url.objects.get(id=id)
    except acortar_Url.DoesNotExist:
        return HttpResponseNotFound(str(id) + " not found")
    return HttpResponseRedirect(url.Url)
