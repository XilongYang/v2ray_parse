#! /usr/bin/python3

import json,base64,os

os.chdir("/home/xilong/.config/v2ray")

raw_file = open("raw", "r")
raw_data = raw_file.read()

origin_data = base64.b64decode(raw_data).decode('utf-8')
origin_data = origin_data.splitlines()
origin_data = [x for x in origin_data if x != ""]

index_vmess = []
for x in range(0, len(origin_data)):
    raw_vmess = origin_data[x][8:]

    origin_vmess = base64.b64decode(raw_vmess).decode('utf-8')
    vmess = json.loads(origin_vmess)
    index_vmess.append((x, vmess))

for i_vmess in index_vmess:
    print("{}: {}".format(i_vmess[0], i_vmess[1]["ps"]))

print("Choose a node: ")
choose = input();
choosed_vmess = index_vmess[int(choose)][1]

template_file = open("template.tson", "r")
template_data = template_file.read()
template_data = template_data.replace("$id", choosed_vmess["id"]);
template_data = template_data.replace("$aid", choosed_vmess["aid"]);
template_data = template_data.replace("$addr", choosed_vmess["add"]);
template_data = template_data.replace("$port", choosed_vmess["port"]);
print(template_data)

config_file = open("config.json", "w")
config_file.write(template_data)
