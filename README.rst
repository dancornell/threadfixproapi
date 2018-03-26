ThreadFix Pro API
**************

A Python module to assist with the `ThreadFix Professional <https://denimgroup.com/threadfix/>`__ RESTFul API to administer scan artifacts and overall ThreadFix vulnerability administration.

Quick Start
~~~~~~~~~~~

Several quick start options are available:

- Install with pip: ``pip install threadfixproapi``
- Build locally: ``python setup.py install``
- `Download the latest release <https://git.target.com/tts-pse/threadfixproapi/releases/new/>`__.

Example
~~~~~~~

::

    # import the package
    from threadfixproapi import threadfixpro

    # setup threadfix connection information
    host = 'https://127.0.0.1:8443/threadfix/'
    api_key = 'your_api_key_from_threadfix_professional'

    # initialize threadfix pro api module
    tfp = threadfixpro.ThreadFixProApi(host, api_key)

    # If you need to disable certificate verification.
    # tfp = threadfixpro.ThreadFixProApi(host, api_key, verify_ssl=False)

    # List your threadfix pro teams
    teams = tfp.list_teams()
    if teams.success:
        print("{}".format(teams.data))

        for team in teams.data:
            print(team['name'])  # Print the name of each team
    else:
        print("ERROR: {}".format(teams.message))

Supporting information for each method available can be found in the `documentation <https://target.github.io/threadfixapi/>`__.

Bugs and Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~

Found something that doesn't seem right or have a feature request? `Please open a new issue <https://git.target.com/tts-pse/threadfixproapi/issues/new>`__.

Copyright and License
~~~~~~~~~~~~~~~~~~~~~
.. image:: https://img.shields.io/github/license/target/threadfixapi.svg?style=flat-square

- Copyright 2018 Target Brands, Inc.
