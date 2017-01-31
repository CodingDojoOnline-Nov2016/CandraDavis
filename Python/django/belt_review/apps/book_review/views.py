from django.shortcuts import render, redirect
from .models import Books
from django.contrib import messages
# Create your views here.
def index(request):
    return redirect('login:index')

def show(request):
    context = {
        'latest_reviews': Books.objects.order_by('updated_at')[:3],
        'books': Books.objects.all(),
        # 'user_name': request.session['user_name']
    }
    return render(request, 'book_review/index.html', context)

def create(request):

    context = {}
    return render(request, 'book_review/add_review.html', context)

def update(request):
    if request.method == 'POST':
        new_book = Books.objects.new_book_review(request)
        print '%'*100
        print new_book
    if new_book[0] == False:
        messages.error(request, new_book[1], extra_tags='adding_book')
        return redirect('books:add_books')
    else:
        print new_book
        request.session['book_id'] = new_book.id
        return redirect('books:show_book')

def show_book(request):
    context = {
        'view_book': Books.objects.get(id=request.session['id']),
        'reviews': Books.objects.order_by('updated_at')[:3],
    }
    return render(request, 'book_review/book.html', context)

def add_another_review(request):
    return redirect('books:create')

def show_user(request):
    context = {}
    return render(request, 'book_review/user.html', context)

def logout(request):
    request.session.clear()
    return redirect('login:index')
