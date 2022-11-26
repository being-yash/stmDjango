from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# To Add new record
def addShow(request):
	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			#'name', 'studentClass', 'rollNo', 'phone', 'email', 'password'
			name = fm.cleaned_data['name']
			studentClass = fm.cleaned_data['studentClass']
			rollNo = fm.cleaned_data['rollNo']
			phone = fm.cleaned_data['phone']
			email = fm.cleaned_data['email']
			password = fm.cleaned_data['password']
			reg = Student(name=name, studentClass=studentClass, rollNo=rollNo, phone=phone, email=email, password=password)
			reg.save()
			fm = StudentRegistration()
	else:
		fm = StudentRegistration()
	students = Student.objects.all()
	return render(request, 'stm/addandshow.html', {'form':fm, 'students':students})

def updateStudent(request, id):
	#def update_data(request, id):
	if request.method == 'POST':
		pi = Student.objects.get(pk=id)
		fm = StudentRegistration (request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
			return HttpResponseRedirect('/')
	else:
		pi = Student.objects.get(pk=id)
		fm = StudentRegistration(instance=pi)
		return render(request, 'stm/updatestudent.html', {'form':fm})

#to delete a record
def delete_student(request, id):
	if request.method == 'GET':
		student = Student.objects.get(pk=id)
		student.delete()
		return HttpResponseRedirect('/')
