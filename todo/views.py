#from django.shortcuts import get_object_or_404
#from django.views.generic import UpdateView
#from django.views.generic import FormView
from django.shortcuts import render
#from django.urls import reverse
from datetime import date
from django.http import HttpResponse
from django.template import loader
from .models import Todo
    #,UserProfile,UserProfileForm
from .forms import EditProfileForm

# Create your views here.


def home(request):
    return render(request, 'Home.html')


def general(request):
    todolist = Todo.objects.all()
    template = loader.get_template('General.html')
    context = {
        'todolist': todolist,
    }

    return HttpResponse(template.render(context,request))









def add(request):
    return render(request, 'AddTask.html')


def detail(request,items_id):
    todolist = Todo.objects.get(pk=items_id)
    template = loader.get_template('details.html')
    context = {
        'todolist': todolist,
    }

    return HttpResponse(template.render(context,request))

def edit_task(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.Todo)

        if form.is_valid():
            form.save()
            return #
        else:
            form = EditProfileForm(instance=request.Todo)
            args = {'form' : form}
            return  render(request,'editProfile.html',args)




def genral_delete(request, items_id):
    item = Todo.objects.get(pk=items_id)
    item.deletion = True
    item.save()
    todolist = Todo.objects.all()
    template = loader.get_template('General.html')
    context = {
        'todolist': todolist,
    }
    return HttpResponse(template.render(context,request))



def add_Task(request):
    template = loader.get_template('General.html')
    title = request.POST['title']
    desc = request.POST['description']
    time = request.POST['time']
    createDate = request.POST['createTime']
    updateDate = date.today()
    delet = False
    status= request.POST['status']
    todo_item = Todo(title=title,status =status, description=desc, Time=time, created=createDate, updated=updateDate, deletion=delet)
    todo_item.save()

    return render(request, 'AddTask.html')
"""
##################################################################################################
class NewUserProfileView(FormView):
    template_name = "user_profile.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('details.html')



class EditUserProfileView(UpdateView):              #Note that we are using UpdateView and not FormView
    model = UserProfile
    form_class = UserProfileForm
    template_name = "user_profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(Todo, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse('details.html')


"""