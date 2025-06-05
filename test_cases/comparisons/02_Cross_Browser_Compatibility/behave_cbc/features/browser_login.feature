Feature: Browser Login

  Scenario Outline: User logs into the application from different browsers
    Given I open the browser "<browser>"
    When I visit the login page
    And I enter the email "admin@helloflask.com"
    And I enter the password "helloflask"
    And I submit the login form
    Then I should see the title containing "Home - Albumy"

    Examples:
      | browser  |
      | chrome   |
      | firefox  |
      | edge     |
