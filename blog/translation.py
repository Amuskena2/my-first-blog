# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from .models import Post


class MyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'text')   # Select here the fields you want to translate
translator.register(Post, MyModelTranslationOptions)
