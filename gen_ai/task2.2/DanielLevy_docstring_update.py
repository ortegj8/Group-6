# ChatGPT Documentation Suggestion
def checkIfStudentFileExists(self, fileName):
    """
    Checks if a student submission file exists in the ZIP directory.

    This method takes a file name containing a student name and an ID, extracts
    both values, and verifies whether the file exists in the specified ZIP directory.
    If the file is missing, an error message is logged.

    Args:
        fileName (str): The name of the file, expected to be in the format
                        "{submission_id}-{student_name}".

    Returns:
        tuple: A tuple containing:
            - subID (int): The extracted submission ID.
            - studentName (str): The extracted student name.
    """
