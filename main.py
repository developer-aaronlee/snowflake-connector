import snowflake.connector

ctx = snowflake.connector.connect(
    user="pvolve_data",
    password="k7n#TE#s8I7CgB!L",
    account="kga28917.us-east-1"
    )

cs = ctx.cursor()

sql_query = "SELECT current_version()"

try:
    cs.execute(sql_query)
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()

ctx.close()