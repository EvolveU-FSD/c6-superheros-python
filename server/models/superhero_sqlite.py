from models.db import query

class Superhero:
  def find_all():
      return query('SELECT * from superhero')


  def find_by_id(id):
      return query(
          f'select id as _id, name, nickname, alterego, sidekick from superhero where id={id}'
      )


  def create(superhero_to_create):
      if 'name' not in superhero_to_create:
          superhero_to_create['name'] = None
      if 'nickname' not in superhero_to_create:
          superhero_to_create['nickname'] = None
      if 'alterego' not in superhero_to_create:
          superhero_to_create['alterego'] = None
      if 'sidekick' not in superhero_to_create:
          superhero_to_create['sidekick'] = None

      insert_sql = f"""
        insert into superhero (name, nickname, alterego, sidekick) values (
        '{superhero_to_create['name'] or None}',
        '{superhero_to_create['nickname'] or None}',
        '{superhero_to_create['alterego'] or None}',
        '{superhero_to_create['sidekick'] or None}'
        )
      """
      answer = query(insert_sql)
      print(answer)
      return answer


  def update(id, superhero_to_update):
      update_sql = f"""
        update superhero set 
        name='{superhero_to_update['name'] or None}',
        nickname='{superhero_to_update['nickname'] or None}',
        alterego='{superhero_to_update['alterego'] or None}',
        sidekick='{superhero_to_update['sidekick'] or None}',
        where id={id}
      """

      print('Going to execute: ' + update_sql)
      return query(update_sql)


  def delete_superhero(id):
      delete_sql = f"delete from superhero where id={id}"
      print('Going to execute: ' + delete_sql)
      return query(delete_sql)
