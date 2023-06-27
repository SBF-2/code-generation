import openai
import time
from pathlib import Path


#输入api_key
openai.api_key = str(input("your openai api_key is:")) #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
class Chat_bot:
    def __init__(self,model):
        self.user = "\nDSSTL: "
        self.bot = "GPT: "
        self.model = model
        self.question_list = []
        self.answer_list = []
        self.text = ''
        self.turns = []
        # self.last_result = ''

    def dialogue_save(self):
        timestamp = time.strftime("%Y%m%d-%H%M-%S", time.localtime())  # 时间戳
        file_name = 'output/Chat_' + timestamp + '.md'  # 文件名
        f = Path(file_name)
        f.parent.mkdir(parents=True, exist_ok=True)
        with open(file_name, "w", encoding="utf-8") as f:
            for q, a in zip(self.question_list, self.answer_list):
                f.write(f"You: {q} \n GPT-3.5-turbo: {a}\n\n")
        print("对话内容已保存到文件中: " + file_name)
        time.sleep(5000)

    def Generate(self):
        print(f'\n欢迎来到DSSTL的GPT世界，本模型的基本信息如下:\n model : {self.model} \n 本模型为多轮对话，终止对话请输出‘exit’')
        while True:#循环输入，保证记忆功能
            # 用户输入
            question = input(self.user)
            self.question_list.append(question) # 将问题添加到问题列表中
            prompt = self.bot + self.text + self.user + question
            # 退出命令
            if question == 'exit':
                break
            else:
                try:
                    response = openai.ChatCompletion.create(
                        # 模型名称
                        model= self.model,
                        messages=[
                        {'role':'system','content':'you are a mathematic expert,when you was asked to give a path,just return a string representing the path'},
                        {"role": "user", "content": prompt},
                        ],
                    )

                    result = response["choices"][0]["message"]["content"].strip()
                    print(result)
                    # print(response)
                    self.answer_list.append(result) #将回答添加到回答列表中

                    # self.last_result = result
                    self.turns += [question] + [result]
                    # 记忆功能所能支持的token数
                    if len(self.turns) <= 10:
                        self.text = " ".join(self.turns)
                    else:
                        self.text = " ".join(self.turns[-50:])

                # 打印异常
                except Exception as exc:
                    print(exc)
        # 退出对话后保存
        self.dialogue_save()

if __name__ =='__main__':
    bot = Chat_bot('gpt-3.5-turbo')
    bot.Generate()

