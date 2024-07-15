from django.shortcuts import render


def home_view(request):
    names = ["Subodh", "Akhil", "Amey", "ajay"]
    items = {
        "pen": 5,
        "pencil":10,
        "eraser":50,
    }
    context = {
        "names": names,
        "items": items,
    }
    return render(request, 'index.html', context)

def contact_view(request):
    return render(request, 'contact.html')