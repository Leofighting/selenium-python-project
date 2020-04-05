Feature: Register User

  As a developer
  This is my first bdd project

  Scenario: open register website
    When I open the register website "http://my.cnki.net/Register/"
    Then I expect that the title is "注册"

  Scenario: input username
    When I set with username "leo2020@163.com"
    And I set with password "leo2020com"
    And I set with email "leo2020@163.com"
    And I set with code "12qw"
    And I click with register_button
    Then I except that text "请输入验证码"

