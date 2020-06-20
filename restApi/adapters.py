from allauth.account.adapter import DefaultAccountAdapter

class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        email = data.get('email')
        name = data.get('name')
        surname = data.get('surname')
        phone_number = data.get('phone_number')
        isEmployer = data.get('isEmployer')
        if email:
            setattr(user, 'email', email)
        if name:
            setattr(user, 'name', name)
        if surname:
            setattr(user, 'surname', surname)
        if phone_number:
            setattr(user, 'phone_number', phone_number)
        if isEmployer:
            setattr(user, 'isEmployer', isEmployer)
        return super().save_user(request, user, form, commit = commit)