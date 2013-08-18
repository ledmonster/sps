import json
from django.http import HttpResponse
from publisher.models import Article

def articles(request, application_name):
    articles = Article.objects\
        .filter(application_id=application_name)\
        .filter(is_active=True)\
        .order_by('-created_at')

    response_data = [{'id': a.id, 'title': a.title, 'content': a.content,
                      'created_at': a.created_at.strftime("%Y-%m-%d %H:%M:%S")}
                     for a in articles]

    return HttpResponse(json.dumps(response_data, ensure_ascii=False),
                        content_type="application/json; charset=utf-8")
