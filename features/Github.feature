# Created by bravo1516 at 6/3/21
Feature: Github Api Validation
  # Enter feature description here

  Scenario: Session management check
    Given User utilize github credentials
    When User hit getRepo API of github
    Then User Verify status code of 200