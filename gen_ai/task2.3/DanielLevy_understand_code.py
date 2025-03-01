# ChatGPT improvement
def verifyStudentUserExistsInMetaData(self):
    for key, value in self.users.items():
        subID, studentName = self.checkIfStudentFileExists(key)

        entry = self.metaData.loc[self.metaData['Id'] == value]

        if entry.empty:
            self.addError(f"Error! No metadata for user ID {value} was found.", 'meta')
            continue

        if entry.shape[0] > 1:
            self.addError(f"Error! User ID {value} has more than one entry.", 'meta')
            continue

        if entry.iloc[0, 2] != studentName:
            self.addError(f"Error! User ID {value} does not have a matching name.", 'meta')
