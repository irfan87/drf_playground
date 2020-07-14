from django.shortcuts import render
from django.http import JsonResponse

def test_view(request):
    data = {
        'name': 'irfan',
        'age': 33,
    }

    return JsonResponse(data)
