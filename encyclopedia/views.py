from django.shortcuts import render
import markdown
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_md(title):
    return markdown.markdown(title)

def show_entry(request, title):
    entry = None
    if util.get_entry(title) == None:
        entry = None
        return render (request, "encyclopedia/title.html", {
            "entry" : convert_md(entry)
        })
    else:
        entry = util.get_entry(title)
        return render (request, "encyclopedia/title.html", {
            "entry" : convert_md(entry),
            "title" : title
        })

def show_entry_search(request):
    q = request.GET.get('q')
    entries_list = util.list_entries()
    entry_found = None
    for entry in entries_list:
        if q in entry:
            entry_found = entry
            break
        else:
            entry_found = None
    if not entry_found == None:
        return show_entry(request, entry_found)
    else:
        return index(request)

def new_entry(request):
    return render(request, "encyclopedia/newentry.html")

def save(request):
    infos = request.POST.get('info')
    title = request.POST.get('title')
    entries_list = util.list_entries()
    if title in entries_list:
        return render(request, "encyclopedia/newentry.html", {
            "error" : "Already found",
            "title" : title
        })
    elif title not in entries_list:
        util.save_entry(title, infos)
        return show_entry(request, title)

def edit(request):
    title = request.POST.get('title')
    info = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "info" : info,
        "title" : title
    })

def save_edit(request):
    info = request.POST.get('info')
    title = request.POST.get('title')
    util.save_entry(title, info)
    return show_entry(request, title)

def random_title(request):
    entries_list = util.list_entries()
    random_title = random.choice(entries_list)
    return show_entry(request, random_title)