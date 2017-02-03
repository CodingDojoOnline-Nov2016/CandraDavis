from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count


from .models import Author, Book, Review, User
# Create your views here.
def index(request):
    return redirect('login:index')

def show(request):
    #show book homepage with list of 3 most recently reviewed books and a list of other reviewed books with links.
    try:
        reviews = Review.objects.order_by('-updated_at')[:5]
        print reviews
        reviewed_books = Book.objects.all()
        print reviewed_books
    except TemplateDoesNotExist:
        pass

    context = {
        'reviews': reviews,
        'reviewed_books': reviewed_books,
        # 'user_name': request.session['user_name']
        }
    return render(request, 'books/index.html', context)# context

def new_book(request):
    #called when clicking "add book review" from homepage. returns add_book_review.html with author_name list
    context = {
        'authors':Author.objects.all(),
    }
    return render(request, 'books/add_book_review.html', context)

def create(request):
    #1. processes post request.
    if request.method == 'POST':
        print '^'*50
        print request.POST
    #2. Adds title, author, user id to Book db after validations
    #3. Adds review, rating, user id, book id to Review db after validations
        u_id = request.session['u_id']
        print '@'*75
        print u_id
        book_review_info = Review.objects.valid_review(request.POST, u_id)
        print book_review_info
    #4. returns book object to redirect to show_book
        if book_review_info[0] == False:
            messages.error(request, book_review_info[1])
            return redirect('books:new_book')
        else:
            print book_review_info
            b_id = book_review_info[1].id
            context = {
                'book': book_review_info,
            }
            return redirect(reverse('books:show_book', kwargs={'b_id':b_id}))

def show_book(request, b_id):
    #1. query review db to pull ALL reviews associated with book.id
    #2. return 3 most recent reviews in a review object to be listed on page
    book_reviews = Review.objects.order_by('-created_at').filter(id=b_id)# this shows all of the reviews!!#[:5]
    # book_reviews = Review.objects.filter(id=b_id)
    print book_reviews, '<-----------------review'
    print b_id, '<------------b_id'
    #3. can post a review on the page, that redirects to the new_review method
    # try:
    book = Book.objects.filter(id=b_id)
    context = {
        'book_reviews': book_reviews,
        'u_id': request.session['u_id'],
        'user_name': request.session['user_name'],
        'b_id': b_id,
        'book': book,
    }
    # except Book.DoesNotExist:
    #     pass
    return render(request, 'books/book.html', context)

def new_review(request, b_id):
    if request.method == 'POST':
        print 'I am in the new_review method!!!!!!!!!'
        print request.POST
        #1. runs validations on the review
        #2. inserts new review into db
        u_id = request.session['u_id']
        add_review = Review.objects.add_new_review(request.POST, b_id, u_id)
        print add_review
        print '&'*75
        if add_review[0] == False:
            messages.error(request, add_review[1])
            return redirect(reverse('books.show_book', kwargs={'b_id':b_id}))
        else:
            messages.success(request, 'You have successfully added a new review.')
            #3. returns a 5 most recent reviews, updated with new review
            #4. return redirects to show_book with latest review
            return redirect(reverse('books.show_book'))#, kwargs={'b_id':b_id})
    else:
        return redirect(reverse('books:show_book', kwargs={'b_id':b_id}))

def user_info(request, u_id):
    #1. queries Book & Review db's to get all of the books that have been reviewed by a user. uses request.session['user_id']
    #2. queries User db to get all of the user info to display on user.html
    #3. renders the page with context variable passing needed data.
    user = User.objects.get(pk=u_id)
    print user, '<-------user id'
    context = {
        'user': User.objects.get(pk=u_id),
        # 'books': User.objects.book_set.all(),
        'book': Book.objects.filter(user=user),
        'total_reviews': Review.objects.annotate(num_reviews=Count('comments')).filter(user=user).count()
    }
    return render(request, 'books/user.html', context)

def delete_review(request):
    pass

def logout(request):
    request.session.clear()
    return redirect('login:index')
