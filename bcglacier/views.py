from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.utils import timezone
import cloudinary
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login

from .models import Sites, Ratings, Sitesavgrating, Photo, Parks
import logging
logging.basicConfig(format='%(message)s')

# Create your views here.
def index(request):
    # set callback page to return after login/signup
    request.session['callback_page'] = request.path

    return render(request, 'bcglacier/index.html')

def detail(request, id):
    # set callback page to return after login/signup
    request.session['callback_page'] = request.path

    site = get_object_or_404(Sites, pk=id)
    rating = Sitesavgrating.objects.get(id=id)
    return render(request, 'bcglacier/detail.html', {'site': site, 'rating' : rating})

def list(request):
    # set callback page to return after login/signup
    request.session['callback_page'] = request.path

    if request.session.get('current_park_name'):
        site_list = Sitesavgrating.objects.filter(park_id=request.session.get('current_park')).order_by('name')
    else:
        site_list = Sitesavgrating.objects.order_by('name')

    context = {
        'site_list' : site_list,
    }
    return render(request, 'bcglacier/list.html', context)

def votecomment(request, id):
    site = get_object_or_404(Sites, pk=id)
    try:
        rating = site.ratings_set.create(rating=request.POST['stars'], comments=request.POST['comment'], user=request.user.username,
                comment_date=timezone.now())
    except (KeyError, Ratings.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bcglacier/detail.html', {
            'site': site,
            'error_message': "You didn't select a choice.",
        })
    else:
        rating.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bcglacier:detail', args=(site.id,)))

def addinfo(request, id):
    site = get_object_or_404(Sites, pk=id)
    try:
        info = site.information_set.create(info=request.POST['comment1'], user=request.user.username, info_date=timezone.now())
    except (KeyError, Information.DoesNotExist):
        # Redisplay the detail form.
        return render(request, 'bcglacier/detail.html', {
            'site': site,
            'error_message': "You didn't enter any info",
        })
    else:
        info.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bcglacier:detail', args=(site.id,)))

def addpicture(request, id):
    site = get_object_or_404(Sites, pk=id)
    print ("printing length of image file")
    print (len(request.FILES['image']))
    if len(request.FILES['image']) != 0:
        cloudinary.config(
        cloud_name="bcsites",
        api_key="679429527975842",
        api_secret = "88WIMzIwclcqtiC2fXfrPXmZh3E"
        )
        res = cloudinary.uploader.upload(request.FILES['image'])
        print(res)
        print(res.get("secure_url", ""))
        st = (res.get("secure_url", "").index("image"))
        resurl = (res.get("secure_url", "")[st:])

    try:
        photo = site.photo_set.create(sid=id, user=request.POST['user2'], image=resurl)
    except (KeyError, Photo.DoesNotExist):
        # Redisplay the detail form.
        return render(request, 'bcglacier/detail.html', {
            'site': site,
            'error_message': "You didn't enter any info",
        })
    else:
        photo.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bcglacier:detail', args=(site.id,)))

def signup(request):
    return render(request, 'bcglacier/signup.html')

def processsignup(request):
    pwd=request.POST['pwd']
    u1=request.POST['user']

    if User.objects.filter(username=u1).exists():
        messages.error(request, 'A user with that name already exists.  Please choose another user name.')
        return HttpResponseRedirect(reverse('bcglacier:signup'))

    duser = User.objects.create_user(username=u1, password=pwd)
    duser = authenticate(username=u1, password=pwd)
    login(request, duser)

    callback = request.session.get('callback_page')

    return HttpResponseRedirect(callback)

@csrf_exempt
def update_park(request):
    if not request.is_ajax() or not request.method=='POST':
        messages.error(request, 'failed the check')
        return HttpResponseNotAllowed(['POST'])

    current_park = Parks.objects.filter(name=request.POST['park'])
    request.session['current_park'] = current_park.values_list('pk', flat=True).first()
    request.session['current_park_name'] = current_park.values_list('name', flat=True).first()
    request.session.save()
    print (request.session.get('current_park_name'))
    print (request.session.get('current_park'))
    return HttpResponse('')

def setMarkers(request):
    site_list = Sites.objects.all()
    return HttpResponse(serializers.serialize("json", site_list))

class ParksView(generic.ListView):
    model = Parks
    template_name = 'bcglacier/parklist.html'
    context_object_name = 'all_parks'

    def get_queryset(self):
        return Parks.objects.all()
