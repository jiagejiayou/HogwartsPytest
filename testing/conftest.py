import pytest
import yaml


@pytest.fixture()
def start():
    print("开始计算")
    yield
    print("计算结束")

# 注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据

# 命令行去添加一个参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",# 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )

# 处理命令行传来的参数，设置成fixture，将 test 环境和dev环境或者其它环境
# 分别处理，获取想要的不同环境下的测试数据。
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default='test')
    if myenv == 'test':
        datapath = '../TestData/test/data.yaml'
    if myenv == 'dev':
        datapath = '../TestData/dev/data.yaml'
    if myenv == 'st':
        datapath = '../TestData/st/data.yaml'
    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv,datas