# code-generation
a simple learning task----use GPT API to generate code,with a simple exe file

## 代码生成小程序
今天给大家介绍的是我大模型兴趣组任务汇报的成果--代码生成小程序。希望和大家分享我在前段时间内的一些学习收获。首先需要说明的是，由于本人也是新手，此程序仍然是基于OpenAI开放的接口进行开发，实现功能也可以由chatGPT完成，但此工具针对代码生成部分进行了提示词优化，具体功能在下方介绍。本工具的使用需要用户自行准备OpenAI密钥！！！

介绍的主要内容有以下几个方面：
- 小程序的获取方式；
- 小程序的功能介绍和使用教程；
- 程序python源码运行环境介绍；
- 程序源码解读；

  形成可执行文件的步骤为：
- 安装pyinstaller包：
    > pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 
- 打开python IDE终端或者cmd命令行，进入到需要打包的代码文件所在文件夹；
- 输入命令行指令生成可执行文件：
    > pyinstaller -F 要打包的文件名.py -n name

生成可执行文件还有其他个性化设置，比如设置exe的图标等，具体请参照[pyinstaller](https://pyinstaller.org/en/stable/usage.html)

完成以上步骤后，在代码文件所在文件夹或自定义生成位置的文件夹下会生成相对应的exe文件，点击即可打开。

### 小程序的功能介绍以及使用教程
#### 功能介绍
- 按照指令生成代码；
- 可以自行指定GPT对话角色；自行选择GPT模型（需要用户自己的API key支持）；
- 可以进行连续多轮对话，对话内容自动保存在本地；
- 可以自行设置GPT上下文记忆能力强弱；
#### 使用教程
以下将分别介绍执行exe可执行文件和执行源文件两方面进行介绍。如果需要自定义设置，参照下面的*源文件执行*。
##### 程序requirment
1. 点击进入程序后，需要提供自己的OPENAI_API_KEY;
2. 需要网络代理（VPN）

##### 前端程序（简易）
- 连接VPN
- 点击进入DSSTL.exe应用程序
- 看到提示输入OPENAI_API_KEY
- 进行提问，可以进行多轮对话
- 对话完毕后，输入'exit'结束对话，界面会显示对话日志存储位置
- 关闭程序

##### 源文件执行
在提供的文件中，找到api.py文件，即为程序执行源文件，可以进入源文件进行执行，并可以自行修改。

执行过程较为简单，此处不进行赘述。以下主要说明如何进行模型修改，文件地址等的修改。

###### 模型修改
本程序默认使用'gpt-3.5-turbo'模型，如需修改模型，此处提供GPT3.5所支持的部分模型：
![](https://img-blog.csdnimg.cn/b60d119ad07148a7a6e7694c6015c353.png#pic_center)
但目前最新的GPT3.5模型即为'gpt-3.5-turbo'模型，如果你的账号为plus账号并且申请了GPT4模型使用权限，那么也可以使用GPT4模型。

###### 文件存储位置
```python
f = Path("你希望存储的文件位置") # api.py文件的 *line22*
```

###### 模型角色改变
模型角色改变，是指可以人为为模型定义其在对话中的角色，模型在不同的角色下的回答会有所不同。

角色修改步骤：
```python
'''
修改'role':'system' 后面的'content'内容
'''
 messages=[
                            {'role':'system','content':'you are a python rookie, can not code python'},
                            {"role": "user", "content": prompt},
                        ]     # api.py文件的 *line45*
```

### 程序python源码运行环境
如果需要进行上述的文件自定义操作，可能部分读者电脑中的python环境无法运行程序。因此这里简要提示一下大家python环境配置。

首先需要注意你的python环境的版本，python版本不要低于3.8，因为部分3.7版本无法安装最新版的openAI包。

接着需要安装OpenAI的安装包，进入到python环境中，直接通过命令行安装:
>   pip install openai

显示安装完成即可。   
