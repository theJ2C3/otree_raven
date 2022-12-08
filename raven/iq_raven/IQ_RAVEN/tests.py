# -*- coding: utf-8 -*-
from __future__ import division

import random

from otree.common import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):
    """Bot that plays one round"""

    def play_round(self):
        yield (pages.IntroRaven)

        yield Submission(pages.Raven, {
            'raven_1': random.randint(1, 8),
            'raven_2': random.randint(1, 8),
            'raven_3': random.randint(1, 8),
            'raven_4': random.randint(1, 8),
            'raven_5': random.randint(1, 8),
            'raven_6': random.randint(1, 8),
            'raven_7': random.randint(1, 8),
            'raven_8': random.randint(1, 8),
            'raven_9': random.randint(1, 8),
            'raven_10': random.randint(1, 8),
        }, check_html=False)

        yield (pages.Results)
