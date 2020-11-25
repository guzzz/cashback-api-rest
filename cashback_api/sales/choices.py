from model_utils import Choices


ACTIVATION_CHOICES = Choices(
    'awaiting_approval', 'approved'
)


ACTIVATION_CHOICES_TRANSLATION = (
    ('awaiting_approval','Em validação'),
    ('approved','Aprovado')
)