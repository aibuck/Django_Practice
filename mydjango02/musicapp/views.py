from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet, Q

import json
from urllib.request import urlopen
from musicapp.models import Song
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
  query = request.GET.get("query", "").strip()

  song_qs : QuerySet[Song] = Song.objects.all()

  if query:
    song_qs = song_qs.filter(
      Q(name__icontains=query)
      |Q(artist_name__icontains=query)
      |Q(album_name__icontains=query)
    )
  return render(
    request=request,
    template_name='musicapp/index.html',
    context={
      'song_list': song_qs,
      'query' : query,
    }

  )