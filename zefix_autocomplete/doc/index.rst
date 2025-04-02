********************************
Abilium Odoo-Zefix-Autocomplete
********************************


Prerequisite
===============

In order to be able to use this service you need to have an authorization (Zefix-Credentials) for the Zefix API.
More on that can be read on the
`Swiss Federal Office of Justice <https://www.bj.admin.ch/bj/de/home/wirtschaft/handelsregister.html>`_'s Page on Zefix.
There you'll find instructions on how to request access.

Setup
===============

Installation
----------------------
Install the app from the Apps module

Configuration
----------------------
In Odoo under Settings > Zefix Autocomplete, enter your credentials and set the checkmark for is Production if you
want to use the productive API. Default (unchecked) is the test API which should only be used by developers since it may contain bugs.

How to use
===============
Go to the Contacts module and create a new contact. As soon as you have written at least 3 characters
the dropdown menu will show you suggestions for your text.

Note
----------------------
You will also see Odoo's autocomplete suggestions. This code does not block that feature in any way,
but for Odoo's autocomplete you will have to buy credits. This module's answers can be selected without any additional costs.  \
You can clearly differentiate the two types of suggestions by the VAT-Number being displayed behind this module's suggestions.