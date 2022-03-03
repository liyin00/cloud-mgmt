# Might change this to using os.environ.get() instead in future sprints
from decouple import config
from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from datetime import datetime
# from classes import *

# Database connection

# EC2 DB port is 3306 instead, change accordingly.
app = Flask(__name__)
# EC2 DB port is 3306 instead, change accordingly.
app.config['SQLALCHEMY_DATABASE_URI'] = config('dbURL') or environ.get("dbURL")
# app.config['SQLALCHEMY_DATABASE_URI'] = config('localURL') or environ.get('localURL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Employee(db.Model):
    __tablename__ = "employee"
    emp_id = db.Column(db.String(10),primary_key=True, nullable=False)
    emp_name = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'employee'
    }

    def json(self):
        employee_info = {
            'emp_id': self.emp_id,
            'emp_name': self.emp_name
        }
        return employee_info
    

class Senior_Engineer(Employee):
    __tablename__ = "senior_engineer"
    emp_id =  db.Column(db.String(10), db.ForeignKey('employee.emp_id'),primary_key=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'senior_engineer',
    }
    
class Engineer(Employee):
    __tablename__ = "engineer"
    emp_id =  db.Column(db.String(10), db.ForeignKey('employee.emp_id'),primary_key=True, nullable=False)


    __mapper_args__ = {
        'polymorphic_identity': 'engineer',
    }

class Trainer(db.Model):
    __tablename__ = "trainer"
    emp_id =  db.Column(db.String(10), db.ForeignKey('employee.emp_id'), nullable=False)
    trainer_id =  db.Column(db.String(10), primary_key=True, nullable=False)



class Learner(db.Model):
    __tablename__ = "learner"
    emp_id =  db.Column(db.String(10), db.ForeignKey('employee.emp_id'), nullable=False)
    learner_id =  db.Column(db.String(10), primary_key=True, nullable=False)



class Completion_Record(db.Model):
    __tablename__ = "completion_record"
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"),primary_key=True, nullable=False)
    learner_id =  db.Column(db.String(10), db.ForeignKey('learner.learner_id'), primary_key=True, nullable=False)


    def insert_into_completion_record(self):
        #insert only if pass 

        db.session.add(self)
        db.session.commit()
        return 200




class Course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.String(10), primary_key=True, nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    course_desc = db.Column(db.String(255), nullable=False)
    prerequisite = db.Column(db.Integer, nullable=False)

    def json(self):
        Course_info = {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_desc': self.course_desc,
            'prerequisite': self.prerequisite
        }
        return Course_info




class Course_Prerequisite(db.Model):
    __tablename__ = "course_prerequisite"
    course_id = db.Column(db.String(10),primary_key=True, nullable=False)
    prereq_course_id = db.Column(db.String(10),primary_key=True, nullable=False)


class Class_Run(db.Model):
    __tablename__ = "class_run"

    # Assuming class_id contains information of the course itself, thus it can be a singular primary key (Important, let team know.)
    class_id = db.Column(db.String(10), primary_key=True)
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"), primary_key=True, nullable=False)
    class_start_date = db.Column(db.String(50),nullable=False)
    class_end_date = db.Column(db.String(50),nullable=False)
    reg_start_date = db.Column(db.String(50),nullable=False)
    reg_end_date = db.Column(db.String(50),nullable=False)

    # Just slots available is enough, don't need class_size.
    slots_available = db.Column(db.Integer, nullable=False)

    def check_commence_of_course(self):
        now = datetime.now()
        ## double check
        dt_string = now.strftime("%Y-%m-%d")
        if(self.class_start_date <= dt_string <= self.class_end_date):
            return True
        return False

    def check_available_end_date(self):
        now = datetime.now()
        ## double check
        dt_string = now.strftime("%Y-%m-%d")
        if(dt_string <= self.reg_end_date):
            return True
        return False

    def check_available_date(self):
        now = datetime.now()
        ## double check
        dt_string = now.strftime("%Y-%m-%d")

        if(self.reg_start_date <= dt_string <= self.reg_end_date):

            return True

        return False
    
    def compute_total_slot_available(self,total_slot_available):
        return total_slot_available + self.slots_available

    
    def compute_slot_available(self,string):
        try:
            if(string == "Assign"):
                if(self.slots_available == 0):
                    return 400

                self.slots_available = self.slots_available- 1
            elif(string == "Withdraw"):
                self.slots_available = self.slots_available + 1
            
            db.session.commit()
            return 200
        except Exception as e:
            return 501




    def json(self):
        class_run_info = {
            'class_id': self.class_id,
            'course_id': self.course_id,
            'class_start_date': self.class_start_date,
            'class_end_date': self.class_end_date,
            'reg_start_date': self.reg_start_date,
            'reg_end_date': self.reg_end_date,
            'slots_available' : self.slots_available
        }
        return class_run_info



        
class Trainer_Record(db.Model):
    __tablename__ = "trainer_record"
    class_id = db.Column(db.String(10), db.ForeignKey("class_run.class_id"),primary_key=True, nullable=False)
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"), nullable=False)
    trainer_id =  db.Column(db.String(10), db.ForeignKey('trainer.trainer_id'), primary_key=True, nullable=False)



class Class_Record(db.Model):
    __tablename__ = "class_record"
    class_id = db.Column(db.String(10), db.ForeignKey("class_run.class_id"),primary_key=True, nullable=False)
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"), nullable=False)
    learner_id =  db.Column(db.String(10), db.ForeignKey('learner.learner_id'), primary_key=True, nullable=False)

    def delete_class_record(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return 200
        except Exception as e:

            return 502

    def insert_class_record(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:
            return 502

            


# db.create_all()

class Registration(db.Model):
    __tablename__ = "registration"
    class_id = db.Column(db.String(10), db.ForeignKey("class_run.class_id"),primary_key=True, nullable=False)
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"), nullable=False)
    learner_id =  db.Column(db.String(10), db.ForeignKey('learner.learner_id'), primary_key=True, nullable=False)
    reg_date = db.Column(db.String(50),nullable=False)

    def delete_registration_db(self):

        try:

            db.session.delete(self)
            db.session.commit()
            return 200
        except Exception as e:

            return 502

    def get_current_date():
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")

        return current_date

    def insert_registration(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:
            return 500

class Chapter(db.Model): 
    __tablename__ = "chapter" 
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"),primary_key=True, nullable=False)
    chapter_id = db.Column(db.String(30), primary_key=True, nullable=False)

    def json(self):
        chapter_info = {
            'course_id': self.course_id,
            'chapter_id': self.chapter_id
        }
        return chapter_info
    

class Chapter_Learner(db.Model):
    __tablename__ = "chapter_learner"

    chapter_id = db.Column(db.String(30), primary_key=True, nullable=False)
    learner_id =  db.Column(db.String(10), db.ForeignKey('learner.learner_id'), primary_key=True, nullable=False)
    completion = db.Column(db.Integer, nullable=False)

    def update_completion(self):
        self.completion = 1

    def json(self):
        info = {
            'chapter_id': self.chapter_id,
            'learner_id': self.learner_id,
            'completion': self.completion
        }

        return info


    def insert_chapter_learner(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:

            return 500


class Quiz(db.Model):
    __tablename__ = "quiz"
    quiz_id = db.Column(db.String(30), primary_key=True, nullable=False)
    timing = db.Column(db.String(50),nullable=False)

class Chapter_Quiz(Quiz):
    __tablename__ = "chapter_quiz"
    quiz_id = db.Column(db.String(30), db.ForeignKey("quiz.quiz_id"), primary_key=True, nullable=False)

    chapter_id = db.Column(db.String(30), primary_key=True, nullable=False)
    total_marks = db.Column(db.String(10), nullable=False)

    def insert_chapter_quiz(self):
        #quiz is a parent of chapter_quiz same as final quiz

        try:
            db.session.add(self)
            db.session.commit()

            return 200
        except Exception as e:

            return 500


    def json(self):
        info = {
            'quiz_id': self.quiz_id,
            'chapter_id': self.chapter_id,
            'total_marks': self.total_marks,
            'timing': Quiz.timing
        }

        return info

    def check_pass(self,learner_marks):
        is_pass = 1
        percentage = (int(learner_marks) / int(self.total_marks)) * 100
        if(percentage >= 85):
            return is_pass
        is_pass = 0
        return is_pass


class Final_Quiz(Quiz): 
    __tablename__ = "final_quiz"
    quiz_id = db.Column(db.String(30), db.ForeignKey("quiz.quiz_id"), primary_key=True, nullable=False)
    course_id = db.Column(db.String(10), db.ForeignKey("course.course_id"),primary_key=True, nullable=False)
    total_marks = db.Column(db.String(10), nullable=False)

    def final_check_pass(self,learner_marks):
        is_pass = 1
        percentage = (int(learner_marks) / int(self.total_marks)) * 100
        if(percentage >= 85):
            return is_pass
        is_pass = 0
        return is_pass

    def json(self):
        final_quiz_info = {
            'quiz_id': self.quiz_id,
            'course_id': self.course_id,
            'total_marks': self.total_marks,
            'timing': Quiz.timing

        }
        return final_quiz_info

    def insert_final_quiz(self):
        try:

            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:
            return 500


class Question(db.Model):
    __tablename__ = "question"
    quiz_id = db.Column(db.String(30), db.ForeignKey("quiz.quiz_id"), primary_key=True, nullable=False)
    question_id = db.Column(db.String(10), primary_key=True, nullable=False)
    question = db.Column(db.String(255), nullable=False)
    question_type = db.Column(db.String(10), nullable=False)
    option = db.Column(db.String(10000), nullable=False)
    question_mark = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(255), nullable=False)

    def json(self):
        self.quiz_id = {
            'quiz_id': self.quiz_id,
            'question_id': self.question_id,
            'question': self.question,
            'question_type': self.question_type,
            'option': self.option,
            'question_mark': self.question_mark,
            'answer': self.answer
        }
        return self.quiz_id 

    def compute_marks(self,answer):

        if(self.answer ==answer):
            return int(self.question_mark)
        return 0 

    def create_question(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:

            return 500



class Chapter_Quiz_Result(db.Model): 
    __tablename__ = "chapter_quiz_result"
    quiz_id = db.Column(db.String(30), db.ForeignKey("quiz.quiz_id"), primary_key=True, nullable=False)
    learner_id =  db.Column(db.String(10), db.ForeignKey('learner.learner_id'), primary_key=True, nullable=False)
    marks = db.Column(db.String(10), nullable=False)

    def update_mark_existing_chapter_quiz_result(self, learner_marks):

        try:
            self.marks = learner_marks
            db.session.commit()
            return 200
        except Exception as e:

            return 500

    def insert_chapter_quiz_result(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:

            return 500
 


class Final_Quiz_Result(db.Model):
    __tablename__ = "final_quiz_result"
    quiz_id = db.Column(db.String(30), db.ForeignKey("quiz.quiz_id"), primary_key=True, nullable=False)
    learner_id =  db.Column(db.String(10), db.ForeignKey('learner.learner_id'), primary_key=True, nullable=False)
    marks = db.Column(db.String(10), nullable=False)
    def update_mark_existing_final_quiz_result(self, learner_marks):

        try:
            self.marks = learner_marks
            db.session.commit()
            return 200
        except Exception as e:

            return 500       
        


    def insert_final_quiz_result(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:

            return 500
 


# db.create_all()

@app.route("/enroll_course_details/<string:course_id>")
def retrieve_course_class(course_id):
    #registration, course, class table # course_id etc
    

    class_run_list = Class_Run.query.filter_by(course_id = course_id).all()
    class_run_array = []
    if(len(class_run_list)):
        
        for class_run in class_run_list:
            is_registration = class_run.check_available_end_date()
            if is_registration:
                class_run_array.append(class_run)
    return jsonify(
        {
            'code': 200,
                course_id: [class_run.json() for class_run in class_run_array]

        }
    )


@app.route("/enrollment_course_list")
def retrieve_all_courses():
    array = []
    course_list = Course.query.all() # course_id etc
    
    if len(course_list):
        for course in course_list:
            course_name = course.course_name
            course_id = course.course_id
            course_description = course.course_desc
            class_run_list = Class_Run.query.filter_by(course_id=course_id).all()
            if len(class_run_list):
                #got class
                class_counter = 0
                total_slot_available = 0
                for class_run in class_run_list:
                    is_registration = class_run.check_available_end_date()
                    if is_registration:
                        #means allow to display 
                        total_slot_available = class_run.compute_total_slot_available(total_slot_available)
                        class_counter+=1
            if(class_counter !=0):
            #dont show out!
                value = {
                    "course_name": course_name,
                    "course_id":course_id,
                    "course_description":course_description,
                    "total_slot_available":total_slot_available,
                    "num_of_class": class_counter
                }

            array.append(value)

        
        return jsonify(
            {
                'code': 200,
                'data': {
                    "courses": [course for course in array]
                }
            }
        )

@app.route("/courses")
def get_course_list():
    course_list = Course.query.all()

    if len(course_list):
        return jsonify(
            {
                'code': 200,
                'data': {
                    "courses": [course.json() for course in course_list]
                }
            }
        )

    return jsonify(
    {
        "code": 404,
        "message": "There are no course."
    }
    ), 404



@app.route('/learner_list/<string:course_id>')
def retrieve_course_learners(course_id):
    ##focus registered tab first
    preassign_learners_array = []
    enrolled_learners_array = []
    registered_learners_array = []

    ##for now remove preassign 


    course_registration_list = Registration.query.filter_by(course_id = course_id).all()
    if(len(course_registration_list)):
        for  course_reg in course_registration_list:
            learner = Learner.query.filter_by(learner_id = course_reg.learner_id).first()
            #get learner already find the emp id
            employee = Employee.query.filter_by(emp_id = learner.emp_id).first()


            string = {
                "name": employee.emp_name,
                "emp_id": learner.emp_id,
                "learner_id": course_reg.learner_id,
                "class_id":course_reg.class_id
            }
            registered_learners_array.append(string)

    class_record_list = Class_Record.query.filter_by(course_id = course_id).all()
    if(len(class_record_list)):
        for  class_record in class_record_list:
            learner = Learner.query.filter_by(learner_id = class_record.learner_id).first()
            #get learner already find the emp id
            employee = Employee.query.filter_by(emp_id = learner.emp_id).first()
            string = {
                "name": employee.emp_name,
                "emp_id": learner.emp_id,
                "learner_id": class_record.learner_id,
                "class_id":class_record.class_id
            }
            enrolled_learners_array.append(string)
    

    return jsonify(
        {
            'code': 200,
            course_id: {
                "preassign_learners": [result for result in preassign_learners_array],
                "registered_learners": [result for result in registered_learners_array],
                "enrolled_learners": [result for result in enrolled_learners_array]
            }
        }
    )




##sprint4 , remove all the register if 1 of them have already approve NEED TEST
def remove_class_run_by_learner_id(data):
    try:
        class_id = data["class_id"]
        course_id = data["course_id"]
        learner_id = data["learner_id"]
        #delete based on emp_id and course_id from front end, assuming this 2 can be a composite key
        registration_list = Registration.query.filter_by(course_id = course_id,learner_id = learner_id).all()

        if(len(registration_list)!= 0):
            for reg in registration_list:

                reg.delete_registration_db()

        else:
            return 502
    except Exception as e:
        return 502
    return 200







@app.route("/assign_learner", methods=['POST'])
def assign_to_course():
    #insert into class record, update slot available, delete from registration
    try:
        data = request.get_json()

        # Should immediately exit upon failing this line.....
       
        class_info = Class_Run.query.filter_by(class_id = data['class_id']).first()
        update_code = class_info.compute_slot_available('Assign')
        if(update_code == 400):
            return jsonify(
            {
                "code": update_code,
                "message": "Slot is full, unable to enroll anymore."
            }
            ), 400
        
        class_record = Class_Record(
            class_id=data['class_id'],
            course_id=data['course_id'],
            learner_id=data['learner_id']
        )

        insert_code = class_record.insert_class_record()
        #update slot available 
        class_id = data["class_id"]
        course_id = data["course_id"]
        learner_id = data["learner_id"]
        #delete based on emp_id and course_id from front end, assuming this 2 can be a composite key
        registration = Registration.query.filter_by(class_id=class_id,course_id = course_id,learner_id = learner_id).first()
        
        #####NEED
        if(registration !=None):
            delete_code = registration.delete_registration_db()
        else:
            #is preassign dont need to even delete 
            delete_code = 200
        #remove the rest if found in class_run
        remove_class_run = remove_class_run_by_learner_id(data)

        if(insert_code == 500 or update_code == 501 or delete_code ==502):
            return jsonify(
            {
                "code": 500,
                "message": "There is an problem performing the execution"
            }
            ), 500
        return jsonify(
            {
                "code": 200,
                "message": "Successfully enrolled into the class."
            }
            ), 200


    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occur when update the slot " + str(e)
            }
        ), 500



    


@app.route("/withdraw_enrolled_learner", methods=['PUT'])
def withdraw_course():
    try:
        data = request.get_json()
        class_record = Class_Record.query.filter_by(class_id=data['class_id'],course_id = data['course_id'],learner_id = data['learner_id']).first()

        if(class_record == None):
            return jsonify(
            {
                "code": 500,
                "message": "learner cannot be found in class record"
            }
            ), 500
        delete_code = class_record.delete_class_record()
    
        ##refractor

        class_info = Class_Run.query.filter_by(class_id = data['class_id']).first() 
        update_code = class_info.compute_slot_available('Withdraw')
    
        if(delete_code == 502 or update_code == 501):
            return jsonify(
            {
                "code": 500,
                "message": "There is an problem performing the execution"
            }
            ), 500
            
        return jsonify(
            {
                "code": 200,
                "data": {
                    "message": "successful withdraw from the course!"
                }
            }
        )
    except Exception as e:

        return jsonify(
            {
                "code": 404,
                "data": {
                    "message": "error"
                },
                "message": "learner not found."
            }
        ), 404



@app.route("/registration_course_list")
def registration_course_list():
    array = []
    course_list = Course.query.all() # course_id etc
    
    if len(course_list):
        for course in course_list:
            course_name = course.course_name
            course_id = course.course_id
            course_description = course.course_desc
            class_run_list = Class_Run.query.filter_by(course_id=course_id).all()
            string_prereq = ""
            course_prereq_list = Course_Prerequisite.query.filter_by(course_id=course_id).all()
            if len(course_prereq_list):
                #means got prereq
                for course_prereq in course_prereq_list:
                    string_prereq  += course_prereq.prereq_course_id   + ","

            if len(class_run_list):
                #got class
                class_counter = 0
                total_slot_available = 0
                for class_run in class_run_list:
                    is_registration = class_run.check_available_date()
                    if is_registration:
                        #means allow this course have 

                        value = {
                                "course_name": course_name,
                                "course_id":course_id,
                                "course_desc":course_description,
                                "prereq_courses" : string_prereq[0:-1]
                            }

                        array.append(value)
                        break
                        #since this course already accounted for go to next course
                


        
        return jsonify(
            {
                'code': 200,
                'course_list': [course for course in array]
                
            }
        )





@app.route("/reg_course_details/<string:course_id>")
def reg_course_details(course_id):
    array = []
    course = Course.query.filter_by(course_id=course_id).first()
    course_name = course.course_name
    course_id = course.course_id
    course_description = course.course_desc
    course_prereq_list = Course_Prerequisite.query.filter_by(course_id=course_id).all()
    string_prereq = ""
    if len(course_prereq_list):
        #means got prereq
        for course_prereq in course_prereq_list:
            string_prereq  += course_prereq.prereq_course_id   + ","

    class_run_list = Class_Run.query.filter_by(course_id=course_id).all()

    if len(class_run_list):
        #got class
        class_counter = 0
        total_slot_available = 0
        for class_run in class_run_list:
            is_registration = class_run.check_available_date()
            if is_registration:
                #means allow this course have 
                total_slot_available = class_run.compute_total_slot_available(total_slot_available)
                #class_counter+=1
                #since this course already accounted for go to next course
        value = {
        "course_name": course_name,
        "course_id":course_id,
        "course_description":course_description,
        "prereq_courses" : string_prereq[0:-1],
        "num_of_slots": total_slot_available
         }
        return jsonify(
            {
                'code': 200,
                'data': value
                
            }
        )




@app.route("/enrollment_status/<string:course_id>/<string:learner_id>")
def enrollment_status(course_id,learner_id):
    prereq_array = []
    course_prereq_list = Course_Prerequisite.query.filter_by(course_id=course_id).all()
    string_prereq = ""
    if len(course_prereq_list):
        #means got prereq
        for course_prereq in course_prereq_list:
            prereq_array.append(course_prereq.prereq_course_id)


    #3 check  , check if approve, check if prereq , last but not least, 
    is_exist_class_record  = Class_Record.query.filter_by(course_id=course_id,learner_id = learner_id).first()
    #this dude exist
    if(is_exist_class_record):
        return jsonify(
            {
                'code': 200,
                'is_approved': 1,
                'results': [],
                'message': 'You have already enrolled in this course.'
            }
        ) 
    is_completed  = Completion_Record.query.filter_by(course_id=course_id,learner_id = learner_id).first()
    if(is_completed):
        return jsonify(
            {
                'code': 200,
                'is_approved': 2,
                'results': [],
                'message': 'You have already completed in this course.'
            }
        )

    course_completion_list  = Completion_Record.query.filter_by(learner_id = learner_id).all()
    course_completion = [course_completion.course_id for course_completion in course_completion_list]

    if(len(prereq_array)):
        for prereq in prereq_array:

            if prereq not in course_completion:
                #gg not inside havent complete prereq
                return jsonify(
                    {
                        'code': 200,
                        'is_approved': 3,
                        'results': [],
                        'message': 'You have not complete the pre-requisite yet.'
                    }
                )

    class_run_list = Class_Run.query.filter_by(course_id=course_id).all()
    result = []
    if len(class_run_list):
        #got class
        for class_run in class_run_list:
            is_registration = class_run.check_available_date()
            if is_registration:
                #means allow this CLASS have 
                class_run_list = Registration.query.filter_by(course_id=course_id,learner_id = learner_id, class_id = class_run.class_id).all()
                if(len(class_run_list) == 0):
                    is_registered = 0
                else:
                    #exist already
                    is_registered = 1

                value = {
                    "class_id": class_run.class_id,
                    "num_of_slots": class_run.slots_available,
                    "reg_start_date": class_run.reg_start_date,
                    "reg_end_date": class_run.reg_end_date,
                    "class_start_date": class_run.class_start_date,
                    "class_end_date":class_run.class_end_date,
                    "is_registered": is_registered
                }
                result.append(value)

        return jsonify(
            {
                'code': 200,
                'is_approved': 0,
                'results': result,
                'message': 'Retrieve successfully.'
                
            }
        )



@app.route("/register", methods=['POST'])
def register():
    #insert into class record, update slot available, delete from registration
    try:
        data = request.get_json()
        #retrieve the slot available, if 0 cannot aply
        class_info = Class_Run.query.filter_by(class_id=data['class_id'], course_id = data['course_id']).first()
        if(not class_info.check_available_date()):
            return jsonify(
            {
                "code": 201,
                "message": "The course is not available yet."
            }
            ), 200 
        
        if(class_info.slots_available == 0):
            return jsonify(
            {
                "code": 201,
                "message": data['class_id'] + " is currently full."
            }
            ), 200 

        is_exist  = Registration.query.filter_by(class_id=data['class_id'], course_id = data['course_id'], learner_id =data['learner_id']).first()
        if(is_exist != None):

            return jsonify(
            {
                "insert_code": 404,
                "message": "You already registered for the course"
            }
            ), 404
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")

        #def __init__(self,emp_id,course_id,class_id,completed):
        registration = Registration(
            class_id=data['class_id'],
            course_id=data['course_id'],
            learner_id=data['learner_id'],
            reg_date = current_date
            
        )
        insert_code = registration.insert_registration()
        #update slot available
        if(insert_code == 500):
            return jsonify(
            {
                "code": insert_code,
                "message": "There is an problem performing the execution"
            }
            ), 500
        elif(insert_code == 404):
            return jsonify(
            {
                "code": insert_code,
                "message": "You already registered for the course"
            }
            ), 404
        return jsonify(
            {
                "code": 200,
                "message": "Successfully register for " + data['class_id'] + "."
            }
            ), 200 


    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occur when executing the function" + str(e)
            }
        ), 500




@app.route("/registration_details/<string:learner_id>")
def registration_details(learner_id):
    #retrieve from registration is_approved = 0 and class_record is_approved = 1
    result = []
    class_record_list = Class_Record.query.filter_by(learner_id=learner_id).all()
    if(len(class_record_list)):
        for class_record in class_record_list:
            course = Course.query.filter_by(course_id = class_record.course_id).first()

            array = {
                'course_id': class_record.course_id,
                'course_name': course.course_name,
                'class_id': class_record.class_id,
                'is_approved': 1
            }
            result.append(array)

    
    registration_list = Registration.query.filter_by(learner_id=learner_id).all()
    if(len(registration_list)):
        for registration in registration_list:
            course = Course.query.filter_by(course_id = registration.course_id).first()

            array = {
                'course_id': registration.course_id,
                'course_name': course.course_name,
                'class_id': registration.class_id,
                'is_approved': 0
            }

            result.append(array)

    return jsonify(
        {
            'code': 200,
            'results': result
            
        }
    )



@app.route("/withdraw_learner_registration", methods=['POST'])
def withdraw_learner_registration():

    try:
        data = request.get_json()
        delete_code = 0
        delete_class_code = 0
        update_code = 0
        #retrieve the slot available, if 0 cannot aply
        if(data["is_approved"] == 0):
            #is from registration table just remove can already


            class_id = data["class_id"]
            course_id = data["course_id"]
            learner_id = data["learner_id"]
            #delete based on emp_id and course_id from front end, assuming this 2 can be a composite key
            registration = Registration.query.filter_by(class_id=class_id,course_id = course_id,learner_id = learner_id).first()
            delete_code = registration.delete_registration_db()
        elif(data["is_approved"] == 1):
            #is from class_record withdraw
            class_record = Class_Record.query.filter_by(class_id=data['class_id'],course_id = data['course_id'],learner_id = data['learner_id']).first()
            if(class_record == None):
                return jsonify(
                {
                    "code": 500,
                    "message": "learner cannot be found in class record"
                }
                ), 500
            delete_code = class_record.delete_class_record()

            class_info = Class_Run.query.filter_by(class_id = data['class_id']).first() 


            update_code = class_info.compute_slot_available('Withdraw')
            
        if(delete_code ==502 or delete_class_code == 502 or update_code == 501):
            return jsonify(
            {

                "code": 500,
                "message": "There is an problem performing the execution"
            }
            ), 500
        return jsonify(
            {
                "code": 200,
                "message": "Successfully withdraw from the class."
            }
            ), 200

    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "message": "An error occur when performing withdraw" + str(e)
                },
            }
        ), 404




@app.route("/retrieve_question/<string:quiz_id>")
def retrieve_question_by_course_class_chapter(quiz_id):
    #retrieve from registration is_approved = 0 and class_record is_approved = 1

    question_list = Question.query.filter_by(quiz_id=quiz_id).all()

    if len(question_list):
        quiz_record = Quiz.query.filter_by(quiz_id=quiz_id).first()

        return jsonify(
            {
                'code': 200,
                'duration':quiz_record.timing,
                "question_records": [question.json() for question in question_list]
                
            }
        )

    return jsonify(
    {
        'code': 500,
        'message' : "question not found"
    })

#coding concatenation
def auto_compute_grade(data):

    learner_marks = 0 
    question_list = Question.query.filter_by(quiz_id=data['quiz_id']).order_by("question_id").all()
    answer_array = []
    question_id = data['question'].split(",")

    answer_array = data['answer'].split(",")

    for i in range(0,len(question_list)):
        index = question_id.index(question_list[i].question_id)
        learner_marks += question_list[i].compute_marks(answer_array[index])


    return learner_marks


#coding concatenation
def insert_update_into_quiz_result_db(data,learner_marks,record):

    try:

        if(data['type'] == "chapter_quiz"):
            if(record == None):


                #def __init__(self,emp_id,course_id,class_id,completed):
                result = Chapter_Quiz_Result(
                    quiz_id=data['quiz_id'],
                    learner_id=data['learner_id'],
                    marks=learner_marks
                    
                )

                code =  result.insert_chapter_quiz_result()
                return code
            else:
                #update instead

                code = record.update_mark_existing_chapter_quiz_result(learner_marks)
                #db.session.commit()
                return code
        else:
            if(record == None):
                #def __init__(self,emp_id,course_id,class_id,completed):
                result = Final_Quiz_Result(
                    quiz_id=data['quiz_id'],
                    learner_id=data['learner_id'],
                    marks=learner_marks
                    
                )
                code = result.insert_final_quiz_result()
                return code

            else:
                #update instead
 
                code = record.update_mark_existing_final_quiz_result(learner_marks)
                #db.session.commit()
                return code
            
    except Exception as e:

        return 500


#coding concatenation
def insert_update_into_chapter_learner_db(data,learner_marks,is_exist_chapter_learner):
    try:
        chapter_quiz = Chapter_Quiz.query.filter_by(quiz_id =data['quiz_id']).first()
        completion = chapter_quiz.check_pass(learner_marks)

        if(is_exist_chapter_learner == None):
            #no record no matter what just insert.
            result = Chapter_Learner(
                chapter_id=data['quiz_id'][0:-1],
                learner_id=data['learner_id'],
                completion=completion      
            )

            code = result.insert_chapter_learner()

            return code
        else:
            # got data inside  if completion fail doesnt matter because either 0 or 1 which is impt to pass dont needoverwrite
            #if completion is 1 just update
            if(completion == 1):
                is_exist_chapter_learner.update_completion()
                db.session.commit()

            return 200

    except Exception as e:
        return 500





@app.route("/submit_quiz", methods=['POST'])
def submit_quiz():
    #insert into class record, update slot available, delete from registration
    try:
        is_exist_chapter_quiz_result = ""
        is_exist_chapter_learner = ""
        data = request.get_json()


        learner_marks = auto_compute_grade(data)

        ##check if this data is already in db
        if(data['type'] == 'chapter_quiz'):
            is_exist_chapter_quiz_result = Chapter_Quiz_Result.query.filter_by(quiz_id=data['quiz_id'],learner_id = data['learner_id']).first()
            code = insert_update_into_quiz_result_db(data,learner_marks,is_exist_chapter_quiz_result)
            if(code != 200):
                return jsonify(
                {
                    "code" : code,
                    "message": "there is an error insert/update into chapter quiz result db"
                }), 200
            ######### NEED
            is_exist_chapter_learner = Chapter_Learner.query.filter_by(chapter_id=data['quiz_id'][0:-1],learner_id =data['learner_id']).first()

            #if fail but exist ignore ,  if fail but not exist(insert) ,if pass check insert or update. 
            code_chapter_learner = insert_update_into_chapter_learner_db(data,learner_marks,is_exist_chapter_learner)
            if(code_chapter_learner != 200):
                return jsonify(
                {
                    "code" : code_chapter_learner,
                    "message": "there is an error insert/update into chapter learner result db"
                }), 200
        else:
            #final
            is_exist_final_quiz_result = Final_Quiz_Result.query.filter_by(quiz_id=data['quiz_id'],learner_id = data['learner_id']).first()
            code = insert_update_into_quiz_result_db(data,learner_marks,is_exist_final_quiz_result)
            if(code != 200):
                return jsonify(
                {
                    "code" : code,
                    "message": "there is an error insert/update into chapter quiz result db"
                }), 200

            #insert into completion table
            #if fail but exist ignore ,  if fail but not exist(insert) ,if pass check insert or update. 

            final_quiz = Final_Quiz.query.filter_by(quiz_id = data['quiz_id']).first()

            is_pass = final_quiz.final_check_pass(learner_marks)

            if(is_pass == 1):

                course_id = data['quiz_id'].split("_")
                course_id = course_id[0]
                result = Completion_Record(
                    course_id=course_id,
                    learner_id=data['learner_id']
                )
                is_exist_completion_record = Completion_Record.query.filter_by(course_id = course_id,learner_id = data['learner_id']).first()
                if(is_exist_completion_record == None):
                    code_completion_record= result.insert_into_completion_record()
                    if(code_completion_record != 200):
                        return jsonify(
                        {
                            "code" : code_completion_record,
                            "message": "there is an error insert/update into completion record db"
                        }), 200
                else:
                    return jsonify(
                    {
                        "code" : 200,
                        "message": "already completed the final quiz"
                    }), 200
            else:
                return jsonify(
                {
                    "code" : code,
                    "message": "successfully done submitting final quiz, but fail not updated into completion table"
                }), 200


   
        return jsonify(
            {
                "code" : code,
                "message": "successfully"
            }), 200

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occur when executing the function" + str(e)
            }
        ), 500


#class_id like BEM460_C1
@app.route("/retrieve_progress_learner_id/<string:class_id>/<string:learner_id>")
def retrieve_progress_learner_id(class_id,learner_id):
    #retrieve from registration is_approved = 0 and class_record is_approved = 1

    Chapter_quiz_list = Chapter_Quiz.query.filter(Chapter_Quiz.quiz_id.contains(class_id)).all()

    final_quiz_list = Final_Quiz.query.filter(Final_Quiz.quiz_id.contains(class_id)).all()
    total_length = len(Chapter_quiz_list) + len(final_quiz_list)


    learner_chapter_completion_list = Chapter_Learner.query.filter(Chapter_Learner.chapter_id.contains(class_id)).filter_by(learner_id = learner_id).all()

    array = class_id.split("_")

    final_quiz_completion = Completion_Record.query.filter_by(course_id = array[0],learner_id = learner_id).all()
    total_completion = len(learner_chapter_completion_list) + len(final_quiz_completion)



    return jsonify(
    {
        'code': 200,
        'progress_percentage':(total_completion/ total_length) * 100
        
    })




@app.route("/retrieve_chapter/<string:course_class_id>")
def retrieve_chapter(course_class_id):



    chapter_list = Chapter.query.filter(Chapter.chapter_id.contains(course_class_id)).all()

    if(len(chapter_list)):


        return jsonify(
        {
            'code': 200,
            'results': [chapter.json() for chapter in chapter_list]
        })
    return jsonify(
    {
        'code': 404,
        'results': "no results found"
    })



#bem460_c3 and learner_id
@app.route("/retrieve_chapter_learner_by_learner_id/<string:course_class_id>/<string:learner_id>/")
def retrieve_chapter_learner_by_learner_id(course_class_id,learner_id):
    #retrieve from registration is_approved = 0 and class_record is_approved = 1

    chapter_learner_list = Chapter_Learner.query.filter(Chapter_Learner.chapter_id.contains(course_class_id)).filter_by(learner_id = learner_id).all()
    if(len(chapter_learner_list)):

        return jsonify(
        {
            'code': 200,
            'results': [chapter_learner.json() for chapter_learner in chapter_learner_list]
        })
    return jsonify(
    {
        'code': 404,
        'results': "no results found"
    })



##trigger this to see if quiz should be make available anot  if so then use back one of the app route to get questions to let them do it
@app.route("/is_complete_all_chapters/<string:course_class_id>/<string:learner_id>/")
def is_complete_all_chapters(course_class_id,learner_id):
    chapter_list = Chapter.query.filter(Chapter.chapter_id.contains(course_class_id)).all()
    chapter_learner_list = Chapter_Learner.query.filter(Chapter_Learner.chapter_id.contains(course_class_id)).filter_by(learner_id = learner_id,completion = 1).all()
    no_of_completion = 0
    no_chapter_list = 0 
    results = 0
    if(len(chapter_learner_list)):
        no_of_completion = len(chapter_learner_list)
    if(len(chapter_list)):
        no_chapter_list = len(chapter_list)
        


    if(no_chapter_list == 0 ):
        return jsonify(
        {
            'code': 404,
            'results': "no results found",
            'number_of_completion': 0
        })

    if(no_of_completion == no_chapter_list):
        results = 1 
    return jsonify(
    {
        'code': 200,
        'results': results,
        'number_of_completion': str(no_of_completion) + "/" + str(no_chapter_list)
    })



##do this later
@app.route("/retrieve_learner_chapter_grade/<string:chapter_id>/<string:learner_id>")
def retrieve_learner_chapter_grade(chapter_id,learner_id):
    quiz_id = chapter_id + "q"
    learner_chapter_result = Chapter_Quiz_Result.query.filter_by(quiz_id = quiz_id, learner_id = learner_id).first()
    marks = learner_chapter_result.marks
    chapter_quiz = Chapter_Quiz.query.filter_by(chapter_id = chapter_id).first()
    total_marks = chapter_quiz.total_marks
    return jsonify(
    {
        "code": 200,
        "data": {
            "marks": marks,
            "total_marks": total_marks
        },
    }), 200

@app.route("/retrieve_learner_final_grade/<string:quiz_id>/<string:learner_id>")
def retrieve_learner_final_grade(quiz_id,learner_id):
    learner_final_result = Final_Quiz_Result.query.filter_by(quiz_id = quiz_id, learner_id = learner_id).first()
    marks = learner_final_result.marks
    final_quiz = Final_Quiz.query.filter_by(quiz_id = quiz_id).first()
    total_marks = final_quiz.total_marks
    return jsonify(
    {
        "code": 200,
        "data": {
            "marks": marks,
            "total_marks": total_marks
        },
    }), 200


################ Trainer 
@app.route("/retrieve_all_course_details_by_trainer_id/<string:trainer_id>/")
def retrieve_all_course_details_by_trainer_id(trainer_id):
    #retrieve from registration is_approved = 0 and class_record is_approved = 1
    array_list = []

    try:
        trainer_record_list = Trainer_Record.query.filter_by(trainer_id = trainer_id).all()
        if(len(trainer_record_list)):
            for trainer_record in trainer_record_list:
                    course_detail = Course.query.filter_by(course_id = trainer_record.course_id).first()
                    #course_detail.course_name
                    #trainer_record.class_id
                    chapter_list = Chapter.query.filter(Chapter.chapter_id.contains(trainer_record.class_id)).all()
                    num_of_chapter = 0
                    if(len(chapter_list)):
                        num_of_chapter = len(chapter_list)     

                    course_info = {
                        "course_name" : course_detail.course_name,
                        "class_id" : trainer_record.class_id,
                        "num_of_chapter" : num_of_chapter
                    }
                    array_list.append(course_info)
            
            return jsonify(
            {
                'code': 200,
                'results': array_list
            })
        else:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "message": "This trainer are unable to find in trainer record"
                    },
                }
            ), 404

    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "message": "An error occur when retrieve trainer course details" + str(e)
                },
            }
        ), 404



def retrieve_chapter_detail(class_id):
    array_list = []
    chapter_list = Chapter.query.filter(Chapter.chapter_id.contains(class_id)).all()
    if(len(chapter_list)):
        for chapter in chapter_list:
            array_chap = chapter.chapter_id.split("_")
            chapter_name = "Chapter " + array_chap[2][5:]

            quiz_record = Chapter_Quiz.query.filter_by(chapter_id = chapter.chapter_id).first()
 
            is_created = 0
            if(quiz_record!= None):
                is_created = 1 
                quiz_id = quiz_record.quiz_id
            else:
                #help frontend create the quiz name 
                quiz_id = chapter.chapter_id  + "q"
            
            string = {
                'type': "chapter_quiz",
                'chapter_id' : chapter.chapter_id,
                'chapter_name': chapter_name,
                'is_created': is_created,
                'quiz_id' : quiz_id
            }
            array_list.append(string)

    return array_list



#coding concatenation
def retrieve_quiz_chapter_detail(class_id):
    ########## QUIZ ############
    array_list = []
    quiz_record = Final_Quiz.query.filter(Final_Quiz.quiz_id.contains(class_id)).first()
    string = ""
    if(quiz_record != None):
        string = {
            'type': "final_quiz",
            'chapter_name': "Finals",
            'is_created': 1,
            'quiz_id' : quiz_record.quiz_id
        }
    else:
        string = {
            'type': "final_quiz",
            'chapter_name': "Finals",
            'is_created': 0,
            'quiz_id' : class_id + "_FinalQuizq"
        }
    array_list.append(string)
    return array_list




#class id is ME111_C1
@app.route("/retrieve_course_details_by_class_id/<string:class_id>/")
def retrieve_course_details_by_class_id(class_id):
    #retrieve from registration is_approved = 0 and class_record is_approved = 1
    try:
        chapter_quiz_array = retrieve_chapter_detail(class_id)

        final_quiz_array = retrieve_quiz_chapter_detail(class_id)


        return jsonify(
        {
            'code': 200,
            'results': chapter_quiz_array + final_quiz_array
        })

    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "message": "An error occur when retrieve chapters quiz informations." + str(e)
                },
            }
        ), 404










@app.route("/create_quiz", methods=['POST'])
def create_quiz():
    data = request.get_json()
    try:
        # create_quiz_code = create_quiz_db(data['quiz_id'],data['timing'])

        if(data['type'] == 'chapter_quiz'):
            #is chapter quiz
            is_exist_chapter_quiz = Chapter_Quiz.query.filter_by(quiz_id = data['quiz_id']).first()

            if(is_exist_chapter_quiz  != None):
                return jsonify(
                {
                    'code': 201,
                    'results': "Chapter Quiz have already been created. You are not allow to have multiple entry"
                    
                })
            chapter_quiz = Chapter_Quiz(
                quiz_id=data['quiz_id'],
                chapter_id=data['quiz_id'][:-1],
                total_marks = data['total_marks'],
                timing = data['timing']
            )

            chapter_quiz.insert_chapter_quiz()
        elif(data['type'] == 'final_quiz'):

            is_exist_final_quiz = Final_Quiz.query.filter_by(quiz_id = data['quiz_id']).first()

            if(is_exist_final_quiz  != None):

                return jsonify(
                {
                    'code': 201,
                    'results': "Final Quiz have already been created. You are not allow to have multiple entry"
                    
                })
            array = data['quiz_id'].split("_")
            course_id = array[0]
            final_quiz = Final_Quiz(
                quiz_id=data['quiz_id'],
                course_id=course_id,
                total_marks = data['total_marks'],
                timing = data['timing']
            )
            final_quiz.insert_final_quiz()

 
        for i in range(data['num_of_questions']):
            question_record = Question(
                quiz_id=data['quiz_id'],
                question_id=data['question_id'][i],
                question=data['question'][i],
                question_type=data['question_type'][i],
                option=data['option'][i],
                question_mark=data['question_mark'][i],
                answer=data['answer'][i]
            )
            create_question_code = question_record.create_question()



        return jsonify(
        {
            'code': 200,
            'results': "Successfully create the quiz"
            
        })
    
    except Exception as e:
        return jsonify(
        {
            'code': 500,
            'results': "error in creating the quiz"
            
        })





@app.route("/view_quiz/<string:quiz_id>/")
def view_quiz(quiz_id):

    array_list = []
    timing = ""
    total_marks = ""
    chapter_quiz = Chapter_Quiz.query.filter_by(quiz_id = quiz_id).first()
    final_quiz = Final_Quiz.query.filter_by(quiz_id = quiz_id).first()
    if(chapter_quiz != None):

        timing = chapter_quiz.timing 
        total_marks = chapter_quiz.total_marks

    if(final_quiz != None):

        timing = final_quiz.timing 
        total_marks = final_quiz.total_marks


    question_list = Question.query.filter_by(quiz_id = quiz_id).all()
    if(len(question_list)):
        for question in question_list:
            question_json = question.json()
            array_list.append(question_json)

    result = {
        "quiz_id" : quiz_id,
        "timing" : timing,
        "total_marks" : total_marks,
        "results": array_list
    }

    return jsonify(
        {
            'code': 200,
            'results': result
            
        })
        


@app.route("/display_course_material_date/<string:class_id>")
def display_course_material_date(class_id):

    class_run_info = Class_Run.query.filter_by(class_id  = class_id).first()
    is_commence = class_run_info.check_commence_of_course()
    if(is_commence):
        return jsonify(
            {
                'code': 200,
                'is_commence': 1
                
            })
    return jsonify(
        {
            'code': 200,
            'is_commence': 0
            
        })  

@app.route("/check_completion_course/<string:course_id>/<string:learner_id>")
def check_completion_course(course_id,learner_id):

    completion_record_info = Completion_Record.query.filter_by(course_id  = course_id,learner_id=learner_id).first()
    if(completion_record_info == None):
        return jsonify(
            {
                'code': 200,
                'is_completed': 0
                
            })
    return jsonify(
        {
            'code': 200,
            'is_completed': 1
            
        })



if __name__ == '__main__':
    print("RUNNING TEST LETS GO")
    app.run(host='0.0.0.0', port=5000, debug=True)