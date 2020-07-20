import json
template = open('main.tf', 'w')
with open('parameters.json') as json_data:
    data = json.load(json_data)
    print(data)
    ssm_dict = {}
    ssm_dict = data['glossary']
    for k,v in ssm_dict.items():
        template.write('resource aws_ssm_parameter "' + k + '" {\n')
        template.write('\t value = "' + v + '"\n')
        template.write('}\n\n')
       # print("Key is " + k + "  value is " + str(v))