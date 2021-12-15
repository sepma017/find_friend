from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    members = Member.objects.all()

    return render(
        request,
        'friend/index.html',
        {
            'members': members,
        }
    )

def single_member_page(request, pk):
    member = Member.objects.get(pk=pk)

    return render(
        request,
        'friend/single_member_page.html',
        {
            'member': member,
        }
    )