 # -*- coding: utf-8 -*-
from datetime import timedelta
from openerp import models, fields, api,exceptions,_
#from openerp import controllers
#from openerp.exceptions import Warning


# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", stleore=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
 
class Course(models.Model):
	_name='openacademy.course'
	name=fields.Char(string="Title")
	description=fields.Text()
	responsible_id=fields.Many2one("res.user",
			ondelete="set null",string="Responsible", index=True)
    
 

class Session(models.Model):
	_name='openacademy.session'
	name=fields.Char(required=True)
	start_date=fields.Date()
	duration=fields.Integer(help="Duration in days")
	seats=fields.Integer(string="Number of seats")

	instructor_id=fields.Many2one("res.partner",string="Instructor")
	course_id=fields.Many2one("openacademy.course",
		ondelete="cascade",string="Course",required=True)
	attendee_ids=fields.Many2many("res.partner",string="Attendees")

	active=fields.Boolean(default=True)
	# date_time(required)
	end_date=fields.Date(string="End Date",store=True,
		compute="_get_end_date",inverse="_set_end_date")
		# ,inverse="_set_end_date")
	 #string="End Date",store=True,
	# 	compute="",inverse="_set_end_date")
	#calendar=fields.
	hours = fields.Float(string="Duration in hours",
				compute='_get_hours', inverse='_set_hours')

	num_attendee=fields.Integer(string="Num of attendee", compute="_get_attendee_ids")
	



	@api.depends("attendee_ids")
	def _get_attendee_ids(self):
		for session in self:
			session.num_attendee=len(session.attendee_ids)  


			








			# self.sttendees_ids >= 0:
			# return{



			# 	len(self.sttendees_ids)
			# }



			




	# @api.depends("start_date","duration")
	# def _get_end_date(self):
	# 	for time in self:
	# 		if not (time.start_date and time.duration)
	# 			time.end_date=time.start_date
	# 			continue


    		# start=fields.Datetime.from_string(r.start_date)


    	# compute='_get_end_date', inverse='_set_end_date')
#class computeModel(object):
#	"""docstring for computeModel"""
#	_name="test.compute"

#	name=fields.Char(compute="_compute_name")

#	@api.multi
#	def _compute_name(self):
#		for record in self:
#			record.name=str(random.randint(1,1e6))

#	@api.depends('value')
#	def _compute_name(self):
#	    for record in self:
#	    	self.name="record with value %s"self.value






	@api.depends('start_date','duration')
	def _get_end_date(self):
		for r in self:
			if not (r.start_date and r.duration):
				r.end_date = r.start_date
				continue



            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
			start = fields.Datetime.from_string(r.start_date)
			duration = timedelta(days=r.duration, seconds=-1)
			r.end_date = start + duration
	

	@api.onchange('start_date','end_date')
	def _set_end_date(self):
		for session in self:
			if not (session.start_date and session.end_date):
				continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
			start_date = fields.Datetime.from_string(session.start_date)
			end_date = fields.Datetime.from_string(session.end_date)
			session.duration = (end_date - start_date).days + 1


	@api.depends('duration')
	def _get_hours(self):
		for r in self:
			r.hours = r.duration * 24

	def _set_hours(self):
		for r in self:
			r.duration = r.hours / 24

	taken_seats=fields.Float(string="taken seats",compute="_taken_seats")
	@api.multi
	@api.depends("seats","attendee_ids")

	def _taken_seats(self):
		for r in self:
			if not r.seats:
				r.taken_seats=0.0
			else:
				r.taken_seats=100.0 * len(r.attendee_ids)/r.seats	




	# @api.constrains("seats","attendee_ids")
	# def _verify_valid_seats(self):
		# for r in self:



		# if self.seats < 0:
		# 	return {
		# 		"warning":{
		# 			"title":"Incorrect 'seats'value",
		# 			"message":"The number of available seats may not be negative",
		# 		},
		# 	}		
		# if self.seats < len(self.attendee_ids):
		# 	return {
		# 		"warning":{
		# 			"title":"Too may attendee",
		# 			"message":"Increase seats or remove excess attendee",
		# 		},
		# 	}
#	sttendees=len(self.sttendees_ids)
	@api.constrains("seats","attendee_ids")
	def _verify_valid_seats(self):
		for session in self:
			if session.seats<0:
				raise exceptions.ValidationError("The number of available seats may not be negative")
			if session.seats<len(self.attendee_ids):
				raise exceptions.ValidationError("Increase seats or remove excess attendee")	




	# @api.constrains("instructor_id","attendee_ids")
	# def _check_instructor_not_in_attdendees(self):
	# 	for r in self:
	# 		if r.instructor_id and r.instructor_id in r.attendee_ids:
	# 			raise exceptions.ValidationError("a big question")

