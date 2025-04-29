from django.contrib import admin
from .models import login, document_detail, document_security_technique
from .models import contact_detail,Feedback_Detail,privillaged_document

# Register your models here.



class showlogin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','password', 'role')


admin.site.register(login, showlogin)


class showdocument_detail(admin.ModelAdmin):
    list_display = ('l_id', 'd_name', 'd_description', 'd_type', 'security_id', 'password', 'document', 'timestamp')


admin.site.register(document_detail, showdocument_detail)

admin.site.register(document_security_technique)


class showcontact_detail(admin.ModelAdmin):
    list_display = ('phone', 'email', 'message', 'timestamp')


admin.site.register(contact_detail, showcontact_detail)


class showfeedback_detail(admin.ModelAdmin):
    list_display = ('l_id', 'comment', 'rating', 'timestamp')


admin.site.register(Feedback_Detail, showfeedback_detail)


class showprivillaged_Document(admin.ModelAdmin):
    list_display = ('d_id', 'l_id', 'demail', 'privillage_status', 'timestamp')


admin.site.register(privillaged_document, showprivillaged_Document)