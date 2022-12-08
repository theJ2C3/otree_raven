from otree.api import *
# import requests

author = 'Thorben Woelk'

doc = """
adjusted to suit otree 5 by Jay
Raven IQ Test. 10 Raven matrices to be solved by participants.
Solutions are 5, 6, 6, 4, 5, 3, 2, 6, 8, 2.
"""

class C(BaseConstants):

    NAME_IN_URL = 'iq_raven'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

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
    # i = None
    # Loop: From 1 to 10
    for i in C.numbers:
        # Add: Variables for every step to data base (not nice, but it works)
        locals()[f'raven_{i}'] = models.IntegerField(
            choices=C.SCALE,
            # verbose_name='Which one is correct?',
            verbose_name='哪一個選項是正確的?',
            blank=True,
            widget=widgets.RadioSelectHorizontal
        )
    # Delete: Auxiliary variables to prevent oTree error
    del i

    def set_payoff_raven(self):
        """ Calculate the player's payoff for the raven task. """
        iq_solution = [5, 6, 6, 4, 5, 3, 2, 6, 8, 2]
        pp_solutions = [
            self.field_maybe_none('raven_1'),
            self.field_maybe_none('raven_2'),
            self.field_maybe_none('raven_3'),
            self.field_maybe_none('raven_4'),
            self.field_maybe_none('raven_5'),
            self.field_maybe_none('raven_6'),
            self.field_maybe_none('raven_7'),
            self.field_maybe_none('raven_8'),
            self.field_maybe_none('raven_9'),
            self.field_maybe_none('raven_10'),
        ]
        # pp_solutions = [
        #     self.raven_1,
        #     self.raven_2,
        #     self.raven_3,
        #     self.raven_4,
        #     self.raven_5,
        #     self.raven_6,
        #     self.raven_7,
        #     self.raven_8,
        #     self.raven_9,
        #     self.raven_10,
        # ]
        list_correct = [x for x, y in zip(iq_solution, pp_solutions) if x == y]
        self.correct_answers = len(list_correct)
        self.payoff = 1 * self.correct_answers



# PAGES

# def vars_for_all_templates(self):
#     return {
#         'raven_incentive': cu(self.session.config['raven_incentive']),
#     }


class IntroRaven(Page):
    pass


class Raven(Page):
    # timeout_seconds = 600
    timeout_seconds = 10

    form_model = 'player'
    # print(['raven_{0}'.format(i) for i in range(1, 11)])
    form_fields = ['raven_{0}'.format(i) for i in range(1, 11)]

    def before_next_page(self,timeout_happened):
        """" Store participant's answers if timeout happened. """
        # if timeout_happened:
        #     print(self)
        #     post_dict = self.request.POST
        #     self.player.raven_1 = int(post_dict.get('raven_1')) if post_dict.get('raven_1') is not None else None
        #     self.player.raven_2 = int(post_dict.get('raven_2')) if post_dict.get('raven_2') is not None else None
        #     self.player.raven_3 = int(post_dict.get('raven_3')) if post_dict.get('raven_3') is not None else None
        #     self.player.raven_4 = int(post_dict.get('raven_4')) if post_dict.get('raven_4') is not None else None
        #     self.player.raven_5 = int(post_dict.get('raven_5')) if post_dict.get('raven_5') is not None else None
        #     self.player.raven_6 = int(post_dict.get('raven_6')) if post_dict.get('raven_6') is not None else None
        #     self.player.raven_7 = int(post_dict.get('raven_7')) if post_dict.get('raven_7') is not None else None
        #     self.player.raven_8 = int(post_dict.get('raven_8')) if post_dict.get('raven_8') is not None else None
        #     self.player.raven_9 = int(post_dict.get('raven_9')) if post_dict.get('raven_9') is not None else None
        #     self.player.raven_10 = int(post_dict.get('raven_10')) if post_dict.get('raven_10') is not None else None


class Results(Page):
    def vars_for_template(player: Player):
        player.set_payoff_raven()


page_sequence = [
    IntroRaven,
    Raven,
    Results
]
