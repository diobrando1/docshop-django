# docshop-django
python project

(1) Testy w /docshop/tests/test_type.py

> python3 manage.py test tests/

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.432s

OK
Destroying test database for alias 'default'...


(2) Pylint

> pylint --load-plugins=pylint_django pdfshop/*.py

************* Module pdfshop.models
pdfshop/models.py:28:24: W0613: Unused argument 'sender' (unused-argument)
pdfshop/models.py:28:0: W0613: Unused argument 'kwargs' (unused-argument)
************* Module pdfshop.views
pdfshop/views.py:65:25: W0212: Access to a protected member _errors of a client class (protected-access)

------------------------------------------------------------------
Your code has been rated at 9.72/10 (previous run: 9.81/10, -0.09)

