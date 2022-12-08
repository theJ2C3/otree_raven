# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return {
        'raven_incentive': c(self.session.config['raven_incentive']),
    }


class IntroRaven(Page):
    pass


class Raven(Page):
    timeout_seconds = 600

    form_model = models.Player
    form_fields = ['raven_{}'.format(i) for i in range(1, 11)]

    def before_next_page(self):
        """" Store participant's answers if timeout happened. """
        if self.timeout_happened:
            post_dict = self.request.POST
            self.player.raven_1 = int(post_dict.get('raven_1')) if post_dict.get('raven_1') is not None else None
            self.player.raven_2 = int(post_dict.get('raven_2')) if post_dict.get('raven_2') is not None else None
            self.player.raven_3 = int(post_dict.get('raven_3')) if post_dict.get('raven_3') is not None else None
            self.player.raven_4 = int(post_dict.get('raven_4')) if post_dict.get('raven_4') is not None else None
            self.player.raven_5 = int(post_dict.get('raven_5')) if post_dict.get('raven_5') is not None else None
            self.player.raven_6 = int(post_dict.get('raven_6')) if post_dict.get('raven_6') is not None else None
            self.player.raven_7 = int(post_dict.get('raven_7')) if post_dict.get('raven_7') is not None else None
            self.player.raven_8 = int(post_dict.get('raven_8')) if post_dict.get('raven_8') is not None else None
            self.player.raven_9 = int(post_dict.get('raven_9')) if post_dict.get('raven_9') is not None else None
            self.player.raven_10 = int(post_dict.get('raven_10')) if post_dict.get('raven_10') is not None else None


class Results(Page):
    def vars_for_template(self):
        self.player.set_payoff_raven()


page_sequence = [
    IntroRaven,
    Raven,
    Results
]
