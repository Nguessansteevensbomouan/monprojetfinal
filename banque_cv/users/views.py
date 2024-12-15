from django.core.paginator import Paginator
from django.shortcuts import render
from .models import User

def trombinoscope(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 10)  # 10 utilisateurs par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/trombinoscope.html', {'page_obj': page_obj})
