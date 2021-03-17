from django import forms
from .models import data, steps

class creatation(forms.Form):
    title = forms.CharField(label='Tiêu đề', max_length=100)
    author = forms.CharField(label='Tác giả', max_length=20)
    step1 = forms.CharField(label='Bước 1', max_length=300)
    #img1 = forms.ImageField(label='Ảnh minh họa')
    step2 = forms.CharField(label='Bước 2', max_length=300)
    #img2 = forms.ImageField(label='Ảnh minh họa')
    step3 = forms.CharField(label='Bước 3', max_length=300)
    #img3 = forms.ImageField(label='Ảnh minh họa')
    step4 = forms.CharField(label='Bước 4', max_length=300)
    #img4 = forms.ImageField(label='Ảnh minh họa')

    def update_data(self):
        a = data()
        step = steps.objects.all()
        a.title = self.cleaned_data['title']
        a.author_name = self.cleaned_data['author']
        num = 4
        a.num_of_steps = num
        s = ''

        b1 = steps()
        b1.step = self.cleaned_data['step1']
        b1.save()
        id = step[len(step) - 1].id
        s = s + str(id) + ' '

        b2 = steps()
        b2.step = self.cleaned_data['step2']
        b2.save()
        s = s + str(id + 1) + ' '

        b3 = steps()
        b3.step = self.cleaned_data['step3']
        b3.save()
        s = s + str(id + 2) + ' '

        b4 = steps()
        b4.step = self.cleaned_data['step4']
        b4.save()
        s = s + str(id + 3) + ' '

        a.steps_address = s
        a.save()

        return s

