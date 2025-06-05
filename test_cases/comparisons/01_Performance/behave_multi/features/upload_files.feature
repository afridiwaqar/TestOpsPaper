Feature: Upload files to the server

  Scenario: Login and upload files
    Given I open the browser
    And I navigate to the login page
    When I fill in the login form
    Then I should be logged in
    When I upload files
    Then the files should be uploaded successfully
