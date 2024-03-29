def priority_zephyr_to_allure(prio):
	match prio:
		case 'High':
			return 'Critical'
		case 'Normal':
			return 'Normal'
		case 'Low':
			return 'Trivial'
		case _:
			raise ValueError
