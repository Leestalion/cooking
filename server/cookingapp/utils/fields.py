from wtforms import SelectField
from wtforms import widgets
from .widgets import ListRadioWidget

class CustomRadioField(SelectField):
    widget = ListRadioWidget(prefix_label=False)
    option_widget = widgets.RadioInput()