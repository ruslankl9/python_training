*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures

Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add New Contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  first_name1  last_name1  address1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Delete Contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Modify Contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  first_name_x   last_name_x  address_x
    Modify Contact  ${contact}  ${new_contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Append To List  ${old_list}  ${new_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}