from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    allpat = Product.objects.all()
    pdt = {'patient': allpat}
    return render(request, 'mytestbasic/dashbord.html', pdt)

def table(request):
    return render(request, 'mytestbasic/table.html')



def dashboard(request):
    allpat = Product.objects.all()
    pdt = {'patient': allpat}
    return render(request, 'mytestbasic/dashbord.html', pdt)


def form(request):
    if (request.method == 'POST'):
        patient = request.POST["fname"]
        healthcare = request.POST["healthcare"]
        fee = request.POST["number"]
        desc = request.POST["message"]
        p = Product(patient_name=patient,
                    health_care=healthcare, Fee=fee, desc=desc)
        p.save()
        allpat = Product.objects.all()
        pdt = {'patient': allpat}
        return redirect('/mytestbasic/dashboard/', pdt)
    return render(request, 'mytestbasic/form.html')

# red_date = models.DateField(default=date.today())
#     customer_id = models.AutoField(primary_key=True)
#     patient_name = models.CharField(max_length=50)
#     health_care = models.CharField(max_length=50, default="")
#     Fee = models.IntegerField(default=0)
#     desc = models.CharField(max_length=3000)


def customer_id(request, cus_id):
    if(request.method == 'POST'):
        patient = request.POST["patient_name"]
        healthcare = request.POST["health_care"]
        fee = request.POST["Fee"]
        desc = request.POST["desc"]
        product = Product.objects.get(customer_id=cus_id)
        product.patient_name = patient
        product.health_care = healthcare
        product.Fee = fee
        product.desc = desc
        product.save()
        allpat = Product.objects.all()
        pdt = {'patient': allpat}
        return redirect('/mytestbasic/dashboard/', pdt)
    product = Product.objects.filter(customer_id=cus_id)
    return render(request, 'mytestbasic/edit.html', {'blog': product[0]})

def delete_patient(request, cus_id):
    product = Product.objects.get(customer_id=cus_id)
    product.delete()
    allpat = Product.objects.all()
    pdt = {'patient': allpat}
    return redirect('/mytestbasic/dashboard/', pdt)