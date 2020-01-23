from django.shortcuts import render,redirect,Http404
from .models import Event,Star,RegisterEventUsers
from django.contrib import  messages
from .utils import id_generator
from django.db.models import  Q
def home(request):
    events = Event.objects.all()
    star = Star.objects.last
    context = {
        'events':events,
        'star':star,

    }
    return render(request,'home.html',context)
def event_detail(request,pk):
    try:
        event = Event.objects.get(pk=pk)
    except:
        event = None
        return Http404
    if event:
        return render(request,'events/event_detail.html',{'event':event})


departments = {
    'robotics':'Robotics',
    }
def add_event(request):
    if request.method == 'POST':
        print(request.POST)
        image = request.FILES['image']
        name = request.POST['name']
        description = request.POST['description']
        category = request.POST['category']
        new_event,created = Event.objects.get_or_create(image=image, name =name, description=description,category = category)
        if created:
            print('success')
            return redirect('events')
        else:
            print('unsuccessful')
            return redirect('home')
    else:
        return render(request,'events/add_event.html',{})

def events(request):
    queryset = Event.objects.all()
    return render(request,'events/events.html',{'events':queryset})
def delete_event(request,id):
    try:
        event = Event.objects.get(id=id)
    except :
        event = None
        return Http404
    
    if event:
        event.delete()
        return redirect('events')
def add_star(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            image = request.FILES['image']
            name = request.POST['name']
            new_star,created = Star.objects.get_or_create(image=image, name =name)
            if created:
                print('success')
                return redirect('home')
            else:
                print('unsuccessful')
                return redirect('home')
        else:
            return render(request,'events/add_event.html',{'star':True})
    else:
        messages.error(request,"You don't have permission to do this operation")
        return redirect('home')
        
def register(request,pk):
    if request.method == 'POST':
        event = Event.objects.get(pk =pk)
        name = request.POST['name']
        college_name = request.POST['cname']
        email = request.POST['email']
        phone_number = request.POST['pnumber']
        registration_id = id_generator()
        try:
            new_registered_user = RegisterEventUsers.objects.create(event = event, name = name,
                                                                                    college_name = college_name,
                                                                                    email = email,
                                                                                    phone_number=phone_number,
                                                                                    registration_id = registration_id)
            new_registered_user.save()
            messages.success(request,'You have successfully registered for the event, now you will have to pay required fees physically for participation')
            return redirect('events')
        except :
            messages.error(request,'Something went wrong while registering try agian')
            return redirect('events')
    else :
        return render(request,'events/register.html',{})

def registered_users_for_event(request,pk):
    if request.user.is_superuser:
        try:
            event = Event.objects.get(pk=pk)
            users = RegisterEventUsers.objects.filter(event = event)
            total = users.count()
            context = {'users':users,'event':event,'total':total}
            return render(request,'events/registered_users_for_event.html',context)
        except:
            # event does not exist
            raise Http404
    raise Http404

def search_registered_users(request,pk):
    try:
        query = request.GET.get('q')
    except:
        query = None
    if query != '':
        users = RegisterEventUsers.objects.filter(
            Q(name__icontains = query)| Q(college_name__icontains=query) |
            Q(registration_id__icontains = query)
            )
        event = Event.objects.get(pk=pk)
        context = {'query': query,'users':users,'total':users.count(),'event':event}
        template = 'events/registered_users_for_event.html'
    else:
        context = {'query':query,'users':False}
        template = 'events/registered_users_for_event.html'
    
    return render(request,template,context)