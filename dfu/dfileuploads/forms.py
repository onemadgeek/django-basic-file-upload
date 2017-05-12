from django import forms



class FileUploadForm(forms.Form):
    file = forms.FileField(
        label='',widget=forms.FileInput(attrs={'class' : 'input'})
    )

    class Meta:
        fields = ['file',]
        
    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()
        print cleaned_data
        if cleaned_data:
            if False:
                #Handle Invalid File Type.
                print "Uploaded file type is not supported."
                raise forms.ValidationError('Please upload a valid file type.')
        else:
            raise forms.ValidationError('Please upload a valid file.')
        return cleaned_data