from django.core.cache import cache
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question=models.TextField()
    answer=RichTextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def get_translation(self,lang_code):

        cache_key=f"faq_{self.id}_{lang_code}"
        cached_translation=cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translator=Translator()
        translated_data={
            'question':translator.translate(self.question,dest=lang_code).text,
            'answer':translator.translate(self.answer,dest=lang_code).text
        }
        cache.set(cache_key,translated_data,timeout=86400)
        return translated_data

    def __str__(self):
        return self.question[:100]