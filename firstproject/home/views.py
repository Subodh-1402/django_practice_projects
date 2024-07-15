from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter

# Create your views here.


def index_view(request):
    return(HttpResponse("hello client"))

def contact_view(request):
    return(HttpResponse("this is contact page"))

def dynamic_route(request, number):
    # for i in range(1, 11):
    #     value = number * i
    #     print(number, "*", i, "=", value)



    count = {}
    for n in number:
        if count.get(n):
            count[n] += 1
        else:
            count[n] = 1
            
    print(count)

    # count = Counter(number)   # Count occurrences of each character in 'number', ouyput will be like 'Counter({'9': 3, 's': 3})'

    


    return(HttpResponse(f"response by dunamic route, you entered {number}"))