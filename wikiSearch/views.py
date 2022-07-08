from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util
import random

error = False
def index(request, name):
    filename = util.list_entries()
    if name in filename:
        return render(request, "wikiSearch/index.html", {
            'name': name,
            'data': util.get_entry(name)
        })
    else:
        error=True
        return render(request, "wikiSearch/index.html", {
            'name':name,
            'error':error
        })
        
def edit(request, name):
    if request.method == "GET":
        filename = util.list_entries()
        if name in filename:
            return render(request, "wikiSearch/edit.html", {
                'name': name,
                'data': util.get_entry(name)
            })
    elif request.method == "POST":
        form = request.POST
        description = form["description"]
        util.save_entry(name, description)
        return HttpResponseRedirect("../" + name)