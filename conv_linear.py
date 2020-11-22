# by Aissa @21/11

#import json library
import json

#file path:
# SHOULD BE MODIFIED
url = "/Users/aisaidi/PycharmProjects/json_tools/test.json"

#Read json file
with open(url, "r") as read_file:
   data = json.load(read_file)

#Get list of binary signals
list_binarys = [item.get('binary') for item in data]

#core program :

#loop through fields :
for k in range(len(data)) :
    #condition : if the signal is analogic
    if not (list_binarys[k]) :
        #then create the wanted keys and values
        data[k]['conv_func'] = 'linear'

        data[k]['conv_params'] = '[ ' + str(data[k]['range_elec_min']) + ', ' \
        + str(data[k]['range_elec_max']) + ', ' + str(data[k]['range_phy_min']) \
        + ', ' + str(data[k]['range_phy_max']) + ' ]'


#Write the new file as results.json
with open( 'outputs.json', 'w', encoding='utf-8' ) as f:
    json.dump(data, f, ensure_ascii=False, indent=4 )

