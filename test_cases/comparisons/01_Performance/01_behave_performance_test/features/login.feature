Feature: Login and upload images

  Scenario: Login and upload images separately
    Given I open the login page
    When I fill in the login form with valid credentials
    And I submit the login form
    Then I should be logged in
    When I navigate to the upload page
    And I upload 1 image
    And I upload another 1 image
    And I upload another 1 image

