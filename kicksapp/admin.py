from django.contrib import admin
from .models import (
    Image, Shoes, Jacket, Category, JacketCategory,
    ShirtCategory, Shirt, DummyUpload, Cart_Items,
    Comment, logo, ChatSpace, Message
)
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

class ReplyForm(forms.Form):
    reply_message = forms.CharField(widget=forms.Textarea, label="Reply Message")

class MessageAdmin(admin.ModelAdmin):
    list_display = ('space', 'user', 'time', 'message')
    search_fields = ('user', 'message')
    list_filter = ('space',)
    ordering = ('-time',)
    actions = ['reply_to_message']

    def has_change_permission(self, request, obj=None):
 
        return True

    def reply_to_message(self, request, queryset):
      if 'action' in request.POST and request.POST['action'] == 'reply_to_message':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_message = form.cleaned_data['reply_message']
            print(reply_message)
            for message in queryset:
                Message.objects.create(
                    space=message.space,
                    user=request.user,  
                    message=reply_message
                )
            self.message_user(request, "Reply sent successfully.")
            return HttpResponseRedirect(reverse('admin:kicksapp_message_changelist'))
      else:
        form = ReplyForm()

      context = {
        'form': form,
        'queryset': queryset,
        'title': 'Reply to selected messages'
    }
      return render(request, "reply_form.html", context)

    reply_to_message.short_description = "Reply to selected messages"

class ChatSpaceAdmin(admin.ModelAdmin):
    list_display = ('space', 'user')

# Registering models with the admin site
admin.site.register(Image)
admin.site.register(Shoes)
admin.site.register(Jacket)
admin.site.register(Shirt)
admin.site.register(Category)
admin.site.register(JacketCategory)
admin.site.register(ShirtCategory)
admin.site.register(DummyUpload)
admin.site.register(Cart_Items)
admin.site.register(Comment)
admin.site.register(logo)
admin.site.register(ChatSpace, ChatSpaceAdmin)
admin.site.register(Message, MessageAdmin)