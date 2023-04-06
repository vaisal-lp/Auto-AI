import utils
import requests
import json


def conversion_pr(html,node_data,main,parent_top,parent_left,from_main):
    # print(node_data)
    # print("##############")
    no_div = False
    brd = "''"
    radius_dt = ""
    RGB = ""
    pos = "absolute"

    if node_data['fills']:
        if 'color' in node_data['fills'][0].keys():
            RGB = str((node_data['fills'][0]['color']['r'])*255)+','+str((node_data['fills'][0]['color']['g'])*255)+','+str((node_data['fills'][0]['color']['b'])*255)+','+str(node_data['fills'][0]['color']['a'])
        else:
            pass
    elif 'backgroundColor' in node_data.keys():
        RGB = str((node_data['backgroundColor']['r'])*255)+','+str((node_data['backgroundColor']['g'])*255)+','+str((node_data['backgroundColor']['b'])*255)+','+str(node_data['backgroundColor']['a'])
    else:
        pass
    if main:
        pos = "''"
        
        parent_top = node_data['absoluteBoundingBox']['y']
        parent_left = node_data['absoluteBoundingBox']['x']
        no_div = True
    else :
        # print(node_data['name'])
        print("-----------------")
        tp = int(node_data['absoluteBoundingBox']['y'])
        lf = int(node_data['absoluteBoundingBox']['x'])
        no_div = False
        if 'cornerRadius' in node_data.keys():
            radius_dt = ";border-style: ridge;border-radius: "+str(node_data['cornerRadius'])+"px;"
        
        t = int(parent_top)
        l = int(parent_left)
        parent_top = abs(int(parent_top) - (tp))
        parent_left = abs(int(parent_left) - lf)
        # print(node_data['name'])
        if node_data['name'] == 'text':
            # print("===================")
            no_div = True
            
            txt_html = utils.text_tags(node_data,html,abs(t),abs(l),from_main)

            html += txt_html
            return html,no_div
        if node_data['name'] == 'button':
            no_div = True
            # print("bbbbbbbbbbbbbbbbbbbbbb")
            txt_html = utils.button_tags(node_data,html,abs(t),abs(l))

            html += txt_html
            # print(node_data['name'],"====",no_div)
            return html,no_div
        if node_data['name'] == 'input':
            no_div = True
            
            txt_html = utils.input_tags(node_data,html,abs(t),abs(l))

            html += txt_html

            return html,no_div
        if node_data['name'] == 'img':
            img_url = f'https://api.figma.com/v1/images/i6x6MjgVWG4xpdTEySLJSu?ids={node_data["id"]}&format=png'
            headers = {'X-Figma-Token': "figd_8UgwgGrTBeR-QclkmojNbv1tRQKvVbOJj7tcIFSr"}
            response = requests.get(img_url, headers=headers)
            data = json.loads(response.text)
            # Get the URL of the image and download it to a local file
            image_url = data['images'][node_data["id"]]
            # image_response = requests.get(image_url)
            # with open('image.png', 'wb') as f:
            #     f.write(image_response.content)

            img_html = utils.img_tag(node_data, html,abs(t),abs(l),image_url,from_main)
            # print(node_data)
            html += img_html

            return html,no_div
            
            # print(node_data['n
        if node_data['name'] == 'Vector':
            img_url = f'https://api.figma.com/v1/images/i6x6MjgVWG4xpdTEySLJSu?ids={node_data["id"]}&format=svg'
            headers = {'X-Figma-Token': "figd_8UgwgGrTBeR-QclkmojNbv1tRQKvVbOJj7tcIFSr"}
            response = requests.get(img_url, headers=headers)
            data = json.loads(response.text)
            # Get the URL of the image and download it to a local file
            image_url = data['images'][node_data["id"]]
            # image_response = requests.get(image_url)
            # with open('image.png', 'wb') as f:
            #     f.write(image_response.content)

            img_html = utils.img_tag(node_data, html,abs(t),abs(l),image_url,from_main)
            # print(node_data)
            html += img_html

            return html,no_div
        elif node_data['name'] == 'vector':
            return html,no_div
    html += '<div name='+node_data['name']+' style="position:'+pos+' ;width: ' + str(node_data['absoluteBoundingBox']['width']) + 'px; height: ' + str(node_data['absoluteBoundingBox']['height']) + 'px;' + ' background-color: ' + 'rgba('+ RGB +');top:'+ str(parent_top) + 'px; left: ' + str(parent_left) + 'px'+str(radius_dt)+'">\n'

    
    return html,no_div




def group_list(json_data,html,from_main,parent_top,parent_left):
    # print(json_data)
    # print("**************")
    html_data = ''
    from_main = False
    close_div = False
    # parent_top = json_data['absoluteBoundingBox']['y']
    # parent_left = json_data['absoluteBoundingBox']['x']
    main = False
    html,no_div = conversion_pr(html,json_data,main,parent_top,parent_left,from_main)

    
    
    if 'children' in json_data.keys():
        
        parent_top = json_data['absoluteBoundingBox']['y']
        parent_left = json_data['absoluteBoundingBox']['x']
        for dt in json_data['children']:
            ht=''
            main =False
    #         # print(dt)\
            if dt['name'] == "Group":
                # parent_top = json_data['absoluteBoundingBox']['y']
                # parent_left = json_data['absoluteBoundingBox']['x']
                print("----------")
                html += group_list(dt,html_data,from_main,parent_top,parent_left)
                
                close_div=True
                
                
            else:
                htl=''
                
                html_data,no_div = conversion_pr(htl,dt,main,parent_top,parent_left,from_main)
                html += html_data
                
                close_div=False
                # if no_div:
                #     html += '\n'
                # else: 
                #     html += '</div>\n'
        
             
    
    # html += html_data
    html += '</div>\n'
    
    return html
    
    