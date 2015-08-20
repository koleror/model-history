from django import forms


class ModelHistoryForm(forms.ModelForm):
    def save(self, commit=True, user=None):
        self.instance.save_model(user=user)
