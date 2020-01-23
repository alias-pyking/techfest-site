from django.shortcuts import render,redirect
from .models import StudentCordinators, Devs, FacultyCordinators
from django.contrib import  messages
def organizers(request):
    faculty_coordinators = FacultyCordinators.objects.all()
    student_coordinators = StudentCordinators.objects.all()
    devs = Devs.objects.all()

    context = {
        'faculty_coordinators':faculty_coordinators,
        'student_coordinators':student_coordinators,
        'devs':devs
    }
    return render(request,'organizers/organizers.html',context)

def add_faculty(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            print(request.POST)
            image = request.FILES['image']
            name = request.POST['name']
            title = request.POST['title']
            new_event,created = FacultyCordinators.objects.get_or_create(image=image, name =name,title =title)
            if created:
                print('success')
                return redirect('organizers')
            else:
                print('unsuccessful')
                return redirect('home')
        else:
            return render(request,'organizers/add_organizer.html',{'text':'Faculty Co-ordinator','faculty':True})
    else :
        messages.error(request,"You Don't have permission to do this operation" )
        return redirect('organizers')

def add_student(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            print(request.POST)
            image = request.FILES['image']
            name = request.POST['name']
            new_event,created = StudentCordinators.objects.get_or_create(image=image, name =name)
            if created:
                print('success')
                return redirect('organizers')
            else:
                print('unsuccessful')
                return redirect('home')
        else:
            return render(request,'organizers/add_organizer.html',{'text':'Student Co-ordinator'})
    else :
        messages.error(request,"You Don't have permission to do this operation" )
        return redirect('organizers')

def add_dev(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            print(request.POST)
            image = request.FILES['image']
            name = request.POST['name']
            typ = request.POST['type']

            new_event,created = Devs.objects.get_or_create(image=image, name =name,typ = typ)
            if created:
                print('success')
                return redirect('organizers')
            else:
                print('unsuccessful')
                return redirect('home')
        else:
            return render(request,'organizers/add_organizer.html',{'text':'Developer','dev':True})
    else :
        messages.error(request,"You Don't have permission to do this operation" )
        return redirect('organizers')

def delete_faculty(request,pk):
    if request.user.is_superuser:
        try:
            faculty = FacultyCordinators.objects.get(pk=pk)
        except :
            faculty = None
            return Http404
        
        if faculty:
            faculty.delete()
            return redirect('organizers')
    else :
        messages.error(request,"You Don't have permission to do this operation" )
        return redirect('organizers')

def delete_student(request,pk):
    if request.user.is_superuser:
        try:
            student = StudentCordinators.objects.get(pk=pk)
        except :
            student = None
            return Http404
        
        if student:
            student.delete()
            return redirect('organizers')
    else :
        messages.error(request,"You Don't have permission to do this operation" )
        return redirect('organizers')

def delete_dev(request,pk):
    if request.user.is_superuser:
        try:
            dev = Devs.objects.get(pk=pk)
        except :
            dev = None
            return Http404
        
        if dev:
            dev.delete()
            return redirect('organizers')
    else :
        messages.error(request,"You Don't have permission to do this operation" )
        return redirect('organizers')