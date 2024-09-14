import re


class ValidateInputs:
    """
    A class to validate the various data fields.

    ...
    
    Methods
    -------
    data_required(field_value):
        performs Data Required Validations on the data field.
    validate_email(email):
        Validates email address of a person
    validate_mobile(mobile, length):
        Validates mobile number of a person
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the ValidateInputs object.
        
        Parameters
        ----------
        """

        pass

    def data_required(self, field_value):
        """
        Validates that input was provided for a field.

        Parameters
        ----------
        field_value : str
            value of a particular data field 

        Returns
        -------
        True or False: boolean
            True if the data field value is not empty otherwise False
        """

        if len(str(field_value).strip()) != 0:
            return True
        else:
            return False



    def validate_email(self, email):
        """
        Validates an e-mail address

        Parameters
        ----------
        email : str
            e-mail address

        Returns
        -------
        error_message: str
            an email validation error message
        """

        email = email.strip()
        mail_regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"

        if not re.search(mail_regex, email):
            error_message = "Email address is not Valid."
            return error_message

    def validate_mobile(self, mobile, length=10):
        """
        Validates a mobile number by checking the number of digits in it

        Parameters
        ----------
        mobile : int
            mobile number 
        length : int
            number of digits in a valid mobile number (default is 10)

        Returns
        -------
        error_message : str
            a mobile validation error message
        """

        mobile = str(mobile)

        if len(mobile) != length:
            error_message = "Mobile number should of " + str(length) + " digits."
            return error_message


    def validate_datatype(self, validations, data):
        """
        Validates the data-types of all the values received via frontend

        Parameters
        ----------
        validations : dict
            dictionary of data types associated with the values
        data : dict
            dictionary containing all the values revceived via frontend

        Returns
        -------
        messages : list
            list of error messages
        """

        validation_keys = list(validations.keys())
        validation_messages = list()
        for value in validation_keys:
            if not isinstance(data[value], validations[value]):
                validation_messages.append(value + " should be a " + str(validations[value]))

        return validation_messages


validator = ValidateInputs()
