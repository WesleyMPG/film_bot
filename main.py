from infeng import Engine

eng = Engine('knowledge_base.json')

while True:
    print('-> ',eng.evaluate(input('>>> ')))
