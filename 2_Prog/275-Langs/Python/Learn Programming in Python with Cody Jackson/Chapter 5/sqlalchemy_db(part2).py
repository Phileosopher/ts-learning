screwdriver = Tools(name="Screwdriver", size="Small", price=10)
crowbar = Tools(name="Crowbar", size="Large", price=60)

items = (box_knife, drill, axe, putty_knife, hammer, screwdriver, crowbar)

session.add_all(items)

session.commit()
