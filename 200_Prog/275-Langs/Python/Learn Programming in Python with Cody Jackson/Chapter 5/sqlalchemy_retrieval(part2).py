# Query all entries in database
tools = session.query(Tools).all()
for tool in tools:
    print(tool.name)

# Return first entry in database
tool = session.query(Tools).first()
print("\n" + tool.name)

# Return the tool with given price
priced_tool = session.query(Tools).filter(Tools.price == 10).one()
print("\n" + priced_tool.name + "\n")
