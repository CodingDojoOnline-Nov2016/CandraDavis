#itermediary table for many-to-many relationship
user = [
    {
        'id':1,
        'user':{
            'first-name': 'blah',
            'last_name': 'blahblah',
            'emai': 'dude@email.com'
        },
        'wish_list':{
            'item': 'thing',
            'create_at': 'time',
            'created_by': 'person',
        },

    },
    {
        'id':2, #id associated with the relationship.
        'user':{
            'first-name': 'blah',
            'last_name': 'blahblah',
            'emai': 'dude@email.com'
        },
        'wish_list':{
            'item': 'thing',
            'create_at': 'time',
            'created_by': 'person',
        },
    },
]
#related name = way of finding this related table (many-to-many) from the user

wish_list = [
    {
        'id': 1,
        'item': 'fries',
        'user': 'refer to many-to-many table',
        'created_by': 'user-object',
        'create_at': 'datetime',
        'updated_at': 'datetime',
    },
    {
        'id': 2,
        'item': 'burgers',
        'user': 'refer to many-to-many table',
        'created_by': 'user-object',
        'create_at': 'datetime',
        'updated_at': 'datetime',
    }
]

def get(item_id):
    for item in wish_list:
        if item['id'] == item_id:
            return item

print get(2)

def filter_list(item_name):
    item_list = []
    for item in wish_list:
        if item['item'] == item_name:
            item_list.append(item)
    return item_list

print filter_list('burgers')

def exclude(item_name):
    item_list = []
    for item in wish_list:
        if item['item'] != item_name:
            item_list.append(item)
    return item_list

print exclude('burgers')
