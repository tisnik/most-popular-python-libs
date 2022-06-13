# naimportujeme vybrané funkce z knihovny `bokeh.io`
from bokeh.io import show

# naimportujeme vybrané funkce z knihovny `bokeh.models`
from bokeh.models import Button, CustomJS

# vytvoření ovládacího prvku
button = Button(label="Foo", button_type="success")

# specifikace handleru
button.js_on_click(CustomJS(code="console.log('button: click!', this.toString())"))

# zobrazení ovládacího prvku
show(button)
