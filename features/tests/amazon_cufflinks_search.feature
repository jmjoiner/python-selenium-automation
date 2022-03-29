# Created by jerma at 12/22/2021
Feature: Test for amazon cufflinks search
  Search for cufflinks on Amazon

  Scenario: User can search for cufflinks on Amazon
    Given Open Amazon page
    When Search for cufflinks
    And Click search icon
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 item(s)

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present

  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by alias <alias>
    And Search for Faust
    Then Verify <department> department is selected
    Examples:
    |alias        |department   |
    |stripbooks   |books        |
    |audible      |audible      |

  Scenario: User can search for long tube headers
    Given Open Amazon page
    When Select department by alias automotive
    And Search for long tube headers
    Then Verify automotive department is selected

  Scenario: User can see New Arrivals while on Product Page
    Given Open product page B074TBCSC8
    When Hover over New Arrivals
    Then Verify user can see deals