from django.shortcuts import render


def video(request, slug):
    videos = {'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': 'XLQRZCvTptk'},
              'laatus': {'titulo': 'Video A vergonha do erro vai ser a sua derrota ', 'youtube_id': 'Lw7CxTOxBpM'},
              }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
