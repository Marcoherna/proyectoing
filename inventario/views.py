from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def inventario_view(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = ProductoForm()
    return render(request, 'inventario/inventario.html', {'productos': productos, 'form': form})

def update_quantity(request, pk, action):
    producto = Producto.objects.get(pk=pk)
    if action == 'increase':
        producto.cantidad += 1
    elif action == 'decrease' and producto.cantidad > 0:
        producto.cantidad -= 1
    producto.save()
    return redirect('inventario')

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('inventario')