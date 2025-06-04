class Menu:

    def __init__(self, home: bool, add: bool):
        self.home = home
        self.add = add


### SI QUISIESE OCULTAR UNA PARTE DEL MENU POR SI ME LO PIDEN 

#class Menu:
 #   def __init__(self, home: bool, add: bool, current: str = ""):
  #      self.home = home
   #     self.add = add
    #    self.current = current  # nuevo atributo

    #### PRIMERO AÑADIRIAS ESTE ATRIBUTO CURRENT , LUEGO EN MAIN.PY AÑADIRIAS :

     #menu = Menu(True, True, current="add") SI ESTAS EN EL HTML DE ELIMINAR

     #menu = Menu(True, True, current="delete") SI ESTAS EN EL HTML DE BORRAR , PARA QUE CUANDO ESTES EN BORRAR , NO LO MUESTRE


### POR ULTIMO , MODIFICAR EL DEFAULT.HTML

#<div class="topnav">
#  {% if menu %}
#    {% if menu.home %}
#      <a href="{{ url_for('get_alumnos') }}">VER TABLA ALUMNOS</a>
 #   {% endif %}
 #   {% if menu.add %}
 #     <a href="{{ url_for('ver_notas') }}">ORDEN ALUMNOS</a>
 #     {% if menu.current != "add" %}
 #       <a href="{{ url_for('form_add_alumnos') }}">AÑADIR ALUMNOS</a>
 #     {% endif %}
 #     {% if menu.current != "delete" %}
 #       <a href="{{ url_for('form_del_alumnos') }}">ELIMINAR ALUMNOS</a>
 #     {% endif %}
 #     {% if menu.current != "update" %}
 #       <a href="{{ url_for('form_update_notas') }}">ACTUALIZAR NOTAS</a>
#      {% endif %}
 #   {% endif %}
 # {% endif %}
#</div>