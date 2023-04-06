import requests
import functions


def search_json(obj, key, value, path=''):
    
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{path}/{k}" if path else k
            if k == key and v == value:
                return (new_path, obj)
            else:
                result = search_json(v, key, value, new_path)
                if result is not None:
                    return result
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_path = f"{path}/{i}"
            result = search_json(v, key, value, new_path)
            if result is not None:
                return result
    return None
    
url = "https://api.figma.com/v1/files/i6x6MjgVWG4xpdTEySLJSu"
headers = {
    "X-Figma-Token": "figd_8UgwgGrTBeR-QclkmojNbv1tRQKvVbOJj7tcIFSr"
}
html = '<html>\n<head>\n<title>' + '</title>\n</head>\n<body>\n'
bs = ""
response = requests.get(url, headers=headers)
if response.status_code == 200:
    design_data = response.json() #Get Figma design as json data
    # print(design_data)
    main_list = []
    main_list = design_data['document']['children'][0]['children']
    if main_list:
        for main in main_list:
            component_name = main['name']
            main_div=True
            from_main = True
            parent_top = main['absoluteBoundingBox']['y']
            parent_left = main['absoluteBoundingBox']['x']
            html,no_div = functions.conversion_pr(html,main,main_div,0,0,False) #create a main div
            
            children_data = list(reversed(main['children'])) #Reverse the children list
            for sub in children_data:
                if sub['name'] == 'Group':
                    from_main = True
                    html = functions.group_list(sub,html,from_main,parent_top,parent_left)
                else:
                    
                    
                    main_div=False
                    from_main = True
                    html,no_div = functions.conversion_pr(html,sub,main_div,parent_top,parent_left,from_main)

                    # if no_div:
                    #     html += '\n'
                    # else: 
                    #     html += '</div>\n'
            
            html += '</div>\n</body>\n</html>'
            
            # Write the HTML to a file
            with open('C:/Users/Vaisal/Desktop/Auto AI/vaisal.html', 'w', encoding='utf-8') as file:
                    file.write(html)


            

   