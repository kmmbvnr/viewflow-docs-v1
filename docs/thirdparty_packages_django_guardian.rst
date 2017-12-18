===============
django-guardian
===============

**PRO Only**

Viewflow
========

Viewflow PRO has support for the django-guardian out of the box.

You can use `obj=` parameter in the `.Permission(..)` specification,
to provide an object to restrict a task access permission::

    accept_bill = flow.View(
      UpdateProcessView,
      fields=[
          'accepted'
      ]
    ).Permission(
        'department.can_accept_bill',
        obj=lambda process: process.department
    ).Next(this.check_bill_accept)

Queue View would restrict available tasks based on user object-level permissions.

Demo: https://github.com/viewflow/cookbook/tree/master/guardian
