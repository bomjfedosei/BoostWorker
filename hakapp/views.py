from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .models import User, Worker, Relation, Tag, Retrain, Profession
import hashlib
import json

# Create your views here.

@csrf_protect
def index(request):
    return render(request, 'log.html')

#################################################
def hr(request):
    user = request.GET.dict()['login']
    data = dict()
    userObject = User.objects.filter(login=user)
    data['person'] = userObject[0].Person
    data['type'] = "HR-специалист"
    data['workers_red'] = list(Worker.objects.filter(Status = 1).values())
    data['count'] = len(data['workers_red'])
    data['workers_wor'] = list(Worker.objects.filter(Status = 2).values())
    return render(request, 'hr.html', context = data)

##def manager(request):
#    user = request.GET.dict()['user']
#    return render(request, 'manager.html')


def autorize(request):
    if (request.POST):
        data = request.POST.dict()
        Enter = User.objects.filter(login = data['login'])
        if (Enter[0].password != hashlib.sha512(data['pass'].encode('utf-8')).hexdigest()):
            return HttpResponse("RESOLVED")
        else:
            if (Enter[0].type == 0):
                return HttpResponseRedirect('hr?login=' + data['login'])
            elif (Enter[0].type == 1):
                return HttpResponseRedirect('manager?user=' + data['login'])

###################################################

def packSkills(array):
    newArray = []
    for part in array:
        title = Tag.objects.filter(id = part['Tag_relate_id']).values()
        position = Profession.objects.filter(id = part['Profession_relate_id']).values()
        newArray.append((title[0]['title']))
    return newArray

def workers(request, id):
    Enter = User.objects.filter(login = request.GET.dict()['login'])
    Human = Worker.objects.filter(id = id)
    data = dict()
    data['person'] = Enter[0].Person
    data['type'] = "HR-специалист"
    data['Human'] = Human[0].Person
    data['Avatar'] = Human[0].Avatar
    data['Position'] = Human[0].Position
    data['Status'] = Human[0].Status
    if (data['Status'] == 1):
        data['Needed_Skills'] = packSkills(list(Relation.objects.filter(Type = 0, Worker_relate = Human[0]).values()))
        data['Recomended_Skills'] = packSkills(list(Relation.objects.filter(Type = 1, Worker_relate = Human[0]).values()))
    elif (data['Status'] == 2):
        Education = Retrain.objects.filter(TargetWorker = Human[0]).values()
        Proffesion1 = Profession.objects.filter(id = Education[0]['Profession1_id']).values()
        Proffesion2 = Profession.objects.filter(id = Education[0]['Profession2_id']).values()
        data['Prof1'] = Proffesion1[0]['title']
        data['Prof2'] = Proffesion2[0]['title']
        data['Prof1_Needed_Skills'] = packSkills(list(Relation.objects.filter(Type = 0, Worker_relate = Human[0], Profession_relate_id = Proffesion1[0]['id']).values()))
        data['Prof1_Recomended_Skills'] = packSkills(list(Relation.objects.filter(Type = 1, Worker_relate = Human[0], Profession_relate_id = Proffesion1[0]['id']).values()))
        count1 = len(data['Prof1_Needed_Skills']) + len(data['Prof1_Recomended_Skills'])
        data['Prof2_Needed_Skills'] = packSkills(list(Relation.objects.filter(Type = 0, Worker_relate = Human[0], Profession_relate_id = Proffesion2[0]['id']).values()))
        data['Prof2_Recomended_Skills'] = packSkills(list(Relation.objects.filter(Type = 1, Worker_relate = Human[0], Profession_relate_id = Proffesion2[0]['id']).values()))
        count2 = len(data['Prof2_Needed_Skills']) + len(data['Prof2_Recomended_Skills'])
        data['progressbar'] = str(round((count2 / (count1 + count2)) * 100))
    return render(request, 'worker.html', context = data)

def employee(request):
    Enter = User.objects.filter(login = request.GET.dict()['login'])
    data = dict()
    data['person'] = Enter[0].Person
    data['type'] = "HR-специалист"
    data['workers'] =list(Worker.objects.all().values())
    return render(request, 'employee.html', context = data)

def skills(request):
    Enter = User.objects.filter(login = request.GET.dict()['login'])
    data = dict()
    data['person'] = Enter[0].Person
    data['type'] = "HR-специалист"
    data['workers'] = list(Tag.objects.all().values())
    return render(request, 'skills.html', context = data)
