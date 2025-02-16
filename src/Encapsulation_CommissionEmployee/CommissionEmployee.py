class CommissionEmployee:
    first_name= ""
    last_name= ""
    social_security_number= ""
    gross_sales = 0.0
    commission_rate = 0.0


    def __init__(self, first_name,
                 last_name,
                 social_security_number,
                 gross_sales,
                 commission_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__social_security_number = social_security_number
        if gross_sales >= 0:
            self.__gross_sales = gross_sales
        else:
            raise Exception("Gross sales must be greater than or equal to zero.")
        if commission_rate < 0 or commission_rate > 1:
            raise Exception("Commission rate must be between 0 and 1.")
        else:
            self.__commission_rate = commission_rate

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_social_security_number(self):
        return self.__social_security_number

    def get_gross_sales(self):
        return self.__gross_sales

    def get_commission_rate(self):
        return self.__commission_rate

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_social_security_number(self, social_security_number):
        self.__social_security_number = social_security_number

    def set_commission_rate(self, commission_rate):
        if commission_rate < 0 or commission_rate > 1:
            raise Exception("Commission rate must be between 0 and 1.")
        else:
            self.__commission_rate = commission_rate

    def set_gross_sales(self, gross_sales):
        if gross_sales < 0:
            raise Exception("Gross sales must be greater than or equal to zero.")
        self.__gross_sales = gross_sales

    def earnings(self):
        return self.__gross_sales * self.__commission_rate

    def to_string(self):
        return ("Employee Details \n"
                "First name: " + self.__first_name +
                "\nLast name: " + self.__last_name +
                "\nSocial security number: " + self.__social_security_number +
                "\nCommission rate: " + str(self.__commission_rate) +
                "\nGross sales: $" + str(self.__gross_sales))

employee = CommissionEmployee(
    "Future",
    "Hendrix",
    "0011223364",
    50000,
    0.5
)
#Employee at the time of creation(instantiation)
print(employee.to_string())

#Employee earnings at the time of creation(instantiation)
print(employee.get_first_name() + " earns $" + str(employee.earnings()))

#Changing employee sales(setting sales)
employee.set_gross_sales(60000)

#Changing employee commission rate(setting the commission rate)
employee.set_commission_rate(0.6)

#Printing the edited employee
print(employee.to_string())

#Printing new earnings
print(employee.get_first_name() +  " now earns " +  str(employee.earnings()))
