"""
Test Cases for Account Model
"""
import json
from random import randrange
import pytest
from models import db
from models.account import Account, DataValidationError
from sqlalchemy.exc import IntegrityError

ACCOUNT_DATA = {}

@pytest.fixture(scope="module", autouse=True)
def load_account_data():
    """ Load data needed by tests """
    global ACCOUNT_DATA
    with open('tests/fixtures/account_data.json') as json_data:
        ACCOUNT_DATA = json.load(json_data)

    # Set up the database tables
    db.create_all()
    yield
    db.session.close()

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """ Truncate the tables and set up for each test """
    db.session.query(Account).delete()
    db.session.commit()
    yield
    db.session.remove()

######################################################################
#  E X A M P L E   T E S T   C A S E
######################################################################

# ===========================
# Test Group: Role Management
# ===========================

# ===========================
# Test: Account Role Assignment
# Author: John Businge
# Date: 2025-01-30
# Description: Ensure roles can be assigned and checked.
# ===========================

def test_account_role_assignment():
    """Test assigning roles to an account"""
    account = Account(name="John Doe", email="johndoe@example.com", role="user")

    # Assign initial role
    assert account.role == "user"

    # Change role and verify
    account.change_role("admin")
    assert account.role == "admin"

# ===========================
# Test: Invalid Role Assignment
# Author: John Businge
# Date: 2025-01-30
# Description: Ensure invalid roles raise a DataValidationError.
# ===========================

def test_invalid_role_assignment():
    """Test assigning an invalid role"""
    account = Account(role="user")

    # Attempt to assign an invalid role
    with pytest.raises(DataValidationError):
        account.change_role("moderator")  # Invalid role should raise an error


######################################################################
#  T O D O   T E S T S  (To Be Completed by Students)
######################################################################

"""
Each student in the team should implement **one test case** from the list below.
The team should coordinate to **avoid duplicate work**.

Each test should include:
- A descriptive **docstring** explaining what is being tested.
- **Assertions** to verify expected behavior.
- A meaningful **commit message** when submitting their PR.
"""

# TODO 1: Test Account Serialization
# - Ensure `to_dict()` correctly converts an account to a dictionary format.
# - Verify that all expected fields are included in the dictionary.

# TODO 2: Test Updating Account Email
# - Ensure an account’s email can be successfully updated.
# - Verify that the updated email is stored in the database.

# ===========================
# Test: Missing Required Fields
# Author: Sarel Erasmus
# Date: 2025-02-05
# Description: Ensure that creating an 'Account()' without required fields raises an error.
# ===========================

def test_missing_required_fields():
    # Create account that has the required fields not included
    account = Account()

    # Pytest is expecting an Integrity Error since the account object doesn't have the required fields
    with pytest.raises(IntegrityError):
        # Try to commit this account to the database to make sure it produces an error
        db.session.add(account)
        db.session.commit()

# ===========================
# Test: Test Positive Deposit
# Author: Alexander Baker
# Date: 2025-02-01
# Description: Ensure a positive deposit increases balance
# ===========================
def test_positive_deposit():
    """Test depositing a positive number"""
    account = Account(balance=0.0)

    # Attempt to deposit a positive number
    account.deposit(100.0)
    assert account.balance == 100.0
    
# TODO 5: Test Deposit with Zero/Negative Values
# - Ensure `deposit()` raises an error for zero or negative amounts.
# - Verify that balance remains unchanged after an invalid deposit attempt.

# ===========================
# Test: Valid Withdrawal
# Author: Daniel Levy
# Date: 2025-02-04
# Description: Ensure `withdraw()` correctly decreases the account balance.
#              Verify that withdrawals within available balance succeed.
# ===========================
def test_valid_withdrawal():
    # Create new account for unit test
    account = Account(name="Daniel Levy", email="levyd1@unlv.nevada.edu", balance=100.00)

    # First Test: Withdraw decreases balance by the correct amount
    original_balance = account.balance
    account.withdraw(20)
    assert account.balance == (original_balance-20)
    
    # Second Test: Withdraw is able to succeed with current available balance
    original_balance = account.balance 
    amount_to_decrease_balance = 30
    account.withdraw(amount_to_decrease_balance)
    assert account.balance > amount_to_decrease_balance
    
# TODO 7: Test Withdrawal with Insufficient Funds
# - Ensure `withdraw()` raises an error when attempting to withdraw more than available balance.
# - Verify that the balance remains unchanged after a failed withdrawal.

# TODO 8: Test Password Hashing
# - Ensure that passwords are stored as **hashed values**.
# - Verify that plaintext passwords are never stored in the database.
# - Test password verification with `set_password()` and `check_password()`.

# TODO 9: Test Role Assignment
# - Ensure that `change_role()` correctly updates an account’s role.
# - Verify that the updated role is stored in the database.

# ===========================
# Test: Test account deactivation/reactivation
# Author: Jesse Ortega
# Date: 2/5/2025
# Description: Ensure accounts can be deactivated.
# - Verify that deactivated accounts cannot perform certain actions. (deposit, withdraw)
# - Ensure reactivation correctly restores the account.
# ===========================

def test_account_deactivate():
    """Verify that an account can be deactivated"""
    # Create an activated test account
    test_account = Account(disabled=False)

    # Assert that the test account is initialized as intented
    assert test_account.disabled == False

    # Deactivate the test account
    test_account.deactivate()

    # Assert that the test account is now disabled
    assert test_account.disabled == True

def test_account_reactivate():
    """Verify that a disabled account can be reactivated"""
    # Create a deactivated test account
    test_account = Account(disabled=True)

    # Assert that the test account is initialized as intented
    assert test_account.disabled == True

    # Reactivate the test account
    test_account.reactivate()

    # Assert that the test account is no longer disabled
    assert test_account.disabled == False

def test_disabled_account_deposit():
    """Verify that disabled accounts cannot perform certain actions: desposit"""
    # Create a deactivated test account with an initial balance
    test_account = Account(disabled=True, balance=100.00)

    # Assert that the test account is initialized as intented
    assert test_account.disabled == True and test_account.balance == 100.00

    # Attempt to deposit funds into the disabled account
    with pytest.raises(DataValidationError):
        test_account.deposit(50.00)

def test_disabled_account_withdraw():
    """Verify that disabled accounts cannot perform certain actions: withdraw"""
    # Create a deactivated test account with an initial balance
    test_account = Account(disabled=True, balance=100.00)

    # Assert that the test account is initialized as intented
    assert test_account.disabled == True and test_account.balance == 100.00

    # Attempt to withdraw funds from the disabled account
    with pytest.raises(DataValidationError):
        test_account.withdraw(50.00)

# TODO 10: Test Invalid Role Assignment
# - Ensure that assigning an invalid role raises an appropriate error.
# - Verify that only allowed roles (`admin`, `user`, etc.) can be set.

# TODO 11: Test Deleting an Account
# - Ensure that `delete()` removes an account from the database.
# - Verify that attempting to retrieve a deleted account returns `None` or raises an error.

