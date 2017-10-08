class Profile:
    __serial = None
    __name = ""
    __visibility = ""
    __birthday = ""
    __gender = ""
    __location = ""
    __status = ""
    __joined = ""
    __job = ""
    __language = ""
    __blog_traffic = ""
    __posts = ""
    __friends = []

    def __init__(self, serial, name, visibility, birhtday, gender, location, status, joined, job, language, blog_traffic, posts,friends):
            self.serial = serial
            self.name = name
            self.visibility = visibility
            self.birhtday = birhtday
            self.gender = gender
            self.location = location
            self.status = status
            self.joined = joined
            self.job = job
            self.language = language
            self.blog_traffic = blog_traffic
            self.posts = posts
            self.friends = friends

    #Properties


    @property
    def name(self):
            return self.__name
            
    @name.setter
    def name(self, value):
            self.__name = value
            
    @property
    def serial(self):
            return self.__serial
            
    @serial.setter
    def serial(self, value):
            self.__serial = value

    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self,value):
        self.__visibility = value

    @property
    def birthday(self):
        return self.__birthday
    @birthday.setter
    def birthday(self,value):
        self.__birthday= value

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,value):
        self.__gender = value

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, value):
        self.__location = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,value):
        self.__status = value

    @property
    def joined(self):
        return self.__joined
    @joined.setter
    def joined(self,value):
        self.__joined = value

    @property
    def job(self):
        return self.__job
    @job.setter
    def job(self,value):
        self.__job = value

    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self,value):
        self.__language = value

    @property
    def blog_traffic(self):
        return self.__blog_traffic
    @blog_traffic.setter
    def blog_traffic(self,value):
        self.__blog_traffic = value

    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def posts(self,value):
        self.__posts = value

    @property
    def friends(self):
        return self.__friends
    @friends.setter
    def friends(self,value):
        self.__friends = value

    def serialize(self):
        return[{
            "serial": self.serial,
            "name": self.name,
            "visibility": self.visibility,
            "birthday":self.birthday,
            "gender":self.gender,
            "location": self.location,
            "status": self.status,
            "joined":self.joined,
            "job":self.job,
            "language":self.language,
            "blog_traffic":self.blog_traffic,
            "posts":self.posts,
            "score": self.posts+self.language
            #"friends": [for i in self.firends]
        } ]



