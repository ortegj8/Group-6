"""
Courses Database Models.

This module defines the Django models used for managing courses, professors, semesters,
and the mapping between professors and specific class sections.
"""

from django.db import models
from users import models as user_model
from django.conf import settings


class Professor(models.Model):
    """
    Professor Model.

    This model represents a professor in the courses database.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model from the users app.
            This field links the professor to their user account.
    """
    user = models.OneToOneField(
        user_model.User,
        on_delete=models.CASCADE,
        related_name="user_professor"
    )

    def __str__(self):
        """
        Return a string representation of the professor.

        Returns:
            str: The professor's full name in "First Last" format.
        """
        return f"{self.user.first_name} {self.user.last_name}"


class Class(models.Model):
    """
    Class Model.

    This model represents a course or class in the academic system.

    Attributes:
        name (CharField): The name of the class, which must be unique.
        professors (ManyToManyField): A many-to-many relationship linking the class to its professors.
            The association is managed through the ProfessorClassSection model, which allows a class
            to be taught by multiple professors across different sections and semesters.
    """
    name = models.CharField(max_length=50, unique=True)

    # Explicitly reference the Professor model from the courses app.
    professors = models.ManyToManyField(
        "courses.Professor",
        # The join table will be created using the ProfessorClassSection model instead
        # of Django automatically generating one between Professor and Class.
        through="ProfessorClassSection",
    )

    def __str__(self):
        """
        Return the class name as its string representation.

        Returns:
            str: The unique name of the class.
        """
        return self.name


class Semester(models.Model):
    """
    Semester Model.

    This model represents an academic semester or term during which classes are offered.

    Attributes:
        name (CharField): The name of the semester, which must be unique.
            For example, "Fall 2023".
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Return the semester name as its string representation.

        Returns:
            str: The unique name of the semester.
        """
        return self.name


class ProfessorClassSection(models.Model):
    """
    Mapping Professors to Class Sections.

    This intermediary model maps a professor to a specific class section within a given semester.
    It serves as the 'through' model for the many-to-many relationship between professors and classes.

    Attributes:
        professor (ForeignKey): A foreign key linking to the Professor model,
            representing the professor teaching the class section.
        class_instance (ForeignKey): A foreign key linking to the Class model,
            representing the class that is being taught.
        semester (ForeignKey): A foreign key linking to the Semester model,
            indicating when the class section is being offered.
        section_number (IntegerField): An optional field representing the section number for the class.
            This field can be blank or null if not applicable.
    """
    professor = models.ForeignKey(
        "courses.Professor",
        on_delete=models.CASCADE,
        related_name="profclassect"
    )
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """
        Return a descriptive string representation of the professor's class section.

        Returns:
            str: A string combining the professor's name, class name, semester, and section number.
        """
        return f"{self.professor} - {self.class_instance} - {self.semester} (Section {self.section_number})"

