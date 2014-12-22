# Create your views here.
import datetime

from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import stripe
from django.contrib import auth
from django.core.context_processors import csrf
from CustomDrumSamples import settings
from userprofile.forms import *
from userprofile.models import *
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET


# def home(request):
#     title = "Pro Essentials Online Learning"
#     form = login(request)
#     return render_to_response('home_page.html', locals(), context_instance=RequestContext(request))
#
# def soon():
#   soon = datetime.date.today() + datetime.timedelta(days=30)
#   return {'month': soon.month, 'year': soon.year}
#
# def login(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#     else:
#         form = SignInForm()
#     return form
#
# def login2(request):
#     form = login(request)
#     next = request.GET.get('next')
#     return render_to_response('login.html', locals(), context_instance=RequestContext(request))
#
# def auth_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     # if there is no match then authenticate returns none.
#     user = auth.authenticate(username=username, password=password)
#     # Need to make this access the next value from Url and Redirect there if login was successful
#     if user is not None:
#         auth.login(request, user)
#         if request.POST.get('next'):
#             next = request.POST.get('next')
#             return HttpResponseRedirect(next)
#         else:
#             return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         return HttpResponseRedirect('/accounts/invalid')
#
# def logged_in(request):
#     form = login(request)
#     full_name = request.user.username
#     return render_to_response('logged_in.html', locals(), context_instance=RequestContext(request))
#
# def invalid_login(request):
#     form = login(request)
#     return render_to_response('invalid_login.html', locals(), context_instance=RequestContext(request))
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect("/accounts/loggedout/")
#
# def logged_out(request):
#     form = login(request)
#     return render_to_response('logged_out.html', locals(), context_instance=RequestContext(request))
#
# def register_user(request):
#     user = None
#     icon_list = ['assets/images/doctor-icon.png',
#              'assets/images/doctor-icon.png',
#              'assets/images/nurse-icon.png',
#              'assets/images/ekg-icon.png',
#              'assets/images/clipboard-icon.png',
#              'assets/images/arrow-right.png']
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             #This will save the registration information for the new user
#             user = User.objects.create_user(username=form.cleaned_data['username'],
#                                             email=form.cleaned_data['email'],
#                                             password=form.cleaned_data['password'],
#                                             first_name = form.cleaned_data['first_name'],
#                                             last_name = form.cleaned_data['last_name'],
#                                             )
#             customer = stripe.Customer.create(
#                 description = form.cleaned_data['email'],
#                 card = form.cleaned_data['stripe_token'],
#                 plan = 'basic'
#             )
#             userprofile = UserProfile(
#                 user = user,
#                 last_4_digits = form.cleaned_data['last_4_digits'],
#                 stripe_id = customer.id
#             )
#             userprofile.save()
#             return HttpResponseRedirect('/accounts/register_success')
#     else:
#         form = UserForm(initial={'first_name': 'Enter First Name',
#                              'last_name': 'Enter Last Name',
#                              'email': '',
#                              'username': '',
#                              'password': 'Enter Password',
#                              'repassword': 'Re-enter Password',
#                              'last_4_digits': '',
#                              'stripe_token': ''})
#     return render_to_response('register_user.html',
#     {
#         'form': form,
#         'months': range(1, 13),
#         'publishable': settings.STRIPE_PUBLISHABLE,
#         'soon': soon(),
#         'user': user,
#         'years': range(2011, 2036),
#         'icon_list': icon_list,
#     }, context_instance=RequestContext(request)
#     )
#
# def register_success(request):
#     return render_to_response('register_success.html', locals(), context_instance=RequestContext(request))
#
# def reactivate(request):
#     return render_to_response('user_not_active.html', locals(), context_instance=RequestContext(request))
#
# @login_required
# def user_profile(request):
#     if request.method == 'POST':
#         form = CardForm(request.POST)
#         if form.is_valid():
#             customer = stripe.Customer.retrieve(user.stripe_id)
#             customer.card = form.cleaned_data['stripe_token']
#             customer.save()
#             request.user.profile.last_4_digits = form.cleaned_data['last_4_digits']
#             request.user.profile.stripe_id = customer.id
#             request.user.profile.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = CardForm()
#     return render_to_response('user_profile.html',
#     {
#         'form': form,
#         'publishable': settings.STRIPE_PUBLISHABLE,
#         'soon': soon(),
#         'months': range(1, 12),
#         'years': range(2011, 2036),
#         'request': request,
#     },
#       context_instance=RequestContext(request))
#====================================================================


























