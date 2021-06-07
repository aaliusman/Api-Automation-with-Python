# Created by bravo1516 at 6/3/21
Feature: Verify Books are Added and Deleted using Library API
  # Enter feature description here

  @Library
  Scenario: Verify AddBook API
    Given User have details which needs to be added to Library
    When User execute the AddBook PostAPI method
    Then User verify book is successfully added
    And User Verify status code of 200

  @Regression
  Scenario Outline: Verify multiple data set for AddBook API
    Given User needs <isbn> and <aisle> to be added to Library
    When User execute the AddBook PostAPI method
    Then User verify book is successfully added
    Examples:
      | isbn     | aisle    |
      | df6787dk | 3998ui29 |
      | af0176dj | 63zxs77  |