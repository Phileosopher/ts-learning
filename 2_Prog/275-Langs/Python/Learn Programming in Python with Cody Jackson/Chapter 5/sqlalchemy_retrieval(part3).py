# Return all the tools with a given price
priced_tools = session.query(Tools).filter(Tools.price == 25).all()
for tool in priced_tools:
    print(tool.name)
