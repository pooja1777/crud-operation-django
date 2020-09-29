from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegisteration
from .models import user

# This fun. will add and show the data
def addshow(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = user(name = nm, email = em, password = pw)
            reg.save()
            fm = StudentRegisteration()
    else:
        fm = StudentRegisteration()
    stud = user.objects.all() 
    return render(request, 'enroll/add_show.html', {'form': fm, 'stu' : stud})

# This function will delete the data

def delete_data(req, id):
    if req.method == 'POST':
        idn = user.objects.get(pk=id)
        idn.delete()
        return HttpResponseRedirect('/')


#This will update the data given previously
def update_stud(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegisteration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegisteration( instance=pi)
    return render(request, 'enroll/update_info.html', {'form' : fm})