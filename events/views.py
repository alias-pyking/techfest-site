from django.shortcuts import render,redirect,Http404
from .models import Event,Star,RegisterEventUsers
from django.contrib import  messages

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

def add_event(request):
    if request.method == 'POST':
        print(request.POST)
        image = request.FILES['image']
        name = request.POST['name']
        description = request.POST['description']
        new_event,created = Event.objects.get_or_create(image=image, name =name, description=description)
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
            description = request.POST['description']
            new_star,created = Star.objects.get_or_create(image=image, name =name, description=description)
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
        try:
            new_registered_user = RegisterEventUsers.objects.create(event = event, name = name,
                                                                                    college_name = college_name,
                                                                                    email = email,
                                                                                    phone_number=phone_number)
            new_registered_user.save()
            messages.success(request,'You have successfully registered for the event, now you will have to pay required fees physically for participation')
            return redirect('events')
        except :
            messages.error(request,'Something went wrong while registering try agian')
            return redirect('events')
    else :
        return render(request,'events/register.html',{})

def registered_users_for_event(request,pk):
    try:
        event = Event.objects.get(pk=pk)
        users = RegisterEventUsers.objects.filter(event = event)
        return render(request,'events/registered_users_for_event.html',{'users':users,'event':event})
    except:
        # event does not exist
        raise Http404
