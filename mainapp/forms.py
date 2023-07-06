from django import forms
from .models import Comment, Publication


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['user', 'course', 'rating', 'comment']
        
#     def save(self, commit=True):
#         comment = super().save(commit=False)
#         if commit:
#             comment.save()
#         return comment


# class PublicationForm(forms.ModelForm):
#     class Meta:
#         model = Publication
#         fields = ['course', 'title', 'description', 'date', 'views', 'photos']
        
#     def save(self, commit=True):
#         publication = super().save(commit=False)
#         if commit:
#             publication.save()
#         return publication





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'  

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'  
