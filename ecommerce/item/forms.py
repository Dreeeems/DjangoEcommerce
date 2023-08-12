from django import forms

from .models import Item

INPUT_CLASSES='bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class NewItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('category','name','description','price','image',)
        widgets = {
            'category': forms.Select(attrs={
                'class':INPUT_CLASSES,
              'id':'category'
            },),
              'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES,
              'id':'name'
            },),
              'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES,
              'id':'description'
            },)
            ,  'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES,
              'id':'price'
            },),
              'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES,
                'id':'image'
              
            },)
        }


class EditItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('name','description','price','image','is_sold')
        widgets = {
            'category': forms.Select(attrs={
                'class':INPUT_CLASSES,
              'id':'category'
            },),
              'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES,
              'id':'name'
            },),
              'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES,
              'id':'description'
            },)
            ,  'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES,
              'id':'price'
            },),
              'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES,
                'id':'image'
              
            },)
        }
