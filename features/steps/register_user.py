# -*- coding:utf-8 -*-
__author__ = "leo"

from behave import *
from features.lib.pages.register_page import RegisterPage

use_step_matcher("re")


@when('I open the register website "([^"]*)"')
def step_register(context, url):
    RegisterPage(context).get_url(url)


@then('I expect that the title is "([^"]*)"')
def step_register1(context, title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title


@when('I set with username "([^"]*)"')
def step_register(context, username):
    RegisterPage(context).send_username(username)


@when('I set with password "([^"]*)"')
def step_register(context, password):
    RegisterPage(context).send_username(password)


@when('I set with email "([^"]*)"')
def step_register(context, email):
    RegisterPage(context).send_username(email)


@when('I set with code "([^"]*)"')
def step_register(context, code):
    RegisterPage(context).send_username(code)


@when('I click with register_button')
def step_register(context):
    RegisterPage(context).click_register_button()


@then('I except that text "([^"]*)"')
def step_register(context, code_text):
    text = RegisterPage(context).get_code_text(code_text)
    assert code_text in text
