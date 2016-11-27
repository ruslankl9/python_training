Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first_name>, <last_name> and <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first_name | last_name | address                 |
  | David      | Stein     | 3765 Lang Avenue        |
  | Wendy      | Franklin  | 665 Philadelphia Avenue |
  | FirstName2 | LastName2 | 1024 Camden Street      |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <first_name>, <last_name> and <address>
  When I modify the contact from the list
  Then the new contact list is equal to the old list with modified contact

  Examples:
  | first_name | last_name | address          |
  | Jack       | Newman    | 37 Sun Street    |
  | Fred       | Baker     | 65 United Avenue |
  | Lewis      | Nicols    | 44 Dell Street   |