Feature: Email existence verification
  # BRD-1037
  # Description of the scenario followed by the requirement

  @webverify
  Scenario: User with invalid credentials can't restore password
    Given I open a browser and navigate to "restore" page
    When I insert an "email"
    And I click on "restore" button
    Then The "email does not exist" message should be displayed