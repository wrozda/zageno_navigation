Feature: Searching products and adding them to the cart

  @staging
  Scenario: As a logged user I search the product and add them to the cart
    Given I log in to the ZAGENO app
    When I search the product using searchbar
    And I add the product to cart
    Then Product should have been in cart
    And Cart should be empty
