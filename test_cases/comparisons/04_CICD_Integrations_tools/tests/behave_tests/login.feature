Feature: Login

  Scenario: User logs into the application
    Given I open the browser "chrome"
    When I visit the login page
    And I enter the email "admin@helloflask.com"
    And I enter the password "helloflask"
    And I submit the login form
    Then I should see the title containing "Home - Albumy"
