from django import forms

import player

FORM_FIELD_TO_PLAYER_OBJECT = {
    'random_player': player.Player,
    'cooperator': player.Cooperator,
    'betrayer': player.Betrayer,
    'tit_for_tat_player': player.TitForTatPlayer,
}


class TournamentInfoForm(forms.Form):
    random_player = forms.IntegerField()
    cooperator = forms.IntegerField()
    betrayer = forms.IntegerField()
    tit_for_tat_player = forms.IntegerField()
