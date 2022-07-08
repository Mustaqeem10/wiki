from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import util
from random import randrange, choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newForm(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newForm.html")
    elif request.method == "POST":
        form = request.POST
        title = form["title"]
        if title in util.list_entries():
            return render(request,"encyclopedia/newForm.html", {
                "error": "Value is already included in encyclopedia!"
            })
        else:
            util.save_entry(title, form["description"])
            return HttpResponseRedirect("wiki/" + title )

def random(request):
    filenames = util.list_entries()
    # rand_idx = randrange(len(filenames))
    # random_name = filenames[rand_idx]
    random_name = choice(filenames)
    return HttpResponseRedirect("wiki/" + random_name)

def search(request):
    form = request.POST
    if request.method == "POST":
        form = request.POST
        name = form["title"]
        # return render(request, "wiki/" + name)
        return HttpResponseRedirect("wiki/" + name)





