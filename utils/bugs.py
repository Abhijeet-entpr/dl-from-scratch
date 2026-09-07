# utils/bugs.py

def trigger_name_error():
    print(total_score)

def trigger_type_error():
    result = "Count: " + 5

def trigger_index_error():
    items = [10, 20, 30]
    print(items[5])

def trigger_key_error():
    user = {"name": "Alice"}
    print(user["age"])

def trigger_attribute_error():
    number = 42
    number.append(5)

def trigger_recursion_error():
    def repeat():
        return repeat()
    repeat()

trigger_recursion_error()