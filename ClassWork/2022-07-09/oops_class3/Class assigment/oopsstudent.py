"""d"""
class Student:
    """d"""

    def __init__(self,username):
        """d"""
        self.__username = username

        def getstudentdetails(self):
            """d"""
            print('getting students\'s details')



class Course:
    """d"""

    def listcourses(self):
        """d"""
        print('getting the list of courses')

    def defineacourse(self,coursename,coursetype,fees,instructor,period):
        """d"""
        print('inserting a new course into database')

    def getcoursedetails(self):
        """d"""
        print('getting the course details')
    
class JobGCourse(Course):
    """d"""
    def getcoursetimings(self,courseid):
        """d"""
        print('getting JG course timings')
    
    def getcoursedetails(self):
        return super().getcoursedetails(), self.getcoursetimings()
        



class StudentCourses(Student, Course):
    """d"""
    def getstudentenrolments(self):
        """d"""
        print('getting user\'s types by checking in database for enrolments')