name=fields.Char(string="Title",required=True)
description=fields.Text()

responsible_id=fields.Many2one("res.users",
	ondelete="set null",string="Responsible",index=True)

class Session(models.Model):
	_name="openacademy.session"
	start_date=fields.Date()
	duration=fields.Float(digits=(6,2),help="Duration in days")
	seats=fields.Inter(string="Number of seats")

	instructor_id=fields.Many2one("res.partner",string="Instructor")
	course_id=fields.Many2one("openacademy.course",
	ondelete="cascade",string="Course",required=True)
