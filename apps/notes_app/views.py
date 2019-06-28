from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Note, Category, Subcategory, Subcontent
import bcrypt

#Landing Page - Localhost:8000
def index(request):
    #Check if user in session, else redirect to login page.
    print("[Localhost:8000/]---Index Page---")

    context = {
        'current_user' : User.objects.get(id=request.session['active_user']),
        'list_of_all_notes' : Note.objects.all(),
        'list_of_categories' : Category.objects.all(), #not sure this is still in use
        'list_of_sub_categories' : Subcategory.objects.all(),
        'sub_categories' : Subcategory.objects.all(),
        'subcontents' : Subcontent.objects.all(),
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
    new_note = Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)

    print(new_note.id)

    new_subcontent = Subcontent.objects.create(content=form_content, parent=new_note)

    print(new_subcontent)

    return redirect('/dashboard')

def append_note(request, id):
    print("[Localhost:8000/append_note/]---Appending a note to Note database---")
    print(Note.objects.get(id=id).title)
    print(Note.objects.get(id=id).category)
    print(Note.objects.get(id=id).content)

    parent_object = Note.objects.get(id=id)
    print(parent_object.id)
    print(parent_object.title)

    form_content = request.POST['new_subnote_text']
    new_subcontent = Subcontent.objects.create(content=form_content, parent=parent_object)
    print(new_subcontent)
    
    print(Note.objects.get(id=id).id)
    print(request.POST['new_subnote_text'])
    return redirect('/dashboard')

def append_note_from_view(request, category, subcategory, id):
    parent_object = Note.objects.get(id=id)
    form_content = request.POST['new_subnote_text']
    new_subnote = Subcontent.objects.create(content=form_content, parent=parent_object)
    return redirect('/notes/view/' + category + '/' + subcategory)

#Add note from view
def add_note_from_view(request, category, subcategory):
    print("[Localhost:8000/add_note_from_view/]---Adding a note from a view and redirecting to view note page---")
    form_title = request.POST['note-title']
    form_category = request.POST['note-category']
    form_form = 1 #Not going to use this, will set it to default value of 1. Should remove completely, but will leave until later.
    form_content = request.POST['form-content']
    
    # Add note to db
    new_note = Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)

    #Added LKQ@$JL@$J@$K
    form_content=request.POST['form-content']
    Subcontent.objects.create(content=form_content, parent=new_note)

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

#Delete Note From View
def delete_note_from_view(request, category, subcategory, id):
    print("[Localhost:8000/delete_note/]---Deleting a note in the Note database---")
    Note.objects.filter(id=id).delete()
    # Category.objects.filter(id=id).delete()
    return redirect('/notes/view/' + category + '/' + subcategory)

#New Category
def add_category(request):
    print("[Localhost:8000/add_category/]---Adding a category to Category database---")
    newCategory = Category.objects.create(name=request.POST['category-name'])
    print(type(newCategory.id))
    return redirect('/dashboard')

#New Category
def add_category_from_view(request, category, subcategory):
    print("[Localhost:8000/add_category/]---Adding a category to Category database from view page---")
    newCategory = Category.objects.create(name=request.POST['category-name'])
    print(type(newCategory.id))
    return redirect('/notes/view/' + category + '/' + subcategory)


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

#Add SubCategory from view
def create_subcategory_from_view(request, category, subcategory, id):
    print("[Localhost:8000/delete_category/]---Creating a subcategory in Subcategory database---")
    Subcategory.objects.create(name=request.POST['subcategory-name'], parent=Category.objects.get(id=id))
    return redirect('/notes/view/' + category + '/' + subcategory)

#Delete SubContent
def delete_subcontent(request, id):
    print("[Localhost:8000/delete_subcontent/]---Delete a subcontent from Subcontent database---")
    Subcontent.objects.filter(id=id).delete()
    return redirect('/dashboard')

#Delete SubContent from view
def delete_subcontent_from_view(request, category, subcategory, id):
    print("[Localhost:8000/delete_subcontent_from_view/]---Delete a subcontent from Subcontent database---")
    Subcontent.objects.filter(id=id).delete()
    return redirect('/notes/view/' + category + '/' + subcategory)

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
        'current_user': User.objects.get(id=request.session['active_user']),
        #Update below with any changes made to homepage
        'list_of_category_notes' : Note.objects.all().filter(category=subcategory),
        'list_of_sub_categories' : Subcategory.objects.all(),
        'list_of_categories' : Category.objects.all(),
        'sub_categories' : Subcategory.objects.all(),
        'subcontents' : Subcontent.objects.all(),
    }
    # print(category)
    # print(subcategory)
    return render(request, "notes_app/view.html", context)

def logout(request):
    print("[Localhost:8000/logout/]---Destroys session key ['active_user'] from session---")
    request.session.clear()
    return redirect('login_app/')