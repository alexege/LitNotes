from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Note, Category, Subcategory
import bcrypt

#Landing Page - Localhost:8000
def index(request):
    print("[Localhost:8000/]---Index Page---")

    context = {
        'list_of_all_notes' : Note.objects.all(),
        'list_of_categories' : Category.objects.all(), #not sure this is still in use
        'list_of_sub_categories' : Subcategory.objects.all(),
        'sub_categories' : Subcategory.objects.all(),
        # 'logged_in_user' : User.objects.
    }

    return render(request, "notes_app/dashboard.html", context)
 
#Add Note
def add_note(request):
    print("[Localhost:8000/add_note/]---Adding a note to Note database---")

    form_title = request.POST['note-title']
    form_category = request.POST['note-category']
    form_form = 1 #Not going to use this, will set it to default value of 1. Should remove completely, but will leave until later.
    form_content = request.POST['form-content']

    # Add note to db
    Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)
    return redirect('/dashboard')

#Add note from view
def add_note_from_view(request, category, subcategory):
    print("[Localhost:8000/add_note_from_view/]---Adding a note from a view and redirecting to view note page---")
    form_title = request.POST['note-title']
    form_category = request.POST['note-category']
    form_form = 1 #Not going to use this, will set it to default value of 1. Should remove completely, but will leave until later.
    form_content = request.POST['form-content']
    
    # Add note to db
    Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)
    return redirect('/notes/view/' + category + '/' + subcategory)

#Update Note
def update_note(request):
    print("[Localhost:8000/update_note/]---Updating a note in the Note database---")
    return redirect('/dashboard')

#Delete Note
def delete_note(request, id):
    print("[Localhost:8000/delete_note/]---Deleting a note in the Note database---")
    Note.objects.filter(id=id).delete()
    # Category.objects.filter(id=id).delete()
    return redirect('/dashboard')

#New Category
def add_category(request):
    print("[Localhost:8000/add_category/]---Adding a category to Category database---")
    newCategory = Category.objects.create(name=request.POST['category-name'])
    print(type(newCategory.id))
    return redirect('/dashboard')

#Delete Category
def delete_category(request, id):
    print("[Localhost:8000/delete_category/]---Delete a category from Category database---")
    Category.objects.filter(id=id).delete()
    return redirect('/dashboard')

#Delete Sub Category
def delete_sub_category(request, id):
    print("[Localhost:8000/delete_sub_category/]---Delete a category from Category database---")
    Subcategory.objects.filter(id=id).delete()
    return redirect('/dashboard')

#Add SubCategory
def create_sub_category(request, id):
    print("[Localhost:8000/delete_category/]---Creating a subcategory in Subcategory database---")
    Subcategory.objects.create(name=request.POST['subcategory-name'], parent=Category.objects.get(id=id))
    return redirect('/dashboard')

# def delete_note(request, id):
#     print("[Localhost:8000/delete_note/]---Delete a note from Note database---")
#     Note.objects.filter(id=id).delete()
#     return redirect('/dashboard')

def view_sub_category(request, category, subcategory):
    print("[Localhost:8000/view_sub_category/]---View all notes belonging to that sub-category---")
    # print(category)

    context = {
        'notes' : Note.objects.all(),
        'category' : category,
        'subcategory' : subcategory,
        #Update below with any changes made to homepage
        'list_of_category_notes' : Note.objects.all().filter(category=subcategory),
        'list_of_sub_categories' : Subcategory.objects.all(),
        'list_of_categories' : Category.objects.all(),
        'sub_categories' : Subcategory.objects.all(),
    }
    # print(category)
    # print(subcategory)
    return render(request, "notes_app/view.html", context)

def logout(request):
    print("[Localhost:8000/logout/]---Destroys session key ['active_user'] from session---")
    request.session.clear()
    return redirect('login_app/')