import sys
from sanic import Sanic, response

sys.path.append('..')

from Util.GetConfig import GetConfig
from Manager.ProxyManager import ProxyManager

app = Sanic()

@app.route('/')
def index():
    return api_list


@app.route('/get')
async def get(request):
    proxy = ProxyManager().get()
    return response.text(proxy)


@app.route('/refresh')
def refresh(request):
    # TODO refresh会有守护程序定时执行，由api直接调用性能较差，暂不使用
    # ProxyManager().refresh()
    pass
    return 'success'


@app.route('/get_all')
def getAll(request):
    proxies = ProxyManager().getAll()
    return response.json(proxies)


@app.route('/delete', methods=['GET'])
def delete(request):
    proxy = request.args.get('proxy')
    ProxyManager().delete(proxy)
    return response.text('success')


@app.route('/get_status')
def getStatus(request):
    status = ProxyManager().getNumber()
    return response.json(status)



def run():
    config = GetConfig()
    app.run(host=config.host_ip, port=config.host_port)

if __name__ == '__main__':
    run()