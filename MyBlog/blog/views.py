from django.shortcuts import render
from django.views.generic import View
from .models import UserProfile, AboutMe, LearnProfile, LifeProfile
# Create your views here.


class UserView(View):
    def get(self, request):
        index_list = UserProfile.objects.all()
        return render(request, 'index.html', {'index_list': index_list})


class LearnView(View):
    def get(self, request):
        learn_list = LearnProfile.objects.all()
        return render(request, 'learn.html', {'learn_list': learn_list, 'msg': '吹灭读书灯，一身都是月。'})


class LifeView(View):
    def get(self, request):
        life_list = LifeProfile.objects.all()
        return render(request, 'life.html', {'life_list': life_list, 'msg': '我喜欢故事，偶尔也喜欢酒。'})


# 关于我
def AboutMeView(request):
    about_list = AboutMe.objects.all()
    return render(request, 'about.html', {'about_list': about_list})


# 留言
def MessageView(request):
    return render(request, 'message.html')


def EmailView(request):
    return render(request, 'email/mail.html')



