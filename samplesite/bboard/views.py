#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Здесь будет выведен список объявлений.")
#
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

#FBV
def contactPage(request):
	form = ContactForm()
	return render(request, "contact.html", {"contactForm": form})

def postContact(request):
	if request.method == "POST" and request.is_ajax():
		form = ContactForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)
