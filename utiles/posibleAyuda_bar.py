_menu = QMenu()

#Define action
_add_action     = _menu.addAction(QIcon("images\add.png"),"Add")
_remove_action  = _menu.addAction(QIcon("images\remove.png"),"Remove")

#Asign events to actions
self.connect(_add_action, SIGNAL("triggered()"), self._add_handle)
self.connect(_remove_action, SIGNAL("triggered()"), self._remove_handle)