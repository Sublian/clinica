import pymysql

def connect():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='todoflask',
        charset='utf8'              
       )

NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item, stat):
    try:
        conn = connect()
        # Once a connection has been established, we use the cursor
        # object to execute queries
        
        with conn.cursor() as c:      
            # Keep the initial status as Not Started
            c.execute('INSERT INTO items(item, status) VALUES (%s, %s)', (item, stat))
            # We commit to save the change
            conn.commit()
            conn.close()            
    except Exception as e:
        print('Adding list error: ', e)        
    
def get_all_items():
    try:
        conn = connect()
        list=[]
        with conn.cursor() as c:              
            c.execute('SELECT item, status FROM items')
            list = c.fetchall()
            conn.close()
            return list
    except Exception as e:
        print('Showing all error: ', e)
        return None

def get_status(item):
    try:
        conn = connect()
        with conn.cursor() as c:                        
            c.execute("SELECT status FROM items WHERE item=%s" ,(item))
            status = c.fetchone()[0]
            conn.close()
            return status
    except Exception as e:
        print('Get Status error: ', e)
        return None

def update_status(item, status):    
    try:
        conn = connect()
        with conn.cursor() as c:            
            c.execute('UPDATE items SET status=%s WHERE item=%s', (status, item))
            conn.commit()
            conn.close()
            
    except Exception as e:
        print('Updating error: ', e)
        return None
    
def delete_item(item):
    try:
        
        conn = connect()
        with conn.cursor() as c:            
            c.execute('DELETE FROM items WHERE item=%s', (item))
            conn.commit()
            conn.close()
    except Exception as e:
        print('Deleting error: ', e)
        return None
    
"""if __name__=='__main__':
    articulos=get_all_items()
    print(articulos)"""