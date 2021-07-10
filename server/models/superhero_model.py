from models.db import query

def find_all():
  
    return query('select id, name, nickname, alterego, sidekick from superhero')

def find_by_id(id):
    try:
        return query(f'select id, name, nickname, alterego, sidekick from superhero where id={id}')[0]
    except Exception as e:
        return {"error":e}


def create(superhero_to_create): 
    if 'nickname' not in superhero_to_create:
        superhero_to_create['nickname']=None
    if 'alterego' not in superhero_to_create:
        superhero_to_create['alterego']=None
    if 'sidekick' not in superhero_to_create:
        superhero_to_create['sidekick']=None
    insert_sql = "insert into superhero (name, nickname, alterego, sidekick) values (%s,%s,%s,%s)" 
    args = (superhero_to_create['name'],superhero_to_create['nickname'],
        superhero_to_create['alterego'],superhero_to_create['sidekick'])
    
    return query(insert_sql, args)

def update_superhero(id,superhero_to_update):
    if 'nickname' not in superhero_to_update:
        superhero_to_update['nickname']=None
    if 'alterego' not in superhero_to_update:
        superhero_to_update['alterego']=None
    if 'sidekick' not in superhero_to_update:
        superhero_to_update['sidekick']=None
    update_sql = f"update superhero set name=%s, nickname=%s, alterego=%s, sidekick=%s where id={id}" 
    args = (superhero_to_update['name'],superhero_to_update['nickname'],
        superhero_to_update['alterego'],superhero_to_update['sidekick'])
    
    return query(update_sql, args)


def delete_superhero(id):
    delete_sql = f"delete from superhero where id={id}"
    query(delete_sql)

