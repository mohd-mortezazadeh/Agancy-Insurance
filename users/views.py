from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import DeleteView

from users.forms import ProfileForm
from users.models import Profile

User = get_user_model()




class UserListView(LoginRequiredMixin, ListView):

    model = User
    template_name="dashboard/user/list.html"
    context_object_name = 'users'
    paginate_by = 20
    permission_required = "user.view_user"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = "لیست کاربران"
        return context 

    def handle_no_permission(self):
        messages.warning(self.request, "شما اجازه دسترسی به این صفحه رو ندارید")
        return redirect("dashboard:home")


@method_decorator(csrf_exempt, name='dispatch')
class DeleteUserView(SuccessMessageMixin,PermissionRequiredMixin, LoginRequiredMixin, DeleteView):

    model = User
    template_name = 'dashboard/user/list.html'
    success_url = reverse_lazy('user:list')
    success_message = "کاربر با موفقیت حذف گردید"
    permission_required = "user.delete_user"

    def handle_no_permission(self):
        messages.warning(self.request, "شما اجازه دسترسی به این صفحه رو ندارید")
        return redirect("dashboard:home")

    def get(self, request, *args, **kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            post_object = User.objects.get_queryset().filter(pk= pk)
            if post_object is not None:
                post_object.delete()
                messages.success(request, 'کاربر با موفقیت حذف گردید.') 
                return redirect('user:user-list')
        return redirect('dashboard/user/list.html')
    


class ProfileView(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "user.create_user"
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'پروفایل'}
        return render(request, 'dashboard/user/create.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=self.profile)
            if form.is_valid():
                profile = form.save()
                profile.user.first_name = form.cleaned_data.get('first_name')
                profile.user.last_name = form.cleaned_data.get('last_name')
                profile.user.email = form.cleaned_data.get('email')
                profile.user.mobile = form.cleaned_data.get('mobile')
                profile.user.save()
                messages.success(request, 'پروفایل با موفقیت ایجاد گردید')
                return redirect('user:user-create')
            else:
                messages.warning(request, 'فرم ارسالی شما مشکل دارد')
                return redirect('user:user-create')

            



@method_decorator(csrf_exempt, name='dispatch')
class ProfileUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    segment = "پروفایل"
    title = "پروفایل"
    model = User
    template_name= 'frontend/accounts/profile.html'
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        user = form.save(commit = False)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.profile.phone = form.cleaned_data['phone']
        user.profile.mobile = form.cleaned_data['mobile']
        user.profile.code = form.cleaned_data['code']
        user.profile.address = form.cleaned_data['address']
        user.profile.zip = form.cleaned_data['zip']
        user.profile.avatar = form.cleaned_data['avatar']
        user.save()
        messages.success(self.request, 'پروفایل با موفقیت آپدیت شد!')
        return redirect('user:user-update', pk=user.pk,)
        

@method_decorator(csrf_exempt, name='dispatch')
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'frontend/accounts/password_change.html'
    success_message = "پسوردتان با موفقیت تغیرر یافت"
    success_url = reverse_lazy('user:password_change')

