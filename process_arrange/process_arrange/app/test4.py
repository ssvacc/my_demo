import json
import random

if __name__ == '__main__':
    a = 'av,c'
    x = a.split(',')
    b = random.uniform(1, 10)

    # str = '[{"id":"start","width":120,"height":40,"coordinate":[400,80],"meta":{"label":"start","name":"start","type":"start"}},{"id":"end","width":120,"height":40,"coordinate":[400,560],"meta":{"label":"end","name":"end","type":"end"}},{"id":"nodeZ2e5JhS9D8IR0Gdg","width":200,"height":40,"coordinate":[360,203],"meta":{"label":"函数A","name":"函数A","function_id":"funcA","type":"process"}},{"id":"nodelCp610I4P6PdlDG4","width":200,"height":40,"coordinate":[360,351],"meta":{"label":"函数B","name":"函数B","function_id":"funcB","type":"process"}}]'
    # x = json.loads(str)
    print(b)
    print(x)