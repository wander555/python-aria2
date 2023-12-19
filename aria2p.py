import Aria2Py as a2p

global client

# 显示当前的任务列表


def tell_active():
    downloads = {}
    active = client.tell_active()
    for i in active:
        download_speed = i['downloadSpeed']
        completed_length = i['completedLength']
        total_length = i['totalLength']
        downloadDir = i['dir']
        gid = i['gid']

        if 'bittorrent' in i.keys():
            try:
                file = downloadDir + "/" + i['bittorrent']['info']['name']
            except:
                file = "正在获取种子" + downloadDir + "/" + i['dir']
        else:
            file = i['files'][0]['path']

        if total_length == completed_length:
            if (int(completed_length) > 536870912):
                print('@', file, 'download complet')
                downloads[downloadDir] = gid

        else:
            now_speed = round(float(download_speed) / 1024, 2)
            percent = (int(completed_length) / int(total_length)) * 100
            print(now_speed, 'KB/s', int(percent), '%', file)

    return downloads


if "__main__" in __name__:
    url = input("输入网址:\n")

    server = 'http://aria.wander555.link'
    port = '6800'
    token = 'junjinking'

    global client
    client = a2p.Aria2Client()
    client.set_server(server_add=server, server_port=port, token=token)
    tell_active()
    print(f'{url}')

    # 添加链接
    # client.add_uri(url, "")
