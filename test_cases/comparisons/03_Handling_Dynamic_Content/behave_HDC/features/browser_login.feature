Feature: Browser Login

  Scenario: User logs into the application and posts a comment
    Given I open the browser "chrome"
    When I visit the login page
    And I fill in the login form with email "admin@helloflask.com" and password "helloflask"
    And I submit the login form
    And I navigate to the photo page with id "34"
    Then I should see the initial number of comments
    When I enter a new comment "This is a test comment."
    And I submit the comment form
    Then I should see the updated number of comments
    And I close the browser

