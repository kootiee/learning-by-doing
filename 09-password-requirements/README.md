# Password Requirements

## Your Mission

You know how when you set a password on a website, normally there are annoying requirements you have to satisfy? "This is not a valid password, it must contain at least one number"? You're going to write a system to do that. Not only that, but it will be an extensible system; it will be easy to add or remove requirements without changing the checking logic.

How will we do that? We're going to write a PasswordChecker class, which handles the basics of looking at a string, and reporting to the user. However, that class won't know anything about the requirements themselves. We're also going to have a number of Requirements classes. Each one will check the password for one specific requirement. They will all have the same interface, so they can all be used in the same way. You'll pass a list of requirements to the constructor of the checker, and that's how it knows which requirements to check for.

## What Are We Doing Exactly?

You're going to need at least three Requirement classes: `MustContainNumberRequirement`, `MustContainCapitalRequirement`, and `MustMeetMinimumLengthRequirement`. They'll all contain the same number of methods, although the implementations will be different:
* `check(self, password)`: You pass in a password to check. The method will return `True` if it meets the requirements, `False` otherwise.
* `message(self)`: Returns a string that explains the requirement, e.g. "The password must contain at least one number."

You may want a constructor (`__init__`), you may not. Remember that constructors are there to initialize objects, to let you configure them. If there's nothing to configure, maybe you don't need one. If you want to easily change something, such as minimum password length, maybe you do.

You'll also want a PasswordChecker:
* `__init__(self, requirements)`: `requirements` is a list of Requirement objects. 
* `check(self, password)`: You pass in the password to check. The method will return `True` if it meets *all* of the requirements, `False` otherwise.
* `messages(self)`: Returns a list of strings, which explain the requirements that were broken on the last call to `check`. For instance, if the minimum password length is 8, and `check` is called with 'Smurfs', `messages` would then return a list of two strings, one regarding the minimum length, and one regarding the need for a number in the password. If `check` is then called with '123Smurfs', `messages` would then return an empty list.

As a final touch, add a fourth Requirement, one of your own design. It can check for whatever you want, as long as it has the same public interface as the other Requirements so that it can be used interchangeably. 

So, once it's all written:
* the system instantiates some requirements
* these requirements are given to the PasswordChecker when it is constructed
* any passwords that need checking are passed to `PasswordChecker.check`
* if the password does not meet the requirements, call `PasswordChecker.messages` to find out why

# Restrictions
* You should be able to run the finished system from the command line, and you should also have unit tests for your classes.
* Remember that we want this system to be flexible; test that you can pass different numbers of requirements into your PasswordChecker.
* Your program should be split up into modules; you can do this at your own discretion, but you should at least keep your `main` in a different module from your class defintions..
* Your module `main.py` contains your import guard and your main function.
* `main.py` *should* be as simple as possible. Most of your program's logic should be in the classes.
* Each test may only have one assert.
* Gijs Compensation Measures are still in effect: no globals.
* As standard from now on, no raw code; everything must be in a function apart from import guards, constants, and decorators.
* A hint; the PasswordChecker needs at least one Requirement in order to do anything useful. Maybe write one of the Requirements first?
