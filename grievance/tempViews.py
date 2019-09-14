# from django.shortcuts import render
# from django.views import generic
# from django.utils.decorators import method_decorator

# from django.contrib.auth.decorators import login_required
# from grievance.customDecorator import cmo_required

# class CMO(generic.TemplateView):
# 	def get(self, request, *args, **kwargs):
# 		# current_user=request.user
# 		# if(current_user.is_authenticated):
# 		# 	if(UserType.objects.get(user=current_user).token == constants.UserType.CMO.value):
# 		# 		print("Success")k
# 		print(request.GET.get("type"))
# 		# print(type1)
# 		print("hello\n")
# 		print(kwargs['type'])
# 		return cmoViews.CMO().get(self, self.request, args, kwargs)

# @method_decorator([login_required,cmo_required], name='dispatch')
# class TEMP(generic.TemplateView):
# 	# @login_required
# 	def get(self, request, *args, **kwargs):
# 		print("inside temp function = ",request.user)
# 		return render(request,"grievance/cmoHomePage.html")

# class loginTimeoutRedirect(generic.TemplateView):
# 	def get(self, request, *args, **kwargs):
# 		return redirect('/ps-grievance/accounts/login')
