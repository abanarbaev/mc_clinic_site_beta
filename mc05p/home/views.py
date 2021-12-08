# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
#загрузка для админки файлов
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#main_page
def main_page(request):
    return render(request, 'home/main_page.html', {})
    

#travma
def travma(request):
    return render(request, 'home/main/travma.html', {})

#gynecology
def gynecology(request):
    return render(request, 'home/main/gynecology.html', {})

#urology
def urology(request):
    return render(request, 'home/main/urology.html', {})

#vaccine
def vaccine(request):
    return render(request, 'home/main/vaccine.html', {})

#laboratory
def laboratory(request):
    return render(request, 'home/main/laboratory.html', {})

#firstaid
def firstaid(request):
    return render(request, 'home/main/firstaid.html', {})

#online
def online(request):
    return render(request, 'home/main/online.html', {})

#callhome
def callhome(request):
    return render(request, 'home/main/callhome.html', {})

#vacancies
def vacancies(request):
    return render(request, 'home/main/vacancies.html', {})


#about
def about(request):
    return render(request, 'home/about.html', {})


#staff
def staff(request):
    return render(request, 'home/about/staff.html', {})

#reviews
def reviews(request):
    return render(request, 'home/about/reviews.html', {})

#for_clients
def for_clients(request):
    return render(request, 'home/about/for_clients.html', {})

#contacts
def contacts(request):
    return render(request, 'home/about/contacts.html', {})

#partners
def partners(request):
    return render(request, 'home/about/partners.html', {})

#pricelist
def pricelist(request):
    return render(request, 'home/about/pricelist.html', {})

#license
def license(request):
    return render(request, 'home/about/license.html', {})

#faq
def faq(request):
    return render(request, 'home/about/faq.html', {})


#occasions
def occasions(request):
    return render(request, 'home/occasions.html', {})

#articles
def articles(request):
    return render(request, 'home/articles.html', {})


#post_list
def post_list(request):
    object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(object_list, 3)  # 3 поста на каждой странице  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request, 'main/post_list.html', {'page': page,'posts': posts})    


#post_detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})


#post_new
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/post_edit.html', {'form': form})


#post_edit
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form})


#загрузка для админки файлов

urlpatterns = [
    path('',  include('home.urls')),
    path('admin/', admin.site.urls),
]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#doctors


def doctors(request):
    return render(request, 'main/doctors.html', {})

#doctor_page

def doctor_page(request):
    return render(request, 'main/doctor_page.html', {})

#contacts

def contacts(request):
    return render(request, 'main/contacts.html', {})

#docsl

def docsl(request):
    return render(request, 'main/docsl.html', {})

#insurance

def insurance(request):
    return render(request, 'main/insurance.html', {})

#job

def job(request):
    return render(request, 'main/job.html', {})

#promo

def promo(request):
    return render(request, 'main/promo.html', {})

#services

def services(request):
    return render(request, 'main/services.html', {})

#analyzes

def analyzes(request):
    return render(request, 'main/analyzes.html', {})

#analyzes_price

"""
def analyzes_price(request):
    object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(object_list, 10)  # 10 поста на каждой странице  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request, 'main/allclinic.html', {'page': page,'posts': posts})    
"""



