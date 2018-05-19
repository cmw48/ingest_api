from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Paper(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    record_id = models.CharField(max_length=100, blank=True, default='')
    article_doi = models.CharField(max_length=100, blank=True, default='')
    journal_publication = models.CharField(max_length=100, blank=True, default='')
    publication_date = models.CharField(max_length=100, blank=True, default='')
    publication_issue = models.CharField(max_length=100, blank=True, default='')
    author_fn = models.CharField(max_length=100, blank=True, default='')
    author_ln= models.CharField(max_length=100, blank=True, default='')
    author_email = models.CharField(max_length=100, blank=True, default='')
    article_title = models.CharField(max_length=100, blank=True, default='')
    papertext = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
