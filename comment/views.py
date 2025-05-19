# comments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Anime
from .forms import CommentForm

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    comments = anime.comment_set.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.anime = anime
            comment.user = request.user
            comment.save()
            return redirect('anime_detail', anime_id=anime.id)
    else:
        form = CommentForm()
    return render(request, "anime-details.html", {
        "anime": anime,
        "comments": comments,
        "form": form,
    })
