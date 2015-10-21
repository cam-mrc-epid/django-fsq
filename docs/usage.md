# Usage

The questionnaire models are accessible via the Django Admin and data can be exported from there.  

To work with the models in another app you can simply import them and use them in the usual way.

```python
from questionnaire.models import Results, Users

results = Results.objects.all()
user = Users.objects.get(user_id='davidg')

```
