import random
import string
from .models import RegisterEventUsers
def id_generator(size = 10, chars = string.ascii_uppercase + string.digits):
	the_id = "ADAV"+ "".join(random.choice(chars) for x in range(size))
	try:
		order = RegisterEventUsers.objects.get(registration_id = the_id)
		id_generator()
	except RegisterEventUsers.DoesNotExist:
		return the_id

