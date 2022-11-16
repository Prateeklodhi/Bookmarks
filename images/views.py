from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST 
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def image_created(request):
    if request.method == 'POST':
        #from is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            #assign current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(request,'Image added successfully.')
            return redirect(new_image.get_absolute_url())
    else:
        #build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request,'images/image/create.html',{'section':'images','form':form})    

def image_detail(request,id,slug):
    image = get_list_or_404(Image,id=id,slug =slug)
    return render(request,'images/image/detail.html',{'section':'images','image':image})

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try :
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'} )
        except Image.DoesNotExist:
            pass
        return JsonResponse({'status':'ok'}) 


@login_required
def image_list(request):
    image = Image.objects.all()
    paginator = Paginator(image, 8)
    page = request.GET.get('page')
    image_only = request.GET.get('image_only')
    try:
        image = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if image_only:
            # if ajax request and page out of range
            # return an empty
            return HttpResponse('')
        # if page out of range return last page of results
        image = paginator.page(paginator.num_pages)
    if image_only:
        return render(request,'image/image/list_images.html',{'section':'image','images':'image'})
    return render(request,'image/image/list_images.html',{'section':'image','images':'image'})