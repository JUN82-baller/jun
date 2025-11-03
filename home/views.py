from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import Quote
from .form import QuoteForm
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import QuoteSerializer
from rest_framework import status

def home(request):
    # Gọi lại index để tái sử dụng logic/ template
    return index(request)

def index(request):
    quotes = Quote.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')  # use namespaced name
        # if not valid -> fall through to render with bound form so errors show
    else:
        form = QuoteForm()

    return render(request, 'home/index.html', {'quotes': quotes, 'form': form})

def quote(request):
    quotes = [
        "The best way to predict the future is to invent it.",
        "Stay hungry, stay foolish.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "Experience is the name everyone gives to their mistakes.",
        "In order to be irreplaceable, one must always be different."
    ]
    quote_of_the_day = random.choice(quotes)
    return render(request, 'home/quote.html', {'quote': quote_of_the_day})

def edit_quote(request, id):
    # quote = Quote.objects.get(id=id)
    # if request.method == 'POST':
    #     form = QuoteForm(request.POST, instance=quote)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = QuoteForm(instance=quote)
    # return render(request, 'home/edit.html', {'form': form})
    
    quote = get_object_or_404(Quote, id=id)

    if request.method == 'POST':
        # optional: use form for validation instead of direct assignment
        quote.text = request.POST.get('text', quote.text)
        quote.author = request.POST.get('author', quote.author)
        quote.save()
        return redirect('home:index')  # use namespaced name
   
    return render(request, 'home/edit.html', {'quote': quote})

def delete_quote(request, id):
      # only allow POST to delete (safer)
    quote = get_object_or_404(Quote, id=id)
    # if request.method == 'POST': #khong xai delete.html
    quote.delete()
    return redirect('home:index')
    # if GET, render a confirmation template or redirect back
    # return render(request, 'home/delete.html', {'quote': quote})
# @api_view(['GET', 'POST'])
# def quote_list(request):
#     if request.method == 'GET':
#         quote = Quote.objects.all()
#         serializer = QuoteSerializer(quote, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = QuoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def quote_detail (request, id):
#     try:
#         quote = Quote.objects.get(pk = id)
#     except Quote.DoesNotExist:
#         return Response({'error': 'Quote not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = QuoteSerializer(quote)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = QuoteSerializer(quote, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         quote.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

def quotes_api(request):
    return render(request, 'home/quote_api.html')

def frontend_view(request):
    return render(request, 'home/frontend.html')

class QuoteViewSet(viewsets.ModelViewSet): # dung modelviewset de tu dong tao ra cac phuong thuc CRUD
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.AllowAny]