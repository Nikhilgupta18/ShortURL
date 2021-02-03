import string
import random


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # new = ''
    # for _ in range(size):
    #     new+=random.choice(chars)
    # return new
    return ''.join(random.choice(chars) for _ in range(size))


# create_shortcode ensures that always unique code is generated for every object
def create_shortcode(instance, size=6):
    new = code_generator(size=size)
    ClassInstance = instance.__class__
    query_exist = ClassInstance.objects.filter(Short=new).exists()
    if query_exist:
        return create_shortcode(size=size)
    return new


