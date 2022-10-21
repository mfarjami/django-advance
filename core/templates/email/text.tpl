{% extends "mail_templated/base.tpl" %}

{% block subject %}
Verified Account
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
{{token}}
{% endblock %}