from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('login:index')

def show(request):
    #show book homepage with list of 3 most recently reviewed books and a list of other reviewed books with links.
    reviews = Review.objects.recent_review()
    print reviews

    reviewed_books = Book.objects.filter(title)
    print reviewed_books

    context = {
        'recent_reviews': reviews,
        'reviewed_books': reviewed_books,
        # 'user_name': request.session['user_name']
    }
    return render('books/index.html', context)

def new_book(request):
    #called when clicking "add book review" from homepage. returns add_book_review.html with author_name list
    context = {
        'authors':Author.objects.filter(author_name),
    }
    return render('books/add_book.html', context)

def create(request):
    #1. processes post request.
    if request.method == 'POST':
    #2. Adds title, author, user id to Book db after validations
    #3. Adds review, rating, user id, book id to Review db after validations
        u_id = request.session['u_id']
        book_review_info = Review.objects.valid_review(request.POST, u_id)
    #4. returns book object to redirect to show_book
        if book_review_info[0] == False:
            messages.error(book_review_info[1])
            return redirect('books:new_book')
        else:
            print book_review_info
            b_id = book_review_info[1].id
            context = {
                'book': book_review_info,

            }
            return redirect('books:show_book', kwargs={'b_id':b_id})

def show_book(request, b_id):
    #1. query review db to pull ALL reviews associated with book.id
    #2. return 3 most recent reviews in a review object to be listed on page
    book_reviews = Review.objects.book_all_reviews(b_id)[:5]
    print book_reviews
    #3. can post a review on the page, that redirects to the new_review method
    context = {
        'book_reviews': book_reviews,
    }
    return render('books/book.html', context)
def new_review(request, b_id):
    #1. runs validations on the review
    #2. inserts new review into db
    #3. returns a 3 most recent reviews, updated with new review
    #4. return redirects to show_book with latest review
    pass

def user_reviews(request, u_id):
    #1. queries Book & Review db's to get all of the books that have been reviewed by a user. uses request.session['user_id']
    #2. queries User db to get all of the user info to display on user.html
    #3. renders the page with context variable passing needed data.
    pass

def logout(request):
    request.session.clear()
    return redirect('login:index')
