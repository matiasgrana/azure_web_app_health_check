Description
===========

Checks web apps health.

`VERSION  <web_app_health_check/VERSION>`__

Install
=======

Linux::

    sudo pip3 install web_app_health_check --upgrade

Also is possible to use::

    sudo python3 -m pip install web_app_health_check --upgrade

On windows with python3.5::

    pip install web_app_health_check --upgrade

For proxies add::

    --proxy='http://user:passw@server:port'

Usage
=====

Use the command line::

    > web_app_health_check --help
      usage: web_app_health_check [-h] [-u [URL]] [-e [EXTRA_ARGS]]

        optional arguments:
        -h, --help            show this help message and exit
        -u [URL], --url [URL]
                              url to check 		
        -e [EXTRA_ARGS], --extra_args [EXTRA_ARGS]
                              extra args


Example usage
=============

Example use:

    > web_app_health_check -u "https://xxx/"


Nagios config
=============

Example command::

    define command{
        command_name  web_app_health_check
        command_line  /usr/local/bin/web_app_health_check -u "$ARG1$" --extra_args='$ARG6$'
    }

Example service::

    define service {
            host_name                       SERVERX
            service_description             service_name
            check_command                   web_app_health_check!http://url/
            use				                generic-service
            notes                           some useful notes
    }

You can use ansible role that already has the installation and command: https://github.com/CoffeeITWorks/ansible_nagios4_server_plugins

TODO
====

* Use hash passwords
* Add Unit tests?
