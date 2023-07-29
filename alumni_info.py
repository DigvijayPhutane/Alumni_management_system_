class Alumni:

    def __init__(self,alid,alnm,aldepart,alcompany,yearg,alnum):
        self.alumni_id = alid
        self.alumni_name = alnm
        self.alumni_department = aldepart
        self.alumni_company = alcompany
        self.year_of_graduation = yearg
        self.alumni_number = alnum

    def __str__(self):
        return f'''{self.__dict__}'''
    def __repr__(self):
        return str(self)
'''
CREATE TABLE ALUMNI_MASTER(
    ALUMNI_ID INT,
    ALUMNI_NAME VARCHAR(30),
    ALUMNI_DEPARTMENT VARCHAR(30),
    ALUMNI_COMPANY VARCHAR(30),
    YEAR_OF_GRADUATION INT,
    ALUMNI_NUMBER BIGINT,
    PRIMARY KEY (ALUMNI_ID)
)'''