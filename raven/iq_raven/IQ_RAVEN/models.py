# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

# </standard imports>

author = 'Thorben Woelk'

doc = """
Raven IQ Test. 10 Raven matrices to be solved by participants.
Solutions are 5, 6, 6, 4, 5, 3, 2, 6, 8, 2.
"""


class Constants(BaseConstants):
    name_in_url = 'iq_raven'
    players_per_group = None
    num_rounds = 1

    numbers = range(1, 11, 1)

    SCALE = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'),
             (7, '7'), (8, '8')]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    correct_answers = models.IntegerField()

    # Screen: Raven
    i = None
    # Loop: From 1 to 10
    for i in Constants.numbers:
        # Add: Variables for every step to data base (not nice, but it works)
        locals()[f'raven_{i}'] = models.IntegerField(
            choices=Constants.SCALE,
            verbose_name='Which one is correct?',
            blank=True,
            widget=widgets.RadioSelectHorizontal
        )
    # Delete: Auxiliary variables to prevent oTree error
    del i

    def set_payoff_raven(self):
        """ Calculate the player's payoff for the raven task. """
        iq_solution = [5, 6, 6, 4, 5, 3, 2, 6, 8, 2]
        pp_solutions = [
            self.raven_1,
            self.raven_2,
            self.raven_3,
            self.raven_4,
            self.raven_5,
            self.raven_6,
            self.raven_7,
            self.raven_8,
            self.raven_9,
            self.raven_10,
        ]
        list_correct = [x for x, y in zip(iq_solution, pp_solutions) if x == y]
        self.correct_answers = len(list_correct)
        self.payoff = self.session.config[
                          'raven_incentive'] * self.correct_answers
