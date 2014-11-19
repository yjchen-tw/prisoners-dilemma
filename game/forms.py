from django import forms

import player

FORM_FIELD_TO_PLAYER_OBJECT = {
    'random_player': player.Player,
    'cooperator': player.Cooperator,
    'betrayer': player.Betrayer,
    'tit_for_tat_player': player.TitForTatPlayer,
}


class TournamentInfoForm(forms.Form):
    random_player = forms.IntegerField(min_value=0)
    cooperator = forms.IntegerField(min_value=0)
    betrayer = forms.IntegerField(min_value=0)
    tit_for_tat_player = forms.IntegerField(min_value=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        if sum(cleaned_data.values()) > 30:
            raise forms.ValidationError(
                "Too much players, number of total players should less than 30.")
        return cleaned_data
