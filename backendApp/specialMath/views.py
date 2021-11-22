from django.shortcuts import render
from django.http import JsonResponse

def generateResponse(input, output):
    return {
        "data": {
            "input": input,
            "output": output
        }
    }

def index(request, number):
    if number in {0,1}:
        return JsonResponse(generateResponse(number, number))
    if number == 2:
        return JsonResponse(generateResponse(number, 3))
    if number == 3:
        return JsonResponse(generateResponse(number, 7))
    last2, last1, cur_number = 1, 3, 7 # n-2 , n-1 , n => n=3
    for i in range(4, number+1):
        last2 = last1
        last1 = cur_number
        cur_number = i + last1 + last2
    return JsonResponse(generateResponse(number, cur_number))