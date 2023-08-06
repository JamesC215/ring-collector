from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ring, Owner
from .forms import CleaningForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def rings_index(request):
    rings = Ring.objects.all()
    return render(request, 'rings/index.html', {
        'rings': rings
    })

def rings_detail(request, ring_id):
  ring = Ring.objects.get(id=ring_id)
  id_list = ring.owners.all().values_list('id')
  owners_ring_doesnt_have = Owner.objects.exclude(id__in=id_list)
  cleaning_form = CleaningForm()
  return render(request, 'rings/detail.html', { 'ring': ring, 'cleaning_form': cleaning_form, 'owners': owners_ring_doesnt_have })


class RingCreate(CreateView):
    model = Ring
    fields = ['name', 'owner', 'description']
    success_url = '/rings'

class RingUpdate(UpdateView):
    model = Ring
    fields = ['owner', 'description']

class RingDelete(DeleteView):
    model = Ring
    success_url = '/rings'

def add_cleaning(request, ring_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.ring_id = ring_id
        new_cleaning.save()
    return redirect('detail', ring_id=ring_id)

class OwnerList(ListView):
  model = Owner

class OwnerDetail(DetailView):
  model = Owner

class OwnerCreate(CreateView):
  model = Owner
  fields = '__all__'

class OwnerUpdate(UpdateView):
  model = Owner
  fields = ['name', 'race']

class OwnerDelete(DeleteView):
  model = Owner
  success_url = '/owners'

def assoc_owner(request, ring_id, owner_id):
  Ring.objects.get(id=ring_id).owners.add(owner_id)
  return redirect('detail', ring_id=ring_id)

def remove_owner(request, ring_id, owner_id):
  Ring.objects.get(id=ring_id).owners.remove(owner_id)
  return redirect('detail', ring_id=ring_id)