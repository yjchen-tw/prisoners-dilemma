from django import forms


class TournamentInfoForm(forms.Form):
    random_player = forms.IntegerField()
    cooperator = forms.IntegerField()
    betrayer = forms.IntegerField()
    tit_for_tat_player = forms.IntegerField()
