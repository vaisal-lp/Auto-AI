#For Text
def text_tags(data,TXT_HTML,part_top,part_left,from_main):
    
    text_position = data['absoluteBoundingBox']
    top =  abs(text_position['y'] +  part_top)
    # print('=====',main)
    if from_main:
        left =  abs(text_position['x'] + part_left)
    else:
        left =  abs(text_position['x'] - part_left)
   
    characters = data['characters']
    color = data['fills'][0]['color']

    final_rgb = str((color['r'])*255)+', '+str((color['g'])*255)+', '+str((color['b'])*255)+', '+str(color['a'])
    # final_pos = str(text_position['x'])+'px; top: '+str(text_position['y'])+'px; width: '+str(text_position['width'])+'px; height: '+str(text_position['height'])
    font_size = 'font-size: '+str(data['style']['fontSize'])+'px;'
    font_color = 'color: rgba('+final_rgb+');'
    font_fam = 'font-family: '+str(data['style']['fontFamily'])+';'

    text_chr = font_size + ' ' + font_color +' ' + font_fam
    TXT_HTML = '<label type="text" value="'+characters+'" style="position: absolute;left: '+str(left)+'px; top: '+str(top)+'px; width: '+str(text_position['width'])+'px; height: '+str(text_position['height'])+'px;'+text_chr+'">'+characters+'</label><br>'  

    return TXT_HTML

def button_tags(data,TXT_HTML,part_top,part_left):
       
    characters = 'Click Me'
    text_chr = ''
    radius_dt = ""
    BTN_HTML = ""
    if 'cornerRadius' in data.keys():
            radius_dt = ";border-style: ridge;border-radius: "+str(data['cornerRadius'])+"px;"
    # json_elemt.append({"type":"button"})
    butn = {}
    # print(data)
    button_position = data['absoluteBoundingBox']
    
    top =  button_position['y'] +  part_top
    left =  button_position['x'] - part_left
    new_dt = data
    for i in new_dt['children']:
        # print(i)
        # print("======================================================")
        if i['children'][0]['type'] == 'TEXT':
            
            characters = i['children'][0]['characters']
            # print(">>>>>>>>>>>>>>>>>",characters)
            text_position = i['children'][0]['absoluteBoundingBox']
            color = i['children'][0]['fills'][0]['color']
            # print("#############",color)
            final_rgb = str((color['r'])*255)+', '+str((color['g'])*255)+', '+str((color['b'])*255)+', '+str(color['a'])
            final_pos = str(text_position['x'])+'px; top: '+str(text_position['y'])+'px; width: '+str(text_position['width'])+'px; height: '+str(text_position['height'])
            font_size = 'font-size: '+str(i['children'][0]['style']['fontSize'])+'px;'
            font_color = 'color: rgba('+final_rgb+');'
            font_fam = 'font-family: '+str(i['children'][0]['style']['fontFamily'])+';'

            text_chr = font_size + ' ' + font_color +' ' + font_fam +' '+ 'text-transform: uppercase;'

                
                

        data = data
        position = data['absoluteBoundingBox']
        
        color = i['fills'][0]['color']
        # print(color)
        BTN_HTML = '<button type="button" style="position: absolute;left: '+str(left)+'px; top: '+str(top)+'px; width: '+str(position['width'])+'px; height: '+str(position['height'])+'px;'+str(radius_dt)+' background-color: rgba('+str((color['r'])*255)+', '+str((color['g'])*255)+', '+str((color['b'])*255)+', '+str(color['a'])+'); cursor: pointer;'+text_chr+'">'+characters+'</button>'
        
    return BTN_HTML

#For Input
def input_tags(data,TXT_HTML,part_top,part_left):
    
    # text_position = data['absoluteBoundingBox']
    # top =  text_position['y'] +  part_top
    # left =  text_position['x'] - part_left
    characters = "Type Here"
    text_chr = ''
    radius_dt = ""
    TXT_HTML = ""
    
    for i in data['children']:
    # text_dict = [d for d in data if d['type'] == 'TEXT']
        if i['type'] == 'TEXT':
            # data = text_dict[0]
            characters = i['characters']
            # print(characters,"==========")
            text_position = i['absoluteBoundingBox']
            color = i['fills'][0]['color']

            final_rgb = str((color['r'])*255)+', '+str((color['g'])*255)+', '+str((color['b'])*255)+', '+str(color['a'])
            final_pos = str(text_position['x'])+'px; top: '+str(text_position['y'])+'px; width: '+str(text_position['width'])+'px; height: '+str(text_position['height'])
            font_size = 'font-size: '+str(i['style']['fontSize'])+'px;'
            font_color = 'color: rgba('+final_rgb+');'
            font_fam = 'font-family: '+str(i['style']['fontFamily'])+';'

            text_chr = font_size + ' ' + font_color +' ' + font_fam
            TXT_HTML = '<input type="text" value="'+characters+'" style="position: absolute;'+radius_dt+'left: '+str(left)+'px; top: '+str(top)+'px; width: '+str(position['width'])+'px; height: '+str(position['height'])+'px;'+text_chr+'">'
        if i['type'] == 'RECTANGLE':
            # data = data
            position = i['absoluteBoundingBox']
            top =  position['y'] +  part_top
            left =  position['x'] - part_left
            if 'cornerRadius' in i.keys():
                radius_dt = ";border-style: ridge;border-radius: "+str(i['cornerRadius'])+"px;"
            
        
            TXT_HTML = '<input type="text" value="'+characters+'" style="position: absolute;'+radius_dt+'left: '+str(left)+'px; top: '+str(top)+'px; width: '+str(position['width'])+'px; height: '+str(position['height'])+'px;'+text_chr+'">'

        

    return TXT_HTML


def img_tag(data,TXT_HTML,part_top,part_left,image_url,from_main):
    
    img_position = data['absoluteBoundingBox']
    top =  abs(img_position['y'] +  part_top)
    # print('=====',main)
    if from_main:
        left =  abs(img_position['x'] + part_left)
    else:
        left =  abs(img_position['x'] - part_left)
    im = f'<img src="{image_url}" style="left: '+str(left)+'px; top: '+str(top)+'px; width: '+str(img_position['width'])+'px; height: '+str(img_position['height'])+'px;">'

    return im

def vector_tag(data,TXT_HTML,part_top,part_left,image_url,from_main):
    img_position = data['absoluteBoundingBox']
    top =  abs(img_position['y'] +  part_top)
    # print('=====',main)
    if from_main:
        left =  abs(img_position['x'] + part_left)
    else:
        left =  abs(img_position['x'] - part_left)
    im = f'<img src="{image_url}" style="left: '+str(left)+'px; top: '+str(top)+'px; width: '+str(img_position['width'])+'px; height: '+str(img_position['height'])+'px;">'

    return im