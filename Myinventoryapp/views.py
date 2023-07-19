from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def view_supplier(request, pk):
    sObjects= Supplier.objects.all()
    v = get_object_or_404(Account, pk=pk)
    return render(request, 'Myinventoryapp/view_supplier.html', {'suppliers':sObjects, 'v':v})

def view_bottles(request, pk):
    bObjects = WaterBottle.objects.all()
    v = get_object_or_404(Account, pk=pk)
    return render(request, 'Myinventoryapp/view_bottles.html', {'bottles':bObjects, 'v':v})

def view_bottle_details(request, pk, pk1):
    v = get_object_or_404(Account, pk=pk1)
    b = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'Myinventoryapp/view_bottle_details.html', {'b':b, 'v':v})

def add_bottle(request, pk):
    v = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        n_sku = request.POST.get('sku')
        n_brand = request.POST.get('brand')
        n_cost = request.POST.get('cost')
        n_size = request.POST.get('size')
        n_mouthsize = request.POST.get('mouth')
        n_color = request.POST.get('color')
        n_suppliedby = request.POST.get('supp')
        n_currentq = request.POST.get('quant')
        # avail_supplier = WaterBottle.objects.filter(Supplied_by__Name=n_suppliedby).values("Supplied_by")
        avail_supplier = get_object_or_404(Supplier, Name = n_suppliedby)

        WaterBottle.objects.create(SKU = n_sku, Brand = n_brand, Cost = n_cost, Size = n_size, Mouth_Size = n_mouthsize, Color = n_color, Supplied_by = avail_supplier, Current_Quantity = n_currentq)
        return redirect('view_bottles', pk=pk)
    
    else:
        return render(request, 'Myinventoryapp/add_bottle.html', {'v':v})
    
def delete_bottle(request, pk, pk1):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles', pk=pk1)

#-----------------------------------------------------------------------------------------------------------------------#
# For the Login/Register Feature #
# When doing forms, we use "POST", since we might change something that involves the database
def SignIn(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        passw = request.POST.get('password')

        try:
            x = get_object_or_404(Account, acc_user = user, acc_pass = passw)
            return redirect('view_supplier', pk=x.pk)
        
        except:
            return redirect('SignIn_Error')
        
    else:
        return render(request, 'Myinventoryapp/signin.html')
    
def Register(request):
    if request.method == 'POST':

        try:
            user = request.POST.get('n_username')
            passw = request.POST.get('n_password')
            Account.objects.create(acc_user = user, acc_pass = passw)
            x_new = get_object_or_404(Account, acc_user = user)
            return render(request, 'Myinventoryapp/register.html')
        
        except:
            Account.objects.filter(acc_user = user, acc_pass = passw).delete()
            return redirect('Register_Error')
        
    else:
        return render(request, 'Myinventoryapp/register_base.html')
    
def ManageAcc(request, pk):
    v = get_object_or_404(Account, pk=pk)
    return render(request, 'Myinventoryapp/manageacc.html', {'v':v})

def DeleteAcc(request, pk):
    Account.objects.filter(pk=pk).delete()
    return redirect('SignIn')

def ChangePass(request, pk):
    v = get_object_or_404(Account, pk=pk)
    return render(request, 'Myinventoryapp/changepass.html', {'v':v})

def NewPass(request, pk):

    if request.method == 'POST':
        old_passw = request.POST.get('current_passw')
        new_passw = request.POST.get('new_passw')
        passw_verify = request.POST.get('new_passw2')

        try:
            idk_another_x = get_object_or_404(Account, acc_pass = old_passw)
            if new_passw == passw_verify:
                Account.objects.filter(pk=pk).update(acc_pass = new_passw)
                return redirect('ManageAcc', pk=pk)
            
            else:
                v = get_object_or_404(Account, pk=pk)
                return render(request, 'Myinventoryapp/newpass_error.html', {'v':v})
        
        except:
            v = get_object_or_404(Account, pk=pk)
            return render(request, 'Myinventoryapp/newpass_error.html', {'v':v})
             
    else:
        return redirect('ChangePass', pk=pk)

def SignIn_Error(request):
    return render(request, 'Myinventoryapp/signin_error.html')

def Register_Error(request):
    return render(request, 'Myinventoryapp/register_error.html')
    
def SignOut(request):
    request.session.flush()
    return redirect("SignIn")
    